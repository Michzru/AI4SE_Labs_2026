"""Compare models on the requirement-extraction step (run: python benchmark_extract.py data/corpus)."""
import argparse
import re
import time
from concurrent.futures import ThreadPoolExecutor

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

from extraction import EXTRACTOR_PROMPT, ExtractionResult, build_user_message
from network import build_graph

MODELS = ["gpt-6-luna", "gpt-5.6-luna", "gpt-5.4-nano", "gpt-5-nano",
          "gpt-5-mini", "gpt-4.1-nano", "gpt-4o-mini"]
# (document id, chunk index) pairs covering different document types
SAMPLES = [("conversations/conv_pines021_item_purging.eml", 0),
           ("meeting_minutes/meeting_2009-07-20_minutes.txt", 1),
           ("early_draft_srs_galecia.txt", 3)]
NOISE = re.compile(r"costco|evelyn hugo|snacks", re.I)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def run(client, model, chunk):
    start = time.time()
    try:
        resp = client.chat.completions.parse(
            model=model,
            messages=[{"role": "system", "content": EXTRACTOR_PROMPT},
                      {"role": "user", "content": build_user_message(
                          chunk["doc_id"], chunk["index"], chunk["total"], chunk["text"])}],
            response_format=ExtractionResult,
            max_completion_tokens=16000,
        )
    except Exception as e:  # report and continue with the other models
        return dict(model=model, chunk=chunk, error=f"{type(e).__name__}: {str(e)[:100]}")
    reqs = resp.choices[0].message.parsed.requirements if resp.choices[0].message.parsed else []
    text = norm(chunk["text"])
    return dict(model=model, chunk=chunk, reqs=reqs, secs=time.time() - start,
                verbatim=sum(norm(r.evidence) in text for r in reqs),
                noise=sum(bool(NOISE.search(r.title + r.description)) for r in reqs),
                usage=resp.usage)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir")
    args = parser.parse_args()
    load_dotenv(find_dotenv(usecwd=True))
    chunks = build_graph(stop_after="chunk_documents").invoke({"input_dir": args.input_dir})["chunks"]
    picked = [next(c for c in chunks if c["doc_id"] == d and c["index"] == i) for d, i in SAMPLES]
    client = OpenAI()
    jobs = [(m, c) for m in MODELS for c in picked]
    with ThreadPoolExecutor(8) as pool:
        results = list(pool.map(lambda j: run(client, *j), jobs))

    print(f"{'model':13} {'sample':8} {'reqs':>4} {'verbatim':>8} {'noise':>5} {'secs':>5} {'in_tok':>6} {'out_tok':>7}")
    for r in results:
        sample = f"{r['chunk']['doc_id'].split('/')[-1][:8]}"
        if "error" in r:
            print(f"{r['model']:13} {sample:8} ERROR {r['error']}")
            continue
        u = r["usage"]
        print(f"{r['model']:13} {sample:8} {len(r['reqs']):>4} {r['verbatim']:>5}/{len(r['reqs']):<2} "
              f"{r['noise']:>5} {r['secs']:>5.1f} {u.prompt_tokens:>6} {u.completion_tokens:>7}")
    print("\nTitles on the e-mail sample (ground truth: weeding criteria, batch status change, "
          "last-copy report, delete volumes/records, last copy per library AND per system):")
    for r in results:
        if "error" not in r and r["chunk"]["doc_id"].endswith("item_purging.eml"):
            print(f"\n[{r['model']}]")
            for q in r["reqs"]:
                print("  -", q.title)


if __name__ == "__main__":
    main()
