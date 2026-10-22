# First steps
We need to load all of the communication so we do a start node - load_corpus which is a first deterministic node which loads
all files present in provided path, also in subfolders.

The deterministic node load_corpus successfully collected all 20 documents and chuned them because each file can have 
different size and email communication can be too long and the performance of our small models would drop fast
. Also, tested by my agent claude sonnet 5.5 medium
it loads text perfectly from the files. 

# the following nodes
Firstly discussed with my agent what is the best approach and what model is the most suitable for it I ran agent to 
test which model satisfies what best. The results were following:


we tested models 6 luna, 5.6 luna, 5.4 nano, 5mini, 5nano, 4.1nano. Not every model got the exact citation only gpt 5.6 luna and gpt 5.4 nano got 100% citation correctlly.
The downsize of nano is thta it has terrible recall on srs, the best recall has gpt 6 luna. and the other models are either sow or imprecise.
The family of model 5 is also expensive and slow on tokens. 

From the analysis we have constructred. Because the extractor gpt 5.6 luna was getting citation correctly we will use extractor node
gpt 5.6 luna and it works in reasonable time. The reviewer will be gpt-6-luna becasue it had the biggest recall so it will be good at finding what extractor missed and it is diff model.
For deduplication and conflicts we will use again the gpt 6 luna. Prioritization will be resolved with gpt 5.4 nano for it speed

# Implementation
We start building nodes by node with testing each node.

The first node is the extract plus verify evidence node - verify evidence is a unit test to test the extractor. 

We try to be efficient and to save already processd node to get it faster and more efficiently.

1. Extraction and verify evidence node - 

   Result on the whole corpus: 20 documents -> 55 chunks -> 780 candidates; 27 quotes are not a contiguous
   passage (the model joined a list heading with a bullet) and are flagged, not dropped.

2. Completeness review and feedback loop (review_completeness, review_gate) -
   gpt-6-luna reads each whole document together with its extracted requirements and lists what is missing, with a
   verbatim quote. The deterministic review_gate drops items with an unverifiable quote and sends the rest back to
   extract (only the chunks of the affected documents, with the feedback). Capped at 2 re-extractions.
   Missing items found per round: 23 -> 3 -> 1 (candidates 780 -> 826), so the loop converges.

3. Merge and conflict resolution (merge_and_resolve) -
   First attempt: one call over all 826 candidates. The model was lazy: 478 items remained, obvious duplicates were
   left ("Report Missing Items" twice) and 54 ids were misused. Fix: code clusters candidates by topic (TF-IDF
   similarity), gpt-6-luna merges each cluster of ~60 in parallel, and a second round re-clusters the merged output to
   catch duplicates that fell into different clusters: 826 -> 576 -> 446 requirements. The model returns only
   decisions (groups of ids, blacklist); code builds sources, quotes and counts from the original candidates, so
   tracing cannot be damaged. 25 candidates were blacklisted (23 too vague or not about the software, 2 describe
   existing behaviour); no real contradiction was found, and a grep of the corpus found no explicit one.

4. Prioritization (prioritize) -
   Goal: the small model (gpt-5.4-nano) must have no room for a mistake that matters, so most of the decision is code.
   Decisions:
   - Signals computed by code from the merged records: (a) an explicit priority tag in the source, found by locating the
     requirement's verbatim quote in its document and reading the tag in the same paragraph (SRS: "[* High Priority]");
     (b) number of distinct documents mentioning the requirement; (c) emphatic words (must, critical, essential, ...) in
     the stakeholders' own quotes, not in the model's paraphrase.
   - We count distinct documents, not raw mentions: mentions are inflated by repeats inside one document (the SRS repeats
     itself a lot) and by re-extraction in the feedback loop. Many independent sources is the real sign of importance.
   - Baseline by code: tag in source -> that level (final, nobody can change it). Otherwise score = (documents - 1) +
     1 for emphatic wording: 3 or more = Must, 1-2 = Should, 0 = Could.
   - The model gets the baseline and may move it by one level at most, for content the signals cannot see (legal,
     privacy and data-integrity needs higher, convenience lower). It answers only with an id, one of three levels and a
     note. Code matches answers by id, clamps the level to baseline +-1, ignores unknown ids and uses the baseline for any
     id it did not answer. Requirements with a stated priority are not sent to the model at all.
   - Three levels (Must, Should, Could) instead of full MoSCoW: no source mentions deferral, so "Won't" would stay empty.
   - Ordering of the final document is done by code (priority, then date), not by the model.
   - Every requirement stores why it got its priority (priority_basis, priority_source), the document explains the scale.
   Result: 446 requirements -> 25 Must, 158 Should, 263 Could. 15 priorities stated in the source, the model changed 28 (6 %)
   and answered every id. Runtime 16 s.

5. Ids and the output document (assign_ids, render_doc) - both deterministic.
   - assign_ids runs after deduplication so ids never change meaning. Requirements are ordered by priority
     (Must, Should, Could), then by first mention, then by title, and numbered REQ-001...; blacklist items are
     numbered BL-001... The conflicts_with links of a blacklist item (stored as candidate ids, which stay valid
     through both merge rounds) are translated to the REQ ids of the requirements that now contain them.
   - render_doc writes one Markdown file: priority scale with an explanation of how a level is chosen, an overview
     table, the requirements grouped by priority (name, priority and why, type, first mention, source documents, the
     description paragraph, up to 2 verbatim quotes) and the blacklist section with reasons.
   - Self-check inside render_doc, mapped to the output spec: unique ids (OS2), name and description present (OS5), valid
     priority (OS6), at least one source (OS4), every id really in the document (OS1), blacklist reason present and
     scale/blacklist sections present (OS6, OS9). The node fails loudly instead of writing a broken document.
   - Offline tests cover ordering, id mapping and the self-check on a broken record.
   First output: 446 requirements, 25 blacklisted, 264 kB. Some duplicates by name remain (e.g. "Control Access
   Through Roles" twice, "Provide Online Help" next to "Provide Navigable Online Help"); to be assessed in the full run.

6. Full clean run and analysis (`python network.py data/corpus`, no checkpoints; `python analyze_output.py output/states`,
   code only, no API calls; the printout is in `output/analysis.txt`, the document is `output/requirements.md`).
   Runtime about 5.5 minutes. Pipeline: 20 documents -> 55 chunks -> 836 candidates -> 453 requirements + 22 blacklisted.
   Two complete runs gave 446 and 453 requirements, so the output is stable in size but not identical (non-deterministic LLM).

   Results per output spec:
   - OS1/OS2/OS5/OS6/OS9: the built-in self-check passes (one document, unique ids, name + description, priority with
     explained scale, blacklist with reasons). Distribution 26 Must, 150 Should, 277 Could; 16 priorities stated in the
     source, the model adjusted 23.
   - OS4 tracing: every one of the 20 documents contributes requirements; 305 requirements come from one document,
     104 from two, 44 from three or more. 25 of 836 quotes (3 %) are not contiguous text (flagged).
   - OS8 completeness: the reviewer found 12 / 6 / 6 missing items in the three rounds; after the cap about 6 items
     (0.7 % of candidates) were still open. The loop recovers most omissions but does not always converge to zero.
   - OS9/OS7 blacklist: 22 items (16 too vague or not about the software, 5 describe existing behaviour, 1 real
     conflict: an earlier "separate reporting database" vs the later "use the main relational database"; the discarded
     one links to REQ-102). No noise (Costco, novels) leaked into the requirements.
   - OS3 duplicates: TF-IDF similarity >= 0.6 flags 54 pairs among 453 requirements. By hand about 10-15 of them are
     real duplicates (e.g. "Provide Pivot Table Output" / "Generate Pivot Table Output", "Claims Returned Report" twice);
     the rest are distinct (e.g. report deletions by location vs by system, filter vs group by home branch).
     So roughly 2-3 % duplicates remain, because the two merge rounds only see items inside a topical cluster.
   - OS7 vocabulary: patron 151x vs user 80x (user often means staff), item 164x vs copy 15x, no borrower/customer.
     Terminology is mostly but not fully unified.
   - OS5 explanation length: the average description is only 124 characters (one to two sentences), shorter than a full
     paragraph. Known weakness: the extractor prompt asks for "one paragraph" but the model keeps it terse.

   Known limits / possible improvements: a third merge round over the remaining near-duplicate pairs, a longer
   description requirement in the extractor prompt, a stronger terminology step, and a repeated benchmark (the model
   comparison was a single run on 3 chunks).

7. Grounded paragraphs and names (retrieve_context, write_paragraphs, name_requirements) -
   Motivation: the first full run had one-sentence descriptions (124 chars on average, OS5 asks for a paragraph) and
   names chosen by the merge model. Three nodes were added after prioritization (so the work is done once per final requirement):
   - retrieve_context (code, a "RAG" without embeddings): every requirement keeps verbatim quotes, so its place in the
     source is known exactly. The quote is located in its document (normalized text) and the surrounding paragraph is
     returned; a bullet list longer than 1200 chars is cut to its heading plus the lines around the quote. For source
     documents without a usable quote, the most similar paragraph (TF-IDF cosine) is the fallback. Up to 4 passages per
     requirement, one per document first. 707 passages came from quotes, 30 from the fallback.
   - write_paragraphs (LLM gpt-5.6-luna): sees only the short summary and the passages and writes a 3-5 sentence
     paragraph (what, why, who, conditions), with a fixed vocabulary (patron, staff, item, branch). Code guard: the text
     must have a sensible length and may not contain a number absent from its grounding; otherwise the old summary stays.
     Nothing was rejected in the run.
   - name_requirements (LLM gpt-5.4-nano): a 3-6 word name derived from the finished paragraph; the old title is the
     fallback when the name is malformed.
   Efficiency: retrieval costs no API call; paragraphs go in batches of 6 (76 calls), names in batches of 40 (12 calls),
   both in parallel. The whole stage takes 82 s.
   Result: average description 124 -> 427 chars; patron 373x vs user 48x (before 151 / 80); items with identical names
   11 -> 3. The TF-IDF duplicate metric rose to 80 pairs, but only because the longer texts share more words; the top
   pairs are distinct requirements (e.g. loans by facility vs by system), so that metric is now less informative.
   The reviewer-measured completeness and the blacklist are unchanged by this stage.

# Final result

## Network

| # | Node | Type | Model |
|---|---|---|---|
| 1 | load_corpus | code | - |
| 2 | chunk_documents | code | - |
| 3 | extract (parallel per chunk) | LLM | gpt-5.6-luna |
| 4 | verify_evidence | code | - |
| 5 | review_completeness (parallel per document) | LLM | gpt-6-luna |
| 6 | review_gate (loop back to extract, max 2x) | code | - |
| 7 | merge_and_resolve (clusters, 2 rounds) | LLM + code clustering | gpt-6-luna |
| 8 | prioritize | LLM with code baseline and clamp | gpt-5.4-nano |
| 9 | retrieve_context | code | - |
| 10 | write_paragraphs | LLM | gpt-5.6-luna |
| 11 | name_requirements | LLM | gpt-5.4-nano |
| 12 | assign_ids | code | - |
| 13 | render_doc (with self-check) | code | - |

Network specs: ANS1 six LLM nodes (3, 5, 7, 8, 10, 11), ANS2 six deterministic nodes, ANS3 feedback loop
review_gate -> extract, ANS4 three models, ANS5 LangGraph `StateGraph`. The input is only a directory path
(`python network.py <dir>`). Output specs OS1-OS9 are addressed by the nodes named in the results below.

## Final clean run (no checkpoints, 5 min 54 s)

20 documents -> 55 chunks -> 803 candidates -> **421 requirements + 25 blacklisted** (`output/requirements.md`, 379 kB;
analysis in `output/analysis.txt`).

| Spec | Result |
|---|---|
| OS1, OS2, OS5, OS6, OS9 | Self-check passes. 25 Must, 123 Should, 273 Could (16 stated in the source, 13 adjusted by the model). Average description 419 characters. |
| OS3 duplicates | Two identical names left. TF-IDF flags 86 similar pairs; the 15 most similar are distinct requirements (e.g. loans by facility vs by system), so only a few true duplicates remain. |
| OS4 tracing | All 20 documents contribute; 278 requirements from one document, 99 from two, 44 from three or more. |
| OS7 consistency | patron 327x vs user 45x, item 391x vs copy 13x; 4 conflicts found and blacklisted. |
| OS8 completeness | Reviewer found 8 / 4 / 3 missing items in the three rounds; 3 (0.4 %) remain open. |
| OS9 blacklist | 21 too vague or not about the software, 4 conflicts. The conflicts are the real ones: a separate reporting database vs the main relational database (twice), automatic item reversion vs the ban on it, and WorldCat integration vs the decision to exclude cataloging from the scope. No noise leaked into the requirements. |

## Findings

- The first design (one merge call over everything) left many duplicates; clustering by topic plus a second round fixed most of them.
- Moving all bookkeeping to code (ids, tracing, quotes, ordering, priority baseline) made the LLM nodes safe: every model answer
  is checked by id, clamped or replaced by a fallback. In the final run no priority or paragraph answer was missing or rejected.
- Three complete runs gave 446, 453 and 421 requirements and 1, 1 and 4 conflicts: the size is stable (+-4 %), the details are not,
  because LLM output is non-deterministic.
- A defect found in the final review: blacklist reasons sometimes cited internal candidate ids ("C050"). `assign_ids` now
  replaces them with REQ ids (tested).

## Limits

- The model benchmark was a single run on three chunks; there is no ground-truth set, so recall is estimated only from the
  reviewer (0.4 % open) and by spot checks.
- 31 of 803 quotes (3.9 %) are not contiguous text (a list heading joined with a bullet); they are flagged, not dropped.
- The WorldCat conflict is debatable (a stated need against a stated scope decision); the blacklist keeps the reason visible.
- Only three priority levels; "Won't" is unused because no source defers anything.
- Vocabulary is mostly unified, not perfectly (user 45x, location / library / branch variants).
- A third merge round and a larger benchmark would be the next steps; the current quality was judged sufficient.
