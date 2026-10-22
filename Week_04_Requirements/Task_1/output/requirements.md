# Software Requirements

Generated 2026-10-22 from 20 source documents by an agentic LangGraph pipeline. 453 requirements, 22 blacklisted items.

## Priority scale

Priorities use three MoSCoW levels. Each requirement states below why it got its level.

- **Must** (26): Essential. Stated as high priority in a source document, or confirmed by several independent documents and strong wording. The system is not acceptable without it.
- **Should** (150): Important. Wanted by more than one document, or stated with strong wording, or marked medium priority. Include unless time is short.
- **Could** (277): Desirable. Mentioned once and without emphasis. Include if capacity allows.

How a level is chosen: an explicit priority tag in a source document is final. Otherwise it is computed from the number of distinct documents that mention the requirement and from emphatic wording in the stakeholders' own words; a language model may move the result by one level for content reasons.

## Overview

| ID | Requirement | Priority | Type | Sources |
|---|---|---|---|---|
| REQ-001 | Control Shared Report Access | Must | functional | 4 |
| REQ-002 | Report Missing and Damaged Items | Must | functional | 4 |
| REQ-003 | Authenticate Individual Staff Members | Must | functional | 1 |
| REQ-004 | Manage Role-Based Permissions | Must | functional | 5 |
| REQ-005 | Record Staff Login Identity | Must | functional | 1 |
| REQ-006 | Support Staff Login Methods | Must | functional | 3 |
| REQ-007 | Report System Last Copies | Must | functional | 3 |
| REQ-008 | Include Null and Blank Fields | Must | functional | 5 |
| REQ-009 | Query Transfer Candidates | Must | functional | 4 |
| REQ-010 | Save Transfer Queries | Must | functional | 3 |
| REQ-011 | Meet Accessibility Requirements | Must | non-functional | 3 |
| REQ-012 | Protect OPAC Performance | Must | non-functional | 2 |
| REQ-013 | Protect Open-Hours Operations | Must | non-functional | 2 |
| REQ-014 | Provide Role-Based Administrator Access | Must | functional | 2 |
| REQ-015 | Support Validated Technical Environments | Must | constraint | 3 |
| REQ-016 | Implement Role-Based Access | Must | functional | 1 |
| REQ-017 | Provide Hierarchical Cross-Linked Help | Must | functional | 3 |
| REQ-018 | Cancel Scheduled and Running Reports | Must | functional | 4 |
| REQ-019 | Provide Real-Time Reporting | Must | functional | 4 |
| REQ-020 | Document Record Data Specifications | Must | functional | 2 |
| REQ-021 | Preserve OPAC Functionality | Must | constraint | 2 |
| REQ-022 | Provide Browser Or Windows Access | Must | constraint | 2 |
| REQ-023 | Support Consortium Scale | Must | non-functional | 2 |
| REQ-024 | Prevent Prohibited Report Content | Must | constraint | 2 |
| REQ-025 | Relational Database Backend | Must | constraint | 1 |
| REQ-026 | Standards-Compliant HTML | Must | constraint | 1 |
| REQ-027 | Analyze Branch Capacity | Should | functional | 2 |
| REQ-028 | Analyze Patron Demographics | Should | functional | 3 |
| REQ-029 | Analyze Staff Productivity | Should | functional | 2 |
| REQ-030 | Construct Complex Queries | Should | functional | 1 |
| REQ-031 | Deliver Reports by Email | Should | functional | 2 |
| REQ-032 | Generate Consortium Statistics | Should | functional | 2 |
| REQ-033 | Generate Reports in Multiple Formats | Should | functional | 3 |
| REQ-034 | Manage Report Templates | Should | functional | 3 |
| REQ-035 | Provide Management Reporting | Should | functional | 2 |
| REQ-036 | Report Aged Debt | Should | functional | 2 |
| REQ-037 | Report Checked-Out Items | Should | functional | 2 |
| REQ-038 | Report Circulation by Location | Should | functional | 2 |
| REQ-039 | Report Deleted Item Counts | Should | functional | 2 |
| REQ-040 | Report Item Addition Counts | Should | functional | 2 |
| REQ-041 | Report Itemless Bibliographic Records | Should | functional | 3 |
| REQ-042 | Report Non-Cataloged Circulation | Should | functional | 2 |
| REQ-043 | Report Outstanding Patron Bills | Should | functional | 2 |
| REQ-044 | Report Overdue Items | Should | functional | 2 |
| REQ-045 | Report Patron Counts | Should | functional | 2 |
| REQ-046 | Report Patrons By Library | Should | functional | 2 |
| REQ-047 | Report Payments Received | Should | functional | 2 |
| REQ-048 | Report Renewal Counts | Should | functional | 2 |
| REQ-049 | Schedule Report Runs | Should | functional | 2 |
| REQ-050 | Show Report Queue Status | Should | functional | 3 |
| REQ-051 | Support Boolean Operators | Should | functional | 3 |
| REQ-052 | Break Down Material Volume | Should | functional | 2 |
| REQ-053 | Report Library Material Volume | Should | functional | 3 |
| REQ-054 | Manage Security Groups | Should | functional | 1 |
| REQ-055 | Show Branch Capacities | Should | functional | 2 |
| REQ-056 | Support Administrator Permissions | Should | functional | 1 |
| REQ-057 | Compare Shelf Space Metrics | Should | functional | 3 |
| REQ-058 | Generate Shelf Space Reports | Should | functional | 2 |
| REQ-059 | Combine Transit Directions | Should | functional | 3 |
| REQ-060 | Report Long In-Transit Items | Should | functional | 2 |
| REQ-061 | Audit Deleted Records | Should | functional | 2 |
| REQ-062 | Audit Record Deletions | Should | functional | 3 |
| REQ-063 | Batch Convert Item Statuses | Should | functional | 3 |
| REQ-064 | Configure Item Purge Criteria | Should | functional | 3 |
| REQ-065 | Delete Itemless Records | Should | functional | 2 |
| REQ-066 | Delete Volumes With Copies | Should | functional | 3 |
| REQ-067 | Generate Last Copy Report | Should | functional | 1 |
| REQ-068 | Prevent Accidental Mass Deletion | Should | non-functional | 1 |
| REQ-069 | Report Last Copies | Should | functional | 2 |
| REQ-070 | Analyze Patron Behavior | Should | functional | 2 |
| REQ-071 | Control Report Creation and Cloning | Should | functional | 2 |
| REQ-072 | Count Check-Ins By Method | Should | functional | 2 |
| REQ-073 | Count Checkouts By Method | Should | functional | 2 |
| REQ-074 | Cross-Tabulate Activity Data | Should | functional | 3 |
| REQ-075 | Report Geographic Patron Statistics | Should | functional | 2 |
| REQ-076 | Retain Transaction History | Should | functional | 2 |
| REQ-077 | Run or Modify Templates | Should | functional | 3 |
| REQ-078 | Show Report Queue Status | Should | functional | 3 |
| REQ-079 | Track Record Deletions | Should | functional | 3 |
| REQ-080 | Group Reports By Patron Characteristics | Should | functional | 3 |
| REQ-081 | Report by Patron Home Branch | Should | functional | 2 |
| REQ-082 | Report by Preferred Language | Should | functional | 2 |
| REQ-083 | Filter and Group Patrons by County | Should | functional | 2 |
| REQ-084 | Filter and Group Patrons by Type | Should | functional | 2 |
| REQ-085 | Group Patron Results by Age | Should | functional | 2 |
| REQ-086 | Group Patron Results by Zip | Should | functional | 2 |
| REQ-087 | Configure Inactive Report Scope | Should | functional | 2 |
| REQ-088 | Report Inactive Patrons | Should | functional | 2 |
| REQ-089 | Automatically Revert Transfers | Should | functional | 3 |
| REQ-090 | Identify Uncataloged Material Usage | Should | functional | 2 |
| REQ-091 | Integrate With WorldCat | Should | functional | 1 |
| REQ-092 | Report Overdue In-Transit Items | Should | functional | 2 |
| REQ-093 | Select Transfer Titles | Should | functional | 2 |
| REQ-094 | Track Uncataloged Inventory | Should | functional | 2 |
| REQ-095 | Transfer Item Batches | Should | functional | 3 |
| REQ-096 | Update Item Locations | Should | functional | 3 |
| REQ-097 | Provide Accessible Reporting Interfaces | Should | non-functional | 2 |
| REQ-098 | Report Invalid Item Types | Should | functional | 2 |
| REQ-099 | Report Item Edit Dates | Should | functional | 2 |
| REQ-100 | Report Long Call Numbers | Should | functional | 2 |
| REQ-101 | Separate System Environments | Should | functional | 4 |
| REQ-102 | Use Main Relational Database | Should | constraint | 2 |
| REQ-103 | Migrate Between Environments | Should | functional | 3 |
| REQ-104 | Provide Accessible Online Help | Should | functional | 3 |
| REQ-105 | Separate Reporting From OPAC | Should | constraint | 1 |
| REQ-106 | Centralize Multi-Location Management | Should | constraint | 3 |
| REQ-107 | Document Major System Processes | Should | functional | 3 |
| REQ-108 | Document Managed Record Specifications | Should | functional | 1 |
| REQ-109 | Ensure Standards-Compliant HTML | Should | non-functional | 2 |
| REQ-110 | Filter Surveys By Name | Should | functional | 2 |
| REQ-111 | Integrate With OPAC | Should | functional | 2 |
| REQ-112 | Interface with Vendor Systems | Should | constraint | 3 |
| REQ-113 | Operate Within Enterprise System | Should | constraint | 3 |
| REQ-114 | Provide High-Level Error Feedback | Should | functional | 3 |
| REQ-115 | Provide Historical Reporting | Should | functional | 3 |
| REQ-116 | Support Historical Reporting | Should | functional | 2 |
| REQ-117 | Comply With Audit Requirements | Should | constraint | 2 |
| REQ-118 | Maintain Payment Audit Trail | Should | functional | 1 |
| REQ-119 | Query High-Balance Accounts | Should | functional | 2 |
| REQ-120 | Report Patron Account Balances | Should | functional | 2 |
| REQ-121 | Report Payments by Period | Should | functional | 2 |
| REQ-122 | Report Waived Fines | Should | functional | 2 |
| REQ-123 | Track Library Financial Activity | Should | functional | 2 |
| REQ-124 | Update Financial Information | Should | non-functional | 2 |
| REQ-125 | Associate Financial Transactions | Should | functional | 2 |
| REQ-126 | Maintain Payment Audit Ledger | Should | functional | 2 |
| REQ-127 | Report Item Collection Values | Should | functional | 2 |
| REQ-128 | In-Transit Item Reports | Should | functional | 1 |
| REQ-129 | Provide Administrator Query Feedback | Should | functional | 2 |
| REQ-130 | Provide Context-Sensitive Help | Should | functional | 1 |
| REQ-131 | Support Required Browsers | Should | constraint | 2 |
| REQ-132 | Use Relational Database | Should | constraint | 1 |
| REQ-133 | Administer Report Permissions By Role | Should | functional | 1 |
| REQ-134 | Archive Transactions Privately | Should | functional | 1 |
| REQ-135 | Choose Picklist Values | Should | functional | 2 |
| REQ-136 | Display Report Criteria | Should | functional | 3 |
| REQ-137 | Enforce Fine-Grained Report Permissions | Should | functional | 2 |
| REQ-138 | Exclude Personal Identifiers | Should | constraint | 1 |
| REQ-139 | Maintain Template Consistency | Should | non-functional | 1 |
| REQ-140 | Provide Executive Reports | Should | functional | 2 |
| REQ-141 | Report Library Activity | Should | functional | 2 |
| REQ-142 | Restrict Ad Hoc Data Access | Should | functional | 1 |
| REQ-143 | Retain Required Transactions | Should | constraint | 1 |
| REQ-144 | Select Report Display Fields | Should | functional | 2 |
| REQ-145 | Simplify Permission Administration | Should | non-functional | 2 |
| REQ-146 | Design User-Friendly Queries | Should | functional | 2 |
| REQ-147 | Priority-Based Report Queuing | Should | functional | 1 |
| REQ-148 | Query Access Controls | Should | functional | 1 |
| REQ-149 | Run Or Modify Templates | Should | functional | 2 |
| REQ-150 | Analyze Patron Behavior | Should | functional | 1 |
| REQ-151 | Anonymize Demographic Data | Should | constraint | 1 |
| REQ-152 | Filter Items by Creation Date | Should | functional | 2 |
| REQ-153 | List Inactive Patrons | Should | functional | 2 |
| REQ-154 | Provide Pivot Table Output | Should | functional | 2 |
| REQ-155 | Provide Report Descriptions | Should | functional | 2 |
| REQ-156 | Provide Weeding Circulation Data | Should | functional | 2 |
| REQ-157 | Report Bibliographic Record Edits | Should | functional | 2 |
| REQ-158 | Report Bibliographic Records Added | Should | functional | 2 |
| REQ-159 | Report Circulation by Categories | Should | functional | 2 |
| REQ-160 | Report Circulation by County | Should | functional | 2 |
| REQ-161 | Report Collection Age | Should | functional | 2 |
| REQ-162 | Report Collection Value | Should | functional | 2 |
| REQ-163 | Report Fines Stopped Reasons | Should | functional | 2 |
| REQ-164 | Report Hold Placement Methods | Should | functional | 2 |
| REQ-165 | Report Holds Purchase Alerts | Should | functional | 2 |
| REQ-166 | Report Long-Overdue Items | Should | functional | 2 |
| REQ-167 | Report Patron Geographic Counts | Should | functional | 2 |
| REQ-168 | Report Staff Account Dates | Should | functional | 2 |
| REQ-169 | Report Stale Holds | Should | functional | 2 |
| REQ-170 | Report Unfilled Holds | Should | functional | 2 |
| REQ-171 | Report Voter Survey Responses | Should | functional | 2 |
| REQ-172 | Select Open Template Filters | Should | functional | 1 |
| REQ-173 | Support Appendix A Reports | Should | functional | 1 |
| REQ-174 | Support Appendix B Reports | Should | functional | 1 |
| REQ-175 | Support Open-Template Reporting | Should | functional | 2 |
| REQ-176 | Upload Text File Filters | Should | functional | 2 |
| REQ-177 | Use Iterative Prototyping | Could | constraint | 1 |
| REQ-178 | Create Custom Reports | Could | functional | 1 |
| REQ-179 | Display Reports to Patrons | Could | functional | 1 |
| REQ-180 | Enable Staff Report Creation | Could | functional | 1 |
| REQ-181 | Exclude Patron-Facing Operations | Could | constraint | 1 |
| REQ-182 | Expose Fields for Reporting | Could | functional | 1 |
| REQ-183 | Filter Report Data | Could | functional | 1 |
| REQ-184 | Provide Executive Reports Interface | Could | functional | 1 |
| REQ-185 | Report Bibliographic Counts | Could | functional | 1 |
| REQ-186 | Report Checkout Counts | Could | functional | 1 |
| REQ-187 | Save Report Definitions | Could | functional | 1 |
| REQ-188 | Schedule Multiple Reports | Could | functional | 1 |
| REQ-189 | Select Fields By Dragging | Could | functional | 1 |
| REQ-190 | Separate Create And Run Permissions | Could | functional | 1 |
| REQ-191 | Sort Report Data | Could | functional | 1 |
| REQ-192 | Support Consortium Administration | Could | functional | 1 |
| REQ-193 | Support Local Configuration | Could | functional | 1 |
| REQ-194 | Support Regular Expressions | Could | functional | 1 |
| REQ-195 | Track Financial Transactions | Could | functional | 1 |
| REQ-196 | Configure Item Categories | Could | functional | 1 |
| REQ-197 | Report Recent Acquisitions | Could | functional | 1 |
| REQ-198 | Show Status Counts Separately | Could | functional | 1 |
| REQ-199 | Color-Code Capacity Status | Could | functional | 1 |
| REQ-200 | Display Capacity Trends | Could | functional | 1 |
| REQ-201 | Drill Into Branch Details | Could | functional | 1 |
| REQ-202 | Export Capacity Data | Could | functional | 1 |
| REQ-203 | Sort And Filter Branches | Could | functional | 1 |
| REQ-204 | Support Department Head Permissions | Could | functional | 1 |
| REQ-205 | Support Front Desk Permissions | Could | functional | 1 |
| REQ-206 | Compare Local And System Results | Could | functional | 1 |
| REQ-207 | Estimate Shelf Space | Could | functional | 1 |
| REQ-208 | Filter Results By Date | Could | functional | 1 |
| REQ-209 | Report Circulation Percentages | Could | functional | 1 |
| REQ-210 | Report Collection Percentages | Could | functional | 1 |
| REQ-211 | Show Side-by-Side Comparisons | Could | functional | 1 |
| REQ-212 | Combined Transit Directions | Could | functional | 1 |
| REQ-213 | Default Transit Threshold | Could | constraint | 1 |
| REQ-214 | Due Date Sorting | Could | functional | 1 |
| REQ-215 | In-Transit Report Scope | Could | functional | 1 |
| REQ-216 | Include Condition Notes | Could | functional | 1 |
| REQ-217 | Report Missing and Damaged Items | Could | functional | 1 |
| REQ-218 | Support Report Date Ranges | Could | functional | 1 |
| REQ-219 | Activity-Based Purging | Could | functional | 1 |
| REQ-220 | Combine Purge Criteria | Could | functional | 1 |
| REQ-221 | Combined Purge Criteria | Could | functional | 1 |
| REQ-222 | Configure Item Purge Criteria | Could | functional | 1 |
| REQ-223 | Confirm Purge Deletions | Could | functional | 1 |
| REQ-224 | Preview Purge Candidates | Could | functional | 1 |
| REQ-225 | Scheduled Purging | Could | functional | 1 |
| REQ-226 | Time-Based Purging | Could | functional | 1 |
| REQ-227 | Deletion Confirmation | Could | functional | 1 |
| REQ-228 | Purge Candidate Utility | Could | functional | 1 |
| REQ-229 | Filter Deletions By Date | Could | functional | 1 |
| REQ-230 | Filter Deletions By Type | Could | functional | 1 |
| REQ-231 | Filter Deletions By User | Could | functional | 1 |
| REQ-232 | Provide Deletion Report Interface | Could | functional | 1 |
| REQ-233 | Rank Deleting Users | Could | functional | 1 |
| REQ-234 | Report Deletions By Location | Could | functional | 1 |
| REQ-235 | Report Deletions By System | Could | functional | 1 |
| REQ-236 | Show Deletion Totals | Could | functional | 1 |
| REQ-237 | Track Denied Deletion Attempts | Could | functional | 1 |
| REQ-238 | Count Holds By Placement | Could | functional | 1 |
| REQ-239 | Report Patron Transactions | Could | functional | 1 |
| REQ-240 | Calculate Age From Birth Date | Could | functional | 1 |
| REQ-241 | Combine Activity And Demographic Filters | Could | functional | 1 |
| REQ-242 | Combine Demographic Filters | Could | functional | 1 |
| REQ-243 | Configure Age Ranges | Could | functional | 1 |
| REQ-244 | Filter Patron Reports by Age | Could | functional | 1 |
| REQ-245 | Filter by Circulation Activity | Could | functional | 1 |
| REQ-246 | Handle Missing Demographics | Could | functional | 1 |
| REQ-247 | Report by County | Could | functional | 1 |
| REQ-248 | Report by Patron Type | Could | functional | 1 |
| REQ-249 | Report by Patron ZIP Code | Could | functional | 1 |
| REQ-250 | Combine Filters With Logic | Could | functional | 1 |
| REQ-251 | Configure Age Brackets | Could | functional | 1 |
| REQ-252 | Filter By Home Branch | Could | functional | 1 |
| REQ-253 | Group By Home Branch | Could | functional | 1 |
| REQ-254 | Cache Report Results | Could | non-functional | 1 |
| REQ-255 | Configure Inactivity Period | Could | functional | 1 |
| REQ-256 | Count Electronic Patron Activity | Could | functional | 1 |
| REQ-257 | Exclude Patron Types | Could | functional | 1 |
| REQ-258 | Export Report as CSV | Could | functional | 1 |
| REQ-259 | Include Mailing Addresses | Could | functional | 1 |
| REQ-260 | Measure Electronic Activity | Could | functional | 1 |
| REQ-261 | Process Reports in Background | Could | non-functional | 1 |
| REQ-262 | Separate Inactive Patrons Owing Fines | Could | functional | 1 |
| REQ-263 | Show Inactive Counts by Branch | Could | functional | 1 |
| REQ-264 | Configure Report Grouping | Could | functional | 1 |
| REQ-265 | Include Transactions in Statistics | Could | functional | 1 |
| REQ-266 | Record Deletion Reasons | Could | functional | 1 |
| REQ-267 | Migrate Report Configurations | Could | functional | 1 |
| REQ-268 | Process Reports in Background | Could | functional | 1 |
| REQ-269 | Use a Relational Database | Could | constraint | 2 |
| REQ-270 | Alert on Transfer Problems | Could | functional | 1 |
| REQ-271 | Efficient Large-Batch Processing | Could | non-functional | 1 |
| REQ-272 | Generate Transfer Pull Lists | Could | functional | 1 |
| REQ-273 | Preview Transfer Changes | Could | functional | 1 |
| REQ-274 | Print Transit Labels | Could | functional | 1 |
| REQ-275 | Restrict Transfer Permissions | Could | constraint | 1 |
| REQ-276 | Revert Unused Transfers | Could | functional | 1 |
| REQ-277 | Select Items For Transfer | Could | functional | 1 |
| REQ-278 | Share Saved Queries | Could | functional | 1 |
| REQ-279 | Status-Based Reversion | Could | functional | 1 |
| REQ-280 | Support Temporary Locations | Could | functional | 1 |
| REQ-281 | Track Transfer History | Could | functional | 1 |
| REQ-282 | Transaction-Safe Updates | Could | non-functional | 1 |
| REQ-283 | Undo Transfer Operations | Could | functional | 1 |
| REQ-284 | Cancel Running Reports | Could | functional | 1 |
| REQ-285 | Check Cancellation Signals | Could | constraint | 1 |
| REQ-286 | Ensure Complete Current Data | Could | non-functional | 1 |
| REQ-287 | Export Reports to CSV | Could | functional | 1 |
| REQ-288 | Export Reports to Excel | Could | functional | 1 |
| REQ-289 | Export Reports to HTML | Could | functional | 1 |
| REQ-290 | Handle Optional Vendor Data | Could | constraint | 1 |
| REQ-291 | Isolate Training Environment | Could | non-functional | 1 |
| REQ-292 | Keep OPAC Data Read-Only | Could | constraint | 1 |
| REQ-293 | Limit Library Manager Access | Could | functional | 1 |
| REQ-294 | Limit Staff Report Access | Could | functional | 1 |
| REQ-295 | Provide Global Administrator Access | Could | functional | 1 |
| REQ-296 | Provide Query-Specific Feedback | Could | functional | 1 |
| REQ-297 | Read Enterprise Library Data | Could | constraint | 1 |
| REQ-298 | Rely On Enterprise Infrastructure | Could | constraint | 1 |
| REQ-299 | Resolve Survey Names Internally | Could | functional | 1 |
| REQ-300 | Support Patron OPAC Access | Could | functional | 1 |
| REQ-301 | Enforce Data Retention | Could | constraint | 1 |
| REQ-302 | Join Financial Data Sources | Could | functional | 1 |
| REQ-303 | Report Accrued Charges | Could | functional | 1 |
| REQ-304 | Report Item Values | Could | functional | 1 |
| REQ-305 | Track Payments By Library | Could | functional | 1 |
| REQ-306 | Branch Item Damage Reports | Could | functional | 1 |
| REQ-307 | Cross-Branch Comparisons | Could | functional | 1 |
| REQ-308 | Data Quality Reports | Could | functional | 1 |
| REQ-309 | Financial Reporting | Could | functional | 1 |
| REQ-310 | Interact With The OPAC | Could | functional | 1 |
| REQ-311 | Inventory Capacity Reports | Could | functional | 1 |
| REQ-312 | Predefined Executive Reports | Could | functional | 1 |
| REQ-313 | Provide PINES-Wide Report Templates | Could | functional | 1 |
| REQ-314 | Queue Background Reports | Could | functional | 1 |
| REQ-315 | Run On Linux Solaris | Could | constraint | 1 |
| REQ-316 | Shelf Space Utilization | Could | functional | 1 |
| REQ-317 | Support Reliable Network Connectivity | Could | non-functional | 1 |
| REQ-318 | Weeding Reports | Could | functional | 1 |
| REQ-319 | Clone Existing Reports | Could | functional | 1 |
| REQ-320 | Display Report Queue Position | Could | functional | 1 |
| REQ-321 | Display Submission Time | Could | functional | 1 |
| REQ-322 | Query All Record Types | Could | functional | 1 |
| REQ-323 | Select Regular Expressions | Could | functional | 1 |
| REQ-324 | Clone Report Templates | Could | functional | 1 |
| REQ-325 | Query Picklists | Could | functional | 1 |
| REQ-326 | Regular Expression Queries | Could | functional | 1 |
| REQ-327 | Add Canned Reports | Could | functional | 1 |
| REQ-328 | Annual Holds Placed | Could | functional | 1 |
| REQ-329 | Archive Privacy-Protected Transactions | Could | constraint | 1 |
| REQ-330 | Background Report Processing | Could | functional | 1 |
| REQ-331 | Barred Patrons List | Could | functional | 1 |
| REQ-332 | Bib Records Missing MARC | Could | functional | 1 |
| REQ-333 | Bibliographic Records Count | Could | functional | 1 |
| REQ-334 | Break Down Circulation | Could | functional | 1 |
| REQ-335 | Cataloged In-House Use | Could | functional | 1 |
| REQ-336 | Check-In Count Report | Could | functional | 1 |
| REQ-337 | Checkout Count Report | Could | functional | 1 |
| REQ-338 | Circulation By Dewey | Could | functional | 1 |
| REQ-339 | Circulation By Home Library | Could | functional | 1 |
| REQ-340 | Circulation By MARC | Could | functional | 1 |
| REQ-341 | Circulation By Modifier | Could | functional | 1 |
| REQ-342 | Circulation Count by Dewey | Could | functional | 1 |
| REQ-343 | Circulation Count by MARC | Could | functional | 1 |
| REQ-344 | Claims Returned Report | Could | functional | 1 |
| REQ-345 | Claims Returned Report | Could | functional | 1 |
| REQ-346 | Clearly Define Criteria | Could | non-functional | 1 |
| REQ-347 | Combine Canned Report Output | Could | functional | 1 |
| REQ-348 | Configure Local Settings | Could | functional | 1 |
| REQ-349 | Consortium-Level System Administration | Could | functional | 1 |
| REQ-350 | Create Report Templates | Could | functional | 1 |
| REQ-351 | Customize Report Displays | Could | functional | 1 |
| REQ-352 | Deliver Prewritten Report Templates | Could | functional | 1 |
| REQ-353 | Detailed Voids Report | Could | functional | 1 |
| REQ-354 | Display Patron Transaction Counts | Could | functional | 1 |
| REQ-355 | Display Query Criteria | Could | functional | 1 |
| REQ-356 | Display Report Queue Position | Could | functional | 1 |
| REQ-357 | Edit Canned Report Options | Could | functional | 1 |
| REQ-358 | Edit Recurring Reports | Could | functional | 1 |
| REQ-359 | Enforce Report Permissions | Could | functional | 1 |
| REQ-360 | Ensure Reliable Output | Could | non-functional | 1 |
| REQ-361 | Enter Report Recipients | Could | functional | 1 |
| REQ-362 | Estimate Renewal Likelihood | Could | functional | 1 |
| REQ-363 | Exclude Renewals From Check-In Times | Could | functional | 1 |
| REQ-364 | Flatten MARC Fields | Could | functional | 1 |
| REQ-365 | Generate Historical Bills Snapshots | Could | functional | 1 |
| REQ-366 | Generate Pivot Table Output | Could | functional | 1 |
| REQ-367 | Generate Transaction Reports | Could | functional | 1 |
| REQ-368 | Group Transactions by Hour | Could | functional | 1 |
| REQ-369 | Group Transactions by System | Could | functional | 1 |
| REQ-370 | Group Transactions by Terminal | Could | functional | 1 |
| REQ-371 | High-Use Items Report | Could | functional | 1 |
| REQ-372 | Historical Snapshot Bills | Could | functional | 1 |
| REQ-373 | Integrated Report Help | Could | functional | 1 |
| REQ-374 | Items By Bib Content | Could | functional | 1 |
| REQ-375 | Items Count Report | Could | functional | 1 |
| REQ-376 | Items Received For Holds | Could | functional | 1 |
| REQ-377 | Items Sent For Holds | Could | functional | 1 |
| REQ-378 | Items by Total Use Count | Could | functional | 1 |
| REQ-379 | Last Circulation Field | Could | functional | 1 |
| REQ-380 | Last Copy Report | Could | functional | 1 |
| REQ-381 | List Added Items | Could | functional | 1 |
| REQ-382 | List Last-Copy Deletions | Could | functional | 1 |
| REQ-383 | Low-Use Weeding Report | Could | functional | 1 |
| REQ-384 | Maintain Email Address Book | Could | functional | 1 |
| REQ-385 | Manage Report Templates | Could | functional | 1 |
| REQ-386 | Measure Return Speed | Could | functional | 1 |
| REQ-387 | Merged Circulation Report | Could | functional | 1 |
| REQ-388 | Monthly Non-Cataloged Use | Could | functional | 1 |
| REQ-389 | Monthly Patron Additions | Could | functional | 1 |
| REQ-390 | New Patrons By Demographics | Could | functional | 1 |
| REQ-391 | Patron Survey Answer List | Could | functional | 1 |
| REQ-392 | Patrons By Expiration Date | Could | functional | 1 |
| REQ-393 | Patrons By Notes Text | Could | functional | 1 |
| REQ-394 | Patrons By Profile Group | Could | functional | 1 |
| REQ-395 | Patrons By Survey Answer | Could | functional | 1 |
| REQ-396 | Preserve Demographic Statistics | Could | functional | 1 |
| REQ-397 | Preserve Report Accuracy | Could | non-functional | 1 |
| REQ-398 | Prioritize Report Queue | Could | functional | 1 |
| REQ-399 | Produce Clean Excel Exports | Could | functional | 1 |
| REQ-400 | Provide Comparative Results | Could | functional | 1 |
| REQ-401 | Provide Financial Reports | Could | functional | 1 |
| REQ-402 | Provide Item Reports | Could | functional | 1 |
| REQ-403 | Provide Patron Reports | Could | functional | 1 |
| REQ-404 | Provide Required Basic Statistics | Could | functional | 1 |
| REQ-405 | Query Transaction Types | Could | functional | 1 |
| REQ-406 | Records Missing MARC Fields | Could | functional | 1 |
| REQ-407 | Records Without Volumes | Could | functional | 1 |
| REQ-408 | Report Accrued Charges | Could | functional | 1 |
| REQ-409 | Report Bibliographic Holds | Could | functional | 1 |
| REQ-410 | Report Branch Renewals | Could | functional | 1 |
| REQ-411 | Report Delivery Address Book | Could | functional | 1 |
| REQ-412 | Report Facility Last-Copy Deletions | Could | functional | 1 |
| REQ-413 | Report Held In-Transit Items | Could | functional | 1 |
| REQ-414 | Report Inactive Items | Could | functional | 1 |
| REQ-415 | Report Invalid Patron Libraries | Could | functional | 1 |
| REQ-416 | Report Item-Level Holds | Could | functional | 1 |
| REQ-417 | Report Items Edited | Could | functional | 2 |
| REQ-418 | Report Items in Transit | Could | functional | 1 |
| REQ-419 | Report Loans by Facility | Could | functional | 1 |
| REQ-420 | Report Loans by System | Could | functional | 1 |
| REQ-421 | Report Notice Activity | Could | functional | 1 |
| REQ-422 | Report Prioritization | Could | functional | 1 |
| REQ-423 | Report Status Conversion | Could | functional | 1 |
| REQ-424 | Report Title Tooltips | Could | functional | 1 |
| REQ-425 | Report Transaction Details | Could | functional | 1 |
| REQ-426 | Report Transaction Totals | Could | functional | 1 |
| REQ-427 | Report Transaction Types | Could | functional | 1 |
| REQ-428 | Restrict Query Data Access | Could | functional | 1 |
| REQ-429 | Retrieve Specific MARC Fields | Could | functional | 1 |
| REQ-430 | Revert Item Locations | Could | functional | 1 |
| REQ-431 | Run Local System Reports | Could | functional | 1 |
| REQ-432 | Run Multiple Reports Together | Could | functional | 1 |
| REQ-433 | Run On-Demand Reports | Could | functional | 1 |
| REQ-434 | Run Scoped Ad Hoc Reports | Could | functional | 1 |
| REQ-435 | Save Reusable Queries | Could | functional | 1 |
| REQ-436 | Schedule Historical Canned Reports | Could | functional | 1 |
| REQ-437 | Schedule Recurring Reports | Could | functional | 1 |
| REQ-438 | Select Query Results | Could | functional | 1 |
| REQ-439 | Select Regular Expressions | Could | functional | 1 |
| REQ-440 | Select Report Data | Could | functional | 1 |
| REQ-441 | Separate Checkin Timestamp | Could | constraint | 1 |
| REQ-442 | Separate Reporting Operations | Could | constraint | 1 |
| REQ-443 | Show Last Circulation Date | Could | functional | 1 |
| REQ-444 | Subtotal Holds by Type | Could | functional | 1 |
| REQ-445 | Support Custom Local Reports | Could | functional | 1 |
| REQ-446 | Support Item Transfer Methods | Could | functional | 1 |
| REQ-447 | Support Listed Report Types | Could | functional | 1 |
| REQ-448 | Support Related Record Reporting | Could | functional | 1 |
| REQ-449 | System Long-Overdue Items | Could | functional | 1 |
| REQ-450 | Three Reporting Interfaces | Could | functional | 1 |
| REQ-451 | Total Circulation Report | Could | functional | 1 |
| REQ-452 | Track Item Usage | Could | functional | 1 |
| REQ-453 | Verify Financial Transactions | Could | functional | 1 |

## Must requirements

### REQ-001 - Control Shared Report Access

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The system must provide shared folders for organizing and accessing reports. Administrators must be able to control whether staff can run specific reports in those folders.

> Shared folders to allow/disallow staff from running specific reports. (`survey_results_2009.txt`)
> Admins can create shared folders to allow or disallow staff from running specific reports, and/or to run ad hoc reports on specific sets of data. (`email_report_features.eml`)

### REQ-002 - Report Missing and Damaged Items

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide periodic reports identifying missing and damaged items, organized by branch and showing counts for auditing. The missing-items report must include items with a system status of lost as well as missing.

> - List of Items with a status of Missing (`early_draft_srs_galecia.txt`)
> - List of Items with Missing Status (`evergreen_reference_2009.txt`)

### REQ-003 - Authenticate Individual Staff Members

**Priority:** Must - Mentioned in 1 document; strong wording (must). Adjusted from Should by model: Individual staff authentication prevents shared identity/audit breakdown.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

Regardless of the login method used, the system must authenticate the specific staff member rather than allowing a shared or non-individual identity.

> The system must track WHICH staff member is logged in for audit purposes. The card is just a convenient way to identify the person, but it shouldn't bypass individual authentication entirely. (`email_staff_login.eml`)

### REQ-004 - Manage Role-Based Permissions

**Priority:** Must - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `early_draft_srs_galecia.txt`, `email_staff_login.eml`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must control staff permissions through assignable roles or security groups for individuals, workgroups, and other staff groups. Administrators must be able to manage access by assigning or changing roles rather than editing individual permissions, and the system must determine a staff member’s permissions from their assigned role after login.

> CO-4: User rights and privileges will be controlled through security groups and or "roles" that allow access control for individuals, workgroups, and arbitrary staff groups. (`early_draft_srs_galecia.txt`)
> we need user rights and privileges to be controlled through security groups and/or "roles." This would allow access control for individuals, workgroups, and arbitrary staff groups. (`email_staff_login.eml`)

### REQ-005 - Record Staff Login Identity

**Priority:** Must - Mentioned in 1 document; strong wording (must). Adjusted from Should by model: Recording login identity is necessary for auditing and accountability.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must record which individual staff member is logged in so that staff activity can be audited.

> The system must track WHICH staff member is logged in for audit purposes. (`email_staff_login.eml`)

### REQ-006 - Support Staff Login Methods

**Priority:** Must - Mentioned in 3 documents. Adjusted from Should by model: Staff authentication must support individual identity across login methods.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `early_draft_srs_galecia.txt`, `email_staff_login.eml`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

Staff must be able to log in using individual username-and-password credentials or an optional streamlined method such as swiping an employee card or RFID badge. The system must not require streamlined login hardware or require either login method, so branches can use supported alternatives.

> 1. System supports (but does not require) streamlined staff login methods, e.g. card swipe or individual login/password. (`email_staff_login.eml`)
> For example, a staff member could swipe a card (like an RFID employee badge) to log in, or alternatively use individual login credentials (username and password). (`early_draft_srs_galecia.txt`)

### REQ-007 - Report System Last Copies

**Priority:** Must - Mentioned in 3 documents; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a report identifying last-copy items at the library-system or consortium level, helping staff prevent accidental deletion and review copies before catalog maintenance.

> - Items that are the last copy in the system (`early_draft_srs_galecia.txt`)
> This is all great. One more thing - the "last copy report" should definitely be available per system, not just per library. We need to make sure no one accidentally deletes the last copy at the consortium level. (`conversations/conv_pines021_item_purging.eml`)

### REQ-008 - Include Null and Blank Fields

**Priority:** Must - Mentioned in 5 documents; strong wording (must).  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

Reports and queries must include records whose relevant fields are null or blank rather than omitting them, including patrons with missing optional characteristics. Missing values must be represented as null where applicable, regardless of filtering or display selections.

> Null values should be included in results (`conversations/conv_pines023_patron_characteristics.eml`)
> All nulls and blank fields must be included in the results no matter what is being filtered or displayed (`early_draft_srs_galecia.txt`)

### REQ-009 - Query Transfer Candidates

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The system must let users query for items that are candidates for transfer, using relevant criteria such as section and circulation inactivity.

> Query for candidate materials (`conversations/conv_pines018_item_transfer.eml`)
> - Ability to query for candidate materials (`early_draft_srs_galecia.txt`)

### REQ-010 - Save Transfer Queries

**Priority:** Must - Mentioned in 3 documents; strong wording (crucial).  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must let users save transfer queries for repeated use in transfer operations.

> The "save queries for repeated use" is crucial. We do this monthly - move all items in genre X that haven't circulated in 6 months. (`conversations/conv_pines018_item_transfer.eml`)
> - Ability to save queries for repeated use (`conversations/conv_pines018_item_transfer.eml`)

### REQ-011 - Meet Accessibility Requirements

**Priority:** Must - Marked as priority in the source document.  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must meet applicable accessibility requirements, including Section 508, and work with assistive technologies such as screen readers, screen-magnification software, JAWS, NVDA, and ZoomText.

> OE-5: The system must be accessible with screen-reading software, screen- magnification software, and other assistive technology programs designed to increase accessibility. (`early_draft_srs_galecia.txt`)
> As a public institution, we MUST comply with Section 508 accessibility requirements. (`interview_sysadmin_2009-05-10.txt`)

### REQ-012 - Protect OPAC Performance

**Priority:** Must - Mentioned in 2 documents; strong wording (must). Adjusted from Should by model: Must not degrade OPAC performance; critical system performance isolation.  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The management reporting system must not constrain or slow the OPAC. Large reporting queries must not degrade patrons' responsive access to the catalog.

> "We absolutely cannot constrain the OPAC," Robert emphasized. "The management reporting system is separate from the public catalog. If a report is running, it should not slow down the OPAC." (`meeting_tech_subcommittee_2009-06-30.txt`)
> The management reporting system must not constrain the OPAC in any way. These are separate concerns. Patrons need fast, responsive access to the catalog. (`interview_sysadmin_2009-05-10.txt`)

### REQ-013 - Protect Open-Hours Operations

**Priority:** Must - Marked as priority in the source document.  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_sysadmin_2009-05-10.txt`

Searches and reports must be processable during open hours without disrupting other system functions, including circulation operations.

> It is highly desirable that searches and reports can be processed during open hours without disrupting other system functions. (`early_draft_srs_galecia.txt`)
> The key requirement is that searches and reports can be processed during open hours without disrupting other system functions. (`interview_sysadmin_2009-05-10.txt`)

### REQ-014 - Provide Role-Based Administrator Access

**Priority:** Must - Mentioned in 2 documents. Adjusted from Should by model: RBAC and branch-level admin access; security-critical permissions.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must control permissions through roles or security groups, including patron, staff, Local Admin, and Global Admin access levels. Local Admins must have branch-level reporting and configuration access.

> The permission system needs to be controlled through security groups and/or "roles." (`interview_sysadmin_2009-05-10.txt`)
> - Local Admin: Branch-level reporting and configuration (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-015 - Support Validated Technical Environments

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must operate in the validated technical environment, including Linux servers (Red Hat Enterprise Linux) and Solaris 10 on SPARC hardware, and support Microsoft Internet Explorer 6.0 and later and Firefox 2.0 and later.

> OE-2: The system must operate on a Linux or Solaris server environment. (`early_draft_srs_galecia.txt`)
> So any reporting system needs to work on both Linux and Solaris. (`interview_sysadmin_2009-05-10.txt`)

### REQ-016 - Implement Role-Based Access

**Priority:** Must - Mentioned in 1 document; strong wording (essential). Adjusted from Should by model: Role-based access enforcement restricts data/functionality; core security.  
**Type:** functional  
**First mentioned:** 2009-05-12  
**Sources:** `interview_sysadmin_2009-05-10.txt`

The system must enforce role-based access control to restrict functionality or data according to user roles.

> - Role-based access control is confirmed as essential (`interview_sysadmin_2009-05-10.txt`)

### REQ-017 - Provide Hierarchical Cross-Linked Help

**Priority:** Must - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-05-12  
**Sources:** `early_draft_srs_galecia.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide online HTML help organized hierarchically, with cross-links between related topics to support navigation. The help must describe and illustrate system functions.

> Also, the help system needs to be online, hierarchical, and cross-linked. (`interview_sysadmin_2009-05-10.txt`)
> UD-3: The system must provide an online, hierarchical, and cross-linked help system in HTML that describes and illustrates all system functions. (`early_draft_srs_galecia.txt`)

### REQ-018 - Cancel Scheduled and Running Reports

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The system must allow users or authorized processes to cancel reports that are scheduled or currently running.

> Ability to cancel a report that has already been scheduled to run or is currently running (`early_draft_srs_galecia.txt`)
> - No ability to cancel a running report (`evergreen_reference_2009.txt`)

### REQ-019 - Provide Real-Time Reporting

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The reporting system must report against current data in real time, including during busy periods, so that results reflect current conditions rather than relying only on limited batch processing.

> - No real-time reporting (all reports are run on current data) (`evergreen_reference_2009.txt`)
> "Some reports need to be real-time - like 'what's overdue today,'" Robert said. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-020 - Document Record Data Specifications

**Priority:** Must - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The developer must provide complete data specifications, including data dictionaries, for authority, bibliographic, order, item, hold/request, and other records maintained or accessed by the Management Processes.

> UD-1: The developer must provide complete data specifications for authority records, bibliographic records, order records, item records, hold/request records, and other records maintained or accessed by the Management Processes. (`early_draft_srs_galecia.txt`)
> UD-1: The software developer shall provide complete data specifications for authority records, bibliographic records, order records, item records, hold/request records, and other records maintained or accessed by Management Processes. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-021 - Preserve OPAC Functionality

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

Management Processes requirements and implementation must not constrain or reduce the functionality or features of the Online Public Access Catalog module.

> CO-5: These requirements must not constrain functionality or features of the Online Public Access Catalog (OPAC) module. (`early_draft_srs_galecia.txt`)
> These requirements shall not constrain functionality or features of the Online Public Access Catalog (OPAC) module. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-022 - Provide Browser Or Windows Access

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

Management Processes must be accessible through a web browser or a client compatible with Microsoft Windows.

> OE-3: The system must be accessible through a web browser or a Windows-compatible client. (`early_draft_srs_galecia.txt`)
> Management Processes shall be accessible through a web-browser or a Windows-compatible client. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-023 - Support Consortium Scale

**Priority:** Must - Marked as priority in the source document.  
**Type:** non-functional  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

Management Processes must support a consortium of 286 locations, 17 million annual circulations, and the purchasing and processing of more than 900,000 items per year.

> OE-1: The system must support a library consortium with 286 locations, 17 million annual circulations, and purchasing/processing over 900,000 items per year. (`early_draft_srs_galecia.txt`)
> Management Processes must support the needs of a large, multiple-system library consortium. Specifically, the system must support a library consortium with 286 locations, 17 million annual circulations, purchasing and processing over 900,000 items per year. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-024 - Prevent Prohibited Report Content

**Priority:** Must - Mentioned in 2 documents. Adjusted from Should by model: Prevents prohibited content and deleted-item leakage; legal/content integrity risk.  
**Type:** constraint  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

Staff must not be able to modify report templates to expose content the template prohibits, including deleted items.

> Front-line staff can set a call number range for a weeding report or add/remove display fields from a pick list, but can't alter the template to display deleted items. (`email_report_features.eml`)
> For example, front-line staff could set a call number range for a weeding report or add/remove display fields from a pick list, but they should not be able to alter the template to display deleted items. (`early_draft_srs_galecia.txt`)

### REQ-025 - Relational Database Backend

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must use a fully relational database as its back-end data store.

> CO-1: The system must use a fully relational database back-end. (`early_draft_srs_galecia.txt`)

### REQ-026 - Standards-Compliant HTML

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

Web-based system components must produce HTML that complies with applicable standards.

> CO-2: The system must produce standards-compliant HTML output for web-based components. (`early_draft_srs_galecia.txt`)


## Should requirements

### REQ-027 - Analyze Branch Capacity

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must provide tools and management reports to analyze branch capacity and determine the optimal distribution of the collection across branches.

> Analyzing branch capacity and optimal distribution of the collection. (`early_draft_srs_galecia.txt`)
> - Analyzing branch capacity and optimal distribution of the collection (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-028 - Analyze Patron Demographics

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must support demographic analysis of patrons and their interests, including analysis for library program planning.

> Analyzing the demographics and interests of patrons. (`early_draft_srs_galecia.txt`)
> - Analyzing demographics and interests of patrons (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-029 - Analyze Staff Productivity

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must provide management reports and analysis tools for analyzing staff productivity and workflow.

> Analyzing staff productivity and workflow. (`early_draft_srs_galecia.txt`)
> - Analyzing staff productivity and workflow (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-030 - Construct Complex Queries

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Complex query building materially impacts report usefulness.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The report writer must support construction of complex queries rather than limiting users to simple query definitions.

> - Complex queries are difficult to construct (`evergreen_reference_2009.txt`)

### REQ-031 - Deliver Reports by Email

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The system must support delivering generated reports, including scheduled reports, by email.

> - No email delivery of reports (`evergreen_reference_2009.txt`)
> - No email delivery (reports can only be downloaded from the web interface) (`evergreen_reference_2009.txt`)

### REQ-032 - Generate Consortium Statistics

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The global system administrator must be able to generate statistical reports for the entire library consortium.

> The individual(s) who manage the ILS at the consortium level, implementing software changes and configurations, and generating statistical reports for the entire system. (`early_draft_srs_galecia.txt`)
> Global System Administrator: Manages PINES at the consortium level, implementing software changes and configurations, and generating statistical reports for PINES as a whole. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-033 - Generate Reports in Multiple Formats

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The reporting system must generate and export reports in multiple formats, including Excel, CSV, and HTML.

> Provide multiple output formats and scheduling options (`evergreen_reference_2009.txt`)
> Output would be in Excel, HTML, and CSV format (`early_draft_srs_galecia.txt`)

### REQ-034 - Manage Report Templates

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`

Administrators must be able to create report templates and make them available to staff, while restricting which filters and display fields individual staff may use or alter.

> System administrators should be able to create report templates that are available to staff. (`early_draft_srs_galecia.txt`)
> Admins need to create report templates that are available to staff. (`email_report_features.eml`)

### REQ-035 - Provide Management Reporting

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must provide management reports and analysis tools for managers, administrators, and staff to evaluate organizational performance, support planning and oversight, and analyze the collection and patron use. Reports must also support strategic planning and board presentations.

> Analyzing the Library collection and its use by patrons. (`early_draft_srs_galecia.txt`)
> - Analyzing the Library collection and its use by patrons (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-036 - Report Aged Debt

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a detailed report categorizing debt by age.

> - Aged Debt detailed report (partially available, needs enhancement) (`evergreen_reference_2009.txt`)
> - Aged Debt (`early_draft_srs_galecia.txt`)

### REQ-037 - Report Checked-Out Items

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report listing items that are currently checked out; the report may also provide their count.

> - Items Currently Checked Out (`early_draft_srs_galecia.txt`)

### REQ-038 - Report Circulation by Location

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide circulation counts organized by shelving location.

> - Circulation Count by Shelving Location (`early_draft_srs_galecia.txt`)

### REQ-039 - Report Deleted Item Counts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a predefined report showing the number of items deleted.

> - Items Deleted Count (`early_draft_srs_galecia.txt`)

### REQ-040 - Report Item Addition Counts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report showing the number of items added.

> - Items Added Count (`evergreen_reference_2009.txt`)

### REQ-041 - Report Itemless Bibliographic Records

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide reports identifying bibliographic records with no associated item records or attached volumes.

> Data quality reports - items with invalid item type, items with long call numbers, bibliographic records with no item records. (`interview_cataloging_2009-05-08.txt`)
> - Bibliographic records with no item records (`early_draft_srs_galecia.txt`)

### REQ-042 - Report Non-Cataloged Circulation

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must count transactions involving non-cataloged material, include them in circulation statistics and reports, and provide a report showing their count.

> Ability to count transactions and include in circulation statistics and reports. (`early_draft_srs_galecia.txt`)
> - Non-Cat Count (`early_draft_srs_galecia.txt`)

### REQ-043 - Report Outstanding Patron Bills

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report of bills currently owed by patrons.

> - Bills Currently Owed by Patrons (`evergreen_reference_2009.txt`)
> - Bills currently Owed by Patrons (`early_draft_srs_galecia.txt`)

### REQ-044 - Report Overdue Items

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report identifying items overdue by a specified or configurable number of days. The report must include daily, shelf-reading, and patron-contact information.

> - Items overdue by X days (daily, shelf reading, patron contact info) (`early_draft_srs_galecia.txt`)
> - Items Overdue by X Days (`evergreen_reference_2009.txt`)

### REQ-045 - Report Patron Counts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report showing the number of patrons.

> - Patron Count (`early_draft_srs_galecia.txt`)

### REQ-046 - Report Patrons By Library

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide patron counts grouped by home library.

> - Patron Count by Home Library (`evergreen_reference_2009.txt`)

### REQ-047 - Report Payments Received

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide detailed reports of payments received, including forgive, work, and goods payments.

> - Detailed Payments Received (`early_draft_srs_galecia.txt`)
> - Detailed Forgive, Work, and Goods Payments Received (`early_draft_srs_galecia.txt`)

### REQ-048 - Report Renewal Counts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a predefined report showing the number of renewals.

> - Renewals Count (`early_draft_srs_galecia.txt`)

### REQ-049 - Schedule Report Runs

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must let staff schedule canned reports to run immediately or on a recurring basis, with options for hourly, daily, weekly, monthly, and yearly schedules.

> Provide multiple output formats and scheduling options (`evergreen_reference_2009.txt`)
> a) Canned reports - generic reports set to run by the individual either ASAP or recurring (`early_draft_srs_galecia.txt`)

### REQ-050 - Show Report Queue Status

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `email_report_features.eml`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The reporting interface must let users see reports in the processing queue and show their position or current processing status, including whether they are waiting, running, or otherwise still processing.

> Status (waiting, running, completed, failed) (`email_report_features.eml`)
> REPORTS QUEUING: See position in queue, status, priority. (`email_report_features.eml`)

### REQ-051 - Support Boolean Operators

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`

The query tool must support Boolean operators for combining query conditions, including AND and OR.

> - Use a full range of Boolean operators (`early_draft_srs_galecia.txt`)
> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)

### REQ-052 - Break Down Material Volume

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`, `early_draft_srs_galecia.txt`

The material-volume report must support category breakdowns, including total items in the library, holds, adult fiction, and board books, and show the number of holds for each applicable category.

> Shows breakdowns with holds count per category (`conversations/conv_pines014_material_volume.eml`)
> The report should allow breaking down volume in categories such as: - Total items in library - Number of holds - Number of adult fiction - Number of board books (`conversations/conv_pines014_material_volume.eml`)

### REQ-053 - Report Library Material Volume

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must generate a report of the material volume held by a specified library, counting all items assigned to that library, including items checked in and checked out. The report must account for acquisitions, shelf inventory, and circulating inventory, and allow users to report volume as of a selected point in time for historical comparison without manually combining data from multiple screens.

> Quick question - how do I get a report that tells me how many items we have at Dalton-Whitman at any given moment? Not just total count, but broken down by categories. (`conversations/conv_pines014_material_volume.eml`)
> The volume should include: 1. New acquisitions (items recently added) 2. Items on the shelf (checked in) 3. Items out in circulation (checked out) (`conversations/conv_pines014_material_volume.eml`)

### REQ-054 - Manage Security Groups

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Manage security groups enables scalable access control.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must allow administrators to create and manage security groups used to control staff access.

> Administrators should be able to create and manage these groups. (`email_staff_login.eml`)

### REQ-055 - Show Branch Capacities

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`, `early_draft_srs_galecia.txt`

The system must provide an interface that displays the capacity of every branch simultaneously.

> The system should provide an interface showing the capacity of all branches. This should include: - High-level overview of all branches' capacity at once (`conversations/conv_pines015_capacity_interface.eml`)
> The system should provide an interface showing the capacity of all branches. (`early_draft_srs_galecia.txt`)

### REQ-056 - Support Administrator Permissions

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Administrator full access is core to manage system, but role exists.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must provide a system administrator role with full access to reports and permissions.

> System administrators (full access to all reports and permissions) (`email_staff_login.eml`)

### REQ-057 - Compare Shelf Space Metrics

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must report, for each genre and format, the percentage of total shelf space occupied, the percentage of the collection, and the percentage of total circulations.

> What percentage of total shelf space it occupies (`conversations/conv_pines016_shelf_space.eml`)
> The system should provide, for each genre and format of material, the ability to compare: - The percentage of total circulations - The percentage of the collection - The percentage of total shelf space (`conversations/conv_pines016_shelf_space.eml`)

### REQ-058 - Generate Shelf Space Reports

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`, `early_draft_srs_galecia.txt`

The system must generate shelf-space reports without requiring users to compile information manually, with results available for an individual library and aggregated for the entire library system.

> Currently I pull reports manually and make spreadsheets. It's tedious. (`conversations/conv_pines016_shelf_space.eml`)
> The report should be able to run per library and per system. (`early_draft_srs_galecia.txt`)

### REQ-059 - Combine Transit Directions

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The in-transit report must combine information about items traveling to and from locations in a single report for staff.

> And the report should merge transit-to and transit-from so front-line staff don't have to run two reports. (`conversations/conv_pines019_020_missing_intransit.eml`)
> It should merge the transit-to and transit-from into one report for ease of use. (`interview_cataloging_2009-05-08.txt`)

### REQ-060 - Report Long In-Transit Items

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`

The system must generate a report of items that have remained in transit longer than a configurable number of days, with results available by branch and for the entire system.

> I need to see what's been in-transit for more than X days (X should be configurable, probably 7 days default). (`conversations/conv_pines019_020_missing_intransit.eml`)
> System generates a list of items that have been in-transit for more than X days (X configurable), per branch and per system. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-061 - Audit Deleted Records

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `conversations/conv_pines022_deletions.eml`

The system must retain an audit trail for deleted items, patrons, and bibliographic records. Each audit record must identify the record type and identifier, the user who performed the deletion, the deletion timestamp, and the location where it occurred.

> Fields: record_type, record_id, deleted_by, deleted_at, location (`conversations/conv_pines022_deletions.eml`)
> We need to track who purged what and when. This is for accountability and troubleshooting. (`conversations/conv_pines021_item_purging.eml`)

### REQ-062 - Audit Record Deletions

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `conversations/conv_pines022_deletions.eml`, `survey_results_2009.txt`

The system must maintain an audit trail of purge and record deletion operations, implemented using database triggers that write events to an audit table. The audit trail must record the deleted record type, deletion timestamp, deleting user, the user’s location, and the location and system scope for tracking deletions. It should optionally capture the record’s pre-deletion status or associated reason, and support counting and tracking deletions.

> 3. Audit trail for all purges (`conversations/conv_pines021_item_purging.eml`)
> A trigger in the database that logs deletions to an audit table (`conversations/conv_pines022_deletions.eml`)

### REQ-063 - Batch Convert Item Statuses

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a report-assisted workflow that allows staff to convert the statuses of multiple items in a single batch operation.

> - Provide a report to assist in the conversion of items from one status to another (`conversations/conv_pines021_item_purging.eml`)
> The system should have a report to assist in the conversion of items from one status to another. (`early_draft_srs_galecia.txt`)

### REQ-064 - Configure Item Purge Criteria

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a utility and reports to identify item records for purging using configurable criteria, including the duration an item has been missing and whether it has a discard or weed status.

> I want the customizable criteria for purging to include: (`conversations/conv_pines021_item_purging.eml`)
> The system should provide a utility and reports for identifying item records to purge, based on customizable criteria such as: (`early_draft_srs_galecia.txt`)

### REQ-065 - Delete Itemless Records

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `interview_cataloging_2009-05-08.txt`

The system must provide a quick and effective operation for deleting records that have no items attached.

> We also need a quick way to delete volume entries along with copy entries, and delete records with no items attached. (`conversations/conv_pines021_item_purging.eml`)
> There also needs to be a quick, effective method for deleting volume entries along with copy entries, as well as records with no items attached. (`interview_cataloging_2009-05-08.txt`)

### REQ-066 - Delete Volumes With Copies

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a quick cleanup operation that deletes volume entries together with their associated copy entries, and can also delete records that have no items attached.

> - Provide a quick effective method for deleting volume entries along with copy entries, as well as records with no items attached (`conversations/conv_pines021_item_purging.eml`)
> The system should provide a quick effective method of deleting volume entries along with copy entries, as well as records with no items attached. (`early_draft_srs_galecia.txt`)

### REQ-067 - Generate Last Copy Report

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must generate a report identifying item records that are the only copy within a selected scope, so catalogers can avoid accidentally deleting the last available copy.

> CRITICAL: We need a "last copy report" that identifies our library system's last copies. This helps catalogers update WorldCat entries so we don't accidentally delete the only copy in the consortium. (`conversations/conv_pines021_item_purging.eml`)

### REQ-068 - Prevent Accidental Mass Deletion

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Mass-deletion safeguards; baseline Could but safety suggests Should.  
**Type:** non-functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must provide safeguards that reduce the risk of users accidentally deleting an entire collection during cleanup or purging.

> "Customizable criteria" is great, but we need to make sure the system is safe - we don't want someone accidentally deleting their entire collection. (`conversations/conv_pines021_item_purging.eml`)

### REQ-069 - Report Last Copies

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `evergreen_reference_2009.txt`

The reporting system must provide a last-copy report that can identify whether an item is the only copy at an individual library or across the entire PINES system.

> - Last Copy Report (partially available, needs enhancement) (`evergreen_reference_2009.txt`)
> For the last copy report - is this per library or per system? I think we need both views. (`conversations/conv_pines021_item_purging.eml`)

### REQ-070 - Analyze Patron Behavior

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must produce statistics that support understanding and prediction of patron behavior and material usage.

> The system should produce statistics that can be used to understand and predict patron behavior and use of materials. (`early_draft_srs_galecia.txt`)
> System produces statistics to understand/predict patron behavior and use of materials. (`survey_results_2009.txt`)

### REQ-071 - Control Report Creation and Cloning

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must provide distinct, fine-grained permissions controlling who can create and clone reports.

> Fine-grained permissions limit who can create and clone reports. (`survey_results_2009.txt`)
> The system should provide distinct, fine-grained permission levels that limit who can create and clone reports. (`early_draft_srs_galecia.txt`)

### REQ-072 - Count Check-Ins By Method

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must report check-in counts separately and cumulatively by method, including book-drop, terminal, user-initiated, and self-service check-ins.

> I need to see check-in counts broken down by method - book drop vs terminal vs self-service (`survey_results_2009.txt`)
> The system counts all types of check-in individually and cumulatively: - book-drop - by terminal - by user or self-service (`early_draft_srs_galecia.txt`)

### REQ-073 - Count Checkouts By Method

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must report checkout and renewal counts separately and cumulatively by method, including staff checkouts, self-checkouts, staff renewals, self-checkout renewals, online renewals, and OPAC renewals.

> Check-out types should be counted separately - staff checkout, self checkout, staff renewal, self checkout renewal, online renewal, OPAC renewal (`survey_results_2009.txt`)
> The system counts all types of check-out individually and cumulatively: - staff check-out - self check-out - staff renewal - self checkout renewal - online renewal - OPAC renewal (`early_draft_srs_galecia.txt`)

### REQ-074 - Cross-Tabulate Activity Data

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `survey_results_2009.txt`

The system must support grouping and cross-tabulating transaction and activity data by terminal, branch, system, hour, patron age range, patron type, and patron location. This capability must also be available in board reports.

> Transactions can be grouped by hour, terminal, branch, and system. (`early_draft_srs_galecia.txt`)
> It should be possible to cross-tabulate per terminal, per branch, per library system, per hour, per patron age range, per patron type, and per patron location. (`early_draft_srs_galecia.txt`)

### REQ-075 - Report Geographic Patron Statistics

**Priority:** Should - Mentioned in 2 documents; strong wording (must).  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must provide patron counts and demographic statistics by geographic region, including county, city, and ZIP code, and by age range. Demographic reports must exclude personally identifiable information.

> The system should produce useful demographic statistics, including transactions by geographical regions, age ranges, etc. (`early_draft_srs_galecia.txt`)
> Transactions by geographical regions - Transactions by age ranges (`survey_results_2009.txt`)

### REQ-076 - Retain Transaction History

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must retain transaction history for a configurable number of days and preserve monthly and annual aggregate transaction data indefinitely.

> Transaction history is maintained for X days (X is configurable). (`early_draft_srs_galecia.txt`)
> Monthly and annual aggregate information is maintained indefinitely. (`early_draft_srs_galecia.txt`)

### REQ-077 - Run or Modify Templates

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `survey_results_2009.txt`

The system must allow staff to run an available report template unchanged or modify it before execution, including editing selection criteria and display options.

> Report templates can be created by administrators and run as-is or modified. (`survey_results_2009.txt`)
> b) Noncanned or On Demand Reports - preset but have the ability to edit selection criteria and display options (`early_draft_srs_galecia.txt`)

### REQ-078 - Show Report Queue Status

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `email_report_features.eml`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `survey_results_2009.txt`

The system must allow users to view the report queue's status or contents, including the current position of their report in the queue.

> - Report queue visibility is important (`meeting_minutes/meeting_2009-07-20_minutes.txt`)
> Ability to see where your report is in the queue. (`survey_results_2009.txt`)

### REQ-079 - Track Record Deletions

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-27  
**Sources:** `conversations/conv_pines022_deletions.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must count and track deletions of item and patron records by location and across the entire library system.

> Yes, we need to count and track record deletions per location and per system. (`interview_cataloging_2009-05-08.txt`)
> The system should count and track record deletions (e.g., item records, patron records) per location and per system. (`conversations/conv_pines022_deletions.eml`)

### REQ-080 - Group Reports By Patron Characteristics

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must allow report results and activity measures, including circulation, checkout, and patron counts, to be grouped by supported patron characteristics, including age demographics.

> - Circulation Count by Age Demographic (`early_draft_srs_galecia.txt`)
> - Circulation Count by Age Demographic (not available) (`evergreen_reference_2009.txt`)

### REQ-081 - Report by Patron Home Branch

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must allow patron reports to be filtered or grouped by the patron’s home branch.

> - Home branch (`conversations/conv_pines023_patron_characteristics.eml`)
> Queries and reports can be limited or grouped by various patron characteristics, including: - home branch (`early_draft_srs_galecia.txt`)

### REQ-082 - Report by Preferred Language

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must support patron preferred language as a reporting characteristic, allowing patron queries and reports to filter and group results by preferred language.

> - Preferred language (`conversations/conv_pines023_patron_characteristics.eml`)
> Queries and reports can be limited or grouped by various patron characteristics, including: - preferred language (`early_draft_srs_galecia.txt`)

### REQ-083 - Filter and Group Patrons by County

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must allow patron queries and reports to filter and group results by county of residence.

> - County of residence (`conversations/conv_pines023_patron_characteristics.eml`)
> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - County of residence (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-084 - Filter and Group Patrons by Type

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must allow patron queries and reports to filter and group results by patron type.

> - Patron type (`conversations/conv_pines023_patron_characteristics.eml`)
> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Patron type (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-085 - Group Patron Results by Age

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must allow patron results to be grouped by age range. Patron queries and reports must also support limitation by age range.

> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Age range (`conversations/conv_pines023_patron_characteristics.eml`)
> Queries and reports can be limited or grouped by various patron characteristics, including: - age range (`early_draft_srs_galecia.txt`)

### REQ-086 - Group Patron Results by Zip

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must allow patron results to be grouped by zip code. Patron queries and reports must also support limitation by zip code.

> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Zip code (`conversations/conv_pines023_patron_characteristics.eml`)
> Queries and reports can be limited or grouped by various patron characteristics, including: - zip code (`early_draft_srs_galecia.txt`)

### REQ-087 - Configure Inactive Report Scope

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`, `early_draft_srs_galecia.txt`

The system must allow the inactive-patron report to be generated at configurable organizational levels, including the system, home library, and county where applicable.

> The list should be configurable to different levels - System, Home Library, County, etc. (`conversations/conv_pines024_inactive_patrons.eml`)
> The list should be configurable to System, Home Library, County, etc. (`early_draft_srs_galecia.txt`)

### REQ-088 - Report Inactive Patrons

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`, `early_draft_srs_galecia.txt`

The system must generate a list of patrons who have had no circulation or electronic activity during a configurable period of preceding days.

> We need a report that shows patrons with no circulation or electronic activity in the last X days. (`conversations/conv_pines024_inactive_patrons.eml`)
> The system should generate a list of patrons with no circulation or electronic activity in the last X days (X configurable). (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-089 - Automatically Revert Transfers

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must return transferred items to their original locations automatically after a specified period or when configured conditions are met.

> Auto-revert mechanism - a scheduled task that checks transferred items and reverts them based on time or status criteria. (`conversations/conv_pines018_item_transfer.eml`)
> Revert after X days (date-based) (`conversations/conv_pines018_item_transfer.eml`)

### REQ-090 - Identify Uncataloged Material Usage

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a way to identify how uncataloged materials are being used.

> - Ability to identify how the material is being used (`early_draft_srs_galecia.txt`)
> The requirements are: quick distribution (we need to process these fast), minimal branch labor (we can't spend a lot of time per item), and ability to identify how the material is being used. (`interview_cataloging_2009-05-08.txt`)

### REQ-091 - Integrate With WorldCat

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `interview_cataloging_2009-05-08.txt`

The system must integrate with WorldCat to assist catalogers in reviewing, editing, or processing records for which an item is the last copy in a library system.

> And the last copy report is CRITICAL. This singles out a library system's last copies, to assist catalogers who need to edit WorldCat entries. (`interview_cataloging_2009-05-08.txt`)
> The last copy report and WorldCat integration are critical (`interview_cataloging_2009-05-08.txt`)

### REQ-092 - Report Overdue In-Transit Items

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must report items that have remained in transit longer than a specified, configurable number of days, with results available by branch and across the entire system.

> - Items that have been in-transit for more than X days (`early_draft_srs_galecia.txt`)
> The report should show items that have been in-transit for more than X days (configurable), per branch and per system. (`interview_cataloging_2009-05-08.txt`)

### REQ-093 - Select Transfer Titles

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The item-transfer utility must allow users to manually select titles from query results for targeted transfers.

> - Ability to manually select titles from query results (`early_draft_srs_galecia.txt`)
> Third, we need to manually select titles from query results if we want to be more targeted. (`interview_cataloging_2009-05-08.txt`)

### REQ-094 - Track Uncataloged Inventory

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must track uncataloged materials as inventory before individual catalog records are created, including shipments such as paperback books and children's board books.

> Ability to control inventory of uncataloged material, such as paperback books and children's board books. (`early_draft_srs_galecia.txt`)
> We need to be able to track these as inventory even though they're not fully cataloged. (`interview_cataloging_2009-05-08.txt`)

### REQ-095 - Transfer Item Batches

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a utility for transferring multiple items in a single batch between branches or other locations, including mobile libraries, outreach collections, and just-in-time warehouses.

> We often need to move batches of items between branches - for example, sending books to a mobile library unit or to an outreach program collection. (`interview_cataloging_2009-05-08.txt`)
> I need a utility for transferring batches of items between branches. We often need to move books to a mobile library, to an outreach program, or to a "just-in-time" warehouse. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-096 - Update Item Locations

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The item transfer utility must allow users to change the records and related location data of selected items so that they are assigned to a new location. Authorized users must be able to perform these transfers.

> Change records of selected items to new location - Mechanisms: changing location field, generating pull lists (`conversations/conv_pines018_item_transfer.eml`)
> - Ability to change records of selected items to move to new location (`conversations/conv_pines018_item_transfer.eml`)

### REQ-097 - Provide Accessible Reporting Interfaces

**Priority:** Should - Mentioned in 2 documents.  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`

The reporting interfaces and capabilities must support accessibility. HTML output must use alt tags, ARIA labels, and proper semantic structure, and conform to applicable HTML standards.

> Implement accessibility compliance (`evergreen_reference_2009.txt`)
> - No accessibility support for report interface (`evergreen_reference_2009.txt`)

### REQ-098 - Report Invalid Item Types

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide periodic data-quality reports identifying items with invalid item types.

> - Items with invalid item type (`early_draft_srs_galecia.txt`)
> Data quality reports - items with invalid item type, items with long call numbers, bibliographic records with no item records. (`interview_cataloging_2009-05-08.txt`)

### REQ-099 - Report Item Edit Dates

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `evergreen_reference_2009.txt`, `interview_cataloging_2009-05-08.txt`

Reports must show an item's last edit date separately from its last circulation date. Circulation activity must not be treated as an item edit.

> - Last edit date not including last circulation - does not exist (`evergreen_reference_2009.txt`)
> I need to be able to see the last edit date on reports, but it should be only when the item is edited and not include the last circulation. The current system combines these dates. (`interview_cataloging_2009-05-08.txt`)

### REQ-100 - Report Long Call Numbers

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide reports identifying items with call numbers that exceed the permitted length, including periodic reporting.

> - Items with a long call number (`early_draft_srs_galecia.txt`)
> Data quality reports - items with invalid item type, items with long call numbers, bibliographic records with no item records. (`interview_cataloging_2009-05-08.txt`)

### REQ-101 - Separate System Environments

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide separate development, training, and production environments so reports can be tested and practiced without affecting production. It must support migrating environment configurations, including report templates and other configurations, from development or training into production.

> CO-3: The system must provide a development and training environment with the ability to migrate configurations to a production environment. (`early_draft_srs_galecia.txt`)
> - No development/training environment separation (`evergreen_reference_2009.txt`)

### REQ-102 - Use Main Relational Database

**Priority:** Should - Mentioned in 2 documents.  
**Type:** constraint  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system should use the main relational database for reporting data and avoid requiring a separate denormalized reporting schema or a synchronized reporting warehouse.

> I'd prefer to keep everything in the main relational database. (`interview_sysadmin_2009-05-10.txt`)
> "I strongly recommend against denormalization for reporting," Robert said. "Maintaining sync between a reporting warehouse and the live database creates more problems than it solves." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-103 - Migrate Between Environments

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-05-12  
**Sources:** `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide separate development and training environments and support migration of relevant content and configuration between development, training, and production. Migration must include exporting and importing templates, permission settings, and saved queries.

> - No configuration migration between environments (`evergreen_reference_2009.txt`)
> Provide a development/training environment with migration capability (`evergreen_reference_2009.txt`)

### REQ-104 - Provide Accessible Online Help

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-05-12  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide online HTML help that staff can use for routine instructions, including running reports, without contacting IT. The help must be searchable, easy to navigate, hierarchical, cross-linked, comprehensive enough to describe and illustrate all system functions, and accessible to screen-reader users.

> Also, the help system needs to be online, hierarchical, and cross-linked. Staff shouldn't have to call IT every time they want to know how to run a report. (`interview_sysadmin_2009-05-10.txt`)
> The HTML help needs to be searchable and easy to navigate. (`interview_sysadmin_2009-05-10.txt`)

### REQ-105 - Separate Reporting From OPAC

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** constraint  
**First mentioned:** 2009-05-12  
**Sources:** `interview_sysadmin_2009-05-10.txt`

The system must keep reporting functionality separate from the OPAC.

> - Separation of reporting from OPAC is critical (`interview_sysadmin_2009-05-10.txt`)

### REQ-106 - Centralize Multi-Location Management

**Priority:** Should - Mentioned in 3 documents.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

Management Processes must be consolidated at a central location while accepting input from and providing services to multiple library locations.

> AS-2: Management Processes are consolidated at a central location, and accept input and provide services to multiple locations. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)
> AS-2: Management Processes are consolidated at a central location, and accept input and provide services to multiple locations. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-107 - Document Major System Processes

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The developer must provide thorough, high-level documentation of major system processes, including bibliographic record import and export, validation against internal and external authority sources, and standard reporting.

> UD-2: The developer must provide a thorough high-level description of major processes, including bibliographic record import and export, validation of bibliographic records against internal and external authority sources, and standard reports. (`early_draft_srs_galecia.txt`)
> UD-2: The software developer shall provide a thorough high-level description of major processes, including bibliographic record import and export, validation of bibliographic records against internal and external authority sources, and standard reports. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-108 - Document Managed Record Specifications

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The developer must provide complete data specifications for authority, bibliographic, order, hold and request, and other records maintained or accessed by Management Processes. Specifications must include field names, data types, and relationships where applicable.

> The developer must provide complete data specifications for: - Authority records (`meeting_tech_subcommittee_2009-06-30.txt`)
> The developer must provide complete data specifications for: - Bibliographic records (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-109 - Ensure Standards-Compliant HTML

**Priority:** Should - Mentioned in 2 documents.  
**Type:** non-functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

Web output, including help and report output, must comply with HTML and W3C standards and be compatible with different browsers and assistive technologies.

> "We need to make sure all HTML output validates against W3C standards," Robert noted. (`meeting_tech_subcommittee_2009-06-30.txt`)
> "We need to make sure all HTML output validates against W3C standards," Robert noted. "This isn't just about looks - it's about compatibility with different browsers and assistive technologies." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-110 - Filter Surveys By Name

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must allow reports or survey queries to be filtered by survey name without requiring staff to enter the survey ID.

> Ability to select the survey name and not have to enter the survey id for filtering (`early_draft_srs_galecia.txt`)
> The ability to filter by survey name rather than survey ID requires the system to resolve names to IDs internally. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-111 - Integrate With OPAC

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

Management Processes must interact with the patron-facing OPAC to access data generated by patron holds and circulation transactions.

> DE-3: Management Processes interact with a patron interface, also known as an Online Public Access Catalog (OPAC). (`early_draft_srs_galecia.txt`)
> DE-3: Management Processes interact with a patron interface (OPAC). "Patrons create holds and circulation transactions through the OPAC," Robert said. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-112 - Interface with Vendor Systems

**Priority:** Should - Mentioned in 3 documents.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

Management Processes must interface with vendor websites through published APIs or automated transfers of standard-format data files, including formats such as USMARC21 and EDIFACT.

> DE-2: Management Processes interface with a variety of vendor websites, via published APIs and/or automated transfer of standard-format data files (e.g., USMARC21, EDIFACT). (`early_draft_srs_galecia.txt`)
> DE-2: Management Processes interface with a variety of vendor websites, via published APIs and/or automated transfer of standard-format data files (e.g., USMARC21, EDIFACT). (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-113 - Operate Within Enterprise System

**Priority:** Should - Mentioned in 3 documents.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

Management Processes must operate as part of an enterprise-level Library Automation System, relying on its data structures and functionality, including Acquisitions and Cataloging, and on enterprise-grade infrastructure.

> DE-1: Management Processes rely on the data structures and functionality of an enterprise-level Library Automation System, including Acquisitions and Cataloging modules. (`early_draft_srs_galecia.txt`)
> AS-1: Management Processes are part of an enterprise-level Library Automation System. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-114 - Provide High-Level Error Feedback

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide thorough, high-level error reporting and feedback when operations or reports fail.

> UD-4: The system must provide thorough high-level error reporting and feedback, and shall allow low-level query-specific feedback for Local and Global System Administrators from the front-end interface. (`early_draft_srs_galecia.txt`)
> UD-4: The system shall provide thorough high-level error reporting and feedback and shall allow low-level query-specific feedback for Local and Global System Administrators from the front-end interface. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-115 - Provide Historical Reporting

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The reporting system must show data as it existed on a specified historical date or within a specified date range. This includes values such as bill amounts and shelving locations as they were at that time, even if they have since changed.

> Ability to have historical reporting - a reporting warehouse such that data can be acquired on a given date or date range (`early_draft_srs_galecia.txt`)
> "Others are historical - 'what was the bill amount on June 30th?' We probably need a reporting warehouse for historical data." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-116 - Support Historical Reporting

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must provide a historical reporting warehouse or an equivalent repository to support reporting on historical data.

> - Historical reporting warehouse - does not exist (`evergreen_reference_2009.txt`)
> - No historical reporting warehouse (`evergreen_reference_2009.txt`)

### REQ-117 - Comply With Audit Requirements

**Priority:** Should - Mentioned in 2 documents; strong wording (must).  
**Type:** constraint  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system's reports and archived data must comply with standard accounting practices and applicable state, county, and municipal auditing requirements.

> All reports and data archiving must comply with standard accounting practice and state, county, and municipal auditing requirements. (`early_draft_srs_galecia.txt`)
> Compliance - all reports and data archiving must comply with standard accounting practice and state, county, and municipal auditing requirements. (`email_financial_reports.eml`)

### REQ-118 - Maintain Payment Audit Trail

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must maintain a financial ledger of patron payments that identifies the specific charge or charges to which each payment was applied, allowing finance staff to trace payments and reconcile accounts.

> The financial audit trail is CRITICAL for our finance department. They need to be able to trace every payment back to the specific charge it was applied to. (`email_financial_reports.eml`)

### REQ-119 - Query High-Balance Accounts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

Staff must be able to query patron accounts whose balances exceed a specified dollar threshold. Payment-method reporting must distinguish cash, credit card, check, and other applicable methods for daily reconciliation.

> The financial reports need to show payments by method - cash, credit card, check, etc. This helps with daily reconciliation. (`email_financial_reports.eml`)
> As an example, a staff user can easily query patron accounts with balances greater than X dollars. (`early_draft_srs_galecia.txt`)

### REQ-120 - Report Patron Account Balances

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must report patron account balances organized by patron, home library, and the overall library system.

> Patron account balances by patron, home library, and system (`email_financial_reports.eml`)
> patron account balances by patron, home library, and system (`early_draft_srs_galecia.txt`)

### REQ-121 - Report Payments by Period

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must report payments for selected time periods, categorized by payment method and payment channel. Supported methods include cash, credit card, and check; supported channels include the staff desk, self-check station, and OPAC.

> payments made per time period and per payment method (e.g., staff desk, self-check station, OPAC) (`early_draft_srs_galecia.txt`)
> Payments made per time period and per payment method (staff desk, self-check, OPAC) (`email_financial_reports.eml`)

### REQ-122 - Report Waived Fines

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must report fines waived for selected time periods and by branch.

> fines waived per time period and per branch (`early_draft_srs_galecia.txt`)
> Fines waived per time period and per branch (`email_financial_reports.eml`)

### REQ-123 - Track Library Financial Activity

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must track fines waived and payments made for each library, with waived fines recorded separately for each library to support independent budget management.

> System tracks fines waived and payments made per library. (`early_draft_srs_galecia.txt`)
> Fines waived should be tracked per library because each library has its own budget for waived fines. (`email_financial_reports.eml`)

### REQ-124 - Update Financial Information

**Priority:** Should - Mentioned in 2 documents.  
**Type:** non-functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

Staff must be able to update financial information easily, and payments made at a front desk must be reflected in the system immediately.

> Financial information can be updated easily. (`early_draft_srs_galecia.txt`)
> Financial information needs to be easily updatable. When a patron makes a payment at the front desk, we need the system to reflect that immediately. (`email_financial_reports.eml`)

### REQ-125 - Associate Financial Transactions

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-14  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must associate fines, charges, waivers, and ecommerce transactions with patron and item records.

> Fines, charges, waivers, and ecommerce transactions are attached to patron and item records. (`early_draft_srs_galecia.txt`)
> Fines, charges, waivers, and ecommerce transactions are attached to patron and item records. (`email_financial_reports.eml`)

### REQ-126 - Maintain Payment Audit Ledger

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-14  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must maintain a ledger of patron payments that identifies the charges to which each payment is applied, supporting financial reconciliation.

> The system maintains a ledger of patron payments, including which charges payments are applied to, to facilitate reconciliation. (`early_draft_srs_galecia.txt`)
> The system maintains a ledger of patron payments, including which charges payments are applied to, to facilitate reconciliation. (`email_financial_reports.eml`)

### REQ-127 - Report Item Collection Values

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-14  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must generate reports of item values using data from item records, for the entire collection or a selected portion of it.

> The system can generate a report of the value of items (based on data in item record) in the entire collection or a portion. (`early_draft_srs_galecia.txt`)
> System can generate a report of the value of items (based on data in item record) in the entire collection or a portion. Examples: value of all items with status of "longoverdue", value of all DVDs in children's collection, value of entire collection. (`email_financial_reports.eml`)

### REQ-128 - In-Transit Item Reports

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports on items currently in transit to support delivery coordination.

> - In-transit item reports are critical for delivery coordination (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-129 - Provide Administrator Query Feedback

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide Local and Global System Administrators with low-level, query-specific feedback through the front-end interface.

> UD-4: The system must provide thorough high-level error reporting and feedback, and shall allow low-level query-specific feedback for Local and Global System Administrators from the front-end interface. (`early_draft_srs_galecia.txt`)
> UD-4: The system shall provide thorough high-level error reporting and feedback and shall allow low-level query-specific feedback for Local and Global System Administrators from the front-end interface. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-130 - Provide Context-Sensitive Help

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system shall provide context-sensitive help so staff can access relevant documentation without leaving the system.

> [Discussion: Context-sensitive help is critical. Staff shouldn't have to leave the system to find documentation.] (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-131 - Support Required Browsers

**Priority:** Should - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

When accessed through a web browser, Management Processes must support Microsoft Internet Explorer version 6.0 or later and Mozilla Firefox version 2.0 or later.

> OE-4: If web-browser based, the system must be accessible through Microsoft Internet Explorer (version 6.0 and later) and Mozilla Firefox (version 2.0 and later). (`early_draft_srs_galecia.txt`)
> If web-browser based, Management Processes shall be accessible through Microsoft Internet Explorer (v.6.0 and later) and Mozilla Firefox (v.2.0 and later). (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-132 - Use Relational Database

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Fully relational DB backend; core data integrity but less emphasized.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

Management Processes must use a fully relational database as its back-end.

> Management Processes shall use a fully relational database back-end. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-133 - Administer Report Permissions By Role

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Role-based permissions with automatic updates; security/administration important.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must make report permissions easy to administer through roles and automatically update a user's report permissions when their role changes.

> If I change someone from "Staff" to "Manager," their report permissions should update automatically based on the role. (`email_report_features.eml`)
> Easy administration through roles. (`email_report_features.eml`)

### REQ-134 - Archive Transactions Privately

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: State-law privacy protections for archived transaction data are critical.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must archive transaction data with privacy protections required by state law while retaining data needed for useful demographic statistics.

> Transactions archived protecting patron privacy per State Law, while providing useful demographic statistics. (`email_report_features.eml`)
> TRANSACTION ARCHIVE: Archive with privacy protection per State Law. (`email_report_features.eml`)

### REQ-135 - Choose Picklist Values

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The query tool must allow users to select query values from predefined picklists.

> - Select values from a picklist of possible values (`early_draft_srs_galecia.txt`)
> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)

### REQ-136 - Display Report Criteria

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`

Report results must show the report name and the selections or criteria used to produce them, including the selected date range when applicable.

> Report results would include the date selection criteria at the top or bottom to quickly see date range selected along with the name of the report (`early_draft_srs_galecia.txt`)
> QUERY SELECTIONS: Show criteria with results. (`email_report_features.eml`)

### REQ-137 - Enforce Fine-Grained Report Permissions

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`, `evergreen_reference_2009.txt`

The reporting system must provide fine-grained permissions governing access to reporting capabilities, reports, and data, including who may create or clone reports.

> Implement fine-grained permissions and template management (`evergreen_reference_2009.txt`)
> We need distinct, fine-grained permission levels limiting who can create and clone reports. (`email_report_features.eml`)

### REQ-138 - Exclude Personal Identifiers

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: No patron PII in archives; strong privacy/security requirement.  
**Type:** constraint  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

Archived transaction data must not retain personally identifiable information about patrons.

> State law requires us to retain transaction data for X years, but patron privacy means we can't keep personally identifiable information. (`email_report_features.eml`)

### REQ-139 - Maintain Template Consistency

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Consistency reduces errors and disputes; important for report reliability.  
**Type:** non-functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

Report templates must ensure that users running the same named report use the same criteria and produce consistent reports.

> We want to make sure that when the director asks for "the weeding report," everyone runs the same report with the same criteria. Templates ensure this. (`email_report_features.eml`)

### REQ-140 - Provide Executive Reports

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must provide predefined reports suitable for library boards and other external consumers, including basic statistics required by the Georgia Annual Report.

> Pre-defined reports for library boards with basic statistics (Georgia Annual Report requirements). (`email_report_features.eml`)
> BOARD REPORTS: Pre-defined reports for boards. (`email_report_features.eml`)

### REQ-141 - Report Library Activity

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must provide activity reports showing traffic and usage-volume statistics for check-outs, check-ins, holds placed, and holds filled.

> Activity reports should indicate traffic and volume of use, displaying statistics on check-outs, check-ins, holds placed, and holds filled. (`early_draft_srs_galecia.txt`)
> Activity reports showing traffic and volume of use - checkouts, check-ins, holds placed, holds filled. (`email_report_features.eml`)

### REQ-142 - Restrict Ad Hoc Data Access

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Controls ad hoc data exposure via shared-folder permissions; important security.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

Shared-folder permissions must be able to control whether staff may run ad hoc reports against specified sets of data.

> Admins can create shared folders to allow or disallow staff from running specific reports, and/or to run ad hoc reports on specific sets of data. (`email_report_features.eml`)

### REQ-143 - Retain Required Transactions

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Retention for required period is legal compliance and cannot be optional.  
**Type:** constraint  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must retain transaction data for the period required by applicable state law.

> State law requires us to retain transaction data for X years, but patron privacy means we can't keep personally identifiable information. (`email_report_features.eml`)

### REQ-144 - Select Report Display Fields

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The query and open-template reporting interfaces must allow users to select the fields displayed in reports, including circulation, patron, item, bill, and bibliographic attributes.

> Staff should be able to: - Select fields to query (`early_draft_srs_galecia.txt`)
> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)

### REQ-145 - Simplify Permission Administration

**Priority:** Should - Mentioned in 2 documents.  
**Type:** non-functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`, `email_staff_login.eml`

The system must make roles and permissions easy for authorized administrators to manage.

> The permissions need to be easy to administer. (`email_report_features.eml`)
> 4. Easy administration of roles and permissions. (`email_staff_login.eml`)

### REQ-146 - Design User-Friendly Queries

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must provide a user-friendly interface for designing queries across bibliographic, item, patron, transaction, and financial records.

> The system should provide a user-friendly interface for designing queries against all record types (bibliographic, item, patron, transaction, financial). (`early_draft_srs_galecia.txt`)
> QUERY TOOL: User-friendly interface for designing queries against all record types. (`email_report_features.eml`)

### REQ-147 - Priority-Based Report Queuing

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Priority queue improves throughput for important reports; operational enhancement.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

The system must allow authorized users to assign priorities so that important reports can move ahead of lower-priority reports in the queue.

> PRIORITY: Important reports can jump queue. (`email_report_features.eml`)

### REQ-148 - Query Access Controls

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Admin control of query tool access is security governance.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

Administrators must be able to control access to the query tool.

> Admin controls access. (`email_report_features.eml`)

### REQ-149 - Run Or Modify Templates

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

Staff must be able to run report templates as-is or modify them for individual reporting needs.

> These templates should be runnable as-is or modifiable for individual needs. (`early_draft_srs_galecia.txt`)
> Run as-is or modified. (`email_report_features.eml`)

### REQ-150 - Analyze Patron Behavior

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The reporting system must analyze patron behavior, including return speed, renewal rates, likelihood of renewal, and the percentage of checkouts that are renewals.

> Patron behavior analysis (how quickly books are returned, renewal rates) - Demographic statistics (must be anonymized - no personally identifiable info) (`survey_results_2009.txt`)

### REQ-151 - Anonymize Demographic Data

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must anonymize data used for demographic statistics by deleting information that could identify a patron.

> The data used to produce these statistics must be anonymized - information that could be used to identify a patron is deleted. (`early_draft_srs_galecia.txt`)

### REQ-152 - Filter Items by Creation Date

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must list items whose creation dates fall within a specified date range.

> - List of Items by Creation Date Range (`early_draft_srs_galecia.txt`)
> - List of Items by Creation Date Range (not available) (`evergreen_reference_2009.txt`)

### REQ-153 - List Inactive Patrons

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must list patrons whose status is inactive.

> - List of Patrons with inactive status (`early_draft_srs_galecia.txt`)
> - List of Patrons with inactive status (not available) (`evergreen_reference_2009.txt`)

### REQ-154 - Provide Pivot Table Output

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must support generating report results in pivot-table format.

> Pivot table output (`early_draft_srs_galecia.txt`)
> - No pivot table output (`evergreen_reference_2009.txt`)

### REQ-155 - Provide Report Descriptions

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reports interface must provide quick access to reports and display a pop-up description when staff hover over a report or template title.

> Ability to hover over each title of canned report/template with pop-up box with description (`early_draft_srs_galecia.txt`)
> - No quick access interface with pop-up descriptions (`evergreen_reference_2009.txt`)

### REQ-156 - Provide Weeding Circulation Data

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a weeding report showing each item's last circulation date and number of circulations.

> - Weeding report (date of last circulation and number of circs) (`early_draft_srs_galecia.txt`)
> - Weeding report with date of last circulation (partially available) (`evergreen_reference_2009.txt`)

### REQ-157 - Report Bibliographic Record Edits

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must report the number of bibliographic records edited.

> - Bib Records Edited Count (`early_draft_srs_galecia.txt`)
> - Bib Records Edited Count (not available) (`evergreen_reference_2009.txt`)

### REQ-158 - Report Bibliographic Records Added

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must report the number of bibliographic records added by each user and by each library.

> - Bib Records Added by user by library Count (`early_draft_srs_galecia.txt`)
> - Bib Records Added by user by library Count (not available) (`evergreen_reference_2009.txt`)

### REQ-159 - Report Circulation by Categories

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report circulation counts by circulation modifier, Cat1, and Cat2 categories, including categories such as Adult, YA, and Juv.

> - Circulation Count by Circ Modifier, Cat1, and Cat2 (Adult, YA, Juv...) (`early_draft_srs_galecia.txt`)
> - Circulation Count by Circ Modifier (partially available) (`evergreen_reference_2009.txt`)

### REQ-160 - Report Circulation by County

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report circulation counts by circulation location, broken down by the patron's county.

> - Circulation Count by Circ Location broken down by Patron County (`early_draft_srs_galecia.txt`)
> - Circulation Count by Circ Location broken down by Patron County (not available) (`evergreen_reference_2009.txt`)

### REQ-161 - Report Collection Age

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report the age of the collection by call number or shelving location.

> - Age of collection by call number or shelving location (`early_draft_srs_galecia.txt`)
> - Age of collection by call number (not available) (`evergreen_reference_2009.txt`)

### REQ-162 - Report Collection Value

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report the price value of the collection by call number or shelving location.

> - Price value of collection by call number or shelving location (`early_draft_srs_galecia.txt`)
> - Price value of collection by call number (not available) (`evergreen_reference_2009.txt`)

### REQ-163 - Report Fines Stopped Reasons

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must list items grouped or filtered by the reason fines were stopped.

> - List of Items by Fines Stopped Reason (`early_draft_srs_galecia.txt`)
> - List of Items by Fines Stopped Reason (not available) (`evergreen_reference_2009.txt`)

### REQ-164 - Report Hold Placement Methods

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

Hold reports must identify whether each hold was placed at a staff desk, on a public computer inside the library, or remotely.

> The system counts all hold requests, including how the hold was placed: - at a staff desk - at a public computer inside the library - remotely (`early_draft_srs_galecia.txt`)
> Holds reports should show how the hold was placed - at staff desk, at public computer, or remotely (`survey_results_2009.txt`)

### REQ-165 - Report Holds Purchase Alerts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report of purchase alerts associated with holds.

> - Holds Purchase Alert (`early_draft_srs_galecia.txt`)
> - Holds Purchase Alert (not available) (`evergreen_reference_2009.txt`)

### REQ-166 - Report Long-Overdue Items

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide reports listing items overdue by more than a specified number of days, including configurable thresholds and patron contact information.

> - Items more than XX days overdue (Overdue Materials Report) (`early_draft_srs_galecia.txt`)
> - List of Long Overdue (`early_draft_srs_galecia.txt`)

### REQ-167 - Report Patron Geographic Counts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide patron counts by county, city, and ZIP code.

> - Patron Count by County (`early_draft_srs_galecia.txt`)
> - Patron Count by County (not available) (`evergreen_reference_2009.txt`)

### REQ-168 - Report Staff Account Dates

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report staff accounts and each account's last password-change date. The report must also include account expiration dates.

> - List of Staff Accounts with date of last password change and account expiration (`early_draft_srs_galecia.txt`)
> - Staff Accounts with date of last password change (not available) (`evergreen_reference_2009.txt`)

### REQ-169 - Report Stale Holds

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report of holds that have remained on the hold shelf awaiting pickup beyond the permitted period.

> - Stale Holds (holds sitting on hold shelf waiting for pickup for too long) (`early_draft_srs_galecia.txt`)
> - Stale Holds (not available) (`evergreen_reference_2009.txt`)

### REQ-170 - Report Unfilled Holds

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report of holds that remain unfilled.

> - Unfilled Holds (`early_draft_srs_galecia.txt`)
> - Unfilled Holds (not available) (`evergreen_reference_2009.txt`)

### REQ-171 - Report Voter Survey Responses

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report voter registration survey responses, including response counts by week and county.

> - Voter Survey Responses County by Week (`early_draft_srs_galecia.txt`)
> - Voter Reg Survey Responses Count by Week (`early_draft_srs_galecia.txt`)

### REQ-172 - Select Open Template Filters

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Expose all relevant attribute filters; broadens usability significantly.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The open template reporting interface must provide all attributes associated with circulation, patrons, items, bills, and bibliographic records for use as report filters.

> Open template would have all attributes associated with say circulation, patrons, items, bills, and bibs to select from for filtering and the same attributes for displaying. (`early_draft_srs_galecia.txt`)

### REQ-173 - Support Appendix A Reports

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must support the reporting definitions specified in the report examples attached as Appendix A.

> The system must be able to support the reporting definitions as described in the attached report examples (see Appendix A). (`early_draft_srs_galecia.txt`)

### REQ-174 - Support Appendix B Reports

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must support the fine-grained reporting requirements specified in the attached Appendix B specification.

> The system must be able to support the fine-grained reports requirements as described in the attached specification (see Appendix B). (`early_draft_srs_galecia.txt`)

### REQ-175 - Support Open-Template Reporting

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must support open-template reporting, allowing staff to select reporting attributes for filtering and display.

> c) Open Template Reporting - all attributes associated with circulation, items, patrons, bills, and bibs to select from for filtering and display (`early_draft_srs_galecia.txt`)
> - Open Template Reporting - does not exist (`evergreen_reference_2009.txt`)

### REQ-176 - Upload Text File Filters

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must allow users to upload text files containing values such as barcodes or TCNs to filter report results.

> Ability to upload a text file such as barcodes or TCN to use for filtering on a report (`early_draft_srs_galecia.txt`)
> - No ability to upload text files for filtering (barcodes, TCNs) (`evergreen_reference_2009.txt`)


## Could requirements

### REQ-177 - Use Iterative Prototyping

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-01-27  
**Sources:** `early_draft_srs_galecia.txt`

Data structures and user interfaces shall be further specified and developed using an iterative, prototype-oriented methodology.

> The requirements cover functional aspects only; data structures and user interfaces will require further specification and development using an iterative, prototype-oriented methodology. (`early_draft_srs_galecia.txt`)

### REQ-178 - Create Custom Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must allow staff to create custom reports through a web-based report writer interface.

> Evergreen includes a report writer that allows staff to create custom reports using a web-based interface. (`evergreen_reference_2009.txt`)

### REQ-179 - Display Reports to Patrons

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system should support making report information available to patrons indirectly through displays or screens at libraries.

> [Note from Katherine: Patrons interact through OPAC; they may use reports indirectly through displays/screens at libraries] (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-180 - Enable Staff Report Creation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system shall support staff as primary creators of management reports.

> [Jenny: Staff are our primary content creators for reports] (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-181 - Exclude Patron-Facing Operations

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The Management Processes system shall exclude day-to-day patron-facing functions, which belong to the OPAC and circulation client.

> She clarified that this does NOT include day-to-day patron-facing functions (those are part of the OPAC and circulation client). (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-182 - Expose Fields for Reporting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must make relevant database fields available for report field selection, including documented sample fields for bibliographic metadata, item and copy details, and patron information.

> 3.3 AVAILABLE FIELDS (SAMPLE) For bibliographic_record: - id, fingerprint, scan_timestamp, record_type, edition, language, ISBN, ISSN, UPC, EAN, publisher_name, publication_date, place_of_publication, physical_description For item: - id, barcode, label, copy_number, location (copy_location), status ... (`evergreen_reference_2009.txt`)
> - Limited field selection (not all database fields are available) (`evergreen_reference_2009.txt`)

### REQ-183 - Filter Report Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The report writer must allow staff to apply filters to report data.

> - Basic filtering and sorting (`evergreen_reference_2009.txt`)

### REQ-184 - Provide Executive Reports Interface

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system shall provide an Executive Reports Interface with reports functionality to support library management and administrative oversight.

> Compile a list of reports needed for an Executive Reports Interface. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-185 - Report Bibliographic Counts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must provide a predefined report showing bibliographic record counts.

> - Bib Records Count (`evergreen_reference_2009.txt`)

### REQ-186 - Report Checkout Counts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must provide a predefined report showing checkout counts.

> - Checkout Count (`evergreen_reference_2009.txt`)

### REQ-187 - Save Report Definitions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must allow staff to save report definitions for later reuse.

> - Ability to save and reuse report definitions (`evergreen_reference_2009.txt`)

### REQ-188 - Schedule Multiple Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The scheduling system must allow multiple reports to be selected and scheduled to run at the same time.

> - No ability to check multiple reports to run at the same time (`evergreen_reference_2009.txt`)

### REQ-189 - Select Fields By Dragging

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The report writer must support drag-and-drop selection of report fields.

> - Drag-and-drop field selection (`evergreen_reference_2009.txt`)

### REQ-190 - Separate Create And Run Permissions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The permission model must provide fine-grained control over who may create reports and who may run reports.

> - No fine-grained control over who can create vs. run reports (`evergreen_reference_2009.txt`)

### REQ-191 - Sort Report Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The report writer must allow staff to sort report results.

> - Basic filtering and sorting (`evergreen_reference_2009.txt`)

### REQ-192 - Support Consortium Administration

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system shall allow the global system administrator to implement software changes and configurations for the PINES consortium.

> Global System Administrator: Manages PINES at the consortium level, implementing software changes and configurations, and generating statistical reports for PINES as a whole. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-193 - Support Local Configuration

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system shall allow local system administrators to configure the system for their local library processes.

> They configure the system locally. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-194 - Support Regular Expressions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The report writer must support regular expression criteria in report queries and filters.

> - No regular expression support (`evergreen_reference_2009.txt`)

### REQ-195 - Track Financial Transactions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system shall track and verify financial transactions for management oversight.

> - Tracking and verifying financial transactions (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-196 - Configure Item Categories

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`

The volume report must break item counts down by item category, including examples such as adult fiction and board books. Authorized users must be able to configure standard and additional categories so libraries can use their own classifications.

> Also, the breakdown by categories is important. We need things like: - Total items - Number of holds - Number of adult fiction - Number of board books - Maybe other categories too (`conversations/conv_pines014_material_volume.eml`)
> At Twin Lakes we need this for our quarterly assessment. Can we make the categories customizable? Different libraries might want different breakdowns. (`conversations/conv_pines014_material_volume.eml`)

### REQ-197 - Report Recent Acquisitions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`

The system must use item acquisition dates to report how much volume was added during selectable recent periods, including 30, 60, and 90 days.

> It would be helpful to see how much volume has been added in the last 30/60/90 days. (`conversations/conv_pines014_material_volume.eml`)

### REQ-198 - Show Status Counts Separately

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`

The system must show separate counts for new acquisitions, checked-in items, checked-out items, and the overall total.

> I think Maria is asking for all three counts separately plus a total. That makes sense for collection management. (`conversations/conv_pines014_material_volume.eml`)

### REQ-199 - Color-Code Capacity Status

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-08  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The interface should use color coding to communicate capacity status, with green for under-capacity branches, yellow for branches nearing capacity, and red for branches at or over capacity.

> Maybe color-coding - green for under capacity, yellow for getting full, red for at/over capacity (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-200 - Display Capacity Trends

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must display trend data indicating whether a branch's capacity or load is growing or shrinking over time.

> - Trend data (growth/shrink patterns) (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-201 - Drill Into Branch Details

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must allow users to select an individual branch and view its detailed capacity information.

> - Ability to drill down into individual branches (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-202 - Export Capacity Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must allow users to export branch capacity information in CSV format.

> - Export to CSV (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-203 - Sort And Filter Branches

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must allow users to sort and filter the branch capacity overview by region, library type, and current load.

> - Sorting and filtering capabilities (region, type, load) (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-204 - Support Department Head Permissions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must provide a department head role that permits creating and modifying templates.

> Department heads (can create and modify templates) (`email_staff_login.eml`)

### REQ-205 - Support Front Desk Permissions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must provide a front desk staff role that permits running basic reports and applying limited filters.

> Front desk staff (can run basic reports, limited filters) (`email_staff_login.eml`)

### REQ-206 - Compare Local And System Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must allow branch managers to view their local shelf space results and compare them with the system average.

> This way branch managers can see their local situation AND see how they compare to the system average. (`conversations/conv_pines016_shelf_space.eml`)

### REQ-207 - Estimate Shelf Space

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must estimate shelf space for each genre and format, using item dimensions or item count as a proxy because shelf space is not directly tracked in the database.

> Shelf space isn't directly tracked in the database. We'd need to estimate based on item dimensions or use item count as a proxy. (`conversations/conv_pines016_shelf_space.eml`)

### REQ-208 - Filter Results By Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must allow users to filter shelf space utilization results by a specified date range.

> Can we also filter by date range? Like, what was the shelf space utilization in Q1 vs. Q2? (`conversations/conv_pines016_shelf_space.eml`)

### REQ-209 - Report Circulation Percentages

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must report, for each genre and format, the percentage of total circulations attributable to that category.

> What percentage of total circulations it has (`conversations/conv_pines016_shelf_space.eml`)

### REQ-210 - Report Collection Percentages

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must report, for each genre and format, the percentage of the collection represented by that category.

> What percentage of the collection it is (`conversations/conv_pines016_shelf_space.eml`)

### REQ-211 - Show Side-by-Side Comparisons

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must provide a comparison view that displays each library's breakdown side by side so users can identify outliers.

> Also, can we include a "comparison" view that shows each library's breakdown side by side? That would make it easy to spot outliers. (`conversations/conv_pines016_shelf_space.eml`)

### REQ-212 - Combined Transit Directions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The system must combine items traveling to a branch and items traveling from a branch into a single in-transit report.

> The report merges transit-to and transit-from into one report for ease of front-line staff. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-213 - Default Transit Threshold

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The configurable threshold for identifying items that have been in transit too long must default to seven days.

> I need to see what's been in-transit for more than X days (X should be configurable, probably 7 days default). (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-214 - Due Date Sorting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The in-transit report must be sortable by due date so that staff can identify and pursue the oldest items first.

> Also, for the in-transit report - can we sort by due date? Front-line staff need to chase the oldest items first. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-215 - In-Transit Report Scope

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The in-transit report must support reporting by branch and by system.

> System generates a list of items that have been in-transit for more than X days (X configurable), per branch and per system. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-216 - Include Condition Notes

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The missing and damaged items report must include notes describing the condition or cause of damage, such as water damage or vandalism.

> Also, can the report include item condition notes? Like "water damage" or "vandalism"? (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-217 - Report Missing and Damaged Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The system must generate a report of items marked as missing or damaged to support inventory auditing and collection management.

> Right now I have no easy way to generate a report of all these items per branch. I need this for my inventory audit and for collection management. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-218 - Support Report Date Ranges

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The missing and damaged items report must allow users to limit results to a specified date range, such as the last 30 days or the last quarter.

> The missing/damaged report can include date ranges (e.g., last 30 days, last quarter, etc.) which would be useful for trending. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-219 - Activity-Based Purging

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The purge criteria must support selecting items based on how long ago they were last circulated, using a configurable period of days, months, or years.

> - Activity-based criteria (last circulated X days/months/years ago) (`conversations/conv_pines021_item_purging.eml`)

### REQ-220 - Combine Purge Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must allow users to combine multiple purge criteria, including combinations of circulation history, status, and item condition.

> The system should let us combine criteria. (`conversations/conv_pines021_item_purging.eml`)

### REQ-221 - Combined Purge Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must allow multiple purge criteria to be combined using logical conditions such as AND.

> Can we combine these? Like "items with status 'missing' for more than 6 months AND haven't circulated in 2 years"? (`conversations/conv_pines021_item_purging.eml`)

### REQ-222 - Configure Item Purge Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

Users must be able to define purge criteria using item status, circulation history, and item condition. Status criteria must include missing, discard or weed, and damaged items.

> I need to identify item records to purge based on customizable criteria. For example: - Item has been in status "missing" for more than X months - Item has status "discard/weed" (`conversations/conv_pines021_item_purging.eml`)
> - Status-based criteria (missing, discard/weed, damaged) (`conversations/conv_pines021_item_purging.eml`)

### REQ-223 - Confirm Purge Deletions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must require a separate confirmation step before executing purge deletions.

> 2. A separate confirmation step for actual deletions (`conversations/conv_pines021_item_purging.eml`)

### REQ-224 - Preview Purge Candidates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must provide a read-only report of item records identified for purging. The report must not modify or delete records, and users must be able to review the candidates before deletion.

> 1. Reports show candidates for purging (read-only) (`conversations/conv_pines021_item_purging.eml`)
> - Read-only reports for identifying candidates (`conversations/conv_pines021_item_purging.eml`)

### REQ-225 - Scheduled Purging

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The purging utility must support scheduled or automatic execution, including recurring runs such as at the end of each year.

> Also wondering - can the purging utility be scheduled? Like, run automatically at the end of each year? (`conversations/conv_pines021_item_purging.eml`)

### REQ-226 - Time-Based Purging

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The purge criteria must support selecting items that have remained in a specified status for a configurable number of months or years.

> - Time-based criteria (in status for X months/years) (`conversations/conv_pines021_item_purging.eml`)

### REQ-227 - Deletion Confirmation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-22  
**Sources:** `conversations/conv_pines021_item_purging.eml`

Actual deletions must require a separate confirmation step after purge candidates have been identified.

> - Separate confirmation step for actual deletions (`conversations/conv_pines021_item_purging.eml`)

### REQ-228 - Purge Candidate Utility

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-22  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must provide a utility and reports for identifying item records that meet the configured purge criteria.

> The system should provide a utility and reports for identifying item records to purge, based on customizable criteria such as: (`conversations/conv_pines021_item_purging.eml`)

### REQ-229 - Filter Deletions By Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

Users must be able to query or aggregate deletion records for a specified date range, including reporting periods such as months, quarters, and years.

> We can aggregate by date range, by user, by record type. (`conversations/conv_pines022_deletions.eml`)

### REQ-230 - Filter Deletions By Type

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

Users must be able to query or aggregate deletion records by record type, including item, patron, bibliographic, and other applicable types.

> We can aggregate by date range, by user, by record type. (`conversations/conv_pines022_deletions.eml`)

### REQ-231 - Filter Deletions By User

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

Users must be able to query or aggregate deletion records according to the user who performed the deletion.

> We can aggregate by date range, by user, by record type. (`conversations/conv_pines022_deletions.eml`)

### REQ-232 - Provide Deletion Report Interface

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must provide a report interface that allows users to query the deletion audit data.

> A report interface to query this audit table (`conversations/conv_pines022_deletions.eml`)

### REQ-233 - Rank Deleting Users

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

Administrative reports must identify the users who deleted the greatest number of records.

> Top users who delete the most records (`conversations/conv_pines022_deletions.eml`)

### REQ-234 - Report Deletions By Location

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

Deletion reports must show and support aggregation of deletions by library location or branch.

> The report should show deletions per location and per system. (`conversations/conv_pines022_deletions.eml`)

### REQ-235 - Report Deletions By System

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

Deletion reports must show and support aggregation of deletions by system.

> The report should show deletions per location and per system. (`conversations/conv_pines022_deletions.eml`)

### REQ-236 - Show Deletion Totals

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

Administrative reports must show total numbers of deletions for selected reporting periods, including monthly, quarterly, and annual periods.

> Total deletions per period (month, quarter, year) (`conversations/conv_pines022_deletions.eml`)

### REQ-237 - Track Denied Deletion Attempts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must track deletion attempts that were denied so that unauthorized or inappropriate deletion activity can be identified for compliance and troubleshooting.

> Can we also track attempted deletions that were denied? That would tell us if someone is trying to delete things they shouldn't. (`conversations/conv_pines022_deletions.eml`)

### REQ-238 - Count Holds By Placement

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `survey_results_2009.txt`

The system must count holds according to their placement method, including staff desk, public computer, and remote placement.

> Holds counted with method of placement: at staff desk, public computer, or remotely. (`survey_results_2009.txt`)

### REQ-239 - Report Patron Transactions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `survey_results_2009.txt`

The system must provide transaction reports showing holds placed, holds filled, and check-outs by patron, library, group of libraries, system, and county.

> Transactions report can show holds placed, holds filled, and check-outs per patron, per library, per group of libraries, per system, per county. (`survey_results_2009.txt`)

### REQ-240 - Calculate Age From Birth Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system shall calculate patron age ranges from the birth date field at query time.

> The "age range" is calculated from the birth_date field, which means we need to compute it at query time. (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-241 - Combine Activity And Demographic Filters

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The reporting system must allow circulation-activity criteria to be combined with demographic filters in the same report query, such as identifying juvenile patrons in a specified ZIP code who have not checked out materials within a defined period.

> Can we combine demographic filters? Like "show me all Juvenile patrons in zip code 30505 who haven't checked anything out in 6 months"? (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-242 - Combine Demographic Filters

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow multiple patron characteristics to be applied together as report filters, such as patron type and zip code.

> Can we combine demographic filters? Like "show me all Juvenile patrons in zip code 30505 who haven't checked anything out in 6 months"? (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-243 - Configure Age Ranges

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow report users to configure the age-range boundaries used for patron reporting.

> The age ranges need to be configurable too. Like, 0-5, 6-10, 11-15, etc. Or 0-6, 7-12, 13-17, 18-24, 25-34... Whatever makes sense for the report. (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-244 - Filter Patron Reports by Age

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow patron queries and reports to be filtered by age range.

> The fields I need: - Age range (`conversations/conv_pines023_patron_characteristics.eml`)
> - Age range (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-245 - Filter by Circulation Activity

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow reports to filter patrons according to whether they have checked out materials within a specified period, including identifying patrons with no checkouts in six months.

> Can we combine demographic filters? Like "show me all Juvenile patrons in zip code 30505 who haven't checked anything out in 6 months"? (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-246 - Handle Missing Demographics

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The reporting capability must address patrons whose demographic fields are missing by supporting either the display of null values or the exclusion of those records.

> Should the report show nulls for missing data, or exclude those records? (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-247 - Report by County

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must support patron reports using county of residence as a reporting characteristic.

> - County of residence (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-248 - Report by Patron Type

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must support patron reports using patron type as a reporting characteristic.

> - Patron type (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-249 - Report by Patron ZIP Code

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must support patron reports using ZIP code as a reporting characteristic, including filtering reports by selected ZIP code values.

> I need to be able to both LIMIT and GROUP BY patron characteristics. For example: - Limit: Show me only patrons in zip code 30501 (`conversations/conv_pines023_patron_characteristics.eml`)
> - Zip code (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-250 - Combine Filters With Logic

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system shall support combining patron-characteristic filters using both AND and OR logic.

> - Filters can be combined with AND/OR logic (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-251 - Configure Age Brackets

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system shall allow age brackets used for age-range reporting to be configured separately for each report.

> - Age ranges should be configurable per report (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-252 - Filter By Home Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system shall allow patron queries and reports to be filtered by home branch.

> - Home branch (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-253 - Group By Home Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system shall allow patron results to be grouped by home branch.

> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Home branch (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-254 - Cache Report Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system shall cache the results of generated inactive patron reports so that report retrieval does not repeatedly execute the potentially slow query.

> We should run it as a background report and cache results. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-255 - Configure Inactivity Period

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must allow users to configure the inactivity threshold to any number of days, rather than limiting it to a fixed period.

> Can we make it fully customizable? Like any number of days? (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-256 - Count Electronic Patron Activity

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

When determining whether a patron is inactive, the system must count electronic activity, including OPAC or patron-account logins, online holds, access to integrated digital collections, and online renewals.

> 3. Renewing items online (`conversations/conv_pines024_inactive_patrons.eml`)
> "Electronic activity" should include: 1. Logging into OPAC/patron account (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-257 - Exclude Patron Types

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system shall allow specified patron categories to be excluded from the inactive patron report, including patrons marked do not disturb, VIP patrons, staff members, and patrons who have opted out of communications.

> One more thing - we should be able to EXCLUDE certain patrons from the inactive report. For example: - Patrons with "do not disturb" flags - VIP patrons - Staff members - Patrons who have opted out of communications (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-258 - Export Report as CSV

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system shall provide the inactive patron report in an exportable CSV format for upload to an outreach system.

> Also, the report should be exportable. We upload it to our outreach system. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-259 - Include Mailing Addresses

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The inactive-patrons report must include each patron’s current mailing address for outreach purposes.

> We mail postcards to inactive patrons, so the report needs to include current mailing addresses. (`conversations/conv_pines024_inactive_patrons.eml`)
> Additional considerations: - Include current mailing addresses for outreach (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-260 - Measure Electronic Activity

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system shall consider OPAC logins, online hold placements, online renewals, and logged digital resource access when determining a patron’s most recent electronic activity.

> For "electronic activity," we track: - OPAC login events - Online hold placements - Online renewals - Digital resource access (if logged) (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-261 - Process Reports in Background

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system shall run inactive patron report generation as a background process to avoid performance problems for the large patron population.

> We should run it as a background report and cache results. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-262 - Separate Inactive Patrons Owing Fines

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must track inactive patrons with outstanding fines separately from other inactive patrons so those accounts can receive different handling.

> - Track inactive patrons with outstanding fines separately (`conversations/conv_pines024_inactive_patrons.eml`)
> And yes, we should track inactive patrons who still owe fines separately. Those accounts need different handling. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-263 - Show Inactive Counts by Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

At the system level, the report must show counts of inactive patrons for each branch so users can identify which branches have the most inactive patrons.

> At the system level, I can see which branches have the most inactive patrons. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-264 - Configure Report Grouping

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-06  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system shall allow the inactive patron report to be configured at the System, Home Library, and County levels, with support for additional levels as needed.

> The list should be configurable to: - System - Home Library - County - (Other levels as needed) (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-265 - Include Transactions in Statistics

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `interview_cataloging_2009-05-08.txt`

The system must count transactions involving uncataloged materials and include those transactions in circulation statistics and reports.

> We also need to count transactions and include them in circulation statistics and reports. (`interview_cataloging_2009-05-08.txt`)

### REQ-266 - Record Deletion Reasons

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `interview_cataloging_2009-05-08.txt`

The system must retain the reason for each record deletion to support auditing and troubleshooting.

> our directors want to know how many records we've deleted and why. It also helps with troubleshooting if something goes missing from the catalog. (`interview_cataloging_2009-05-08.txt`)

### REQ-267 - Migrate Report Configurations

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`

The system must provide export and import functionality to migrate report templates, permission settings, and other configuration from development or training into production.

> The key is that configurations developed in training/dev need to be migratable to production. We need export/import functionality for report templates, permission settings, and other configuration. (`interview_sysadmin_2009-05-10.txt`)

### REQ-268 - Process Reports in Background

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`

The system must support queuing and background processing for complex reports so report execution does not block interactive operations.

> We need to make sure reports can be queued and processed in the background. (`interview_sysadmin_2009-05-10.txt`)

### REQ-269 - Use a Relational Database

**Priority:** Could - Mentioned in 2 documents; strong wording (must). Adjusted from Should by model: Use existing PostgreSQL relational database; implementation constraint.  
**Type:** constraint  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must use and operate with the existing fully relational PostgreSQL database structure, support complex relational joins, and remain compatible with PostgreSQL.

> The reporting system needs to work with the relational structure, not fight against it. (`interview_sysadmin_2009-05-10.txt`)
> - Database architecture needs are clear (relational, PostgreSQL-compatible) (`interview_sysadmin_2009-05-10.txt`)

### REQ-270 - Alert on Transfer Problems

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must notify designated users when an item transfer is delayed or encounters an issue.

> If an item transfer is delayed or has issues, notify me. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-271 - Efficient Large-Batch Processing

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must process large transfer operations efficiently and in smaller batches to avoid locking the database.

> One concern: with 9.6 million items, batch updates need to be efficient. We should process in smaller batches to avoid locking the database. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-272 - Generate Transfer Pull Lists

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must generate pull lists identifying items that need to be gathered for transfer.

> Pull list generation - create a printable list of items to be moved. (`conversations/conv_pines018_item_transfer.eml`)
> - Mechanisms: changing location field, generating pull lists (`conversations/conv_pines018_item_transfer.eml`)

### REQ-273 - Preview Transfer Changes

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The utility must show a preview of the items and resulting locations before applying a transfer and request confirmation from the user.

> Also, the utility should show a preview before making changes. "If you run this now, 25 items will be moved from Dalton-Whitman to Mobile Library Unit 3. Confirm?" (`conversations/conv_pines018_item_transfer.eml`)

### REQ-274 - Print Transit Labels

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must generate printable transit labels for items being transferred between locations, including item barcodes.

> Also, can we generate transit labels? Like, printable barcodes for the items being transferred? (`conversations/conv_pines018_item_transfer.eml`)
> - Printable transit labels (`conversations/conv_pines018_item_transfer.eml`)

### REQ-275 - Restrict Transfer Permissions

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

Transfer operations must be limited to authorized roles, such as managers, administrators, and transfer coordinators, rather than being available to every staff member.

> Not every staff member should be able to transfer items between branches. This should be limited to certain roles (managers, administrators, transfer coordinators). (`conversations/conv_pines018_item_transfer.eml`)

### REQ-276 - Revert Unused Transfers

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must base transfer reversion on checkout activity at the destination: transferred items that are checked out there must remain at the destination, while items that remain unused must revert to their original location.

> Revert when item is checked out at the destination (event-based) (`conversations/conv_pines018_item_transfer.eml`)
> We send items to a mobile library, and when they're checked out there, they should stay. But if they just sit there unused, they come back. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-277 - Select Items For Transfer

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The transfer utility must allow users to manually select individual titles or items from query results to include in a transfer.

> Manually select titles from query results (`conversations/conv_pines018_item_transfer.eml`)
> I should be able to check boxes and select which ones to include. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-278 - Share Saved Queries

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must allow saved transfer queries to be shared with other users.

> 2. Save/share queries - similar to report templates. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-279 - Status-Based Reversion

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must support reverting transferred items when a configured item status changes, including statuses such as "sold" or "returned."

> Can we also revert "based on other criteria"? Like, if the item's status changes to "sold" at the book sale, automatically revert it? (`conversations/conv_pines018_item_transfer.eml`)

### REQ-280 - Support Temporary Locations

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must support transferring items to temporary locations for specific events or programs.

> Also, for the outreach program use case - can we transfer items to a temporary location for a specific event or program? (`conversations/conv_pines018_item_transfer.eml`)

### REQ-281 - Track Transfer History

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must record item transfer activity so it can be audited, including each item's transfer history and the number of transfers over a specified period.

> 6. Logging - track all transfers for audit purposes. (`conversations/conv_pines018_item_transfer.eml`)
> Can we track transfer history? Like, "this item has been transferred 5 times in the past year." (`conversations/conv_pines018_item_transfer.eml`)

### REQ-282 - Transaction-Safe Updates

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

Batch location updates must be performed with transaction safety so that transfer changes are reliably committed or rolled back.

> 3. Batch update of location field - straightforward database update with transaction safety. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-283 - Undo Transfer Operations

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The utility must provide an undo function so users can reverse an incorrectly initiated transfer.

> And we need an undo function! What if someone clicks the wrong button? (`conversations/conv_pines018_item_transfer.eml`)

### REQ-284 - Cancel Running Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must allow users or authorized processes to cancel reports that are currently being processed.

> The ability to cancel a scheduled or running report is technically feasible, but requires the system to check for cancellation signals during report processing. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-285 - Check Cancellation Signals

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

During report processing, the system must check for cancellation signals so that scheduled or running reports can be cancelled.

> The ability to cancel a scheduled or running report is technically feasible, but requires the system to check for cancellation signals during report processing. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-286 - Ensure Complete Current Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must ensure that centrally consolidated data received from all library locations is complete and current.

> The challenge is making sure data from all locations is complete and current. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-287 - Export Reports to CSV

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must support exporting report results in CSV format for reliable data export.

> Excel, HTML, and CSV formats are required. Robert noted that CSV is the most reliable for data export, Excel is preferred by business users for pivot tables, and HTML is needed for web display. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-288 - Export Reports to Excel

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must support exporting report results in Excel format for business users and pivot-table analysis.

> Excel, HTML, and CSV formats are required. Robert noted that CSV is the most reliable for data export, Excel is preferred by business users for pivot tables, and HTML is needed for web display. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-289 - Export Reports to HTML

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must support producing report results in HTML format for web display.

> Excel, HTML, and CSV formats are required. Robert noted that CSV is the most reliable for data export, Excel is preferred by business users for pivot tables, and HTML is needed for web display. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-290 - Handle Optional Vendor Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must handle vendor integration data when it is available without requiring that such data be present at every library.

> "The reporting system needs to handle this data, but we can't rely on it being present at every library." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-291 - Isolate Training Environment

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The training environment must allow staff to experiment without risking or modifying production data.

> "And the training environment needs to be safe - staff should be able to experiment without risking production data." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-292 - Keep OPAC Data Read-Only

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must query data from the OPAC without modifying that data.

> "The reporting system queries this data, but doesn't modify it." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-293 - Limit Library Manager Access

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a Library Manager role that can run approved reports and make only limited template modifications.

> - Library Manager: Run approved reports, limited template modification (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-294 - Limit Staff Report Access

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a Staff role that permits users to run reports only within their assigned permissions.

> - Staff: Run reports within assigned permissions (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-295 - Provide Global Administrator Access

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a Global Admin role with full system access.

> - Global Admin: Full system access (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-296 - Provide Query-Specific Feedback

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide administrators with low-level, query-specific feedback that identifies relevant error details such as the affected table, field, and error type.

> and shall allow low-level query-specific feedback for administrators. "When a report fails, we need to know WHY," Robert said. "Generic error messages like 'query failed' are useless. We need specifics - which table, which field, what kind of error." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-297 - Read Enterprise Library Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must read data from the enterprise Library Automation System and must not manage acquisitions or cataloging activities.

> "All our data comes from the ILS," Robert said. "The reporting system doesn't manage acquisitions or cataloging - it just reads the data." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-298 - Rely On Enterprise Infrastructure

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system may rely on enterprise infrastructure such as redundant servers, backup systems, and network connectivity rather than providing those capabilities itself.

> Robert: "This means we can rely on the infrastructure - redundant servers, backup systems, network connectivity." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-299 - Resolve Survey Names Internally

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

When a survey filter is specified by name, the system must resolve that name to the corresponding survey ID internally.

> The ability to filter by survey name rather than survey ID requires the system to resolve names to IDs internally. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-300 - Support Patron OPAC Access

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must support patron access indirectly through OPAC displays rather than through direct access to the management reporting system.

> - Patron: Indirect access through OPAC displays (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-301 - Enforce Data Retention

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must enforce applicable data-retention policies, including retaining designated data for seven years when required for audit purposes.

> Some data needs to be retained for 7 years for audit purposes. The system needs to enforce retention policies. (`email_financial_reports.eml`)

### REQ-302 - Join Financial Data Sources

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must support financial reporting queries that combine financial data attached to patron records with financial data attached to item records.

> The financial data is attached to patron records AND item records. So when we query for financial reports, we need to be able to join these data sources. (`email_financial_reports.eml`)

### REQ-303 - Report Accrued Charges

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must report fines and charges accrued during selectable time periods, including the last 12 months, year to date, and the last month, and categorize them by charge type, including overdue fines, damaged-item charges, and lost-item charges.

> Fines and charges accrued per time period (last 12 months, YTD, last month) (`email_financial_reports.eml`)
> Fines and charges accrued per time period (last 12 months, YTD, last month) and per type of charge (overdue fines, damaged item charges, lost item charges, etc.) (`email_financial_reports.eml`)

### REQ-304 - Report Item Values

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must calculate and report the value of items using purchase-price data from item records, for the entire collection or for filtered subsets such as status, format, or collection.

> Value of items report - staff should be able to get the value of items based on data in item records. This could be the entire collection, or a portion. (`email_financial_reports.eml`)

### REQ-305 - Track Payments By Library

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must track payments by the library or branch where they were collected so that each location can view its collected payments.

> Payments tracking by library is important for our end-of-month reports. Each branch needs to be able to see what payments were collected at their location. (`email_financial_reports.eml`)

### REQ-306 - Branch Item Damage Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide branch-level reports for missing and damaged items.

> - Missing/damaged item reports are needed per branch (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-307 - Cross-Branch Comparisons

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must support reports that compare data across library branches.

> - Need for cross-branch comparison reports (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-308 - Data Quality Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports for identifying and assessing data quality issues.

> - Data quality reports are needed (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-309 - Financial Reporting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide financial reports suitable for review by library directors.

> - Financial report needs are understood at the director level (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-310 - Interact With The OPAC

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

Management Processes shall interact with the patron-facing Online Public Access Catalog to query data created through the patron interface, including holds and circulation data.

> DE-3: Management Processes interact with a patron interface, also known as an Online Public Access Catalog (OPAC). (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-311 - Inventory Capacity Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide inventory and capacity reports for operational use.

> - Inventory and capacity reports are used daily (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-312 - Predefined Executive Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide predefined reports for boards and executive stakeholders.

> - Board/executive reports need to be pre-defined (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-313 - Provide PINES-Wide Report Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The Reports functionality shall provide templates that meet the needs of all PINES libraries.

> Determine and create templates needed for all PINES libraries. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-314 - Queue Background Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must process searches and reports in the background or through queuing so that report generation during open or peak hours does not slow down circulation clients or disrupt other system functions.

> It is highly desirable that searches and reports can be processed during open hours without disrupting other system functions. We need background processing/queuing to prevent report generation from slowing down the circulation client. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-315 - Run On Linux Solaris

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

Management Processes must operate on a server running either Linux or Solaris.

> Management Processes shall operate on a Linux or Solaris server. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-316 - Shelf Space Utilization

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports showing shelf space utilization.

> - Shelf space utilization reports are important (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-317 - Support Reliable Network Connectivity

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The Management Processes system shall support reliable network connectivity between the centralized Management Processes and the multiple locations it serves.

> Centralization enables consistent reporting but requires good network connectivity. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-318 - Weeding Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports to support collection weeding activities.

> - Weeding reports are frequently used (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-319 - Clone Existing Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

Users with appropriate permissions must be able to create a new report variant based on an existing report template without modifying the original template.

> We also need the ability to "clone" reports - take an existing template and create a new one based on it. This is different from modifying the template - it's creating a new variant. (`email_report_features.eml`)

### REQ-320 - Display Report Queue Position

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must show staff that a submitted report is in the processing queue and how many reports are ahead of it.

> They need to see: - That their report is in the queue - How many reports are ahead of theirs (`email_report_features.eml`)

### REQ-321 - Display Submission Time

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must show when a report was submitted.

> When their report was submitted (`email_report_features.eml`)

### REQ-322 - Query All Record Types

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The query tool must support queries against every record type in the system.

> We need a user-friendly interface for designing queries against all record types. (`email_report_features.eml`)
> QUERY TOOL: User-friendly interface for designing queries against all record types. (`email_report_features.eml`)

### REQ-323 - Select Regular Expressions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

Users must be able to choose regular expressions from a dropdown when constructing queries.

> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)

### REQ-324 - Clone Report Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

Users must be able to clone report templates.

> Clone capability. (`email_report_features.eml`)

### REQ-325 - Query Picklists

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

The query tool must provide picklists for query construction.

> Boolean operators, picklists, regex support. (`email_report_features.eml`)

### REQ-326 - Regular Expression Queries

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

The query tool must support regular expressions for query construction.

> Boolean operators, picklists, regex support. (`email_report_features.eml`)

### REQ-327 - Add Canned Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow authorized users to add additional canned reports according to their permission level.

> Ability to add more canned reports via permission level (`early_draft_srs_galecia.txt`)

### REQ-328 - Annual Holds Placed

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall report the annual number of holds placed.

> - Annual # of holds placed (`early_draft_srs_galecia.txt`)

### REQ-329 - Archive Privacy-Protected Transactions

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must archive transaction data in a form that protects patron privacy in accordance with applicable state law.

> Transactions should be archived in a form that protects patron privacy as defined by State Law, while providing useful demographic statistics. (`early_draft_srs_galecia.txt`)

### REQ-330 - Background Report Processing

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must process long-running reports in the background.

> - No background processing for long-running reports (`evergreen_reference_2009.txt`)

### REQ-331 - Barred Patrons List

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a list of patrons with barred status.

> - List of patrons who are BARRED (`early_draft_srs_galecia.txt`)

### REQ-332 - Bib Records Missing MARC

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must identify bibliographic records missing specified MARC fields.

> - Bib Records missing specific MARC fields (not available) (`evergreen_reference_2009.txt`)

### REQ-333 - Bibliographic Records Count

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report showing the number of bibliographic records.

> - Bib Records Count (`early_draft_srs_galecia.txt`)

### REQ-334 - Break Down Circulation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must retrieve total circulation, including checkouts, renewals, and noncataloged transactions, with a breakdown by circulation type.

> Ability to retrieve total circ including checkouts, renewals, and noncats with a breakdown displaying those circ types (`early_draft_srs_galecia.txt`)

### REQ-335 - Cataloged In-House Use

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide counts of cataloged in-house use.

> - Cataloged In House Use Count (`early_draft_srs_galecia.txt`)

### REQ-336 - Check-In Count Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report showing the number of items checked in.

> - Check in Count (`early_draft_srs_galecia.txt`)

### REQ-337 - Checkout Count Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report showing checkout counts and excluding renewals and other circulation activity.

> - Checkout Count (includes checkouts only) (`early_draft_srs_galecia.txt`)

### REQ-338 - Circulation By Dewey

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide circulation counts organized by Dewey classification.

> - Circulation Count by Dewey (`early_draft_srs_galecia.txt`)

### REQ-339 - Circulation By Home Library

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide circulation counts by circulation location, broken down by the patron's home library.

> - Circulation Count by Circ Location broken down by Patron Home Library (`early_draft_srs_galecia.txt`)

### REQ-340 - Circulation By MARC

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide circulation counts organized by MARC data.

> - Circulation Count by MARC (`early_draft_srs_galecia.txt`)

### REQ-341 - Circulation By Modifier

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide circulation counts organized by circulation modifier.

> - Circulation Count by Circ Modifier (`early_draft_srs_galecia.txt`)

### REQ-342 - Circulation Count by Dewey

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide circulation counts broken down by Dewey classification.

> - Circulation Count by Dewey (not available) (`evergreen_reference_2009.txt`)

### REQ-343 - Circulation Count by MARC

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide circulation counts grouped or filtered by MARC fields.

> - Circulation Count by MARC fields (not available) (`evergreen_reference_2009.txt`)

### REQ-344 - Claims Returned Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report of items marked as claims returned.

> - Claims returned (`early_draft_srs_galecia.txt`)

### REQ-345 - Claims Returned Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide a claims-returned report.

> - Claims Returned report (not available) (`evergreen_reference_2009.txt`)

### REQ-346 - Clearly Define Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must present report selection criteria in a clearly defined manner.

> Selection criteria is clearly defined (`early_draft_srs_galecia.txt`)

### REQ-347 - Combine Canned Report Output

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must present the output of canned reports selected for simultaneous execution within a single document.

> Canned reports can be checked off from a list to run at the same time and will be viewed within one document. (`early_draft_srs_galecia.txt`)

### REQ-348 - Configure Local Settings

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

Local System Administrators must have elevated permissions that allow them to configure local system settings.

> They can configure local settings and run system reports. (`early_draft_srs_galecia.txt`)

### REQ-349 - Consortium-Level System Administration

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow Global System Administrators to implement software changes and configurations for the ILS at the consortium level.

> * Global System Administrator: The individual(s) who manage the ILS at the consortium level, implementing software changes and configurations, and generating statistical reports for the entire system. (`early_draft_srs_galecia.txt`)

### REQ-350 - Create Report Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The reports interface must allow users to create reusable report templates.

> Ability to create report templates: 81% (`survey_results_2009.txt`)

### REQ-351 - Customize Report Displays

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow users to edit canned reports for display purposes, including adding fields such as shelving location.

> Ability to edit canned report for display purposes such as adding shelving location as a display (`early_draft_srs_galecia.txt`)

### REQ-352 - Deliver Prewritten Report Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The product must include a defined set of prewritten canned report templates.

> There should be a certain set of templates that are pre-written and delivered with the product. (`early_draft_srs_galecia.txt`)

### REQ-353 - Detailed Voids Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a detailed report of voided transactions.

> - Detailed Voids (`early_draft_srs_galecia.txt`)

### REQ-354 - Display Patron Transaction Counts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must display the number of check-outs and placed holds for each patron.

> The system displays the number of check-outs and placed holds per patron. (`early_draft_srs_galecia.txt`)

### REQ-355 - Display Query Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must display the query selections together with report results so users can see the criteria used to generate the report.

> The system should provide the query selections along with the results, so users can see what criteria were used to generate the report. (`early_draft_srs_galecia.txt`)

### REQ-356 - Display Report Queue Position

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

Staff must be able to view the position of their report in the queue of reports waiting to run.

> Staff should be able to see where their report is in the queue of reports waiting to run. (`early_draft_srs_galecia.txt`)

### REQ-357 - Edit Canned Report Options

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must allow users to edit the display options of canned reports.

> - No ability to edit canned report display options (`evergreen_reference_2009.txt`)

### REQ-358 - Edit Recurring Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow users to modify recurring reports by adding or removing report selections and editing recipient email addresses.

> Ability to edit recurring reports by adding or removing report selections as well as editing the email addresses (`early_draft_srs_galecia.txt`)

### REQ-359 - Enforce Report Permissions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide fine-grained permissions controlling which users can create and run particular reports.

> Fine-grained permissions (who can create/run what): 76% (`survey_results_2009.txt`)

### REQ-360 - Ensure Reliable Output

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

Report output must be tested and proven reliable before being provided to users.

> Tested and proven output (`early_draft_srs_galecia.txt`)

### REQ-361 - Enter Report Recipients

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow users to enter email addresses for report delivery.

> Ability to enter email addresses for report to be sent to - would be great to (`early_draft_srs_galecia.txt`)

### REQ-362 - Estimate Renewal Likelihood

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must report the likelihood that a particular book will be renewed.

> How likely is a particular book to be renewed? (`early_draft_srs_galecia.txt`)

### REQ-363 - Exclude Renewals From Check-In Times

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

Check-in date and time reporting must exclude renewal transactions.

> Checkin date/time should not include renewals (`survey_results_2009.txt`)

### REQ-364 - Flatten MARC Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must retrieve MARC record fields and present them on a single row of report data.

> Ability to pull MARC record fields so that they appear on a single row of data (`early_draft_srs_galecia.txt`)

### REQ-365 - Generate Historical Bills Snapshots

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide snapshot bills reports for historical points in time.

> Need a snapshot bills report going back in time (`survey_results_2009.txt`)

### REQ-366 - Generate Pivot Table Output

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must support generating report results in pivot table format.

> Pivot table output would be great (`survey_results_2009.txt`)

### REQ-367 - Generate Transaction Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must generate transaction reports for holds placed, holds filled, and check-outs by patron, library, selected groups of libraries, system, or county.

> The system can generate a report of transactions (holds placed, holds filled, and check-outs) per patron, per library, per selected group of libraries, per system, per county. (`early_draft_srs_galecia.txt`)

### REQ-368 - Group Transactions by Hour

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support grouping transaction statistics by hour.

> Transactions can be grouped by hour, terminal, branch, and system. (`early_draft_srs_galecia.txt`)

### REQ-369 - Group Transactions by System

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support grouping transaction statistics by system.

> Transactions can be grouped by hour, terminal, branch, and system. (`early_draft_srs_galecia.txt`)

### REQ-370 - Group Transactions by Terminal

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support grouping transaction statistics by terminal.

> Transactions can be grouped by hour, terminal, branch, and system. (`early_draft_srs_galecia.txt`)

### REQ-371 - High-Use Items Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a list of items whose total use count exceeds a configurable threshold.

> - List of Items with a > Total Use Count (`early_draft_srs_galecia.txt`)

### REQ-372 - Historical Snapshot Bills

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide snapshot bills reports for dates in the past.

> - Snapshot bills report going back in time - does not exist (`evergreen_reference_2009.txt`)

### REQ-373 - Integrated Report Help

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide an online help system integrated with reports.

> - No online help system integrated with reports (`evergreen_reference_2009.txt`)

### REQ-374 - Items By Bib Content

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a list of items whose bibliographic records contain a specified value or text.

> - List of items with XXX in bib record (`early_draft_srs_galecia.txt`)

### REQ-375 - Items Count Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report showing the number of items.

> - Items Count (`early_draft_srs_galecia.txt`)

### REQ-376 - Items Received For Holds

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report of items received to fulfill holds.

> - Items Received for Holds (`early_draft_srs_galecia.txt`)

### REQ-377 - Items Sent For Holds

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report of items sent to fulfill holds.

> - Items Sent for Holds (`early_draft_srs_galecia.txt`)

### REQ-378 - Items by Total Use Count

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must list items having a specified total use count.

> - List of Items with specific Total Use Count (not available) (`evergreen_reference_2009.txt`)

### REQ-379 - Last Circulation Field

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide the last circulation date as a separate reportable field.

> - Ability to indicate last circulation date - not available as separate field (`evergreen_reference_2009.txt`)

### REQ-380 - Last Copy Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report of the last copy owned by a library system that was deleted.

> - Last Copy Report (last copy owned by a library system that was deleted) (`early_draft_srs_galecia.txt`)

### REQ-381 - List Added Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a list of items that were added.

> - List of Items Added (`early_draft_srs_galecia.txt`)

### REQ-382 - List Last-Copy Deletions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of items deleted when they were the last copy owned by the library system, to support WorldCat updates.

> Ability to get a list of items deleted that was the last copy owned by the library system in order to update WorldCat (`early_draft_srs_galecia.txt`)

### REQ-383 - Low-Use Weeding Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a list of items whose total use count is below a configurable threshold for weeding purposes.

> - List of Items with a < Total Use Count [Weeding Report] (`early_draft_srs_galecia.txt`)

### REQ-384 - Maintain Email Address Book

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system should provide an address book for regularly used report recipient email addresses.

> have an address book of regularly used addresses (`early_draft_srs_galecia.txt`)

### REQ-385 - Manage Report Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide capabilities for managing report templates.

> - No report template management system (`evergreen_reference_2009.txt`)
> Implement fine-grained permissions and template management (`evergreen_reference_2009.txt`)

### REQ-386 - Measure Return Speed

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must report the average time taken for a particular book to be returned.

> How quickly is a particular book returned, on average? (`early_draft_srs_galecia.txt`)

### REQ-387 - Merged Circulation Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a total circulation report that merges cataloged and non-cataloged circulation data.

> - Total Circulation Count (Merging both Cat and Non-Cat circulation data) (`early_draft_srs_galecia.txt`)

### REQ-388 - Monthly Non-Cataloged Use

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide monthly counts of non-cataloged in-house use.

> - NonCat In House Use Count by Month (`early_draft_srs_galecia.txt`)

### REQ-389 - Monthly Patron Additions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report showing patron additions by month.

> - Patron Added Count by Month (`early_draft_srs_galecia.txt`)

### REQ-390 - New Patrons By Demographics

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall report the number of patrons added during the previous month by demographic category.

> - New Patron Count (patrons added the previous month by Demographic Category) (`early_draft_srs_galecia.txt`)

### REQ-391 - Patron Survey Answer List

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a list of patrons grouped or filtered by survey answer.

> - List of patrons by survey answer (`early_draft_srs_galecia.txt`)

### REQ-392 - Patrons By Expiration Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a list of patrons filtered or organized by expiration date.

> - List of Patrons by Expiration Date (`early_draft_srs_galecia.txt`)

### REQ-393 - Patrons By Notes Text

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a list of patrons whose notes contain specified wording.

> - List of Patrons with specific wording in notes (`early_draft_srs_galecia.txt`)

### REQ-394 - Patrons By Profile Group

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide patron counts by profile group.

> - Patron Count by Profile Group (`early_draft_srs_galecia.txt`)

### REQ-395 - Patrons By Survey Answer

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide patron counts grouped by survey answer.

> - Patron Count by survey answer (`early_draft_srs_galecia.txt`)

### REQ-396 - Preserve Demographic Statistics

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

Archived transaction data must remain usable for producing useful demographic statistics.

> Transactions should be archived in a form that protects patron privacy as defined by State Law, while providing useful demographic statistics. (`early_draft_srs_galecia.txt`)

### REQ-397 - Preserve Report Accuracy

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

Modifying a report template must not compromise the accuracy of its results.

> Changes to templates should not compromise the accuracy of results. (`early_draft_srs_galecia.txt`)

### REQ-398 - Prioritize Report Queue

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow certain report types to be prioritized so that they are placed ahead of resource-consuming reports in the execution queue.

> Ability to prioritize certain types of reports so they will pop to the top of the queue over resource-consuming reports (`early_draft_srs_galecia.txt`)

### REQ-399 - Produce Clean Excel Exports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

Excel exports must avoid producing unnecessary duplicate rows in the exported data.

> I need to export to Excel but the data has too many duplicate rows (`survey_results_2009.txt`)

### REQ-400 - Provide Comparative Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support report results with separate columns for current and prior periods, percentage differences, and corresponding periods from the previous year.

> Ability to determine the output results in a way such that a result could have one column for last month's circs, another for previous month's circ, a percent difference column, previous year's month column, a percent difference from last month to last year's month column (`early_draft_srs_galecia.txt`)

### REQ-401 - Provide Financial Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide financial reports covering fines and payments.

> - Financial reports (fines, payments): 34% (`survey_results_2009.txt`)

### REQ-402 - Provide Item Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide item reports supporting inventory, weeding, and missing-item activities.

> - Item reports (inventory, weeding, missing): 65% (`survey_results_2009.txt`)

### REQ-403 - Provide Patron Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide patron reports that identify inactive accounts.

> - Patron reports (demographics, inactive accounts): 52% (`survey_results_2009.txt`)

### REQ-404 - Provide Required Basic Statistics

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

Predefined executive reports must include basic statistics required by the Georgia Annual Report and Application for State Aid.

> These should include basic statistics like those required by the Georgia Annual Report and Application for State Aid. (`early_draft_srs_galecia.txt`)

### REQ-405 - Query Transaction Types

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must record transaction categories including check-ins, check-outs, fines collected, and patron registrations, and allow queries across all transactions or by transaction type.

> Transactions include check-ins, check-outs, fines collected, patron registrations, etc., and can be queried by all transactions or by type of transaction. (`early_draft_srs_galecia.txt`)

### REQ-406 - Records Missing MARC Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report of bibliographic records missing specified MARC fields.

> - Bib Records missing specific MARC fields (`early_draft_srs_galecia.txt`)

### REQ-407 - Records Without Volumes

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report of bibliographic records with no attached volumes.

> - Bib Records with No Volumes attached (`early_draft_srs_galecia.txt`)

### REQ-408 - Report Accrued Charges

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must report fines and charges accrued for selected time periods and by charge type, including overdue, damaged-item, and lost-item charges.

> fines and charges accrued per time period (e.g., last twelve months, YTD, last month) and per type of charge (overdue fines, damaged item charges, lost item charges, etc.) (`early_draft_srs_galecia.txt`)

### REQ-409 - Report Bibliographic Holds

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must support periodic reports identifying bibliographic records with holds.

> - Bibliographic records with holds (`early_draft_srs_galecia.txt`)

### REQ-410 - Report Branch Renewals

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must report the percentage of check-outs at a particular branch that are renewals.

> What percent of check-outs at a particular branch are renewals? (`early_draft_srs_galecia.txt`)

### REQ-411 - Report Delivery Address Book

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide an address book for report delivery recipients.

> - No address book for report delivery (`evergreen_reference_2009.txt`)

### REQ-412 - Report Facility Last-Copy Deletions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow users to run reports on items deleted when they were the last copy in a facility.

> Ability to run a report on deleted items that were the last copy in the facility (`early_draft_srs_galecia.txt`)

### REQ-413 - Report Held In-Transit Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must support periodic reports identifying in-transit items with outstanding holds.

> - In-transit items with outstanding hold (`early_draft_srs_galecia.txt`)

### REQ-414 - Report Inactive Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must support periodic reports identifying items that have not been checked out for a specified number of days.

> - Items that have not been checked out in X days (`early_draft_srs_galecia.txt`)

### REQ-415 - Report Invalid Patron Libraries

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must support periodic reports identifying patrons with invalid home libraries.

> - Patrons with invalid home library (`early_draft_srs_galecia.txt`)

### REQ-416 - Report Item-Level Holds

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must support periodic reports identifying item-level holds.

> - Item-level holds (`early_draft_srs_galecia.txt`)

### REQ-417 - Report Items Edited

**Priority:** Could - Mentioned in 2 documents. Adjusted from Should by model: Items edited count supports auditing but is relatively narrow.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must provide a report showing the number of items edited.

> - Items Edited Count (`early_draft_srs_galecia.txt`)
> - Items Edited Count (not available) (`evergreen_reference_2009.txt`)

### REQ-418 - Report Items in Transit

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must report items in transit, organized by sending library and destination library.

> - List of Items in Transit by both sending library and destination library (`early_draft_srs_galecia.txt`)
> - Items In Transit to Destination Library (`early_draft_srs_galecia.txt`)

### REQ-419 - Report Loans by Facility

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide IntraPINES loan reporting across all facilities, organized by facility.

> - IntraPINES Loans for all Facilities (`early_draft_srs_galecia.txt`)
> - IntraPINES Loans by Facility (`early_draft_srs_galecia.txt`)

### REQ-420 - Report Loans by System

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide IntraPINES loan reporting across all systems, organized by system.

> - IntraPINES Loans for all Systems (`early_draft_srs_galecia.txt`)
> - IntraPINES Loans by System (`early_draft_srs_galecia.txt`)

### REQ-421 - Report Notice Activity

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support reports on pre-overdue, overdue, and holds notices that were sent.

> Ability to run reports for pre-overdue, overdue, and holds notices sent (`early_draft_srs_galecia.txt`)

### REQ-422 - Report Prioritization

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must allow authorized users to prioritize selected types of reports.

> - No ability to prioritize certain types of reports (`evergreen_reference_2009.txt`)

### REQ-423 - Report Status Conversion

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report that assists with batch conversion of statuses.

> The system provides a report to assist in the batch conversion of statuses (`early_draft_srs_galecia.txt`)

### REQ-424 - Report Title Tooltips

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting interface must provide hover tooltips for report titles.

> - No hover tooltips for report titles (`evergreen_reference_2009.txt`)

### REQ-425 - Report Transaction Details

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow users to run reports on transactions occurring at a specified date and time, workstation, or staff member.

> Ability to run a report on transactions that occurred on x date and time on x workstation or by x staff (`early_draft_srs_galecia.txt`)

### REQ-426 - Report Transaction Totals

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide total transaction counts per patron, per library, and per system.

> Need total transactions report - per patron, per library, per system (`survey_results_2009.txt`)

### REQ-427 - Report Transaction Types

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The reporting system must support transaction reports covering check-ins, check-outs, fines collected, patron registrations, and other transaction types.

> Transactions include check-ins, check-outs, fines collected, patron registrations, etc. (`survey_results_2009.txt`)

### REQ-428 - Restrict Query Data Access

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

Administrators must be able to control staff access to database tables and fields used by the query tool.

> Administrators should control staff access to tables and fields. (`early_draft_srs_galecia.txt`)

### REQ-429 - Retrieve Specific MARC Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The reporting system must retrieve and report specific MARC fields even when those fields are stored across multiple rows.

> Need to pull specific MARC fields but they're spread across multiple rows (`survey_results_2009.txt`)

### REQ-430 - Revert Item Locations

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow users to revert items to their original location.

> Revert items to original location: 18% (`survey_results_2009.txt`)

### REQ-431 - Run Local System Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

Local System Administrators must be able to run system reports.

> They can configure local settings and run system reports. (`early_draft_srs_galecia.txt`)

### REQ-432 - Run Multiple Reports Together

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must allow users to select multiple canned reports from a list and run them at the same time.

> Canned reports can be checked off from a list to run at the same time and will be viewed within one document. (`early_draft_srs_galecia.txt`)

### REQ-433 - Run On-Demand Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must support running preset reports on demand, including maintenance and collections-development reports.

> On Demand Reports would be for pre-selected criteria but for things like maintenance reports or collections development and would be set to run on demand. (`early_draft_srs_galecia.txt`)

### REQ-434 - Run Scoped Ad Hoc Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow authorized staff to run ad hoc reports against specific sets of data, subject to administrative controls.

> System administrators should be able to create shared folders to allow or disallow staff from running specific reports, and/or to run ad hoc reports on specific sets of data. (`early_draft_srs_galecia.txt`)

### REQ-435 - Save Reusable Queries

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow users to save queries and reuse them later.

> Ability to save and reuse queries: 73% (`survey_results_2009.txt`)

### REQ-436 - Schedule Historical Canned Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must allow canned reports to run using data from yesterday, last week, last month, or last year.

> Will have the ability for it to run by yesterday's data, last week's, last month's, or last year's. (`early_draft_srs_galecia.txt`)

### REQ-437 - Schedule Recurring Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow users to schedule reports to run repeatedly on a recurring basis.

> Ability to schedule recurring reports: 52% (`survey_results_2009.txt`)

### REQ-438 - Select Query Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

Users must be able to manually select individual records from query results.

> Manually select from query results: 39% (`survey_results_2009.txt`)

### REQ-439 - Select Regular Expressions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The query tool must allow staff to select regular expressions from a drop-down menu.

> - Select regular expressions from a drop-down menu (`early_draft_srs_galecia.txt`)

### REQ-440 - Select Report Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow users to select individual parts of the available data for inclusion in a report.

> Check off any part of data you want (`early_draft_srs_galecia.txt`)

### REQ-441 - Separate Checkin Timestamp

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must store checkin date and time separately from renewal timestamps.

> - Checkin Date/time not including renewals - checkin and renewal timestamps are stored together (`evergreen_reference_2009.txt`)

### REQ-442 - Separate Reporting Operations

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must be separated from production operations so that reporting activities do not depend on or interfere with production operations.

> Separate reporting from production operations (`evergreen_reference_2009.txt`)

### REQ-443 - Show Last Circulation Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

Item reports must indicate the last circulation date for each item.

> Ability to indicate last circulation date on item reports (`survey_results_2009.txt`)

### REQ-444 - Subtotal Holds by Type

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must subtotal holds by hold type, including active, frozen, and frozen-until holds.

> Holds are subtotaled by type, e.g., active, frozen, and frozen-until holds. (`early_draft_srs_galecia.txt`)

### REQ-445 - Support Custom Local Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow users to create or use custom and locally defined reports, including collection development, program attendance, and staff productivity reports.

> Among those who use custom reports, the most common are: - Collection development reports - Program attendance tracking - Staff productivity reports (time spent per transaction) (`survey_results_2009.txt`)

### REQ-446 - Support Item Transfer Methods

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The item-transfer utility must let users move selected items by changing their location records and by generating pull lists.

> - Ability to change records of selected items to move to new location (`early_draft_srs_galecia.txt`)
> - Mechanisms for moving items: changing location field, generating pull lists (`early_draft_srs_galecia.txt`)

### REQ-447 - Support Listed Report Types

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must support reports based on bibliographic records, items, patrons, circulation actions, hold actions, monetary records, and actors.

> The following record types are available for reporting: - bibliographic_record: Title, author, ISBN, publication info, subjects, etc. - item: Call number, barcode, location (copy location), status, etc. - patron: Name, address, library, patron type, etc. - action_circulation: Checkout, checkout, ren... (`evergreen_reference_2009.txt`)

### REQ-448 - Support Related Record Reporting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must support traversing the documented relationships between bibliographic records and items, items and circulation transactions, patrons and circulation transactions, patrons and monetary records, and actors and circulation transactions.

> 3.2 KEY RELATIONSHIPS - bibliographic_record -> item (through asset.copy) - item -> action.circulation (through circulation transactions) - patron -> action.circulation (through patron_id) - patron -> money (through debt records) - actor -> action.circulation (through librarian link) (`evergreen_reference_2009.txt`)

### REQ-449 - System Long-Overdue Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a report listing items marked long overdue by the system.

> - Items marked longoverdue by system (`early_draft_srs_galecia.txt`)

### REQ-450 - Three Reporting Interfaces

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide separate canned, on-demand, and open-template reporting interfaces.

> - Three interfaces (canned, on-demand, open template) - only basic canned exists (`evergreen_reference_2009.txt`)

### REQ-451 - Total Circulation Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system shall provide a total circulation report including checkouts, renewals, and non-cataloged circulation.

> - Circulation Count - total circ including checkouts, renewals, and noncats (`early_draft_srs_galecia.txt`)

### REQ-452 - Track Item Usage

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide total item use counts and usage counts broken down by configurable date ranges, such as fiscal-year or monthly periods.

> Ability to have a total use count on items as well as a use count broken down by usage date range such as an FY use count or monthly use count (`early_draft_srs_galecia.txt`)

### REQ-453 - Verify Financial Transactions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support tracking and verification of financial transactions.

> Tracking and verifying financial transactions. (`early_draft_srs_galecia.txt`)

## Blacklist

Items found in the sources but discarded, with the reason. They are not part of the requirements above.

### BL-001 - Separate Reporting Database

**Reason (Conflicts with another requirement):** This earlier requirement to provide a separate reporting database or replica conflicts with the later direction to retain reporting data in the main relational database and avoid a separate synchronized reporting warehouse.  
**Conflicts with:** REQ-102  
**Sources:** `evergreen_reference_2009.txt`

### BL-002 - Accelerate Material Distribution

**Reason (Too vague or not a software requirement):** The requirement calls for rapid processing and distribution but does not define measurable criteria for what constitutes rapid processing.  
**Sources:** `interview_cataloging_2009-05-08.txt`

### BL-003 - Avoid Defining Common Terminology

**Reason (Too vague or not a software requirement):** This is guidance for writing requirements documentation, not a requirement for the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-004 - Complete Reports Promptly

**Reason (Too vague or not a software requirement):** “Adequate performance” and “excessively long” do not define a testable performance threshold.  
**Sources:** `survey_results_2009.txt`

### BL-005 - Create Library Templates

**Reason (Too vague or not a software requirement):** This assigns the project a task to determine and create templates rather than specifying behavior required of the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-006 - Defer Detailed UI Specification

**Reason (Too vague or not a software requirement):** This describes a future specification and prototyping process rather than a testable requirement for the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-007 - Distribute Uncataloged Material Quickly

**Reason (Too vague or not a software requirement):** The requirement does not define what distribution involves or how quickly it must occur, so it is too vague to test.  
**Sources:** `early_draft_srs_galecia.txt`

### BL-008 - Ensure SRS Readability

**Reason (Too vague or not a software requirement):** This is a quality goal for the requirements specification, not a requirement for the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-009 - Expand Report Types

**Reason (Too vague or not a software requirement):** The requirement does not identify the needed report types or define how to determine whether the reporting gaps have been covered, so it is not testable.  
**Sources:** `evergreen_reference_2009.txt`

### BL-010 - Filter Reports Development

**Reason (Too vague or not a software requirement):** This specifies an organizational review and testing process for development rather than a requirement for the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-011 - Limit Specification Scope

**Reason (Too vague or not a software requirement):** This describes the scope of the requirements document rather than a requirement for the software.  
**Sources:** `early_draft_srs_galecia.txt`

### BL-012 - Minimize Branch Labor

**Reason (Too vague or not a software requirement):** The request concerns managing uncataloged materials rather than the reporting system, and 'minimal staff effort' has no measurable acceptance criterion.  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

### BL-013 - Preserve Template Results

**Reason (Too vague or not a software requirement):** The requirement is too vague to test: it does not define what correctness or intended results mean, or how template changes must be evaluated.  
**Sources:** `email_report_features.eml`

### BL-014 - Provide Findable Reports

**Reason (Too vague or not a software requirement):** The requirement relies on subjective terms such as “understandable enough” and provides no testable criteria for report organization or findability.  
**Sources:** `survey_results_2009.txt`

### BL-015 - Specify Item Records

**Reason (Too vague or not a software requirement):** This requests a developer data-specification deliverable rather than behavior or a capability of the software.  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

### BL-016 - Support Field Filtering

**Reason (Too vague or not a software requirement):** The requirement is too vague to test because it does not define which fields are relevant or available for filtering.  
**Sources:** `survey_results_2009.txt`

### BL-017 - Support Management and Reporting

**Reason (Too vague or not a software requirement):** This states only a broad goal to support management and reporting, without specifying a capability that can be tested.  
**Sources:** `early_draft_srs_galecia.txt`

### BL-018 - Define Executive Reports

**Reason (Describes existing behaviour, not a new need):** This asks the project to compile a list of reports, rather than requiring functionality from the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-019 - Document Future Reporting Requirements

**Reason (Describes existing behaviour, not a new need):** This describes documenting requirements and functionality for a future release, rather than a need the reporting software must meet.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-020 - Enable Iterative User Review

**Reason (Describes existing behaviour, not a new need):** This describes a development and review process rather than a requirement for the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-021 - Focus On Management Activities

**Reason (Describes existing behaviour, not a new need):** This describes the scope of the requirements effort rather than a testable requirement for the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-022 - Support Multiple SRS Audiences

**Reason (Describes existing behaviour, not a new need):** This specifies who the requirements document should serve, not behavior or a quality of the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

