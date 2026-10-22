# Software Requirements

Generated 2026-10-22 from 20 source documents by an agentic LangGraph pipeline. 421 requirements, 25 blacklisted items.

## Priority scale

Priorities use three MoSCoW levels. Each requirement states below why it got its level.

- **Must** (25): Essential. Stated as high priority in a source document, or confirmed by several independent documents and strong wording. The system is not acceptable without it.
- **Should** (123): Important. Wanted by more than one document, or stated with strong wording, or marked medium priority. Include unless time is short.
- **Could** (273): Desirable. Mentioned once and without emphasis. Include if capacity allows.

How a level is chosen: an explicit priority tag in a source document is final. Otherwise it is computed from the number of distinct documents that mention the requirement and from emphatic wording in the stakeholders' own words; a language model may move the result by one level for content reasons.

## Overview

| ID | Requirement | Priority | Type | Sources |
|---|---|---|---|---|
| REQ-001 | Control Report Access With Folders | Must | functional | 4 |
| REQ-002 | Show Report Queue With Criteria | Must | functional | 5 |
| REQ-003 | Report Material Volume Snapshot | Must | functional | 5 |
| REQ-004 | Control Staff Access By Roles | Must | functional | 6 |
| REQ-005 | Report Missing Damaged Items ByBranch | Must | functional | 4 |
| REQ-006 | Generate Last Copy Report | Must | functional | 4 |
| REQ-007 | Record Deletion Audit Via Trigger | Must | functional | 2 |
| REQ-008 | Anonymize Archived Patron Transactions | Must | constraint | 3 |
| REQ-009 | Record Deletion Audit Tracking | Must | functional | 4 |
| REQ-010 | Include Nulls For Missing Values | Must | functional | 4 |
| REQ-011 | Query Transfer Candidate Items | Must | functional | 4 |
| REQ-012 | Revert Transferred Items To Origin | Must | functional | 4 |
| REQ-013 | Save Reusable Transfer Candidate Queries | Must | functional | 4 |
| REQ-014 | Update Item Records New Location | Must | functional | 4 |
| REQ-015 | Ensure Section 508 Accessibility Support | Must | non-functional | 5 |
| REQ-016 | Provide Integrated Context Sensitive Help | Must | functional | 5 |
| REQ-017 | Support Linux And Solaris Servers | Must | constraint | 2 |
| REQ-018 | Cancel Scheduled Or Running Reports | Must | functional | 4 |
| REQ-019 | Generate Standards Compliant HTML | Must | constraint | 3 |
| REQ-020 | Provide Authority Bibliographic Data Specs | Must | functional | 3 |
| REQ-021 | Use Relational Database For Reporting | Must | constraint | 3 |
| REQ-022 | Support Consortium Scale Processing | Must | non-functional | 2 |
| REQ-023 | Allow Busy Hours Reporting | Must | non-functional | 2 |
| REQ-024 | Avoid Restricting OPAC Functionality | Must | constraint | 1 |
| REQ-025 | Enable Web And Windows Client Access | Must | constraint | 1 |
| REQ-026 | Checkout-Only Circulation Report | Should | functional | 2 |
| REQ-027 | Combine Patron Filters With Logic | Should | functional | 2 |
| REQ-028 | Count Bibliographic Records Only | Should | functional | 2 |
| REQ-029 | Items Added Count Report | Should | functional | 2 |
| REQ-030 | Items Currently Checked Out | Should | functional | 2 |
| REQ-031 | List Bibliographic Records No Volumes | Should | functional | 2 |
| REQ-032 | Manage Fine Grained Report Access | Should | functional | 3 |
| REQ-033 | Missing Or Damaged Items Report | Should | functional | 3 |
| REQ-034 | Monthly Quarterly Yearly Deletion Totals | Should | functional | 3 |
| REQ-035 | Overdue Items Daily Shelf Reading | Should | functional | 2 |
| REQ-036 | Provide Aged Debt Report | Should | functional | 2 |
| REQ-037 | Provide Detailed Payment Receipts Report | Should | functional | 2 |
| REQ-038 | Provide Local Admin Role | Should | functional | 2 |
| REQ-039 | Report Circulation By Shelving Location | Should | functional | 2 |
| REQ-040 | Report Patron Counts By Home Library | Should | functional | 2 |
| REQ-041 | Report Patron Counts By Home Library | Should | functional | 2 |
| REQ-042 | Restrict Patron Direct Management Reporting | Should | functional | 2 |
| REQ-043 | Run Multiple Reports Concurrently | Should | functional | 2 |
| REQ-044 | Schedule And Consolidate Report Runs | Should | functional | 2 |
| REQ-045 | Separate Renewal Count Report | Should | functional | 2 |
| REQ-046 | Allow RFID Card Staff Login | Should | functional | 3 |
| REQ-047 | Authenticate Individual Staff For Audit | Should | functional | 1 |
| REQ-048 | Determine Permissions On Every Login | Should | functional | 2 |
| REQ-049 | Export Reports CSV And Excel | Should | functional | 3 |
| REQ-050 | Compare Branch Breakdowns SideBySide | Should | functional | 2 |
| REQ-051 | Compare Shelf Space Utilization | Should | functional | 3 |
| REQ-052 | Generate Shelf Space Reports Branches | Should | functional | 2 |
| REQ-053 | Merge In-Transit To From | Should | functional | 3 |
| REQ-054 | Provide In-Transit Overdue Report | Should | functional | 3 |
| REQ-055 | Convert Multiple Item Statuses Batch | Should | functional | 3 |
| REQ-056 | Provide Purge Criteria Utility | Should | functional | 3 |
| REQ-057 | Purge Candidate Utility With Duration | Should | functional | 2 |
| REQ-058 | Select Purge Candidates By Status Criteria | Should | functional | 2 |
| REQ-059 | Report Status Conversion Candidates | Should | functional | 3 |
| REQ-060 | Anonymized Demographic Transaction Stats | Should | functional | 2 |
| REQ-061 | Configurable Transaction History Retention | Should | functional | 2 |
| REQ-062 | Control Report Template Permissions | Should | functional | 3 |
| REQ-063 | Indefinite Aggregate Transaction Retention | Should | functional | 2 |
| REQ-064 | Provide Anonymized Patron Behavior Analytics | Should | functional | 2 |
| REQ-065 | Provide Region Age Anonymized Demographics | Should | functional | 2 |
| REQ-066 | Typed Transaction Query Grouping | Should | functional | 2 |
| REQ-067 | Filter Patron By Demographics | Should | functional | 2 |
| REQ-068 | Filter And Group Patron Counts By Age | Should | functional | 2 |
| REQ-069 | Group Patrons By Geographic Attributes | Should | functional | 3 |
| REQ-070 | Generate Configurable Inactivity Report | Should | functional | 2 |
| REQ-071 | Manually Select Items For Transfer | Should | functional | 3 |
| REQ-072 | Process Uncataloged Material Rapid Distribution | Should | functional | 2 |
| REQ-073 | Report Uncataloged Material Usage | Should | functional | 2 |
| REQ-074 | Track Uncataloged Material Inventory Control | Should | functional | 2 |
| REQ-075 | Uncataloged Material Circulation Counting | Should | functional | 2 |
| REQ-076 | Periodic Reports For Invalid Item Types | Should | functional | 2 |
| REQ-077 | Periodic Reports For Long Call Numbers | Should | functional | 2 |
| REQ-078 | Prevent OPAC Performance Impact | Should | non-functional | 2 |
| REQ-079 | Produce Standards Compliant Semantic HTML | Should | non-functional | 2 |
| REQ-080 | Queue Searches And Reports During Peak | Should | non-functional | 2 |
| REQ-081 | Separate Development Training Environments | Should | functional | 2 |
| REQ-082 | Support Development Training Production Environments | Should | functional | 5 |
| REQ-083 | Support Legacy Browser Versions | Should | constraint | 2 |
| REQ-084 | Use Relational PostgreSQL Schema | Should | constraint | 2 |
| REQ-085 | Batch Location Updates TransactionSafe | Should | non-functional | 1 |
| REQ-086 | Restrict Transfer Permissions By Role | Should | constraint | 1 |
| REQ-087 | Transfer Batch Items And PullLists | Should | functional | 2 |
| REQ-088 | Transfer Utility With Pull List And Audit | Should | functional | 2 |
| REQ-089 | Keep Reporting Architecturally Separate | Should | constraint | 2 |
| REQ-090 | Support Linux And Solaris Server Environments | Should | constraint | 2 |
| REQ-091 | Centralize Management Processes Across Branches | Should | constraint | 3 |
| REQ-092 | Consolidate Multi-Branch Enterprise Data | Should | non-functional | 1 |
| REQ-093 | Document Major System Processes | Should | functional | 3 |
| REQ-094 | Export Reports Multiple Formats | Should | functional | 2 |
| REQ-095 | Expose Query-Specific Error Details | Should | functional | 3 |
| REQ-096 | Filter Surveys By Survey Name | Should | functional | 2 |
| REQ-097 | Integrate Vendor Data Via APIs | Should | functional | 3 |
| REQ-098 | Keep Reporting Separate From OPAC | Should | constraint | 2 |
| REQ-099 | Provide Detailed Error Reporting Feedback | Should | functional | 3 |
| REQ-100 | Provide Historical Reporting Warehouse | Should | functional | 2 |
| REQ-101 | Provide Management Record Data Specifications | Should | functional | 1 |
| REQ-102 | Use Acquisitions Cataloging As Source | Should | constraint | 3 |
| REQ-103 | Accounting-Compliant Report Archival | Should | constraint | 2 |
| REQ-104 | Patron Payment Charge Ledger | Should | functional | 2 |
| REQ-105 | Threshold Patron Balance Query | Should | functional | 2 |
| REQ-106 | Patron Item Financial Association | Should | functional | 2 |
| REQ-107 | In Transit Items Destination Grouping | Should | functional | 2 |
| REQ-108 | Interface With OPAC For Reporting | Should | functional | 2 |
| REQ-109 | Activity Reports With Permission Cross Tabs | Should | functional | 2 |
| REQ-110 | Assign Report Queue Priorities | Should | functional | 2 |
| REQ-111 | Choose Query Values From Picklists | Should | functional | 2 |
| REQ-112 | Cross Tabulate Board Activity | Should | functional | 2 |
| REQ-113 | Design Queries With Boolean Regex | Should | functional | 2 |
| REQ-114 | Differentiate Create And Clone Permission | Should | functional | 2 |
| REQ-115 | Display Selection Criteria With Results | Should | functional | 3 |
| REQ-116 | Provide Georgia Annual Activity Reports | Should | functional | 2 |
| REQ-117 | Select Query Fields Across Records | Should | functional | 2 |
| REQ-118 | Show Report Queue Position | Should | functional | 3 |
| REQ-119 | Count Edited Bibliographic Records | Should | functional | 2 |
| REQ-120 | Deliver Report Output By Email | Should | functional | 2 |
| REQ-121 | Dewey Grouped Circulation Counts | Should | functional | 2 |
| REQ-122 | Expose Last Circulation Date Field | Should | functional | 2 |
| REQ-123 | Fines Stopped Reason Item List | Should | functional | 2 |
| REQ-124 | Group Circulation Counts By Age | Should | functional | 2 |
| REQ-125 | Group Collection Age By Call Number | Should | functional | 2 |
| REQ-126 | Items Created Date Range Report | Should | functional | 2 |
| REQ-127 | Items Edited Count Capability | Should | functional | 2 |
| REQ-128 | List Inactive Patrons | Should | functional | 2 |
| REQ-129 | Location And County Circulation | Should | functional | 2 |
| REQ-130 | MARC Field Circulation Counts | Should | functional | 2 |
| REQ-131 | Method-Based Check-In Counting | Should | functional | 2 |
| REQ-132 | Modifier Grouped Circulation Counts | Should | functional | 2 |
| REQ-133 | Patron Balance Financial Reporting | Should | functional | 1 |
| REQ-134 | Present Results As Pivot Tables | Should | functional | 3 |
| REQ-135 | Provide Anonymized Demographic Reporting | Should | non-functional | 1 |
| REQ-136 | Provide Geographic Demographic Reporting | Should | functional | 1 |
| REQ-137 | Provide RealTime Reporting On Current | Should | functional | 2 |
| REQ-138 | Provide Three Reporting Interfaces | Should | functional | 2 |
| REQ-139 | Report Claims-Returned Items | Should | functional | 2 |
| REQ-140 | Report Holds Requiring Purchase Alert | Should | functional | 2 |
| REQ-141 | Report Missing MARC Fields | Should | functional | 2 |
| REQ-142 | Report Staff Password Change Dates | Should | functional | 2 |
| REQ-143 | Report Stale Holds Awaiting Pickup | Should | functional | 2 |
| REQ-144 | Report Unfilled Holds Only | Should | functional | 2 |
| REQ-145 | Support Assistive Technology For Web | Should | constraint | 1 |
| REQ-146 | Support Fine-Grained Queueable Reporting | Should | constraint | 1 |
| REQ-147 | Type-Based Checkout Renewal Counting | Should | functional | 2 |
| REQ-148 | Use Canned Report Definitions Appendix A | Should | constraint | 1 |
| REQ-149 | Allow Staff Report Content Creation | Could | functional | 1 |
| REQ-150 | Analyze Branch Capacity Distribution | Could | functional | 2 |
| REQ-151 | Analyze Collection Usage For Management | Could | functional | 2 |
| REQ-152 | Analyze Patron Demographics And Interests | Could | functional | 2 |
| REQ-153 | Analyze Staff Productivity Workflow | Could | functional | 2 |
| REQ-154 | Build Complex Queries Without Workarounds | Could | functional | 1 |
| REQ-155 | Compile Executive Reports Interface List | Could | functional | 1 |
| REQ-156 | Cover Management Activities Reporting Requirements | Could | constraint | 1 |
| REQ-157 | Create PINES Library Report Templates | Could | functional | 1 |
| REQ-158 | Define Management Processes Scope | Could | constraint | 1 |
| REQ-159 | Email Deliver Scheduled Report Results | Could | functional | 1 |
| REQ-160 | Expose All Database Fields | Could | functional | 1 |
| REQ-161 | Manage Consortium PINES Settings | Could | functional | 1 |
| REQ-162 | Provide Management Reporting Tools | Could | functional | 1 |
| REQ-163 | Provide Non Cataloged Items Report | Could | functional | 1 |
| REQ-164 | Provide Web Reporting Drag Drop | Could | functional | 1 |
| REQ-165 | Restrict Staff Report Filters | Could | functional | 1 |
| REQ-166 | Show Current Patron Bills Owed | Could | functional | 1 |
| REQ-167 | Support Regex In Query Filters | Could | functional | 2 |
| REQ-168 | Track Financial Transactions Verification | Could | functional | 2 |
| REQ-169 | Report Acquisition Period Volume | Could | functional | 1 |
| REQ-170 | Define Branch Capacity Calculation | Could | constraint | 1 |
| REQ-171 | Drilldown Branch Capacity Details | Could | functional | 1 |
| REQ-172 | Filter Branch Capacity By Criteria | Could | functional | 1 |
| REQ-173 | Show Branch Capacity Status Colors | Could | functional | 1 |
| REQ-174 | Sort Branch Capacity Results | Could | functional | 1 |
| REQ-175 | Assign Roles For Differentiated Access | Could | functional | 1 |
| REQ-176 | Display Branch Capacity Overview | Could | functional | 1 |
| REQ-177 | Manage Security Groups Or Roles | Could | functional | 1 |
| REQ-178 | Show Branch Capacity Trend Direction | Could | functional | 1 |
| REQ-179 | Update Permissions By Role Change | Could | non-functional | 1 |
| REQ-180 | Compare Library Shelf Space SystemAverage | Could | functional | 1 |
| REQ-181 | Estimate Shelf Space By Dimensions | Could | constraint | 1 |
| REQ-182 | Filter Shelf Utilization Date Range | Could | functional | 1 |
| REQ-183 | Report Circulation Category Percentages | Could | functional | 1 |
| REQ-184 | Report Collection Category Percentages | Could | functional | 1 |
| REQ-185 | Sum Checkouts For Category Share | Could | functional | 1 |
| REQ-186 | Configure In-Transit Threshold Days | Could | constraint | 1 |
| REQ-187 | Filter Missing Damaged Reports Dates | Could | functional | 1 |
| REQ-188 | Identify Repeated Missing Titles | Could | functional | 1 |
| REQ-189 | Include Condition Notes In Reports | Could | functional | 1 |
| REQ-190 | Sort In-Transit By Due Date | Could | functional | 1 |
| REQ-191 | Combine Purge Criteria With AND | Could | functional | 1 |
| REQ-192 | Configure Purge Eligibility Criteria | Could | functional | 1 |
| REQ-193 | Confirm Purge Deletions Manually | Could | functional | 1 |
| REQ-194 | Delete Orphan Records Fast | Could | functional | 1 |
| REQ-195 | Delete Volume With Items | Could | functional | 3 |
| REQ-196 | Filter Purge By Last Circulation | Could | functional | 1 |
| REQ-197 | Maintain Purge Operation Audit Trail | Could | functional | 1 |
| REQ-198 | Present Purge Candidates Read Only | Could | functional | 1 |
| REQ-199 | Schedule Automatic Purge Utility | Could | functional | 1 |
| REQ-200 | Separate Candidate From Deletion | Could | non-functional | 1 |
| REQ-201 | Filter Deletion Reports By Criteria | Could | functional | 1 |
| REQ-202 | Identify Top Deleting Staff | Could | functional | 1 |
| REQ-203 | Provide Deletion Audit Query Interface | Could | functional | 1 |
| REQ-204 | Report Deletions By Branch | Could | functional | 1 |
| REQ-205 | Report Deletions By System | Could | functional | 1 |
| REQ-206 | Track Denied Deletion Attempts | Could | functional | 1 |
| REQ-207 | Count Check-in Methods Individually | Could | functional | 1 |
| REQ-208 | Count Checkout And Renewal Variants | Could | functional | 1 |
| REQ-209 | Count Holds By Placement Method | Could | functional | 1 |
| REQ-210 | Group Transaction Data By Branch | Could | functional | 1 |
| REQ-211 | Calculate Patron Age Ranges At Query | Could | functional | 1 |
| REQ-212 | Configure Patron Age Brackets | Could | functional | 1 |
| REQ-213 | Filter Patrons By Checkout Inactivity | Could | functional | 1 |
| REQ-214 | Generate Patron Demographic Reports | Could | functional | 1 |
| REQ-215 | Group Patron Results With Metrics | Could | functional | 1 |
| REQ-216 | Configure Report Specific Age Ranges | Could | functional | 1 |
| REQ-217 | Group Patron Results By Fields | Could | functional | 1 |
| REQ-218 | Group Patrons By Home Branch | Could | functional | 1 |
| REQ-219 | Group Patrons By Patron Type | Could | functional | 1 |
| REQ-220 | Group Patrons By Preferred Language | Could | functional | 1 |
| REQ-221 | Limit Patron Results By Filters | Could | functional | 1 |
| REQ-222 | Cache Inactivity Report Results | Could | non-functional | 1 |
| REQ-223 | Combine Electronic Activity Histories | Could | functional | 1 |
| REQ-224 | Count Electronic Activity Inactivity | Could | functional | 1 |
| REQ-225 | Exclude Selected Patron Types | Could | functional | 1 |
| REQ-226 | Generate Inactive Patron Results | Could | functional | 1 |
| REQ-227 | Include Patron Mailing Address | Could | functional | 1 |
| REQ-228 | Provide Inactive Totals By Branch | Could | functional | 1 |
| REQ-229 | Run Inactivity Reports Background | Could | non-functional | 1 |
| REQ-230 | Separate Inactive With Fines | Could | functional | 1 |
| REQ-231 | Support Configurable Inactivity Days | Could | functional | 1 |
| REQ-232 | Display Last Item Edit Date | Could | functional | 1 |
| REQ-233 | Enable Search In HTML Help | Could | functional | 1 |
| REQ-234 | Organize Hierarchical Online Help | Could | functional | 1 |
| REQ-235 | Provide Separate Searchable Help System | Could | non-functional | 1 |
| REQ-236 | Report Bibliographics With No Items | Could | functional | 1 |
| REQ-237 | Auto Return Temporary Event Transfers | Could | functional | 1 |
| REQ-238 | Auto Revert Transfers By Criteria | Could | functional | 1 |
| REQ-239 | Confirm Transfer With Item Preview | Could | functional | 1 |
| REQ-240 | Generate Printable Transit Labels | Could | functional | 1 |
| REQ-241 | Log Item Transfers For Audit | Could | functional | 1 |
| REQ-242 | Notify Users Transfer Delays Issues | Could | functional | 1 |
| REQ-243 | Prevent Reversion When CheckedOut | Could | functional | 1 |
| REQ-244 | Process Large Transfers Efficiently | Could | non-functional | 1 |
| REQ-245 | Retain Item Transfer History | Could | functional | 1 |
| REQ-246 | Share Saved Candidate Queries | Could | functional | 1 |
| REQ-247 | Support Event Temporary Transfers | Could | functional | 1 |
| REQ-248 | Undo Item Transfers After Confirmation | Could | functional | 1 |
| REQ-249 | Check Report Cancellation Signals | Could | constraint | 1 |
| REQ-250 | Handle Optional Vendor Integration Data | Could | constraint | 1 |
| REQ-251 | Provide Current Data Reports | Could | functional | 1 |
| REQ-252 | Provide Global Admin Full Access | Could | functional | 1 |
| REQ-253 | Provide Historical Date Reporting | Could | functional | 1 |
| REQ-254 | Provide Library Manager Role | Could | functional | 1 |
| REQ-255 | Provide Staff Role For Report Runs | Could | functional | 1 |
| REQ-256 | Provide Training With Data Migration | Could | constraint | 1 |
| REQ-257 | Query OPAC Data Read Only | Could | constraint | 1 |
| REQ-258 | Read From Library Automation System | Could | constraint | 1 |
| REQ-259 | Read OPAC Holds And Circulation | Could | functional | 1 |
| REQ-260 | Accrue Fines And Charges Reporting | Could | functional | 1 |
| REQ-261 | Enforce Financial Data Retention | Could | constraint | 1 |
| REQ-262 | Generate Item Value Reports | Could | functional | 1 |
| REQ-263 | Join Financial Patron And Item Data | Could | functional | 1 |
| REQ-264 | Provide Patron Account Balance Reports | Could | functional | 1 |
| REQ-265 | Report Payments By Channel And Type | Could | functional | 1 |
| REQ-266 | Track Waived Fines By Branch | Could | functional | 1 |
| REQ-267 | Update Financial Information Easily | Could | functional | 1 |
| REQ-268 | Control Access By Roles | Could | functional | 1 |
| REQ-269 | Provide Collection Weeding Reports | Could | functional | 1 |
| REQ-270 | Provide Data Quality Assessment Reports | Could | functional | 1 |
| REQ-271 | Provide Director-Level Financial Reports | Could | functional | 1 |
| REQ-272 | Provide Inventory Tracking Reports | Could | functional | 1 |
| REQ-273 | Provide Library Capacity Reports | Could | functional | 1 |
| REQ-274 | Provide Predefined Board Reports | Could | functional | 1 |
| REQ-275 | Provide Shelf Space Utilization | Could | functional | 1 |
| REQ-276 | Provide Web Or Windows Client Access | Could | functional | 1 |
| REQ-277 | Support Demographic Program Planning Analysis | Could | functional | 1 |
| REQ-278 | Support Internet Explorer And Firefox | Could | constraint | 1 |
| REQ-279 | Support Linux Or Solaris Processing | Could | constraint | 1 |
| REQ-280 | Clone Report Template Variants | Could | functional | 1 |
| REQ-281 | Display Report Submission Timestamp | Could | functional | 1 |
| REQ-282 | Indicate Report Processing Status | Could | functional | 1 |
| REQ-283 | Maintain Named Report Consistency | Could | functional | 1 |
| REQ-284 | Preserve Report Template Results | Could | non-functional | 1 |
| REQ-285 | Provide Regex Dropdown Selection | Could | functional | 1 |
| REQ-286 | Restrict Template Filter And Fields | Could | functional | 2 |
| REQ-287 | Retain Transactions Per State Law | Could | constraint | 1 |
| REQ-288 | Support Boolean Query Operators | Could | functional | 1 |
| REQ-289 | Update Report Permissions On Role | Could | functional | 1 |
| REQ-290 | Clone Existing Report Templates | Could | functional | 1 |
| REQ-291 | Provide Query Designer Picklists | Could | functional | 1 |
| REQ-292 | Allow Admin Manage Report Templates | Could | functional | 1 |
| REQ-293 | Allow Admin Run System Reports | Could | functional | 1 |
| REQ-294 | Allow Canned Display Editing | Could | functional | 1 |
| REQ-295 | Allow Local System Admin Configuration | Could | functional | 1 |
| REQ-296 | Allow Staff Report Templates | Could | functional | 1 |
| REQ-297 | Annual Report Holds Placed Count | Could | functional | 1 |
| REQ-298 | Breakdown Circulation Counts By Type | Could | functional | 1 |
| REQ-299 | Cataloged And Uncataloged Merge | Could | functional | 1 |
| REQ-300 | Combined Total Circulation Report | Could | functional | 1 |
| REQ-301 | Compare Period Values And Percentages | Could | functional | 1 |
| REQ-302 | Control Display Field Alteration | Could | functional | 1 |
| REQ-303 | Control Fine Grained Report Permissions | Could | functional | 1 |
| REQ-304 | Control Fine Grained Template Permissions | Could | functional | 1 |
| REQ-305 | Count Bibliographic Additions By Staff | Could | functional | 1 |
| REQ-306 | Deliver Generated Reports By Email | Could | functional | 1 |
| REQ-307 | Deliver Prewritten Canned Templates | Could | functional | 1 |
| REQ-308 | Display OpenTemplate Attributes | Could | functional | 1 |
| REQ-309 | Display Report Name And Date Range | Could | functional | 1 |
| REQ-310 | Edit Canned Report Display Options | Could | functional | 1 |
| REQ-311 | Edit OnDemand Report Criteria | Could | functional | 1 |
| REQ-312 | Enhance Detailed Aged Debt Report | Could | functional | 1 |
| REQ-313 | Estimate Item Renewal Likelihood | Could | functional | 1 |
| REQ-314 | Estimate Item Renewal Likelihood | Could | functional | 1 |
| REQ-315 | Exclude Last Edit From Circulation | Could | functional | 1 |
| REQ-316 | Export Report Output Formats | Could | functional | 1 |
| REQ-317 | Export Reports Multiple File Formats | Could | functional | 1 |
| REQ-318 | Expose Bibliographic Report Fields | Could | functional | 1 |
| REQ-319 | Expose Item Report Fields | Could | functional | 1 |
| REQ-320 | Filter Reports By All Fields | Could | functional | 1 |
| REQ-321 | Filter With OpenTemplate Attributes | Could | functional | 1 |
| REQ-322 | Generate Combined In-Transit Items Reports | Could | functional | 1 |
| REQ-323 | Generate Consortium Wide Statistical Reports | Could | functional | 1 |
| REQ-324 | Generate Item Use Count List | Could | functional | 1 |
| REQ-325 | High Use Threshold Item Report | Could | functional | 1 |
| REQ-326 | Hold Request Placement Counting | Could | functional | 1 |
| REQ-327 | Identify Hold Placement Method | Could | functional | 1 |
| REQ-328 | Include Null And Blank Fields | Could | functional | 1 |
| REQ-329 | Integrate With Enterprise ILS Data | Could | constraint | 1 |
| REQ-330 | Item Value Collection Reporting | Could | functional | 1 |
| REQ-331 | Last Copy Deleted Items Report | Could | functional | 1 |
| REQ-332 | List Barred Patrons Only | Could | functional | 1 |
| REQ-333 | List Bibliographic Text-Matching Items | Could | functional | 1 |
| REQ-334 | List Deleted Last Owned Items | Could | functional | 1 |
| REQ-335 | List Of Items Added | Could | functional | 1 |
| REQ-336 | List Patrons By Expiration Date | Could | functional | 1 |
| REQ-337 | List Patrons By Notes Wording | Could | functional | 1 |
| REQ-338 | List Patrons By Survey Answer Filter | Could | functional | 1 |
| REQ-339 | Location And Home Library Counts | Could | functional | 1 |
| REQ-340 | Long Overdue System Marked List | Could | functional | 1 |
| REQ-341 | Low Use Threshold Item Report | Could | functional | 1 |
| REQ-342 | Maintain Report Recipient Address Book | Could | functional | 1 |
| REQ-343 | Manage Report Templates Administration | Could | functional | 1 |
| REQ-344 | Modifier Category Circulation Breakdown | Could | functional | 1 |
| REQ-345 | Modify Recurring Report Selections | Could | functional | 1 |
| REQ-346 | Monthly Cataloged In-House Use Count | Could | functional | 1 |
| REQ-347 | Monthly Non-Cataloged In-House Use Report | Could | functional | 1 |
| REQ-348 | Patron Hold Status Display | Could | functional | 1 |
| REQ-349 | Periodic Reports For Bibliographic Holds | Could | functional | 1 |
| REQ-350 | Periodic Reports For In-Transit Held Items | Could | functional | 1 |
| REQ-351 | Periodic Reports For Inactive Checkouts | Could | functional | 1 |
| REQ-352 | Periodic Reports For Invalid Patron Home | Could | functional | 1 |
| REQ-353 | Periodic Reports For Item-Level Holds | Could | functional | 1 |
| REQ-354 | Periodic Reports For Itemless Bibliographics | Could | functional | 1 |
| REQ-355 | Present Consolidated Multiple Canned Results | Could | functional | 1 |
| REQ-356 | Prevent Excel Export Duplicate Rows | Could | functional | 1 |
| REQ-357 | Prevent Unauthorized Template Violations | Could | functional | 1 |
| REQ-358 | Prioritize Selected Report Types | Could | functional | 1 |
| REQ-359 | Process Long Running Reports In Background | Could | functional | 1 |
| REQ-360 | Provide Age Range Demographic Reporting | Could | functional | 1 |
| REQ-361 | Provide Aggregated Administrator Reports | Could | functional | 1 |
| REQ-362 | Provide Board Executive Cross Tabs | Could | functional | 1 |
| REQ-363 | Provide Forgive Work Goods Payments | Could | functional | 1 |
| REQ-364 | Provide Historical Snapshot Bills Reports | Could | functional | 1 |
| REQ-365 | Provide Item Total Use Counts | Could | functional | 1 |
| REQ-366 | Provide Manager Planning And Evaluation | Could | functional | 1 |
| REQ-367 | Provide Patron Fields In Reports | Could | functional | 1 |
| REQ-368 | Provide Real Time Busy Period Reporting | Could | functional | 1 |
| REQ-369 | Provide Recipient Email Address Book | Could | functional | 1 |
| REQ-370 | Provide Report Title Quick Access | Could | functional | 1 |
| REQ-371 | Provide Snapshot Bills Historical Report | Could | functional | 1 |
| REQ-372 | Provide Weeding Collection Review | Could | functional | 1 |
| REQ-373 | Report Actor Circulation Using Librarian Link | Could | functional | 1 |
| REQ-374 | Report Average Item Return Time | Could | functional | 1 |
| REQ-375 | Report Bibliographic Additions By User And Library | Could | functional | 1 |
| REQ-376 | Report Bibliographic Asset Copy Relationship | Could | functional | 1 |
| REQ-377 | Report Branch Renewals Percentage | Could | functional | 1 |
| REQ-378 | Report Collection Price By Call Number | Could | functional | 1 |
| REQ-379 | Report Collection Value By Location | Could | functional | 1 |
| REQ-380 | Report Holds Fulfillment Items Received | Could | functional | 1 |
| REQ-381 | Report Holds Fulfillment Items Sent | Could | functional | 1 |
| REQ-382 | Report IntraPINES Loans All Facilities | Could | functional | 1 |
| REQ-383 | Report IntraPINES Loans All Systems | Could | functional | 1 |
| REQ-384 | Report IntraPINES Loans Grouped By Facility | Could | functional | 1 |
| REQ-385 | Report IntraPINES Loans Grouped By System | Could | functional | 1 |
| REQ-386 | Report Item Circulation Transaction Relationship | Could | functional | 1 |
| REQ-387 | Report Monthly Patron Additions | Could | functional | 1 |
| REQ-388 | Report Patron Circulation Using Patron Id | Could | functional | 1 |
| REQ-389 | Report Patron Counts By Age Demographic | Could | functional | 1 |
| REQ-390 | Report Patron Counts By Profile Group | Could | functional | 1 |
| REQ-391 | Report Patron Counts By Survey Answer | Could | functional | 1 |
| REQ-392 | Report Patron Debt Using Debt Records | Could | functional | 1 |
| REQ-393 | Report Previous Month Patrons Demographics | Could | functional | 1 |
| REQ-394 | Report Sent Notice Statuses | Could | functional | 1 |
| REQ-395 | Report Voided Transactions Detail | Could | functional | 1 |
| REQ-396 | Report Voter Survey Counts By County Week | Could | functional | 1 |
| REQ-397 | Report Voter Survey Responses | Could | functional | 1 |
| REQ-398 | Restrict Canned Template Additions | Could | constraint | 1 |
| REQ-399 | Restrict Queryable Tables And Fields | Could | functional | 1 |
| REQ-400 | Retrieve Distributed MARC Fields | Could | functional | 1 |
| REQ-401 | Retrieve MARC Fields In Rows | Could | functional | 1 |
| REQ-402 | Run Canned Reports By Interval | Could | functional | 1 |
| REQ-403 | Run Preset OnDemand Reports | Could | functional | 1 |
| REQ-404 | Run Reports By Date Time And Staff | Could | functional | 1 |
| REQ-405 | Run Templates Without Modification | Could | functional | 1 |
| REQ-406 | Schedule Recurring Report Execution | Could | functional | 1 |
| REQ-407 | Select And Deselect Data Parts | Could | functional | 1 |
| REQ-408 | Select Individual Records Manually | Could | functional | 1 |
| REQ-409 | Select Regular Expressions From Dropdown | Could | functional | 1 |
| REQ-410 | Separate Check In And Renewal Timestamps | Could | constraint | 1 |
| REQ-411 | Separate Check-in From Renewals | Could | functional | 1 |
| REQ-412 | Show Branch Capacity Interface | Could | functional | 1 |
| REQ-413 | Show Canned Template Hover Descriptions | Could | functional | 1 |
| REQ-414 | Support Core Report Categories | Could | functional | 1 |
| REQ-415 | Support Custom Locally Defined Reports | Could | functional | 1 |
| REQ-416 | Support Multiple Report Record Types | Could | functional | 1 |
| REQ-417 | Total Items Count Report | Could | functional | 1 |
| REQ-418 | Upload Patron Filter Identifier Text Files | Could | functional | 1 |
| REQ-419 | Upload Text File For Filtering | Could | functional | 1 |
| REQ-420 | Use Full Boolean Operator Set | Could | functional | 1 |
| REQ-421 | Weekly Report Voter Registration Responses | Could | functional | 1 |

## Must requirements

### REQ-001 - Control Report Access With Folders

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The system must allow administrators to create shared folders for organizing reports and controlling staff access. Administrators must be able to allow or disallow staff from running specific reports through these folders. The system must also authorize staff to run ad hoc reports against specific data sets selected by administrators. These controls are needed to manage which reports staff can run and which data sets may be used for ad hoc reporting.

> System administrators should be able to create shared folders to allow or disallow staff from running specific reports, and/or to run ad hoc reports on specific sets of data. (`early_draft_srs_galecia.txt`)
> Admins can create shared folders to allow or disallow staff from running specific reports, and/or to run ad hoc reports on specific sets of data. (`email_report_features.eml`)

### REQ-002 - Show Report Queue With Criteria

**Priority:** Must - Mentioned in 5 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `survey_results_2009.txt`

The system must let staff view the report queue, including the queue’s contents, each report’s status, and each report’s position. This capability is needed because report queue visibility is important to branch managers and directors, while staff need to know where a report is among reports waiting to run. The system should also show the criteria used to generate report results, so staff can understand the selections associated with reports. If report priority is used, queue details should include that priority.

> - No query queue visibility (`evergreen_reference_2009.txt`)
> Add report queue visibility and status indicators (`evergreen_reference_2009.txt`)

### REQ-003 - Report Material Volume Snapshot

**Priority:** Must - Mentioned in 5 documents.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`, `conversations/conv_pines016_shelf_space.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The system must report material volume for a selected library at a specified point in time. It must count acquisitions, items on the shelf, and items in circulation, providing overall totals and breakdowns by configurable categories such as genre, format, fiction and non-fiction, adult fiction, board books, and holds. The report is needed for understanding collection volume and supporting monthly board reporting. It must include only items associated with the selected library and preserve figures as they existed on a specified past date, including when later shelving-location changes would otherwise alter the results.

> Quick question - how do I get a report that tells me how many items we have at Dalton-Whitman at any given moment? (`conversations/conv_pines014_material_volume.eml`)
> The volume should include: 1. New acquisitions (items recently added) 2. Items on the shelf (checked in) 3. Items out in circulation (checked out) I think Maria is asking for all three counts separately plus a total. (`conversations/conv_pines014_material_volume.eml`)

### REQ-004 - Control Staff Access By Roles

**Priority:** Must - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `email_staff_login.eml`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must allow administrators to manage staff access to reporting and query tools through configurable roles or security groups. Access control must apply to individuals, workgroups, and arbitrary staff groups, with permissions appropriate to each role, including limited report access for front desk staff, report-template creation and modification for department heads, and full access for system administrators. Role administration should be straightforward so changing a staff member’s role assignment can change the associated permissions.

> CO-4: User rights and privileges will be controlled through security groups and or "roles" that allow access control for individuals, workgroups, and arbitrary staff groups. (`early_draft_srs_galecia.txt`)
> 2. User rights and privileges controlled through security groups/roles. (`email_staff_login.eml`)

### REQ-005 - Report Missing Damaged Items ByBranch

**Priority:** Must - Mentioned in 4 documents; strong wording (crucial).  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports of missing and damaged items organized by branch. Staff need these reports to support accountability, track collection health, and identify patterns such as branches or shelves associated with repeated item loss. The report must present missing and damaged items in a manner that allows staff to investigate branch-level processes.

> I want the missing/damaged report to be per branch. That's crucial for accountability. (`conversations/conv_pines019_020_missing_intransit.eml`)
> System provides reports of missing and damaged items per branch. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-006 - Generate Last Copy Report

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a last-copy report identifying items that are the only copy of their title within a selected scope. The scope must support an individual library and the entire library system across the consortium. Staff need this report to avoid deleting a title’s only copy and to support cataloging review, including editing external catalog records. The report is especially needed when a rare item may be removed, so staff can verify its status before deletion.

> This is all great. One more thing - the "last copy report" should definitely be available per system, not just per library. We need to make sure no one accidentally deletes the last copy at the consortium level. (`conversations/conv_pines021_item_purging.eml`)
> For the last copy report - is this per library or per system? I think we need both views. (`conversations/conv_pines021_item_purging.eml`)

### REQ-007 - Record Deletion Audit Via Trigger

**Priority:** Must - Mentioned in 2 documents. Adjusted from Should by model: Comprehensive deletion audit for item/patron/bibliographic records, with trigger logging.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`, `interview_cataloging_2009-05-08.txt`

The system must retain an audit record whenever an item, patron, or bibliographic record is deleted. Each audit record must identify the record type and identifier, the staff member who performed the deletion, the staff member’s branch, and the deletion timestamp; it should also retain the deletion reason or prior status when available. Deletion logging must be initiated by a database trigger and written to a dedicated audit table. These records support auditing and tracking deletions by location and system.

> We need to be able to count and track record deletions (item records, patron records) per location and per system. This is for auditing purposes. (`conversations/conv_pines022_deletions.eml`)
> 1. A trigger in the database that logs deletions to an audit table (`conversations/conv_pines022_deletions.eml`)

### REQ-008 - Anonymize Archived Patron Transactions

**Priority:** Must - Mentioned in 3 documents; strong wording (must).  
**Type:** constraint  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `survey_results_2009.txt`

The system must archive transaction data in a form that protects patron privacy as defined by State Law. Archived demographic transaction data must be anonymized so that individual patrons cannot be identified, while retaining useful demographic statistics. The archived information should support statistics involving transactions, geographical regions, and age ranges. This protection is required while preserving information needed to understand or predict patron behavior and use of materials.

> Transactions should be archived in a form that protects patron privacy as defined by State Law, while providing useful demographic statistics. (`early_draft_srs_galecia.txt`)
> TRANSACTION ARCHIVE: Archive with privacy protection per State Law. (`email_report_features.eml`)

### REQ-009 - Record Deletion Audit Tracking

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-04-27  
**Sources:** `conversations/conv_pines022_deletions.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The system must count and track record deletions by location and by library system, including item records and patron records. Deletion tracking must include the record type, the timestamp, the staff member who performed the deletion, and that staff member’s location. This information is needed for auditing and troubleshooting, enabling directors and staff to determine how many records were deleted and investigate records that go missing from the catalog.

> Ability to count and track record deletions (e.g., item records, patron records) per location and per system. (`early_draft_srs_galecia.txt`)
> The system should count and track record deletions (e.g., item records, patron records) per location and per system. (`conversations/conv_pines022_deletions.eml`)

### REQ-010 - Include Nulls For Missing Values

**Priority:** Must - Mentioned in 4 documents; strong wording (must).  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The system must define how reports handle missing or blank values and must include such values in results, representing included missing values as nulls. It must retain patrons who lack optional characteristics when filters are applied or fields are displayed, rather than excluding them and producing misleading results. Demographic reports must specify whether missing values are shown as nulls or excluded, while the general reporting requirement is to include all null and blank fields.

> "All nulls and blank fields must be included in the results," Robert noted. (`meeting_tech_subcommittee_2009-06-30.txt`)
> All nulls and blank fields must be included in results (`survey_results_2009.txt`)

### REQ-011 - Query Transfer Candidate Items

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The system must allow users to query for items that are candidates for transfer between branches or to other locations. Query selection must support criteria such as section and circulation history, including identifying items in the children’s section that have not circulated in 6 months. This capability is needed when staff identify batches of materials for a mobile library, an outreach program collection, or a just-in-time warehouse. The query results must support subsequent selection of titles for transfer.

> Query for candidate materials (`conversations/conv_pines018_item_transfer.eml`)
> Ability to query for candidate materials (`conversations/conv_pines018_item_transfer.eml`)

### REQ-012 - Revert Transferred Items To Origin

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The system must allow staff to return transferred items to their original locations after a specified or configured period. This capability is needed when items are temporarily moved between branches, such as for a mobile library, an outreach program, or a just-in-time warehouse. The system should preserve the original location so that selected items can be reverted when the temporary transfer period ends.

> - Ability to revert items to original location after a set period of time (`early_draft_srs_galecia.txt`)
> Revert items to original location after a set period of time (`conversations/conv_pines018_item_transfer.eml`)

### REQ-013 - Save Reusable Transfer Candidate Queries

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The system must allow users to save queries and reuse them for repeated tasks, including identifying items that are candidates for transfer. This capability is needed because the same candidate queries may be run repeatedly, such as a monthly process for selecting materials. Saved queries should support the transfer utility’s query, selection, and location-change activities. The system should provide this capability as part of the reporting interface, where the ability to save and reuse queries is an important feature.

> Save queries for repeated use (`conversations/conv_pines018_item_transfer.eml`)
> Ability to save queries for repeated use (`conversations/conv_pines018_item_transfer.eml`)

### REQ-014 - Update Item Records New Location

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The item transfer utility must allow users to select items and update their records to assign them to a new location, such as a destination library. This capability is needed when selected items are moved between branches, sent to a mobile library or outreach program, or placed in another location. The utility must provide mechanisms for moving items, including changing the location field and generating pull lists. It must also allow items to be reverted to their original location after a set period of time, such as when a mobile library returns to base.

> Change records of selected items to new location (`conversations/conv_pines018_item_transfer.eml`)
> Ability to change records of selected items to move to new location (`conversations/conv_pines018_item_transfer.eml`)

### REQ-015 - Ensure Section 508 Accessibility Support

**Priority:** Must - Marked as priority in the source document.  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system, its management processes, reporting interfaces, and online help must meet applicable accessibility requirements, including Section 508. It must support patrons and staff who use screen readers, screen-magnification software, and other assistive technology programs designed to increase accessibility. Accessibility is a legal requirement, and the system must also be accessible through Microsoft Internet Explorer version 6.0 and later and Mozilla Firefox version 2.0 and later when it is web-browser based.

> Implement accessibility compliance (`evergreen_reference_2009.txt`)
> - Accessibility is not just a nice-to-have - it's a legal requirement (`interview_sysadmin_2009-05-10.txt`)

### REQ-016 - Provide Integrated Context Sensitive Help

**Priority:** Must - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide integrated online help in HTML that describes and illustrates all system functions. The help must be organized hierarchically, cross-linked, searchable, and easy to navigate, and staff must be able to access context-sensitive help without leaving the system. This capability is needed so staff can learn how to perform system tasks and run reports without routine IT assistance. The help must be comprehensive enough to explain major processes and standard reports.

> The HTML help needs to be searchable and easy to navigate. (`interview_sysadmin_2009-05-10.txt`)
> UD-3: The system must provide an online, hierarchical, and cross-linked help system in HTML that describes and illustrates all system functions. (`early_draft_srs_galecia.txt`)

### REQ-017 - Support Linux And Solaris Servers

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_sysadmin_2009-05-10.txt`

The reporting system must operate on either a Linux or Solaris server environment. Specifically, it must support Red Hat Enterprise Linux and Solaris 10 running on SPARC hardware. This requirement is needed because the consortium uses Linux for its main server environment and Solaris 10 on SPARC hardware for disaster recovery and reporting. Support for these environments is identified as high priority.

> OE-2: The system must operate on a Linux or Solaris server environment. (`early_draft_srs_galecia.txt`)
> So any reporting system needs to work on both Linux and Solaris. (`interview_sysadmin_2009-05-10.txt`)

### REQ-018 - Cancel Scheduled Or Running Reports

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The system must allow staff or processes to cancel reports that are scheduled to run or are currently running. Cancellation must apply both before execution begins and while report processing is underway. To support cancellation of a running report, the system must check for cancellation signals during report processing. This control is needed because scheduled or active reports may need to be stopped after they have been initiated or queued.

> Ability to cancel a report that has already been scheduled to run or is currently running (`early_draft_srs_galecia.txt`)
> - No ability to cancel a running report (`evergreen_reference_2009.txt`)

### REQ-019 - Generate Standards Compliant HTML

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must produce standards-compliant HTML for all system-generated web content. This includes web-based components, report output, the web-based interface, and help content. The generated HTML must be valid and comply with applicable HTML standards, including validation against W3C standards.

> CO-2: The system must produce standards-compliant HTML output for web-based components. (`early_draft_srs_galecia.txt`)
> Management Processes shall produce standards-compliant HTML. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-020 - Provide Authority Bibliographic Data Specs

**Priority:** Must - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The developer must provide complete data specifications for authority, bibliographic, order, item, hold/request, and other records maintained or accessed by Management Processes. The specifications must include field names, data types, and relationships. This documentation is needed so staff can understand the data structures and write effective queries against the records used by the system.

> UD-1: The developer must provide complete data specifications for authority records, bibliographic records, order records, item records, hold/request records, and other records maintained or accessed by the Management Processes. (`early_draft_srs_galecia.txt`)
> The software developer shall provide complete data specifications for authority records, bibliographic records, order records, item records, hold/request records, and other records maintained or accessed by Management Processes. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-021 - Use Relational Database For Reporting

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must use a fully relational database as its backend for Management Processes and reporting. The reporting layer must operate consistently with the relational database structure rather than against it. This requirement is needed so staff can run reporting and analytical queries directly within the relational structure without requiring a separate reporting warehouse or denormalized reporting database.

> CO-1: The system must use a fully relational database back-end. (`early_draft_srs_galecia.txt`)
> Management Processes shall use a fully relational database back-end. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-022 - Support Consortium Scale Processing

**Priority:** Must - Marked as priority in the source document.  
**Type:** non-functional  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must support a library consortium operating across 286 locations, with 17 million annual circulations and the purchasing and processing of more than 900,000 items annually. It must provide capacity for the Management Processes needed by this large, multiple-system consortium. Searches and reports should be processable during library open hours without disrupting other system functions, as this capability is identified as highly desirable and high priority.

> OE-1: The system must support a library consortium with 286 locations, 17 million annual circulations, and purchasing/processing over 900,000 items per year. (`early_draft_srs_galecia.txt`)
> Specifically, the system must support a library consortium with 286 locations, 17 million annual circulations, purchasing and processing over 900,000 items per year. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-023 - Allow Busy Hours Reporting

**Priority:** Must - Marked as priority in the source document.  
**Type:** non-functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must allow searches and reports to run during library open hours, including busy periods, without excessive delays or disruption to other system functions. This capability is needed because reports currently take too long during busy hours, when the consortium is carrying out its regular operations. The reporting system should also make it possible for staff to determine whether a report is still processing, while supporting searches and reports as part of normal system use.

> It is highly desirable that searches and reports can be processed during open hours without disrupting other system functions. (`early_draft_srs_galecia.txt`)
> Reports take too long to run during busy hours (`survey_results_2009.txt`)

### REQ-024 - Avoid Restricting OPAC Functionality

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The requirements for Management Processes must not restrict the functionality or features of the Online Public Access Catalog module. The reporting and access-control requirements must therefore operate without constraining OPAC capabilities. This condition applies to the system’s design and implementation of Management Processes.

> CO-5: These requirements must not constrain functionality or features of the Online Public Access Catalog (OPAC) module. (`early_draft_srs_galecia.txt`)

### REQ-025 - Enable Web And Windows Client Access

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must be accessible through a web browser or a Windows-compatible client so that staff can access its reporting capabilities. If the system uses a web-browser-based implementation, it must be accessible through Microsoft Internet Explorer version 6.0 and later and Mozilla Firefox version 2.0 and later. The server environment remains subject to the requirement that the system operate on Linux or Solaris. Access through a web browser or Windows-compatible client is identified as high priority, while the browser-version condition is medium priority.

> OE-3: The system must be accessible through a web browser or a Windows-compatible client. (`early_draft_srs_galecia.txt`)


## Should requirements

### REQ-026 - Checkout-Only Circulation Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a checkout-count report that counts check-outs only and excludes renewals, non-cataloged circulation, and other circulation activity. This report is needed when circulation activity must be measured specifically as items checked out rather than as a combined circulation total. The report should be available as a predefined circulation report for staff, consistent with the listed checkout-count reporting capability.

> - Checkout Count (includes checkouts only) (`early_draft_srs_galecia.txt`)
> - Checkout Count (`evergreen_reference_2009.txt`)

### REQ-027 - Combine Patron Filters With Logic

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `evergreen_reference_2009.txt`

The reporting interface must allow multiple filters, including patron-characteristic filters, to be combined in one query with Boolean AND and OR operators. Staff need this capability to identify patron groups defined by more than one condition, such as juvenile patrons in a zip code who have not checked anything out in six months. Optional characteristic fields that have not been provided must remain in the report with null values rather than being excluded.

> Can we combine demographic filters? Like "show me all Juvenile patrons in zip code 30505 who haven't checked anything out in 6 months"? (`conversations/conv_pines023_patron_characteristics.eml`)
> Combining filters is also doable - just add WHERE clauses. We can support both AND and OR logic. (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-028 - Count Bibliographic Records Only

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report showing the number of bibliographic records. Staff need this count as part of the available bibliographic records reporting. The report must represent bibliographic records rather than item, patron, circulation, or bill counts.

> - Bib Records Count (`early_draft_srs_galecia.txt`)

### REQ-029 - Items Added Count Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide an items report showing the number of items added. The report is needed to support reporting on item additions as part of the available items-reporting functions. Staff must be able to use this report when reviewing item activity. The report should be provided as an Items Added Count report, consistent with the listed predefined reports.

> - Items Added Count (`early_draft_srs_galecia.txt`)

### REQ-030 - Items Currently Checked Out

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide an items report listing items that are currently checked out. This report is needed to support review of current checkout status as part of the items-reporting functions. Staff must be able to use the report when examining items that remain checked out. The report should be available as an Items Currently Checked Out report, which is also identified among the predefined items reports.

> - Items Currently Checked Out (`early_draft_srs_galecia.txt`)

### REQ-031 - List Bibliographic Records No Volumes

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a canned report listing bibliographic records with no attached volumes. Staff need this report to identify records that lack an associated volume. The report must list the affected bibliographic records, not merely provide a count, and it must be available as a bibliographic records report.

> - Bib Records with No Volumes attached (`early_draft_srs_galecia.txt`)
> - Bib Records with No Volumes Attached (`evergreen_reference_2009.txt`)

### REQ-032 - Manage Fine Grained Report Access

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `email_report_features.eml`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The system must provide fine-grained, role-manageable permissions controlling which staff may create, run, and clone reports. Administrators need to manage these permissions through roles, while shared folders must support allowing or disallowing staff from running specific reports. The requirement addresses the existing lack of separate controls for creating and running reports and the lack of controls over which filters staff may use. Permission administration should also support access for individuals, workgroups, and arbitrary staff groups.

> REPORTS PERMISSIONS: Fine-grained permission levels. Shared folders. Easy administration through roles. (`email_report_features.eml`)
> - No fine-grained control over who can create vs. run reports (`evergreen_reference_2009.txt`)

### REQ-033 - Missing Or Damaged Items Report

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report of items marked missing or damaged, including items with a missing status, and must show how many items went missing or were damaged. The report must support review per branch so staff can use it during monthly shelf reading, inventory audits, and collection management. The system should make these records available for auditing and for managing collection conditions.

> - List of Items with a status of Missing (`early_draft_srs_galecia.txt`)
> - Missing items (`early_draft_srs_galecia.txt`)

### REQ-034 - Monthly Quarterly Yearly Deletion Totals

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `conversations/conv_pines022_deletions.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report total deletion counts for selected monthly, quarterly, and yearly periods. Staff need these reports to review deletion activity from an administrative perspective and to understand how many records were deleted during each period. The system must break the counts down by record type, including items, patrons, bibliographic records, and other applicable record types, and the reports may also show the associated location.

> Total deletions per period (month, quarter, year) (`conversations/conv_pines022_deletions.eml`)
> - Items Deleted Count (`early_draft_srs_galecia.txt`)

### REQ-035 - Overdue Items Daily Shelf Reading

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide reports of items overdue by more than a specified number of days, including daily reports for staff review. Each overdue-items report must include patron contact information and shelf-reading information. Staff need these reports to identify overdue materials, support contact with affected patrons, and assist with shelf reading. The reporting condition is that the overdue period must be evaluated against the specified number of days.

> - Items more than XX days overdue (Overdue Materials Report) (`early_draft_srs_galecia.txt`)
> - Items Overdue by X Days (`evergreen_reference_2009.txt`)

### REQ-036 - Provide Aged Debt Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide an aged debt report that categorizes debt by age. The report is needed within the bills reporting area, together with reports for bills currently owed by patrons and detailed payments received. The system must also include a predefined, or canned, aged debt report, and scheduled reports may run daily, weekly, or monthly but not hourly.

> - Aged Debt (`early_draft_srs_galecia.txt`)

### REQ-037 - Provide Detailed Payment Receipts Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a detailed report of payments received and must include a canned report for this payment activity. Staff need the report within the bills reporting functions, alongside reports for bills currently owed by patrons, alternative payments, voids, and aged debt. If the report is scheduled, scheduling is limited to regular daily, weekly, or monthly intervals; it cannot be scheduled hourly or delivered by email.

> - Detailed Payments Received (`early_draft_srs_galecia.txt`)

### REQ-038 - Provide Local Admin Role

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a Local Admin role for local administrators, including branch managers and assistant directors. This role must support branch-level reporting and local system configuration because these management staff oversee library processes and configure the system locally. Roles must support access control for individuals, workgroups, and arbitrary staff groups. The system should make permission changes manageable by changing a person's role assignment.

> They configure the system locally. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)
> - Local Admin: Branch-level reporting and configuration (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-039 - Report Circulation By Shelving Location

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide reports showing circulation counts broken down by shelving location. This capability is needed for staff who must examine circulation activity by the location where items are shelved. The report must be available as a predefined circulation report, and the reporting facilities remain subject to stated limitations such as difficult complex queries, limited field selection, and no regular expression support.

> - Circulation Count by Shelving Location (`evergreen_reference_2009.txt`)

### REQ-040 - Report Patron Counts By Home Library

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report showing the number of patrons. This report is needed by staff to measure the patron population and support library reporting activities. The available patron reporting categories also include counts by home library, while report scheduling is limited to intervals such as daily, weekly, and monthly when scheduling is supported.

> - Patron Count (`early_draft_srs_galecia.txt`)

### REQ-041 - Report Patron Counts By Home Library

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a patron report that presents patron counts broken down by home library. The report must support library reporting in situations where patron totals need to be viewed for each home library rather than only as an overall patron count. Staff need this report to review patron counts by the relevant library grouping. The source identifies this as a patrons report and does not state additional conditions or limits.

> - Patron Count by Home Library (`early_draft_srs_galecia.txt`)

### REQ-042 - Restrict Patron Direct Management Reporting

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must support patrons' indirect access to management-report information through library or OPAC displays. Patrons interact through the OPAC and may encounter reports indirectly through displays or screens at libraries. The system must not provide patrons with direct access to management reporting. Management reports are primarily created and used by staff, while patron access is limited to the indirect display of relevant information.

> [Note from Katherine: Patrons interact through OPAC; they may use reports indirectly through displays/screens at libraries] (`meeting_minutes/meeting_2009-03-15_minutes.txt`)
> - Patron: Indirect access through OPAC displays (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-043 - Run Multiple Reports Concurrently

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must allow staff to select multiple reports from a list and run them concurrently. This capability must apply to reports initiated immediately as well as reports scheduled to run concurrently, including recurring reports. It is needed when staff require several canned reports together rather than starting each report separately, while scheduled reports may otherwise run at regular daily, weekly, or monthly intervals.

> Canned reports can be checked off from a list to run at the same time and will be viewed within one document. (`early_draft_srs_galecia.txt`)
> - No ability to check multiple reports to run at the same time (`evergreen_reference_2009.txt`)

### REQ-044 - Schedule And Consolidate Report Runs

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must allow staff to run reports immediately or as soon as possible, or to schedule them hourly, daily, weekly, monthly, or yearly. Staff must be able to select these execution options through the reporting interface, including for canned reports, and must be able to select multiple reports to run at the same time and view them within one document. Reports are downloaded from the web interface rather than delivered by email.

> Canned reports are generic reports set to run by the individual either ASAP or recurring. (`early_draft_srs_galecia.txt`)
> Ability to select Run ASAP, Hourly, Daily, Weekly, Monthly, Yearly (`early_draft_srs_galecia.txt`)

### REQ-045 - Separate Renewal Count Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report showing the number of renewals. Renewal activity must be reported separately from check-outs, non-cataloged circulation, and combined circulation totals so that staff can identify renewal volume independently. The report should be available as a predefined circulation report, while reporting remains based on current data because the cited reporting capabilities do not include real-time or historical reporting warehouses.

> - Renewals Count (`early_draft_srs_galecia.txt`)

### REQ-046 - Allow RFID Card Staff Login

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `early_draft_srs_galecia.txt`, `email_staff_login.eml`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must support streamlined staff login using an RFID employee badge or equivalent card while retaining individual username-and-password login as an alternative. Card-based login is needed to reduce the time staff spend logging into terminals and to address security concerns associated with shared passwords or terminals left logged in. The system must not require card-based login, so staff and branches without card-reader infrastructure can use traditional login. The available methods must support staff serving patrons during busy periods.

> The system should support streamlined methods of logging into terminals. (`early_draft_srs_galecia.txt`)
> For example, a staff member could swipe a card (like an RFID employee badge) to log in, or alternatively use individual login credentials (username and password). (`early_draft_srs_galecia.txt`)

### REQ-047 - Authenticate Individual Staff For Audit

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must authenticate and identify the specific staff member who logs in and record that identity for audit purposes. This identification must remain individual even when a streamlined method such as a card swipe is used, because the streamlined method must not bypass individual authentication. The system should support streamlined staff login methods but must not require them, allowing smaller branches without card-reader infrastructure to use individual login and password methods.

> The system must track WHICH staff member is logged in for audit purposes. The card is just a convenient way to identify the person, but it shouldn't bypass individual authentication entirely. (`email_staff_login.eml`)

### REQ-048 - Determine Permissions On Every Login

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`, `interview_sysadmin_2009-05-10.txt`

The system must determine a staff member’s permissions from the assigned security group or role at every login, regardless of the login method used. Administrators must be able to create and manage roles so access can be controlled for individual staff members, workgroups, and arbitrary staff groups. The role-based model must support the stated patron, staff, local administrator, and global administrator access levels. Changing a staff member’s permissions should be handled by changing the assigned role.

> when a staff member logs in (by any method), their permissions should be determined by their assigned security group/role. (`email_staff_login.eml`)
> 3. Access control for individuals, workgroups, and arbitrary staff groups. (`email_staff_login.eml`)

### REQ-049 - Export Reports CSV And Excel

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`, `conversations/conv_pines024_inactive_patrons.eml`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must allow report data to be generated or exported in CSV format. Inactive-patron data must be exportable for upload to an outreach system, and branch capacity information must also support CSV export. CSV is required as a reliable data-export format, while Excel and HTML are also required output formats for reports, including spreadsheet use and web display.

> Also, the report should be exportable. We upload it to our outreach system. (`conversations/conv_pines024_inactive_patrons.eml`)
> Excel, HTML, and CSV formats are required. Robert noted that CSV is the most reliable for data export, Excel is preferred by business users for pivot tables, and HTML is needed for web display. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-050 - Compare Branch Breakdowns SideBySide

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports and comparison views that compare data across library branches. The comparison view must display each library's breakdown side by side so users can identify outliers. This capability is needed by directors who review the data quarterly and by branch managers who need cross-branch comparison reports, while supporting both per-library and per-system views.

> Also, can we include a "comparison" view that shows each library's breakdown side by side? That would make it easy to spot outliers. (`conversations/conv_pines016_shelf_space.eml`)
> - Need for cross-branch comparison reports (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-051 - Compare Shelf Space Utilization

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide shelf-space analysis for each material genre and format by reporting the category’s percentage of total shelf space. The analysis must compare that percentage with the category’s percentage of total circulations and its percentage of the collection. Staff need these comparisons for collection management and to decide where to allocate resources based on shelf-space use, collection representation, and circulation activity.

> What percentage of total shelf space it occupies (`conversations/conv_pines016_shelf_space.eml`)
> For each genre and format of material, ability to compare: - The percentage of total circulations - The percentage of the collection - The percentage of total shelf space (`early_draft_srs_galecia.txt`)

### REQ-052 - Generate Shelf Space Reports Branches

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`, `early_draft_srs_galecia.txt`

The system must provide shelf-space reports at both the individual library and entire library system levels. For each genre and format of material, the report must compare the percentage of total circulations, the percentage of the collection, and the percentage of total shelf space. This is needed so branch managers can review their local situation and examine it in relation to the system average.

> The report should be able to run per library and per system. (`conversations/conv_pines016_shelf_space.eml`)
> The report should be available per library and per system. (`conversations/conv_pines016_shelf_space.eml`)

### REQ-053 - Merge In-Transit To From

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must combine items traveling to a destination branch and items traveling from a source branch into a single in-transit report. The report must support front-line staff who need one report rather than separate transit-to and transit-from reports. It must identify items that have been in transit longer than a configurable period, including the stated default of seven days when applicable. The report must be available by branch and by system.

> And the report should merge transit-to and transit-from so front-line staff don't have to run two reports. (`conversations/conv_pines019_020_missing_intransit.eml`)
> The report should merge the transit-to and transit-from into one report for ease of front-line staff use. (`early_draft_srs_galecia.txt`)

### REQ-054 - Provide In-Transit Overdue Report

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide periodic reports identifying items that have remained in transit longer than a configurable number of days. The report must identify items whose arrival date is absent and whose departure date exceeds the configured threshold. Results must be organized by branch and for the system, and the report must merge transit-to and transit-from information for front-line staff use.

> I need to see what's been in-transit for more than X days (X should be configurable, probably 7 days default). (`conversations/conv_pines019_020_missing_intransit.eml`)
> The system should generate a list of items that have been in-transit for more than X days (X configurable), per branch and per system. (`early_draft_srs_galecia.txt`)

### REQ-055 - Convert Multiple Item Statuses Batch

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must support a report or workflow for converting multiple item statuses in a single batch operation. Staff must be able to use this capability when items need to be changed from one status to another, such as changing items from missing to discard/weed. The system must support batch conversion, including cases involving 100 items, to assist with item purging and related cataloging work.

> - Items to be Converted (batch converting items from one status to another) (`early_draft_srs_galecia.txt`)
> Sometimes I need to change 100 items from "missing" to "discard/weed" in batch. (`interview_cataloging_2009-05-08.txt`)

### REQ-056 - Provide Purge Criteria Utility

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a utility and reports for identifying item records that meet customizable purge criteria. Criteria must be able to include item status, the time an item has remained in a status, circulation history, and combinations of these conditions, such as missing for more than a specified period or having discard/weed status. The capability is needed by staff for weeding and collection management. The system should also provide a report to assist with converting items from one status to another in batch.

> I need to identify item records to purge based on customizable criteria. For example: - Item has been in status "missing" for more than X months - Item has status "discard/weed" (`conversations/conv_pines021_item_purging.eml`)
> The system should provide a utility and reports for identifying item records to purge, based on customizable criteria such as: (`conversations/conv_pines021_item_purging.eml`)

### REQ-057 - Purge Candidate Utility With Duration

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`

The system must provide a utility and reports that identify item records as candidates for purging when they have remained in a specified status for a configurable duration. The duration must be expressible in months or years, including criteria such as an item remaining in missing status for more than the configured period. Staff need this capability to support customizable item-record purging decisions.

> - An item has been in status "missing" for more than X months (`early_draft_srs_galecia.txt`)
> - Time-based criteria (in status for X months/years) (`conversations/conv_pines021_item_purging.eml`)

### REQ-058 - Select Purge Candidates By Status Criteria

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`

The system must identify item records eligible for purging according to customizable status-based criteria. The supported statuses must include missing, discard or weed, and damaged. This capability is needed by staff preparing item-record purging reports so that records can be identified based on the status assigned to each item.

> - An item has status "discard/weed" (`early_draft_srs_galecia.txt`)
> - Status-based criteria (missing, discard/weed, damaged) (`conversations/conv_pines021_item_purging.eml`)

### REQ-059 - Report Status Conversion Candidates

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-22  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a report that assists staff in converting items from one status to another. The report should help identify the item records requiring conversion, including situations where staff need to change many items from missing to discard/weed in batch. This capability is needed as part of item purging activities based on criteria such as an item remaining missing for more than a specified period or having discard/weed status. The report supports identification for conversion rather than replacing the required status-conversion action.

> - Provide a report to assist in the conversion of items from one status to another (`conversations/conv_pines021_item_purging.eml`)
> The system should have a report to assist in the conversion of items from one status to another. (`early_draft_srs_galecia.txt`)

### REQ-060 - Anonymized Demographic Transaction Stats

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must generate transaction reports showing counts by patron, branch, selected group of branches, system, or county. Reports must include check-ins, check-outs, holds placed, holds filled, fines collected, and patron registrations, with check-out types and hold-placement methods counted separately where applicable. The system should support additional grouping by hour, terminal, branch, and system to identify transaction patterns and busy periods. Demographic transaction statistics by geographical region and age range must be anonymized.

> - Check in Count (`early_draft_srs_galecia.txt`)
> The system can generate a report of transactions (holds placed, holds filled, and check-outs) per patron, per library, per selected group of libraries, per system, per county. (`early_draft_srs_galecia.txt`)

### REQ-061 - Configurable Transaction History Retention

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must retain detailed transaction-level history for a configurable number of days. It must retain monthly and annual aggregate information indefinitely after the detailed history period. Staff must be able to query transactions, including check-ins, check-outs, fines collected, and patron registrations, and group them by hour, terminal, branch, or library system, either across all transactions or by transaction type.

> Transaction history is maintained for X days (X is configurable). (`early_draft_srs_galecia.txt`)
> Transaction history maintained for X days (configurable), with monthly and annual aggregates retained indefinitely. (`survey_results_2009.txt`)

### REQ-062 - Control Report Template Permissions

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `survey_results_2009.txt`

The system must allow administrators to create report templates and make those templates available to staff. Staff must be able to run a template as-is or modify it for individual needs without compromising the accuracy of the resulting report. Administrators must be able to limit which filters and display fields staff can alter, supporting dependable output. Access to creating and cloning reports must be governed by fine-grained permissions.

> Admins need to create report templates that are available to staff. (`email_report_features.eml`)
> REPORT TEMPLATES: Admins create templates available to staff. Run as-is or modified. Limit alterable filters/fields. Clone capability. (`email_report_features.eml`)

### REQ-063 - Indefinite Aggregate Transaction Retention

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must retain monthly and annual aggregate transaction information indefinitely. This retention supports ongoing historical reporting of transaction activity after detailed transaction history is no longer maintained. The retained aggregates must cover transaction information, while the detailed transaction history remains subject to a configurable retention period. Staff need this information for continuing statistical and reporting requirements.

> Monthly and annual aggregate information is maintained indefinitely. (`early_draft_srs_galecia.txt`)
> Transaction history maintained for X days (configurable), with monthly and annual aggregates retained indefinitely. (`survey_results_2009.txt`)

### REQ-064 - Provide Anonymized Patron Behavior Analytics

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system should produce statistics that help staff understand and predict patron behavior and the use of materials. The statistics must include how quickly a particular item is returned on average, how likely a particular item is to be renewed, and what percentage of check-outs at a particular branch are renewals. Reporting should also support transactions by patron, branch, group of branches, system, county, geographical region, and age range where specified. Demographic statistics must be anonymized and must not include personally identifiable information.

> The system should produce statistics that can be used to understand and predict patron behavior and use of materials. (`early_draft_srs_galecia.txt`)
> System produces statistics to understand/predict patron behavior and use of materials. (`survey_results_2009.txt`)

### REQ-065 - Provide Region Age Anonymized Demographics

**Priority:** Should - Mentioned in 2 documents; strong wording (must).  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must produce demographic statistics for transactions, including breakdowns by geographical region and age range. The statistics are needed to understand and predict patron behavior and use of materials. The statistics must use anonymized data, with information that could identify a patron deleted.

> The system should produce useful demographic statistics, including transactions by geographical regions, age ranges, etc. (`early_draft_srs_galecia.txt`)
> Demographic statistics include transactions by geographical regions and age ranges. Data must be anonymized. (`survey_results_2009.txt`)

### REQ-066 - Typed Transaction Query Grouping

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must support queries for all transactions or for transactions by type, including check-ins, check-outs, fines collected, and patron registrations. It must group transaction results by hour, terminal, branch, and system. These capabilities are needed to review total activity, identify busy periods, and analyze transaction activity across library locations and systems. Transaction reporting must support the transaction categories identified by the sources.

> Transactions can be grouped by hour, terminal, branch, and system. Transactions include check-ins, check-outs, fines collected, patron registrations, etc., and can be queried by all transactions or by type of transaction. (`early_draft_srs_galecia.txt`)
> Transactions can be grouped by hour, terminal, branch, and system. (`survey_results_2009.txt`)

### REQ-067 - Filter Patron By Demographics

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must allow patron queries and reports to be limited or grouped by age range, zip code, county of residence, home branch, patron type, and preferred language. Staff must be able to use these characteristics both to filter results and to aggregate results by characteristic. Filters must support combined AND and OR logic, include patrons whose applicable values are null, and allow age ranges to be configurable per report.

> I need to be able to both LIMIT and GROUP BY patron characteristics. For example: - Limit: Show me only patrons in zip code 30501 (`conversations/conv_pines023_patron_characteristics.eml`)
> Queries and reports can be limited or grouped by various patron characteristics, including: - age range - zip code - county of residence - home branch - patron type - preferred language (`early_draft_srs_galecia.txt`)

### REQ-068 - Filter And Group Patron Counts By Age

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `evergreen_reference_2009.txt`

The system must support patron-count reports grouped by age demographic or configurable age range. Staff should be able to use age as either a limit or a grouping criterion, and age-range definitions must be configurable for each report. The system should support combining this criterion with other patron-characteristic filters through AND or OR logic and should include null values in results.

> - Patron Count by Age Demographic (not available) (`evergreen_reference_2009.txt`)
> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Age range (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-069 - Group Patrons By Geographic Attributes

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report or group patron results and counts by county, city, and ZIP code. Staff need this capability to analyze patron characteristics geographically and to review geographic differences in report results. The reporting functions must support both limiting results, such as showing only patrons in a specified ZIP code, and grouping results by geographic characteristics; the source material also identifies these geographic report types as not available.

> - Patron Count by County (`early_draft_srs_galecia.txt`)
> - Patron Count by County (not available) (`evergreen_reference_2009.txt`)

### REQ-070 - Generate Configurable Inactivity Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`, `early_draft_srs_galecia.txt`

The system must generate a configurable report listing patrons with no circulation or electronic activity during a configurable preceding period. Staff must be able to set the threshold in days, including 30, 90, 180, or 365 days, and adjust it as needed. The report must support organizational scopes such as system, home branch, and county. It is needed for monthly, quarterly, semi-annual, or annual checks of patron inactivity.

> The system should generate a list of patrons with no circulation or electronic activity in the last X days (X configurable). (`conversations/conv_pines024_inactive_patrons.eml`)
> The system should generate a list of patrons with no circulation or electronic activity in the last X days (X configurable). The list should be configurable to System, Home Library, County, etc. (`early_draft_srs_galecia.txt`)

### REQ-071 - Manually Select Items For Transfer

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The item transfer utility must allow users to manually select individual titles or items from query results for inclusion in a transfer. This capability is needed when a query returns more candidate items than should be moved, such as when only 25 of 100 results are wanted. Users must be able to target the items to include rather than transferring every query result. The selected items are then available for the utility’s transfer processing between branches or to other locations.

> Manually select titles from query results (`conversations/conv_pines018_item_transfer.eml`)
> I should be able to check boxes and select which ones to include. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-072 - Process Uncataloged Material Rapid Distribution

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must support rapid processing and distribution of uncataloged material, including paperback books and children's board books. The capability is needed for large shipments that arrive without individual catalog records and must allow quick distribution while minimizing labor at branches. The system must also support identifying how the material is used and counting its transactions in circulation statistics and reports.

> Support needed for: - Quick distribution - Minimal branch labor (`early_draft_srs_galecia.txt`)
> The requirements are: quick distribution (we need to process these fast), minimal branch labor (we can't spend a lot of time per item), and ability to identify how the material is being used. (`interview_cataloging_2009-05-08.txt`)

### REQ-073 - Report Uncataloged Material Usage

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a way for staff to identify how uncataloged material is being used. This capability is needed for uncataloged paperback books and children's board books that must be tracked as inventory despite lacking individual catalog records. Transactions involving this material must be countable and included in circulation statistics and reports.

> - Ability to identify how the material is being used (`early_draft_srs_galecia.txt`)
> The requirements are: quick distribution (we need to process these fast), minimal branch labor (we can't spend a lot of time per item), and ability to identify how the material is being used. (`interview_cataloging_2009-05-08.txt`)

### REQ-074 - Track Uncataloged Material Inventory Control

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must support inventory control for uncataloged material, including paperback books and children's board books, before individual catalog records are created. This capability is needed because large shipments can arrive without individual catalog records while staff still need to track the material as inventory. Transactions involving uncataloged material must be countable and included in circulation statistics and reports.

> Ability to control inventory of uncataloged material, such as paperback books and children's board books. (`early_draft_srs_galecia.txt`)
> We need to be able to track these as inventory even though they're not fully cataloged. (`interview_cataloging_2009-05-08.txt`)

### REQ-075 - Uncataloged Material Circulation Counting

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must count transactions involving uncataloged material and include those counts in circulation statistics and reports. This capability is needed for materials such as paperback books and children's board books that may arrive without individual catalog records, while staff need to identify how the material is being used. The reporting must support inventory and circulation tracking despite incomplete cataloging, while accommodating quick distribution and minimal branch labor.

> - Non-Cat Count (`early_draft_srs_galecia.txt`)
> Ability to count transactions and include in circulation statistics and reports. (`early_draft_srs_galecia.txt`)

### REQ-076 - Periodic Reports For Invalid Item Types

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide periodic reports identifying items with invalid item types. Staff need these reports as data quality reports to help maintain data integrity. The invalid-item-type report must be available as a periodic reporting option alongside other reports concerning item, bibliographic record, and patron data quality. Its purpose is to identify affected items so staff can review the reported data.

> - Items with invalid item type (`early_draft_srs_galecia.txt`)
> Data quality reports - items with invalid item type, items with long call numbers, bibliographic records with no item records. (`interview_cataloging_2009-05-08.txt`)

### REQ-077 - Periodic Reports For Long Call Numbers

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide periodic reports identifying items with long call numbers. Staff need these reports as data quality reports to help maintain data integrity. The long-call-number report must be available as a periodic reporting option alongside reports for other item and bibliographic record data conditions. The report must identify the affected items so staff can review call numbers that exceed the applicable length.

> - Items with a long call number (`early_draft_srs_galecia.txt`)
> Data quality reports - items with invalid item type, items with long call numbers, bibliographic records with no item records. (`interview_cataloging_2009-05-08.txt`)

### REQ-078 - Prevent OPAC Performance Impact

**Priority:** Should - Mentioned in 2 documents; strong wording (must).  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The management reporting system must not constrain or materially slow down the OPAC, including while large reporting queries are running. Reporting and the public catalog must remain separate concerns so patrons retain fast, responsive access to catalog information. A report executing a big query must not slow down the OPAC. This requirement applies to management reporting activity regardless of the size of the query.

> If a report is running, it should not slow down the OPAC. (`meeting_tech_subcommittee_2009-06-30.txt`)
> The management reporting system must not constrain the OPAC in any way. If the reporting system is doing a big query, it should NOT slow down the OPAC. (`interview_sysadmin_2009-05-10.txt`)

### REQ-079 - Produce Standards Compliant Semantic HTML

**Priority:** Should - Mentioned in 2 documents; strong wording (must).  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must produce standards-compliant, properly structured HTML for its web interface, help system, and report output. The HTML must use semantic elements, alternative text, and ARIA labels so that it works with screen readers, screen magnification software, and other assistive technology programs. This capability is required for Section 508 accessibility compliance and is necessary so staff, including blind staff members, can use the reporting system and run reports.

> The HTML output needs to be properly structured with alt tags, ARIA labels, and proper semantic HTML. And the system needs to produce standards-compliant HTML. (`interview_sysadmin_2009-05-10.txt`)
> The system must produce standards-compliant HTML. This was discussed in the context of the web-based interface, the help system, and report output. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-080 - Queue Searches And Reports During Peak

**Priority:** Should - Mentioned in 2 documents.  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

During open hours, the system must process searches and reports in the background or through queuing, or use read-only reporting replicas as appropriate. Report processing must not tie up the database or slow the circulation client. The capability is needed so staff can run searches and reports without disrupting circulation or other system functions. This requirement is particularly important during peak hours.

> The key requirement is that searches and reports can be processed during open hours without disrupting other system functions. (`interview_sysadmin_2009-05-10.txt`)
> It is highly desirable that searches and reports can be processed during open hours without disrupting other system functions. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-081 - Separate Development Training Environments

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`

The system must provide separate development and training environments that are distinct from production. Developers need a place to test new reports without affecting production, while new staff need a training environment in which they can practice running reports without making production mistakes. Configurations created in development or training must be migratable to production through export and import functionality for report templates, permission settings, and other configuration. This separation supports development, testing, and staff practice without affecting production operations.

> - No development/training environment separation (`evergreen_reference_2009.txt`)
> Provide a development/training environment with migration capability (`evergreen_reference_2009.txt`)

### REQ-082 - Support Development Training Production Environments

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide separate development, training, and production environments for Management Processes. It must support exporting configurations from one environment and importing them into another so development and training work can be transferred to production. Migratable configurations must include report templates, permission settings, and saved queries, allowing staff to prepare and test reporting configurations before production use.

> CO-3: The system must provide a development and training environment with the ability to migrate configurations to a production environment. (`early_draft_srs_galecia.txt`)
> Management Processes shall provide a development and training environment with the ability to migrate configurations to a production environment. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-083 - Support Legacy Browser Versions

**Priority:** Should - Mentioned in 2 documents.  
**Type:** constraint  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must support Microsoft Internet Explorer version 6.0 and later and Firefox version 2.0 and later. This support is needed because libraries use both browsers, while IE 6.0 remains common and upgrading browsers on more than 200 library computers is expensive and time-consuming. Library staff need to access the reporting system through the browsers standardized or still in use at their locations.

> So we need to support IE 6.0+ and Firefox 2.0+. (`interview_sysadmin_2009-05-10.txt`)
> - Browser requirements (IE/Firefox) confirmed (`interview_sysadmin_2009-05-10.txt`)

### REQ-084 - Use Relational PostgreSQL Schema

**Priority:** Should - Mentioned in 2 documents.  
**Type:** constraint  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must use the existing fully relational PostgreSQL database structure and work with that relational structure rather than against it. It must not require a denormalized reporting schema or a reporting warehouse that must be synchronized with the live database. This constraint is needed because maintaining synchronization creates additional problems, while a modern relational database can support complex analytical queries when they are written properly.

> - Database architecture needs are clear (relational, PostgreSQL-compatible) (`interview_sysadmin_2009-05-10.txt`)
> The reporting system needs to work with the relational structure, not fight against it. I'd prefer to keep everything in the main relational database. (`interview_sysadmin_2009-05-10.txt`)

### REQ-085 - Batch Location Updates TransactionSafe

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Transaction safety is critical for data integrity in batch updates.  
**Type:** non-functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must perform batch updates to item locations with transaction safety. Location changes must be handled reliably when the utility updates items as part of a transfer operation. This applies to the database update of the location field and must support the transfer workflow, including selecting candidate items and generating a printable list of items to be moved. The requirement concerns reliable processing of location changes rather than selection or list generation.

> 3. Batch update of location field - straightforward database update with transaction safety. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-086 - Restrict Transfer Permissions By Role

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Restrict permissions for security and misuse prevention.  
**Type:** constraint  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must restrict item-transfer permissions to authorized roles. Not every staff member may transfer items between branches, so access to this operation must be limited to designated roles such as managers, administrators, or transfer coordinators. The restriction applies to staff performing branch-to-branch item transfers. Unauthorized staff must not be permitted to use the transfer function.

> Not every staff member should be able to transfer items between branches. This should be limited to certain roles (managers, administrators, transfer coordinators). (`conversations/conv_pines018_item_transfer.eml`)

### REQ-087 - Transfer Batch Items And PullLists

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`

The system must provide a utility for transferring batches of items between branches and other locations. The utility is needed for moving books to a mobile library, an outreach program collection, or a just-in-time warehouse. It must support querying candidate materials, saving queries, manually selecting titles, changing selected item records to a new location, and generating pull lists. The utility must also support reverting items to their original location after a set period of time and/or based on other criteria.

> I need a utility for transferring batches of items between branches. (`conversations/conv_pines018_item_transfer.eml`)
> The system should provide a utility for transferring batches of items between branches. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-088 - Transfer Utility With Pull List And Audit

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`

The transfer utility must allow staff to query for candidate materials, save queries for repeated use, and manually select titles from query results. For selected items, it must support changing location fields to identify a new location and generating printable pull lists of the items to be moved between branches. The utility must also support reverting items to their original location after a set period of time and logging transfers for audit purposes.

> - Mechanisms for moving items: changing location field, generating pull lists (`early_draft_srs_galecia.txt`)
> Mechanisms: changing location field, generating pull lists (`conversations/conv_pines018_item_transfer.eml`)

### REQ-089 - Keep Reporting Architecturally Separate

**Priority:** Should - Mentioned in 2 documents; strong wording (critical).  
**Type:** constraint  
**First mentioned:** 2009-05-12  
**Sources:** `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`

The system must keep reporting functionality architecturally separate from production operations, including the OPAC. This separation is needed because reporting activity must not be part of or interfere with production operations. The separation is considered critical for the OPAC and must support the reporting system while preserving the distinct production environment. The requirement applies to reporting architecture within the management processes reporting system.

> Separate reporting from production operations (`evergreen_reference_2009.txt`)
> - Separation of reporting from OPAC is critical (`interview_sysadmin_2009-05-10.txt`)

### REQ-090 - Support Linux And Solaris Server Environments

**Priority:** Should - Mentioned in 2 documents.  
**Type:** constraint  
**First mentioned:** 2009-05-12  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The server environment must support the required operating systems, including Linux and Solaris. This support is needed to satisfy the technical constraints identified for the reporting system and to provide a validated server environment for its operation. The requirement applies to the system environment used by staff and IT personnel, alongside the stated needs for browser support, accessibility, role-based access control, and separation of reporting from the OPAC.

> - Server environment (Linux/Solaris) is validated (`interview_sysadmin_2009-05-10.txt`)
> - Technical constraints (server OS, browser support) (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-091 - Centralize Management Processes Across Branches

**Priority:** Should - Mentioned in 3 documents.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must centralize Management Processes at a central location while accepting input from and providing services to multiple branches. It must provide library administrators, managers, and staff with a consolidated basis for analyzing operations, managing collections, and making data-driven decisions. This centralization is needed to support consistent reporting and a single source of truth across locations. The system must depend on complete and current data from all locations, and effective network connectivity is required.

> The Management Processes are consolidated at a central location and accept input from and provide services to multiple library locations. (`early_draft_srs_galecia.txt`)
> Management Processes are consolidated at a central location, and accept input and provide services to multiple locations. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-092 - Consolidate Multi-Branch Enterprise Data

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Ensures consolidated data correctness and freshness.  
**Type:** non-functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must consolidate data from all locations so that the resulting data is complete and current. Central consolidation is needed to provide a single source of truth for reporting and to support management processes that accept input and provide services to multiple locations. The consolidated data must rely on the data structures and functionality of an enterprise-level Library Automation System, including its Acquisitions and Cataloging modules.

> Centralization is good for reporting," Katherine noted. "We get a single source of truth. The challenge is making sure data from all locations is complete and current." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-093 - Document Major System Processes

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system documentation must provide thorough, high-level descriptions of major system processes. These descriptions must cover bibliographic record import and export, validation of bibliographic records against internal and external authority sources, and production of standard reports. The documentation should also describe the data structures, including field names, data types, and relationships, so staff can understand the records and write effective queries.

> The developer must provide a thorough high-level description of major processes, including: - Bibliographic record import and export (`meeting_tech_subcommittee_2009-06-30.txt`)
> UD-2: The developer must provide a thorough high-level description of major processes, including bibliographic record import and export, validation of bibliographic records against internal and external authority sources, and standard reports. (`early_draft_srs_galecia.txt`)

### REQ-094 - Export Reports Multiple Formats

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must produce reports in Excel, HTML, and CSV formats and must provide configurable report scheduling options. CSV is required as the most reliable format for data export, Excel is needed by business users for pivot tables, and HTML is needed for web display. Scheduling and these output formats must support both operational reporting needs and the broader requirement to provide multiple report formats and scheduling options.

> Excel, HTML, and CSV formats are required. Robert noted that CSV is the most reliable for data export, Excel is preferred by business users for pivot tables, and HTML is needed for web display. (`meeting_tech_subcommittee_2009-06-30.txt`)
> Provide multiple output formats and scheduling options (`evergreen_reference_2009.txt`)

### REQ-095 - Expose Query-Specific Error Details

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide local and global system administrators with low-level, query-specific feedback through the front-end interface. This feedback must identify relevant details about an error, including the affected table, the affected field, and the type of error. The capability is needed when a report or other query fails so administrators can understand the cause instead of receiving only a generic failure message.

> Generic error messages like 'query failed' are useless. We need specifics - which table, which field, what kind of error. (`meeting_tech_subcommittee_2009-06-30.txt`)
> UD-4: The system must provide thorough high-level error reporting and feedback, and shall allow low-level query-specific feedback for Local and Global System Administrators from the front-end interface. (`early_draft_srs_galecia.txt`)

### REQ-096 - Filter Surveys By Survey Name

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must allow survey-related report results to be selected or filtered by survey name without requiring entry of a survey ID. When a survey name is supplied, the system must resolve that name internally to the corresponding survey ID for filtering. This capability is needed to make survey filtering available through the survey name while retaining the identifier needed to process the report.

> Ability to select the survey name and not have to enter the survey id for filtering (`early_draft_srs_galecia.txt`)
> The ability to filter by survey name rather than survey ID requires the system to resolve names to IDs internally. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-097 - Integrate Vendor Data Via APIs

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must interface with a variety of vendor websites through published APIs and/or automated transfers of standard-format data files, including formats such as USMARC21 and EDIFACT. This capability is needed because some libraries use external vendors for certain functions and reporting must handle data from those sources. The interface supports centralized management processes serving multiple branches. The system must handle vendor data when it is available, but it cannot rely on such data being present at every library.

> DE-2: Management Processes interface with a variety of vendor websites, via published APIs and/or automated transfer of standard-format data files (e.g., USMARC21, EDIFACT). (`early_draft_srs_galecia.txt`)
> Management Processes interface with a variety of vendor websites, via published APIs and/or automated transfer of standard-format data files (e.g., USMARC21, EDIFACT). (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-098 - Keep Reporting Separate From OPAC

**Priority:** Should - Mentioned in 2 documents.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The management reporting system must remain separate from the Online Public Access Catalog and must not constrain its functionality, features, or operation. Changes to management reporting must not affect patron access through the OPAC. Report execution should not slow down the OPAC, so reporting activity must not impair the public-facing catalog. Security groups and roles may control management access, but they must not restrict OPAC capabilities.

> These requirements shall not constrain functionality or features of the Online Public Access Catalog (OPAC) module. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)
> The management reporting system is separate from the public catalog. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-099 - Provide Detailed Error Reporting Feedback

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide thorough, high-level error reporting and feedback when operations fail. Error messages must help staff and other users understand the reason for a failure, including failures that occur when producing reports, rather than presenting only generic messages. The system must also allow low-level, query-specific feedback for local and global system administrators through the front-end interface.

> The system shall provide thorough high-level error reporting and feedback, and shall allow low-level query-specific feedback for administrators. (`meeting_tech_subcommittee_2009-06-30.txt`)
> UD-4: The system must provide thorough high-level error reporting and feedback, and shall allow low-level query-specific feedback for Local and Global System Administrators from the front-end interface. (`early_draft_srs_galecia.txt`)

### REQ-100 - Provide Historical Reporting Warehouse

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a reporting warehouse or equivalent historical-data store that preserves past data states for reporting. Staff need this capability when a report concerns what the data was at a prior point in time, such as determining a bill amount on a particular date. The historical store must support reports separately from real-time reports, which address current conditions such as what is overdue today.

> - No historical reporting warehouse (`evergreen_reference_2009.txt`)
> "Others are historical - 'what was the bill amount on June 30th?' We probably need a reporting warehouse for historical data." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-101 - Provide Management Record Data Specifications

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The developer must provide complete data specifications for records maintained or accessed by Management Processes. The specifications must identify field names, data types, and relationships so staff can understand the data structures and write effective queries. Coverage must include authority, bibliographic, order, item, and hold/request records, as well as other relevant records maintained or accessed by Management Processes. The documentation must therefore serve as data dictionaries for the defined record structures.

> The developer must provide complete data specifications for: - Authority records (`meeting_tech_subcommittee_2009-06-30.txt`)
> The developer must provide complete data specifications for: - Other records maintained or accessed by Management Processes (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-102 - Use Acquisitions Cataloging As Source

**Priority:** Should - Mentioned in 3 documents.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must rely on the data structures and functionality of the enterprise-level library automation system, including its Acquisitions and Cataloging modules. It must use that system as the source for reporting data rather than managing acquisitions or cataloging itself. This dependency supports management processes consolidated at a central location that accepts input and provides services to multiple branches. The system should account for the need for data from all locations to be complete and current so that reporting remains consistent.

> DE-1: Management Processes rely on the data structures and functionality of an enterprise-level Library Automation System, including Acquisitions and Cataloging modules. (`early_draft_srs_galecia.txt`)
> Management Processes rely on the data structures and functionality of an enterprise-level Library Automation System, including Acquisitions and Cataloging modules. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-103 - Accounting-Compliant Report Archival

**Priority:** Should - Mentioned in 2 documents; strong wording (must).  
**Type:** constraint  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must ensure that reports and archived data, including financial data, comply with standard accounting practices. Compliance must also address applicable state, county, and municipal auditing requirements. This requirement applies to the financial reports and archived information needed by staff, including reports on patron account balances, fines, charges, waived fines, and payments. The system must support these requirements without limiting reporting to a particular time period, branch, or payment method.

> All reports and data archiving must comply with standard accounting practice and state, county, and municipal auditing requirements. (`early_draft_srs_galecia.txt`)
> Compliance - all reports and data archiving must comply with standard accounting practice and state, county, and municipal auditing requirements. (`email_financial_reports.eml`)

### REQ-104 - Patron Payment Charge Ledger

**Priority:** Should - Mentioned in 2 documents; strong wording (must).  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must maintain a ledger of patron payments that identifies the specific charges to which each payment was applied. Staff need this audit trail to reconcile payments with the charges recorded on patron accounts. The ledger must support the financial reporting of payments by time period and payment method, including payments made at the staff desk, self-check station, or OPAC. This requirement applies to patron payments regardless of the associated charge.

> The system maintains a ledger of patron payments, including which charges payments are applied to, to facilitate reconciliation. (`early_draft_srs_galecia.txt`)
> Audit trail - system must maintain a ledger of patron payments, including which charges payments are applied to, to facilitate reconciliation. (`email_financial_reports.eml`)

### REQ-105 - Threshold Patron Balance Query

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must allow staff to query patron accounts whose balances exceed a dollar amount or threshold specified by the staff member. This capability is needed to identify accounts that require attention. Financial data attached to patron and item records must be available for the query, including the information needed to join those sources when financial reports are prepared. The threshold must be user-specified rather than fixed by the system.

> As an example, a staff user can easily query patron accounts with balances greater than X dollars. (`early_draft_srs_galecia.txt`)
> A staff user can easily query patron accounts with balances greater than X dollars. (`email_financial_reports.eml`)

### REQ-106 - Patron Item Financial Association

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-14  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must associate fines, charges, waivers, and ecommerce transactions with the relevant patron and item records. It must track fines waived and payments made for each library, allowing each branch to identify financial activity collected there. Staff must be able to update financial information easily. The associated records must support financial queries, including queries involving patron account balances and information drawn from both patron and item records.

> Fines, charges, waivers, and ecommerce transactions are attached to patron and item records. System tracks fines waived and payments made per library. Financial information can be updated easily. (`early_draft_srs_galecia.txt`)
> Fines, charges, waivers, and ecommerce transactions are attached to patron and item records. (`email_financial_reports.eml`)

### REQ-107 - In Transit Items Destination Grouping

**Priority:** Should - Mentioned in 2 documents; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide a report of items currently in transit. The report must identify items sent to a specified destination library and must group or organize results by both sending library and destination library. This capability is needed because in-transit item reports are critical for delivery coordination, including coordination by branch staff and managers.

> - List of Items in Transit by both sending library and destination library (`early_draft_srs_galecia.txt`)
> - Items In Transit by Sending Library (`early_draft_srs_galecia.txt`)

### REQ-108 - Interface With OPAC For Reporting

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must interact with the patron interface, also known as the Online Public Access Catalog (OPAC), to access data created through that interface. This is needed because patron data, including holds and circulation data, is created in the OPAC and must be available for reports. Management processes require this interaction so staff can query the data for reporting purposes. The requirement applies to reports using data from the patron interface.

> DE-3: Management Processes interact with a patron interface, also known as an Online Public Access Catalog (OPAC). (`early_draft_srs_galecia.txt`)
> Management Processes interact with a patron interface, also known as an Online Public Access Catalog (OPAC). (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-109 - Activity Reports With Permission Cross Tabs

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must provide activity reports showing traffic and volume of library use. These reports must display statistics for check-outs, check-ins, holds placed, and holds filled. Staff and other authorized report users need these reports to examine circulation activity. The system must support cross-tabulation of the activity statistics by terminal, branch, library system, hour, patron age range, patron type, and patron location, subject to the applicable report permissions.

> Activity reports should indicate traffic and volume of use, displaying statistics on check-outs, check-ins, holds placed, and holds filled. (`early_draft_srs_galecia.txt`)
> Activity reports showing traffic and volume of use - checkouts, check-ins, holds placed, holds filled. (`email_report_features.eml`)

### REQ-110 - Assign Report Queue Priorities

**Priority:** Should - Mentioned in 2 documents; strong wording (crucial).  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must allow authorized users to assign priorities to reports in the processing queue. Higher-priority reports must be able to move ahead of lower-priority reports, including reports that would otherwise wait behind resource-consuming work. This capability is needed when staff require important reports, such as a director’s board report, to be processed before an ad-hoc query, and report queuing must support clear processing order.

> Ability to prioritize certain types of reports so they will pop to the top of the queue over resource-consuming reports (`early_draft_srs_galecia.txt`)
> Also, the ability to prioritize certain reports is crucial. A director's board report should be able to jump ahead of a staff member's ad-hoc query. (`email_report_features.eml`)

### REQ-111 - Choose Query Values From Picklists

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must allow staff to select query values from picklists containing possible values. This capability must be provided through the user-friendly query interface used to design queries against bibliographic, item, patron, transaction, and financial records. It is needed so staff can choose applicable values while constructing queries.

> - Select values from a picklist of possible values (`early_draft_srs_galecia.txt`)
> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)

### REQ-112 - Cross Tabulate Board Activity

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must support cross-tabulation of activity and board report data by terminal, branch, library system, hour, patron age range, patron type, and patron location. Activity reports must present traffic and volume-of-use statistics for checkouts, check-ins, holds placed, and holds filled. The capability is needed for pre-defined reports consumed by library boards and other external consumers, including statistics such as those required by the Georgia Annual Report and Application for State Aid.

> Cross- tabulated per terminal, per branch, per system, per hour, per age range, per patron type, per patron location. (`email_report_features.eml`)
> BOARD REPORTS: Pre-defined reports for boards. Cross-tabulated per terminal/branch/system/hour/age/patron type/location. (`email_report_features.eml`)

### REQ-113 - Design Queries With Boolean Regex

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must provide a user-friendly interface for designing queries across bibliographic, item, patron, transaction, and financial records. Staff must be able to select fields to query and choose values from a picklist of possible values. The interface must support selecting regular expressions from a drop-down menu and using a full range of Boolean operators. Access to the query tool must be subject to administrator controls.

> The system should provide a user-friendly interface for designing queries against all record types (bibliographic, item, patron, transaction, financial). (`early_draft_srs_galecia.txt`)
> We need a user-friendly interface for designing queries against all record types. (`email_report_features.eml`)

### REQ-114 - Differentiate Create And Clone Permission

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must provide distinct, fine-grained permission levels controlling which staff may create and clone reports. These permissions must be easy to administer so administrators can manage reporting access. The controls are needed to limit report creation and cloning to authorized staff rather than applying the same access to everyone. The permission model must distinguish the ability to create reports from the ability to clone them.

> The system should provide distinct, fine-grained permission levels that limit who can create and clone reports. (`early_draft_srs_galecia.txt`)
> We need distinct, fine-grained permission levels limiting who can create and clone reports. (`email_report_features.eml`)

### REQ-115 - Display Selection Criteria With Results

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`

The system must display the query or selection criteria used to generate a report alongside the report results. Staff need to see the criteria so they can understand what conditions produced the displayed results. This requirement applies to reports generated from query selections, including periodic reports. The criteria and results must be presented together rather than leaving the selection conditions unavailable in the report output.

> The system should provide the query selections along with the results, so users can see what criteria were used to generate the report. (`early_draft_srs_galecia.txt`)
> System provides query selections along with results. (`email_report_features.eml`)

### REQ-116 - Provide Georgia Annual Activity Reports

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must provide predefined reports for consumption by library boards and other external consumers. These reports must include basic statistics required by the Georgia Annual Report and Application for State Aid, including activity statistics for check-outs, check-ins, holds placed, and holds filled. Activity reports must support cross-tabulation by terminal, branch, library system, hour, patron age range, patron type, and patron location.

> The system should provide pre-defined reports for consumption by library boards and other external consumers. (`early_draft_srs_galecia.txt`)
> Pre-defined reports for library boards with basic statistics (Georgia Annual Report requirements). (`email_report_features.eml`)

### REQ-117 - Select Query Fields Across Records

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must provide a user-friendly query interface that allows staff to select the fields used in a query. Query field selection must be available when designing queries against bibliographic, item, patron, transaction, and financial records. This capability is needed to support staff in creating queries across all supported record types.

> Staff should be able to: - Select fields to query (`early_draft_srs_galecia.txt`)
> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)

### REQ-118 - Show Report Queue Position

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The system must show staff where a submitted report is in the processing queue. It must display how many reports are ahead of the report and whether processing is still occurring, including the report’s applicable queue status. This visibility is needed because staff become frustrated when they submit a report and receive no indication of what is happening. The status information must distinguish waiting, running, completed, and failed reports.

> They need to see: - That their report is in the queue - How many reports are ahead of theirs (`email_report_features.eml`)
> - No report queue visibility (staff can't see where their report is in queue) (`evergreen_reference_2009.txt`)

### REQ-119 - Count Edited Bibliographic Records

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report showing the number of bibliographic records that have been edited. Staff need this report as part of bibliographic records reporting to monitor edited records. The edited bibliographic records count is identified as a report type that was not available in the referenced reporting system, so this system must provide that capability.

> - Bib Records Edited Count (`early_draft_srs_galecia.txt`)
> - Bib Records Edited Count (not available) (`evergreen_reference_2009.txt`)

### REQ-120 - Deliver Report Output By Email

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must support delivering report output by email and must allow staff to enter email addresses for the recipients. This capability is needed because email delivery of reports and the ability to specify report recipients are required for distributing generated output. Recipient addresses must be usable with report delivery, including reports scheduled to run ASAP, hourly, daily, weekly, monthly, or yearly. When a recurring report is edited, its email addresses must also be editable.

> Ability to enter email addresses for report to be sent to - would be great to have an address book of regularly used addresses (`early_draft_srs_galecia.txt`)
> - No email delivery of reports (`evergreen_reference_2009.txt`)

### REQ-121 - Dewey Grouped Circulation Counts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide circulation counts grouped by Dewey classification. Staff need this report to review circulation activity according to the Dewey organization of items. The report must group the circulation counts by Dewey rather than presenting only an overall total or another circulation grouping. The source material identifies this report type as not available, so the required Dewey reporting capability must address that stated limitation.

> - Circulation Count by Dewey (`early_draft_srs_galecia.txt`)
> - Circulation Count by Dewey (not available) (`evergreen_reference_2009.txt`)

### REQ-122 - Expose Last Circulation Date Field

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The system must expose each item’s last circulation date as a separate field in reports, including the enhanced weeding report. Staff need this information to identify the most recent circulation activity for items and to support weeding-related reporting. The last circulation date must remain distinct from other dates, because the source identifies its separate availability as a missing reporting capability.

> Ability to indicate last circulation date on item reports (`survey_results_2009.txt`)
> - Weeding report with date of last circulation (partially available) (`evergreen_reference_2009.txt`)

### REQ-123 - Fines Stopped Reason Item List

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide an items report listing items grouped by the reason that fines were stopped. This report is needed to support review of items according to their fines-stopped reason within the items-reporting functions. Staff must be able to use the grouped list when examining those reasons. The source of predefined reports identifies the List of Items by Fines Stopped Reason as not available, so the system must address that stated limitation before the report is available.

> - List of Items by Fines Stopped Reason (`early_draft_srs_galecia.txt`)
> - List of Items by Fines Stopped Reason (not available) (`evergreen_reference_2009.txt`)

### REQ-124 - Group Circulation Counts By Age

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide circulation counts grouped by patron age demographic. This report is needed as a circulation report alongside counts by circulation modifier, category, Dewey, shelving location, MARC fields, circulation location, patron county, and patron home library. The source identifies circulation count by age demographic as a missing report type, so the system must support the specified grouping rather than leaving this report unavailable.

> - Circulation Count by Age Demographic (not available) (`evergreen_reference_2009.txt`)
> - Circulation Count by Age Demographic (`early_draft_srs_galecia.txt`)

### REQ-125 - Group Collection Age By Call Number

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report the age of the collection grouped by call number. Where shelving-location information applies, the report must also group collection age by shelving location. This capability must provide collection-age results in the item reporting area and must preserve the specified grouping dimensions so staff can review the age of collection holdings.

> - Age of collection by call number or shelving location (`early_draft_srs_galecia.txt`)
> - Age of collection by call number (not available) (`evergreen_reference_2009.txt`)

### REQ-126 - Items Created Date Range Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report listing items created within a specified date range. The report must use the selected date range to identify items by their creation date. Staff need this report to review items added during a defined period as part of item reporting. The report is limited to items whose creation dates fall within the specified range.

> - List of Items by Creation Date Range (`early_draft_srs_galecia.txt`)
> - List of Items by Creation Date Range (not available) (`evergreen_reference_2009.txt`)

### REQ-127 - Items Edited Count Capability

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide an items report showing the number of items edited. This report is needed to support review of item-editing activity as part of the required items reports. Staff must be able to use the report when reporting edited item counts. The source of predefined reports identifies Items Edited Count as not available, so the system must address that stated limitation before this report can be considered available.

> - Items Edited Count (`early_draft_srs_galecia.txt`)
> - Items Edited Count (not available) (`evergreen_reference_2009.txt`)

### REQ-128 - List Inactive Patrons

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a list of patrons whose status is inactive. Staff need this list to identify patrons with inactive status as part of patron reporting. The requirement is limited to reporting patrons by inactive status and is needed because this report type is identified as unavailable.

> - List of Patrons with inactive status (not available) (`evergreen_reference_2009.txt`)
> - List of Patrons with inactive status (`early_draft_srs_galecia.txt`)

### REQ-129 - Location And County Circulation

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide circulation counts by circulation location, with each location's counts broken down by the patron's county. Staff need this report to examine circulation activity at circulation locations in relation to patron county. The report must retain both dimensions so that counts can be reviewed by location and then by county. The source material identifies this report type as not available, so the required reporting capability must address that stated limitation.

> - Circulation Count by Circ Location broken down by Patron County (`early_draft_srs_galecia.txt`)
> - Circulation Count by Circ Location broken down by Patron County (not available) (`evergreen_reference_2009.txt`)

### REQ-130 - MARC Field Circulation Counts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide circulation counts grouped by MARC fields. Staff need this report to examine circulation activity using the MARC field information associated with items. The report must organize the counts by MARC rather than limiting staff to circulation totals or other groupings. The source material identifies circulation counts by MARC fields as not available, so the required capability must address that stated limitation.

> - Circulation Count by MARC (`early_draft_srs_galecia.txt`)
> - Circulation Count by MARC fields (not available) (`evergreen_reference_2009.txt`)

### REQ-131 - Method-Based Check-In Counting

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must count check-ins individually by method and provide cumulative check-in counts. The supported methods must include book-drop, terminal, and self-service check-ins. This reporting is needed by staff to compare check-in activity across methods and to review total check-in volume. The system must preserve both the separate method counts and the cumulative result.

> The system counts all types of check-in individually and cumulatively: - book-drop - by terminal - by user or self-service (`early_draft_srs_galecia.txt`)
> I need to see check-in counts broken down by method - book drop vs terminal vs self-service (`survey_results_2009.txt`)

### REQ-132 - Modifier Grouped Circulation Counts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide circulation counts grouped by circulation modifier. Staff need this report to examine circulation activity according to the modifiers associated with circulation records. The broader circulation reporting requirements also identify counts by circulation modifier together with category groupings such as Adult, YA, and Juv. The source material states that circulation counts by circulation modifier are only partially available, so the required report must address that limitation.

> - Circulation Count by Circ Modifier (`early_draft_srs_galecia.txt`)
> - Circulation Count by Circ Modifier (partially available) (`evergreen_reference_2009.txt`)

### REQ-133 - Patron Balance Financial Reporting

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Financial reports are important, but not the strict core reporting minimum.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide financial reports covering patron account balances by patron, home library, and system. Reports must show fines and charges accrued by time period and charge type, including overdue fines, damaged item charges, and lost item charges. They must also show fines waived by time period and branch, and payments made by time period and payment method, such as the staff desk, self-check station, or OPAC. These reports are needed by staff to review bills currently owed and related financial activity.

> The system provides financial reports including: - patron account balances by patron, home library, and system - fines and charges accrued per time period (e.g., last twelve months, YTD, last month) and per type of charge (overdue fines, damaged item charges, lost item charges, etc.) - fines waived ... (`early_draft_srs_galecia.txt`)
> - Bills currently Owed by Patrons (`early_draft_srs_galecia.txt`)

### REQ-134 - Present Results As Pivot Tables

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The reporting system must support presenting report results as pivot tables. This output is needed when staff require an additional way to organize and examine report results, and it was identified as a desired reporting feature. Pivot table presentation must be available as a report output format rather than requiring results to remain in a conventional display. The requirement does not specify a restriction on the reports that may use this output.

> Pivot table output (`early_draft_srs_galecia.txt`)
> Pivot table output would be great (`survey_results_2009.txt`)

### REQ-135 - Provide Anonymized Demographic Reporting

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** non-functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must report demographic statistics without personally identifiable information. It must support anonymized analysis of transactions and patron activity using demographic groupings such as geographical regions and age ranges. This condition applies to demographic reporting used for programming and patron behavior analysis.

> Demographic statistics (must be anonymized - no personally identifiable info) (`survey_results_2009.txt`)

### REQ-136 - Provide Geographic Demographic Reporting

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must support demographic reporting that analyzes transactions by geographical region, including useful groupings such as ZIP codes. This capability is needed for demographic analysis and for planning programming, where geographic information is considered useful. Demographic statistics must be anonymized and must not include personally identifiable information.

> - Transactions by geographical regions - Transactions by age ranges - Patron behavior analysis (how quickly books are returned, renewal rates) - Demographic statistics (must be anonymized - no personally identifiable info) (`survey_results_2009.txt`)

### REQ-137 - Provide RealTime Reporting On Current

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must support real-time reporting against current data. This capability is needed for situations requiring information that reflects the current state of the data, including reports such as what is overdue today. The system should make current data available for real-time report execution rather than relying only on a historical reporting warehouse. Real-time reporting is a distinct capability from historical reporting for a specified date or date range.

> Ability to have real time reporting (`early_draft_srs_galecia.txt`)
> - No real-time reporting (all reports are run on current data) (`evergreen_reference_2009.txt`)

### REQ-138 - Provide Three Reporting Interfaces

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide three reporting interfaces: canned reporting, on-demand reporting, and open-template reporting. Canned reports must support generic reports that can run immediately or recur, while on-demand reports must provide preset reports whose selection criteria and display options can be edited. Open-template reporting must allow selection of attributes associated with circulation, items, patrons, bills, and bibs for filtering and display.

> Three interfaces are needed: a) Canned reports - generic reports set to run by the individual either ASAP or recurring b) Noncanned or On Demand Reports - preset but have the ability to edit selection criteria and display options c) Open Template Reporting - all attributes associated with circulatio... (`early_draft_srs_galecia.txt`)
> - Three interfaces (canned, on-demand, open template) - only basic canned exists (`evergreen_reference_2009.txt`)

### REQ-139 - Report Claims-Returned Items

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report listing items marked as claims returned. The report must identify the items associated with that status so staff can review claims-returned records as part of item reporting. The source identifies this as an item report and also notes that the claims returned report was not available in the referenced reporting set.

> - Claims returned (`early_draft_srs_galecia.txt`)
> - Claims Returned report (not available) (`evergreen_reference_2009.txt`)

### REQ-140 - Report Holds Requiring Purchase Alert

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report identifying holds that require a purchase alert. Staff need this report as part of the holds reports to determine which holds are associated with a purchase alert. The report must identify the relevant holds rather than report items sent or received for holds, unfilled holds, or stale holds. The cited report listing identifies Holds Purchase Alert as not available, so the system must provide this reporting capability.

> - Holds Purchase Alert (`early_draft_srs_galecia.txt`)
> - Holds Purchase Alert (not available) (`evergreen_reference_2009.txt`)

### REQ-141 - Report Missing MARC Fields

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must list bibliographic records that are missing specified MARC fields. This report is needed by staff to identify incomplete bibliographic records and support record-quality review. The source material also identifies this report type as not available, so that stated limitation must be recognized when assessing the reporting capability.

> - Bib Records missing specific MARC fields (`early_draft_srs_galecia.txt`)
> - Bib Records missing specific MARC fields (not available) (`evergreen_reference_2009.txt`)

### REQ-142 - Report Staff Password Change Dates

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report of staff accounts that includes the date of each account’s last password change. Staff need this report to review password-change information for staff accounts. The report may also include account expiration dates, but expiration dates are not required by this requirement. The report must focus on staff accounts and their last password-change dates, and the cited report listing identifies the capability as one that was not available.

> - List of Staff Accounts with date of last password change and account expiration (`early_draft_srs_galecia.txt`)
> - Staff Accounts with date of last password change (not available) (`evergreen_reference_2009.txt`)

### REQ-143 - Report Stale Holds Awaiting Pickup

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a stale holds report identifying holds that have remained on the hold shelf awaiting patron pickup for too long. Staff need this report to identify holds that have exceeded the permitted waiting time. The report is required as a holds reporting function, although the source documentation identifies stale holds as not available in the referenced system.

> - Stale Holds (holds sitting on hold shelf waiting for pickup for too long) (`early_draft_srs_galecia.txt`)
> - Stale Holds (not available) (`evergreen_reference_2009.txt`)

### REQ-144 - Report Unfilled Holds Only

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide staff with a report of holds that remain unfilled. The report is needed to identify holds for which fulfillment has not occurred, supporting staff review of outstanding hold activity. This capability must be provided as part of the holds reports and must remain distinct from reports of items sent for holds, items received for holds, IntraPINES loans, and stale holds.

> - Unfilled Holds (`early_draft_srs_galecia.txt`)
> - Unfilled Holds (not available) (`evergreen_reference_2009.txt`)

### REQ-145 - Support Assistive Technology For Web

**Priority:** Should - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

If the system provides a web-browser-based interface, it must be accessible through Microsoft Internet Explorer version 6.0 and later and Mozilla Firefox version 2.0 and later. This capability is needed to support access through the specified browsers for staff and other library system users who use the web interface. The system must also be accessible with screen-reading software, screen-magnification software, and other assistive technology programs designed to increase accessibility.

> OE-4: If web-browser based, the system must be accessible through Microsoft Internet Explorer (version 6.0 and later) and Mozilla Firefox (version 2.0 and later). (`early_draft_srs_galecia.txt`)

### REQ-146 - Support Fine-Grained Queueable Reporting

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support the fine-grained reporting requirements described in the attached Appendix B specification. These requirements must be available as part of the system’s reporting capabilities. Staff should be able to use the supported reports and see where a report is in the queue of reports waiting to run. This requirement is separate from support for the canned report definitions described in Appendix A.

> The system must be able to support the fine-grained reports requirements as described in the attached specification (see Appendix B). (`early_draft_srs_galecia.txt`)

### REQ-147 - Type-Based Checkout Renewal Counting

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must count checkouts and renewals individually by transaction type and cumulatively. It must distinguish staff checkouts, self-checkouts, staff renewals, self-checkout renewals, online renewals, and OPAC renewals. This reporting enables staff to examine the sources of checkout and renewal activity while also reviewing total volume. Each listed transaction type must remain separately identifiable in the resulting statistics.

> The system counts all types of check-out individually and cumulatively: - staff check-out - self check-out - staff renewal - self checkout renewal - online renewal - OPAC renewal (`early_draft_srs_galecia.txt`)
> Check-out types should be counted separately - staff checkout, self checkout, staff renewal, self checkout renewal, online renewal, OPAC renewal (`survey_results_2009.txt`)

### REQ-148 - Use Canned Report Definitions Appendix A

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support the reporting definitions described in the canned report examples in Appendix A. These definitions must be available for the reporting needs represented by the attached examples. Staff should be able to use the resulting reports as part of the reporting process, including seeing where a report is in the queue while it waits to run. The system must also support the separate fine-grained reporting requirements described in Appendix B.

> The system must be able to support the reporting definitions as described in the attached report examples (see Appendix A). (`early_draft_srs_galecia.txt`)


## Could requirements

### REQ-149 - Allow Staff Report Content Creation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must allow staff to create report content as primary report content creators. This capability must include frontline circulation staff and supervisors, as well as other paid staff involved in designing and providing library services. Staff need this capability because they are identified as the primary creators of reports. The system should therefore support report-content creation across the staff roles involved in library service delivery.

> [Jenny: Staff are our primary content creators for reports] (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-150 - Analyze Branch Capacity Distribution

**Priority:** Could - Mentioned in 2 documents. Adjusted from Should by model: Branch capacity analysis supports planning; not essential reporting.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must support analysis of branch capacity and the optimal distribution of the library collection across branches. This capability is needed within management processes to evaluate how collection resources are distributed in relation to branch capacity. Staff involved in management activities need the analysis to support decisions concerning library services, programs, and policies. The requirement is limited to functions directly or indirectly related to management activities, with Acquisitions and Cataloging covered by separate specifications.

> - Analyzing branch capacity and optimal distribution of the collection. (`early_draft_srs_galecia.txt`)
> - Analyzing branch capacity and optimal distribution of the collection (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-151 - Analyze Collection Usage For Management

**Priority:** Could - Mentioned in 2 documents. Adjusted from Should by model: Collection use analysis is valuable, but more advanced analytics.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must support analysis of the library collection and how patrons use it. This capability is needed as part of management processes for analyzing the collection and its use by patrons. Staff involved in management activities need this analysis to support library service, program, and policy management. The requirement is limited to capabilities directly or indirectly related to management activities, while Acquisitions and Cataloging are addressed through separate specifications.

> - Analyzing the Library collection and its use by patrons. (`early_draft_srs_galecia.txt`)
> - Analyzing the Library collection and its use by patrons (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-152 - Analyze Patron Demographics And Interests

**Priority:** Could - Mentioned in 2 documents. Adjusted from Should by model: Demographic analysis is advanced and nonessential.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must support analysis of patron demographics and interests. This capability is needed as part of management processes that assess the characteristics and interests of patrons. Staff involved in management activities need the analysis to support management of library services, programs, and policies. The requirement is limited to capabilities directly or indirectly related to management activities, while Acquisitions and Cataloging are addressed through separate specifications.

> - Analyzing the demographics and interests of patrons. (`early_draft_srs_galecia.txt`)
> - Analyzing demographics and interests of patrons (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-153 - Analyze Staff Productivity Workflow

**Priority:** Could - Mentioned in 2 documents. Adjusted from Should by model: Staff productivity analysis is advanced; not required for core reports.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must support analysis of staff productivity and workflow. This capability is needed within management processes to assess how staff work is performed and organized. Staff involved in management activities need the analysis to support the management of library services, programs, and policies. The requirement is limited to functions directly or indirectly related to management activities, with Acquisitions and Cataloging covered by separate specifications.

> - Analyzing staff productivity and workflow. (`early_draft_srs_galecia.txt`)
> - Analyzing staff productivity and workflow (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-154 - Build Complex Queries Without Workarounds

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The reporting interface must support construction of complex queries without requiring difficult or impractical workarounds. It should provide capabilities beyond basic filtering and sorting, because those functions alone do not adequately support complex query construction. The system should avoid limiting query construction to simple filters without Boolean operators such as AND or OR when staff construct reports for reporting needs.

> - Complex queries are difficult to construct (`evergreen_reference_2009.txt`)

### REQ-155 - Compile Executive Reports Interface List

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The project must compile a list of reports required for an Executive Reports Interface. This list is needed to document the reporting functionality planned for a future Evergreen release and to guide the Reports Working Group’s requirements work. The resulting reports must also support the group’s role as a testing group through which new Reports development is filtered.

> - Compile a list of reports needed for an Executive Reports Interface. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-156 - Cover Management Activities Reporting Requirements

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system specification must cover requirements that directly or indirectly support management activities. It should support analysis of the library collection and its use by patrons, branch capacity and collection distribution, patron demographics and interests, staff productivity and workflow, and the tracking and verification of financial transactions. Acquisitions and cataloging functionality must remain outside this specification because PINES is defining separate specifications for those modules.

> The group agreed to specify only those requirements that directly or indirectly relate to management activities. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-157 - Create PINES Library Report Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The project must determine and create the report templates needed by all PINES libraries. These templates are needed to provide a consistent basis for reporting across the libraries and to support the Reports Working Group’s effort to document optimal Reports functionality. The work must address the templates required for the libraries rather than only compiling a list of reports for an Executive Reports Interface.

> - Determine and create templates needed for all PINES libraries. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-158 - Define Management Processes Scope

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must define the Management Processes scope around reports and analysis tools for library managers, administrators, and staff. These tools are needed for planning, evaluation, and oversight activities. The scope must exclude day-to-day patron-facing functions, which are handled through the OPAC and circulation client. This boundary ensures that management reporting remains separate from routine patron-facing library services.

> She clarified that this does NOT include day-to-day patron-facing functions (those are part of the OPAC and circulation client). (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-159 - Email Deliver Scheduled Report Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must deliver the results of scheduled reports by email so that staff do not have to download them from the web interface. This capability is needed for reports that run at regular intervals, including daily, weekly, or monthly schedules. The system should retain these scheduling intervals while replacing web-interface-only retrieval with email delivery; hourly scheduling and running multiple selected reports at the same time are not required by this requirement.

> - No email delivery (reports can only be downloaded from the web interface) (`evergreen_reference_2009.txt`)

### REQ-160 - Expose All Database Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must make all relevant database fields available for report construction rather than limiting field selection to a subset. This access is needed because limited field selection prevents reports from using all relevant data and can make complex queries difficult to construct. Field selection should therefore expose the relevant database fields available to the reporting system instead of restricting staff to only the fields presented by a limited selection.

> - Limited field selection (not all database fields are available) (`evergreen_reference_2009.txt`)

### REQ-161 - Manage Consortium PINES Settings

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must allow the global system administrator to manage PINES at the consortium level. This includes implementing software changes and configurations and generating statistical reports for PINES as a whole. The capability is needed by the central IT team responsible for consortium-level administration. Consortium administration must therefore cover both system management and statistical reporting across PINES.

> Global System Administrator: Manages PINES at the consortium level, implementing software changes and configurations, and generating statistical reports for PINES as a whole. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-162 - Provide Management Reporting Tools

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must provide reports and analysis tools for library managers, administrators, and staff. These tools are needed to support management processes, including planning, evaluation, and oversight. The scope applies to management activities and must not include day-to-day patron-facing functions handled by the OPAC and circulation client.

> Katherine explained that the group would focus on Management Processes - that is, reports and analysis tools used by library managers, administrators, and staff for planning, evaluation, and oversight purposes. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-163 - Provide Non Cataloged Items Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must provide a canned report showing the number of non-cataloged items. This report is needed as a predefined circulation report for staff who require a count of non-cataloged items without constructing a complex query. The report should be available among the canned reports, whose construction is subject to limitations including simple filters, limited field selection, and no Boolean operators beyond those filters.

> - Non-Cataloged Count (`evergreen_reference_2009.txt`)

### REQ-164 - Provide Web Reporting Drag Drop

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must provide a web-based reporting interface through which staff can create custom reports. The interface must support drag-and-drop field selection, basic filtering, and sorting so staff can define report contents and criteria. Staff must also be able to save report definitions and reuse them for later reporting, with report results available in CSV, HTML, and sometimes Excel formats.

> Evergreen includes a report writer that allows staff to create custom reports using a web-based interface. Key features: - Drag-and-drop field selection - Basic filtering and sorting - Multiple output formats (CSV, HTML, sometimes Excel) - Ability to save and reuse report definitions (`evergreen_reference_2009.txt`)

### REQ-165 - Restrict Staff Report Filters

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The permission model must allow administrators to limit which filters individual staff members may use when running reports. This control is needed because the existing model allows staff to run any report they can access but does not limit the filters they can use. The restriction must apply at the individual staff level and should supplement, rather than replace, the existing report-access permissions.

> - No ability to limit which filters staff can use (`evergreen_reference_2009.txt`)

### REQ-166 - Show Current Patron Bills Owed

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must provide a canned report showing bills currently owed by patrons. This report is needed by staff who require a predefined view of outstanding patron bills rather than a custom query. It must be included among the available bills reports, alongside detailed payments received and aged debt, and it may be scheduled at regular daily, weekly, or monthly intervals subject to the stated scheduling limitations.

> - Bills Currently Owed by Patrons (`evergreen_reference_2009.txt`)

### REQ-167 - Support Regex In Query Filters

**Priority:** Could - Mentioned in 2 documents. Adjusted from Should by model: Regex filters add power but can be optional for many users.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `email_report_features.eml`, `evergreen_reference_2009.txt`

The reporting interface and query designer must support regular expressions when users define report query criteria or filters. This capability is needed to support more complex searches than basic filtering and sorting, since the identified limitations include difficulty constructing complex queries and the absence of regular expression support. Authorized report users should be able to apply regular expressions while defining queries against available report data.

> QUERY TOOL: User-friendly interface for designing queries against all record types. Boolean operators, picklists, regex support. Admin controls access. (`email_report_features.eml`)
> - No regular expression support (`evergreen_reference_2009.txt`)

### REQ-168 - Track Financial Transactions Verification

**Priority:** Could - Mentioned in 2 documents. Adjusted from Should by model: Financial transaction verification is important but not central here.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must support tracking and verification of financial transactions. This capability is needed as part of management processes for monitoring and confirming financial activity. Staff involved in management activities need this capability to support the management of library services, programs, and policies. The requirement is limited to capabilities directly or indirectly related to management activities, while Acquisitions and Cataloging are addressed through separate specifications.

> - Tracking and verifying financial transactions. (`early_draft_srs_galecia.txt`)
> - Tracking and verifying financial transactions (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-169 - Report Acquisition Period Volume

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`

The system must support reporting on the volume acquired during a selected acquisition period. Staff should be able to use this reporting to assess how much volume has been added during periods such as the last 30, 60, or 90 days. The acquisition period must be based on acquisition dates recorded for the relevant items. The system should support customizable categories so different libraries can examine newly added volume using breakdowns appropriate to their needs.

> It would be helpful to see how much volume has been added in the last 30/60/90 days. (`conversations/conv_pines014_material_volume.eml`)

### REQ-170 - Define Branch Capacity Calculation

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-04-08  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

Before the capacity interface is built, the system’s capacity measure and its underlying metrics must be defined. The definition must establish the basis for calculating and comparing branch capacity, including whether it is based on the number of items versus shelf space, physical items versus a configured limit, or circulation volume versus processing capacity. This condition is necessary so that aggregated capacity queries and interface comparisons use an agreed measure.

> Also, what specific metrics define "capacity"? Is it: - Number of items vs. shelf space? - Number of physical items vs. a configured limit? - Circulation volume vs. processing capacity? Need to nail this down before building the interface. (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-171 - Drilldown Branch Capacity Details

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-08  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must allow staff to select an individual branch from the high-level capacity overview and view detailed capacity information for that branch. This capability is needed when the overview identifies a branch that requires closer examination. The system should retain the overview as a summary of all branches while providing a drill-down into the selected branch. The detailed view must concern the capacity information for the selected branch.

> 2. Ability to drill down into individual branches (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-172 - Filter Branch Capacity By Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-08  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must allow staff to filter branch capacity results by region, library type, and current load. Filtering is needed to narrow the all-branch capacity results to the branches relevant to a particular review. The filters must be available within the branch capacity interface and operate on the displayed branch results. This supports staff analysis of capacity by geographic grouping, branch classification, or present load.

> By region, by library type, by current load... (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-173 - Show Branch Capacity Status Colors

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-08  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must provide a visual capacity status for each branch using green when the branch is under capacity, yellow when it is nearing full capacity, and red when it is at or over capacity. The status must be available in a high-level view showing all branches and their key metrics. The system should also allow staff to drill down from the overview into an individual branch when more detail is needed.

> Maybe color-coding - green for under capacity, yellow for getting full, red for at/over capacity (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-174 - Sort Branch Capacity Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-08  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must allow staff to sort the branch capacity results displayed in the capacity interface. Sorting is needed to organize the all-branch results for review and comparison. The capability applies to the capacity results shown in the high-level interface. It should support the intended staff workflow of arranging branch information while examining capacity across branches.

> I'd want to be able to sort and filter. (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-175 - Assign Roles For Differentiated Access

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must support assigning roles to individual staff members and use those assignments to provide differentiated access. Roles must accommodate front desk staff who can run basic reports with limited filters, department heads who can create and modify templates, and system administrators with full access to reports and permissions. Role administration should make changing a staff member’s permissions a simple change to the role assignment rather than edits to individual permissions.

> Each of these should be a role that can be assigned to staff members. (`email_staff_login.eml`)

### REQ-176 - Display Branch Capacity Overview

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must provide a high-level capacity interface that displays the capacity of all branches simultaneously. The overview is needed so staff can assess branch capacity across the library organization rather than reviewing branches individually. It should present the branches together in a summary view with key capacity information. This interface provides the starting point for viewing branch capacity at an organizational level.

> The system should provide an interface showing the capacity of all branches. - High-level overview of all branches' capacity at once (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-177 - Manage Security Groups Or Roles

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must allow administrators to create, manage, and maintain security groups or roles used for access control. When a staff member logs in by any supported method, the system must determine that staff member’s permissions from the assigned security group or role. Streamlined staff login methods may be supported but must not be required, because smaller branches may not have infrastructure for card readers.

> Administrators should be able to create and manage these groups. (`email_staff_login.eml`)

### REQ-178 - Show Branch Capacity Trend Direction

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must provide trend data indicating whether each branch’s capacity is growing or shrinking over time. This information must be available through an interface that presents the capacity of all branches in a high-level overview and supports drill-down to individual branches. The interface should also support sorting and filtering by region, type, or load so staff can examine capacity trends for relevant groups or branches.

> Trend data (growth/shrink patterns) (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-179 - Update Permissions By Role Change

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must allow administrators to change a staff member’s permissions by changing the person’s role assignment. This approach is needed so permission administration remains simple when a different access level is needed. The system should apply the permissions defined for the newly assigned role rather than requiring administrators to modify individual permissions.

> changing someone's permissions should be a simple matter of changing their role assignment, not modifying individual permissions. (`email_staff_login.eml`)

### REQ-180 - Compare Library Shelf Space SystemAverage

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must allow a library-level shelf-space report to be compared with the system average. The comparison must cover, for each genre and format of material, the percentage of total circulations, the percentage of the collection, and the percentage of total shelf space. This capability is needed by branch managers to understand their local situation in relation to the broader library system.

> This way branch managers can see their local situation AND see how they compare to the system average. (`conversations/conv_pines016_shelf_space.eml`)

### REQ-181 - Estimate Shelf Space By Dimensions

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

Because shelf space is not directly tracked in the database, the system must estimate shelf space for each genre and format of material. The estimate must use item dimensions or item count as a proxy. The resulting estimate must support calculation of each category's percentage of total shelf space for the shelf-space report, alongside the percentage of the collection and percentage of total circulations.

> Shelf space isn't directly tracked in the database. We'd need to estimate based on item dimensions or use item count as a proxy. (`conversations/conv_pines016_shelf_space.eml`)

### REQ-182 - Filter Shelf Utilization Date Range

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must allow shelf-space utilization reports to be filtered by a specified date range. The filtering is needed at the system level so staff can examine how shelf-space utilization changes between periods such as Q1 and Q2. This supports review of seasonal collection conditions and the use of data to redistribute materials when some branches have too many or too few items in a category.

> Can we also filter by date range? Like, what was the shelf space utilization in Q1 vs. Q2? (`conversations/conv_pines016_shelf_space.eml`)

### REQ-183 - Report Circulation Category Percentages

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must report, for each material genre and format, the percentage of total circulations attributable to that category. It must allow these circulation percentages to be compared across genres and formats so staff can assess usage distribution. The shelf space report should be available for an individual library and for the system, supporting collection-management decisions about how resources are allocated.

> What percentage of total circulations it has (`conversations/conv_pines016_shelf_space.eml`)
> The system should provide, for each genre and format of material, the ability to compare: - The percentage of total circulations (`conversations/conv_pines016_shelf_space.eml`)

### REQ-184 - Report Collection Category Percentages

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must report, for each material genre and format, the percentage of the collection represented by that category. It must support comparison of these collection percentages across genres and formats so staff can evaluate the composition of the collection. This information is needed for assessing whether the distribution of collection materials supports efficient shelf-space use.

> What percentage of the collection it is (`conversations/conv_pines016_shelf_space.eml`)
> The system should provide, for each genre and format of material, the ability to compare: - The percentage of the collection (`conversations/conv_pines016_shelf_space.eml`)

### REQ-185 - Sum Checkouts For Category Share

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must sum checkouts for each genre and format of material. These totals must support calculation of each category's percentage of total circulations within the shelf-space report. The report also concerns the corresponding percentage of the collection and percentage of total shelf space, allowing the circulation measure to be considered alongside those measures.

> Sum checkouts per genre/format (this is the "percentage of circulations") (`conversations/conv_pines016_shelf_space.eml`)

### REQ-186 - Configure In-Transit Threshold Days

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The system must use a configurable number of days as the threshold for identifying items overdue in transit. The threshold must default to seven days while allowing the applicable value to be changed. This setting supports staff who need to identify items that have remained in transit beyond the expected delivery period.

> I need to see what's been in-transit for more than X days (X should be configurable, probably 7 days default). (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-187 - Filter Missing Damaged Reports Dates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The missing and damaged items report must support filtering by a specified date range. Staff need this capability to review recent activity and analyze trends over selected periods. The supported periods must include examples such as the last 30 days and the last quarter.

> The missing/damaged report can include date ranges (e.g., last 30 days, last quarter, etc.) which would be useful for trending. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-188 - Identify Repeated Missing Titles

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The system must support the missing and damaged items report in identifying titles that have been lost repeatedly. This capability is needed for collection decisions, in addition to auditing how many items went missing or were damaged. Staff must be able to use the results to decide whether to obtain different items or move titles to another location. The report therefore must expose repeated loss patterns at the title level.

> Collection decisions - if we keep losing the same titles, maybe we need different copies or to move them to a different location (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-189 - Include Condition Notes In Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The missing and damaged items report must include condition notes for each applicable item. These notes should describe the recorded condition, including examples such as water damage or vandalism. Staff need this information to understand possible root causes and investigate patterns in missing or damaged items.

> Also, can the report include item condition notes? Like "water damage" or "vandalism"? (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-190 - Sort In-Transit By Due Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The system must allow staff to sort the in-transit items report by due date. This sorting is needed so front-line staff can identify and pursue the oldest in-transit items first. The report remains a combined report of items traveling to and from branches, rather than separate transit-to and transit-from reports. It applies to the in-transit items identified by the configurable time condition.

> Also, for the in-transit report - can we sort by due date? Front-line staff need to chase the oldest items first. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-191 - Combine Purge Criteria With AND

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must let staff combine multiple purge criteria using logical conditions such as AND. The criteria must support status-based conditions, time in status, and activity-based conditions such as when an item was last circulated. This is needed to identify precise purge candidates, including items that are damaged and have not circulated for a specified period or items that are missing for a specified period and have not circulated for another specified period. The criteria must remain customizable.

> The system should let us combine criteria. (`conversations/conv_pines021_item_purging.eml`)
> Can we combine these? Like "items with status 'missing' for more than 6 months AND haven't circulated in 2 years"? (`conversations/conv_pines021_item_purging.eml`)

### REQ-192 - Configure Purge Eligibility Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must provide customizable criteria for identifying item records eligible for purging. Staff must be able to use status-based criteria, including missing, discard/weed, and damaged. The system must also support time-based criteria based on how long an item has remained in a status, expressed in months or years. Criteria must additionally support activity-based conditions based on how long it has been since an item was last circulated, and the criteria may be combined.

> I want the customizable criteria for purging to include: (`conversations/conv_pines021_item_purging.eml`)

### REQ-193 - Confirm Purge Deletions Manually

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must require a separate confirmation step before performing deletions identified through a purging workflow. Purge reports must first present candidate records in read-only form, so staff can review the proposed action before deletion. This safeguard is needed to prevent accidental deletion of an entire collection when customizable criteria are used. Actual deletion must therefore occur only after staff provide the required confirmation.

> 2. A separate confirmation step for actual deletions (`conversations/conv_pines021_item_purging.eml`)
> - Separate confirmation step for actual deletions (`conversations/conv_pines021_item_purging.eml`)

### REQ-194 - Delete Orphan Records Fast

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must provide an efficient method for deleting records that have no items attached. It must also provide a quick, effective method for deleting volume entries along with their associated item entries. This capability is needed to support item purging and related record maintenance. The deletion method should be available to staff who need to remove obsolete volume entries, item entries, and records without attached items.

> We also need a quick way to delete volume entries along with copy entries, and delete records with no items attached. (`conversations/conv_pines021_item_purging.eml`)
> - Provide a quick effective method for deleting volume entries along with copy entries, as well as records with no items attached (`conversations/conv_pines021_item_purging.eml`)

### REQ-195 - Delete Volume With Items

**Priority:** Could - Mentioned in 3 documents. Adjusted from Should by model: Quick deletion of volumes with related copies; remove itemless records.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a quick, effective method for deleting volume entries together with their associated item entries. It must also support deleting records that have no attached items. This capability is needed by staff to clean up orphaned records efficiently during collection maintenance. The deletion method must address both volume entries with associated items and records with no items attached.

> We also need a quick way to delete volume entries along with copy entries, and delete records with no items attached. (`conversations/conv_pines021_item_purging.eml`)
> - Provide a quick effective method for deleting volume entries along with copy entries, as well as records with no items attached (`conversations/conv_pines021_item_purging.eml`)

### REQ-196 - Filter Purge By Last Circulation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must allow purge candidates to be identified based on the elapsed time since an item was last circulated. Staff must be able to express this activity-based threshold in days, months, or years. This criterion is needed to identify item records for possible purging according to circulation activity. The activity-based condition must function as part of the customizable purge criteria and may be combined with other criteria.

> - Activity-based criteria (last circulated X days/months/years ago) (`conversations/conv_pines021_item_purging.eml`)

### REQ-197 - Maintain Purge Operation Audit Trail

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must maintain an audit trail for every purge operation. The audit trail must record what was purged, who performed the purge, and when it occurred. This information is needed for accountability and troubleshooting after records are deleted. The requirement applies to purges performed using status-based, time-based, or activity-based criteria, including combined criteria.

> 3. Audit trail for all purges (`conversations/conv_pines021_item_purging.eml`)
> We need to track who purged what and when. This is for accountability and troubleshooting. (`conversations/conv_pines021_item_purging.eml`)

### REQ-198 - Present Purge Candidates Read Only

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must initially present records that meet purge criteria as read-only candidates rather than deleting them directly. This precaution is needed because customizable criteria could otherwise allow someone to accidentally delete an entire collection. Purge reports must allow staff to review the proposed records before any deletion occurs. For a last copy report, the system must flag an item record when it is the only copy within the specified library or system scope.

> 1. Reports show candidates for purging (read-only) (`conversations/conv_pines021_item_purging.eml`)

### REQ-199 - Schedule Automatic Purge Utility

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The purging utility must support scheduled automatic execution without requiring staff to initiate each run manually. Staff need this capability for recurring purge activities that may be performed at a defined time, such as automatically at the end of each year. The schedule applies to execution of the purging utility and should allow the utility to run according to the configured recurring timing. No other scheduling condition is specified.

> Also wondering - can the purging utility be scheduled? Like, run automatically at the end of each year? (`conversations/conv_pines021_item_purging.eml`)

### REQ-200 - Separate Candidate From Deletion

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-04-22  
**Sources:** `conversations/conv_pines021_item_purging.eml`

Reports used to identify purge candidates must be read-only and must not directly modify item, patron, or bibliographic records. Staff need this separation so candidate identification can occur safely before any deletion or other record-changing action. Actual deletions must require a separate confirmation step, rather than being performed by the candidate report itself. The system must therefore keep reporting and destructive actions distinct.

> - Read-only reports for identifying candidates (`conversations/conv_pines021_item_purging.eml`)

### REQ-201 - Filter Deletion Reports By Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must allow staff to filter or aggregate deletion-report results by a selected date range, the staff member who performed the deletion, and record type. This capability is needed so deletion activity can be examined according to the relevant period, deleting account, or kind of record involved. The reporting interface must apply these criteria to deletion data recorded in the audit table.

> We can aggregate by date range, by user, by record type. (`conversations/conv_pines022_deletions.eml`)

### REQ-202 - Identify Top Deleting Staff

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The reporting interface must identify the staff members with the highest numbers of deleted records. Administrative staff need this information to determine which staff members delete the most records. The system should present deletion activity in a way that supports identifying the top deleting staff members within the deletion reports, alongside the requested deletion counts.

> Top users who delete the most records (`conversations/conv_pines022_deletions.eml`)

### REQ-203 - Provide Deletion Audit Query Interface

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must provide an interface that allows authorized staff to query deletion audit data. The interface must support viewing deletions by branch and by the library system, with aggregation by date range, staff member, and record type. It must query the audit table containing deletion details such as record type, record identifier, deleting staff member, deletion timestamp, and location. This reporting capability is needed for auditing records that would otherwise disappear when deleted.

> 3. A report interface to query this audit table (`conversations/conv_pines022_deletions.eml`)

### REQ-204 - Report Deletions By Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must provide deletion reports that group or count deletion activity by branch or other location. Staff must be able to use the reporting interface to review where deletions occurred and compare deletion activity among locations. The reports should also support aggregation by date range, deleting staff member, record type, and system, using the recorded location associated with each deletion.

> The report should show deletions per location and per system. (`conversations/conv_pines022_deletions.eml`)

### REQ-205 - Report Deletions By System

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must provide deletion reports that group or count deletion activity by system. Staff must be able to query the deletion audit data through the reporting interface and review system-level deletion activity. The reports should also support aggregation by date range, deleting staff member, record type, and location, using recorded deletion details such as the record type, record identifier, deleting account, deletion time, and location.

> The report should show deletions per location and per system. (`conversations/conv_pines022_deletions.eml`)

### REQ-206 - Track Denied Deletion Attempts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must track deletion attempts that were denied, in addition to deletion activity that was completed. Library administrators and staff need to review denied attempts for compliance and troubleshooting, including identifying attempts to delete records that should not be deleted. This tracking also supports audits for retention schedules, where libraries may need to demonstrate what records were deleted and when.

> Can we also track attempted deletions that were denied? That would tell us if someone is trying to delete things they shouldn't. (`conversations/conv_pines022_deletions.eml`)

### REQ-207 - Count Check-in Methods Individually

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `survey_results_2009.txt`

The system must count book-drop, terminal, patron-performed, and self-service check-ins both individually and cumulatively. These distinctions are needed so staff can review the separate methods of check-in as well as combined check-in activity. Check-in transactions must also remain available for grouping by hour, terminal, branch, and system.

> All types of check-in counted individually and cumulatively: book-drop, terminal, by user or self-service. (`survey_results_2009.txt`)

### REQ-208 - Count Checkout And Renewal Variants

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `survey_results_2009.txt`

The system must count staff checkouts, self checkouts, staff renewals, self-checkout renewals, online renewals, and OPAC renewals both individually and cumulatively. Staff need these separate and combined counts to analyze checkout and renewal activity in transaction reports. The resulting transaction data must support grouping by hour, terminal, branch, and system.

> All types of check-out counted individually and cumulatively: staff checkout, self checkout, staff renewal, self checkout renewal, online renewal, OPAC renewal. (`survey_results_2009.txt`)

### REQ-209 - Count Holds By Placement Method

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `survey_results_2009.txt`

The system must count holds according to their placement method, distinguishing holds placed at a staff desk, through a public computer, or remotely. This information is needed for transaction reporting that shows holds placed and holds filled. Staff must be able to view these hold counts per patron, per library, per group of libraries, per system, or per county. The system must preserve these reporting scopes when presenting hold-placement counts.

> Holds counted with method of placement: at staff desk, public computer, or remotely. (`survey_results_2009.txt`)

### REQ-210 - Group Transaction Data By Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `survey_results_2009.txt`

The system must support grouping transaction data by branch. This grouping is needed for transaction reports that analyze activity by library location, including check-ins, check-outs, fines collected, and patron registrations. Staff must be able to use branch as a grouping dimension alongside hour, terminal, and system when reviewing transaction activity.

> Transactions can be grouped by hour, terminal, branch, and system. (`survey_results_2009.txt`)

### REQ-211 - Calculate Patron Age Ranges At Query

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must calculate patron age ranges from the birth_date field when producing queries or reports. The calculation must occur at query time because age range is derived from birth_date rather than stored directly as an age range. The system must create age brackets in the query and support configurable age ranges per report. The resulting age range must be usable with filters and grouping, including combinations using AND or OR logic.

> The "age range" is calculated from the birth_date field, which means we need to compute it at query time. (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-212 - Configure Patron Age Brackets

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow staff to configure the age ranges used to group or filter patrons in reports. This is needed because different reports may require different age brackets, such as 0-5, 6-10, and 11-15 or 0-6, 7-12, and 13-17. Configured age ranges must be usable for both limiting report results and grouping report results.

> The age ranges need to be configurable too. Like, 0-5, 6-10, 11-15, etc. Or 0-6, 7-12, 13-17, 18-24, 25-34... Whatever makes sense for the report. (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-213 - Filter Patrons By Checkout Inactivity

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow patron reports to be filtered by checkout activity over a specified period. Staff must be able to identify patrons who have not checked out materials within six months. Checkout-activity filters must be usable with other patron-report filters, such as patron type and zip code, when defining the requested group.

> Can we combine demographic filters? Like "show me all Juvenile patrons in zip code 30505 who haven't checked anything out in 6 months"? (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-214 - Generate Patron Demographic Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must generate reports on patrons using age range, zip code, county of residence, home branch, patron type, and preferred language as reporting characteristics. Staff need these reports to examine patron groups by demographic and account-related attributes. The system must support each listed characteristic as a basis for reporting.

> I need to run reports on patrons grouped by characteristics. The fields I need: - Age range - Zip code - County of residence - Home branch - Patron type - Preferred language (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-215 - Group Patron Results With Metrics

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must group report results by patron characteristics, including age range, zip code, county of residence, home branch, patron type, and preferred language. Grouped results must support measures such as circulation, checkout counts, and patron counts. Staff need this capability for program planning, including examining activity or population totals for defined patron groups.

> Can we also GROUP BY these fields? Like, show me circulation by age range, or patron count by home branch? (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-216 - Configure Report Specific Age Ranges

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow each report to configure its own age brackets or age ranges. Reports must support limiting or grouping patron results by age range and other patron characteristics, including zip code, county of residence, home branch, patron type, and preferred language. Filters must support AND/OR combinations, and null values must be included in results.

> Age ranges should be configurable per report (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-217 - Group Patron Results By Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow staff to group query and report results according to patron characteristics. Supported grouping fields must include age range, zip code, county of residence, home branch, patron type, and preferred language. Grouping is needed for reporting and analysis of patron results, while filters may be combined using AND or OR logic when limiting those results. Null values must be included, and age ranges must be configurable per report.

> Key points: - Both LIMIT (filter) and GROUP BY (aggregate) should be supported (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-218 - Group Patrons By Home Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow staff to group patron results by home branch in queries and reports. This capability is needed for program planning, such as examining patrons in a specified age range and zip code while comparing results across branches. The grouping must present patron counts or circulation results by home branch when those patron characteristics are used in reporting. The system should support this grouping as part of the report criteria selected for the planning activity.

> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Home branch (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-219 - Group Patrons By Patron Type

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow staff to group patron results by patron type in queries and reports. This capability supports reporting on patron characteristics for planning and analysis. Patron type must be available as a grouping field alongside age range, zip code, county of residence, home branch, and preferred language. Grouping results must include null values, and reports must continue to support configurable age ranges when age range is also used.

> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Patron type (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-220 - Group Patrons By Preferred Language

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow staff to group patron results by preferred language in queries and reports. This capability supports reporting and planning based on patron characteristics. Preferred language must be available as a grouping field alongside age range, zip code, county of residence, home branch, and patron type. Grouping results must include null values, and reports must continue to support configurable age ranges when age range is also used.

> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Preferred language (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-221 - Limit Patron Results By Filters

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow staff to limit query and report results according to patron characteristics. Supported characteristics must include age range, zip code, county of residence, home branch, patron type, and preferred language. Filters must be combinable using AND or OR logic, and null values must be included in results. Age ranges must be configurable for each report, while the system also supports grouping as a separate reporting operation.

> Key points: - Both LIMIT (filter) and GROUP BY (aggregate) should be supported (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-222 - Cache Inactivity Report Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must cache inactive-patron report results after generating them. Caching is required to reduce the performance impact of repeatedly querying the patron population and combining activity information from different tables. This is particularly necessary because the report query could be slow for approximately 3.5 million patrons. Cached results should support the background-report approach required for large populations.

> One performance note: for 3.5 million patrons, this query could be slow. We should run it as a background report and cache results. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-223 - Combine Electronic Activity Histories

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must consider OPAC logins, online hold placements, and online renewals as electronic activity when determining whether a patron is inactive. It must also consider digital resource access when that access is logged. These activity types are recorded in different tables, so the inactivity determination must combine the relevant activity information. The combined activity history must be used to identify the patron’s most recent activity.

> For "electronic activity," we track: - OPAC login events - Online hold placements - Online renewals - Digital resource access (if logged) (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-224 - Count Electronic Activity Inactivity

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must count electronic activity when determining whether a patron is inactive. Electronic activity must include logging into the OPAC or patron account, placing holds online, and renewing items online. Access to integrated digital collections must also count as electronic activity when such collections are integrated.

> "Electronic activity" should include: 1. Logging into OPAC/patron account 2. Placing holds online 3. Renewing items online 4. Accessing digital collections (if integrated) (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-225 - Exclude Selected Patron Types

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must allow staff to exclude selected patrons from the inactive-patron report. Exclusion options must include patrons marked do not disturb, VIP patrons, staff members, and patrons who have opted out of communications. This capability is needed when the inactive-patron list is prepared for outreach or other handling, so specified patron types are not included.

> One more thing - we should be able to EXCLUDE certain patrons from the inactive report. For example: - Patrons with "do not disturb" flags - VIP patrons - Staff members - Patrons who have opted out of communications (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-226 - Generate Inactive Patron Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must generate inactive-patron results for patrons with no circulation or electronic activity during a configurable period. Staff must be able to produce or group these results at the system, home-library, and county levels. The system must also support additional organizational levels as needed. The configurable levels are needed to support different views of inactive patrons and related follow-up activities.

> The list should be configurable to different levels - System, Home Library, County, etc. (`conversations/conv_pines024_inactive_patrons.eml`)
> The list should be configurable to: - System - Home Library - County - (Other levels as needed) (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-227 - Include Patron Mailing Address

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The inactive-patron report must include each patron’s current mailing address. Staff need these addresses to conduct outreach to patrons who have not visited recently. The address information must support mailing postcards intended to re-engage inactive patrons.

> We mail postcards to inactive patrons, so the report needs to include current mailing addresses. (`conversations/conv_pines024_inactive_patrons.eml`)
> Include current mailing addresses for outreach (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-228 - Provide Inactive Totals By Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

At the system level, the report must provide inactive-patron totals by branch. Staff need this comparison to identify which branches have the most inactive patrons and to direct database-cleanup work. At the home-library level, the results must support assigning cleanup tasks to specific branches.

> At the system level, I can see which branches have the most inactive patrons. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-229 - Run Inactivity Reports Background

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must run inactive-patron reports as background processes rather than requiring the report query to remain in the foreground. This is needed because determining inactivity requires a combined query across different activity tables and may be slow for large patron populations. Running the report in the background must keep the system usable while the report is generated. The requirement specifically addresses a population of approximately 3.5 million patrons.

> We should run it as a background report and cache results. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-230 - Separate Inactive With Fines

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must identify inactive patrons with outstanding fines separately from other inactive patrons. This separation is required because accounts with outstanding fines need different handling. Inactive results must continue to use the configured inactivity period and electronic-activity criteria when determining which patrons belong in the separate category.

> And yes, we should track inactive patrons who still owe fines separately. Those accounts need different handling. (`conversations/conv_pines024_inactive_patrons.eml`)
> Track inactive patrons with outstanding fines separately (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-231 - Support Configurable Inactivity Days

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-06  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must generate an inactive-patrons report listing patrons with no circulation or electronic activity during a configurable number of days. Electronic activity must include OPAC login, online hold placement, and online renewals. The report must support grouping by home library so staff can view inactive-patron totals for each branch and identify branches with the most inactive patrons, and it must provide current mailing addresses for outreach. The system must separately track patrons with outstanding fines, permit exclusion of specified patron types, support CSV export, and use background processing for performance.

> The list should be configurable to: - System - Home Library - County - (Other levels as needed) (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-232 - Display Last Item Edit Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_cataloging_2009-05-08.txt`

The system must display the last item edit date in reports. The displayed date must be the date of the most recent edit to the item and must exclude circulation activity. This information is needed by cataloging staff because the current system combines item-edit and last-circulation dates. Reports must therefore distinguish item editing from circulation when presenting the last edit date.

> I need to be able to see the last edit date on reports, but it should be only when the item is edited and not include the last circulation. The current system combines these dates. (`interview_cataloging_2009-05-08.txt`)

### REQ-233 - Enable Search In HTML Help

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`

The system must allow staff to search the HTML help content. Searchable help is needed so staff can find information about system tasks, including how to run reports, without routinely calling IT. The search capability applies to the online help and must support the requirement that the help be easy to navigate.

> The HTML help needs to be searchable and easy to navigate. (`interview_sysadmin_2009-05-10.txt`)

### REQ-234 - Organize Hierarchical Online Help

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`

The help system must organize its content in a hierarchical structure. Online hierarchical help is needed so staff can find information about running reports without routinely calling IT. The help must also be easy to navigate, and the source identifies cross-linking and searchability as related requirements for accessing its content.

> Also, the help system needs to be online, hierarchical, and cross-linked. (`interview_sysadmin_2009-05-10.txt`)

### REQ-235 - Provide Separate Searchable Help System

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`

The system must provide an online HTML help system that is searchable and easy for staff to navigate. It should organize help hierarchically and provide cross-links so staff can find instructions for running reports without contacting IT for every question. The help system must remain separate from the OPAC so reporting activity and related support functions do not constrain patrons’ fast, responsive access to the catalog.

> The HTML help needs to be searchable and easy to navigate. (`interview_sysadmin_2009-05-10.txt`)

### REQ-236 - Report Bibliographics With No Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_cataloging_2009-05-08.txt`

The system must provide data quality reports that identify bibliographic records with no associated item records. These reports are needed to help maintain data integrity and to identify incomplete relationships between bibliographic records and items. The capability supports cataloging staff who need to review data quality issues. The report must specifically include bibliographic records that have no item records.

> Data quality reports - items with invalid item type, items with long call numbers, bibliographic records with no item records. (`interview_cataloging_2009-05-08.txt`)

### REQ-237 - Auto Return Temporary Event Transfers

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must automatically return temporarily transferred items to their original location when a configured period or specified criterion is met. Reversion may be based on a set period of time or another defined condition, including the end of the associated event or program. This supports temporary outreach or program transfers while preventing items from remaining at the temporary location indefinitely. The system must preserve the original location so it can restore the items when the applicable condition occurs.

> Ability to revert items to original location after a set period of time and/or based on other criteria (`conversations/conv_pines018_item_transfer.eml`)
> Like, move 20 biographies to the community center for their genealogy workshop, then revert them after the event. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-238 - Auto Revert Transfers By Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must automatically revert transferred items to their original location when configured criteria are met. Criteria must support a set period of time and status-based or other specified conditions, such as an item changing to sold at a book sale. This capability is needed for temporary transfers, including items sent to a book sale for a defined period, and should allow the configured reversion condition to determine when the item returns.

> Can we also revert "based on other criteria"? Like, if the item's status changes to "sold" at the book sale, automatically revert it? (`conversations/conv_pines018_item_transfer.eml`)

### REQ-239 - Confirm Transfer With Item Preview

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must display a preview before applying an item transfer, identifying the number of items and the source and destination locations. It must request confirmation before making the changes. Transfer execution must be limited to authorized staff roles, including managers, administrators, or transfer coordinators, because not every staff member should be permitted to move items between branches. The preview supports careful review of the proposed transfer before it is applied.

> Also, the utility should show a preview before making changes. "If you run this now, 25 items will be moved from Dalton-Whitman to Mobile Library Unit 3. Confirm?" (`conversations/conv_pines018_item_transfer.eml`)

### REQ-240 - Generate Printable Transit Labels

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The transfer utility must generate printable transit labels for items being transferred. Each label must contain the barcode for the item so staff can identify the item while it is in transit. This capability is needed when items are moved between branches or other transfer locations. The labels must be printable for use with the transferred items.

> - Printable transit labels (`conversations/conv_pines018_item_transfer.eml`)
> Also, can we generate transit labels? Like, printable barcodes for the items being transferred? (`conversations/conv_pines018_item_transfer.eml`)

### REQ-241 - Log Item Transfers For Audit

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must log all item transfers so that transfer activity can be audited. The log must record transfers performed as part of item movement between branches and support review of the activity after transfers occur. This requirement applies alongside the transfer utility’s other operations, including scheduled auto-reversion based on time or status criteria, so that transfer activity remains traceable for audit purposes.

> 6. Logging - track all transfers for audit purposes. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-242 - Notify Users Transfer Delays Issues

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must notify designated users when an item transfer is delayed or encounters an issue. This notification is needed so staff can respond to transfer problems and monitor items moving between branches. The system must make these alerts available for the transfer situations that require attention.

> If an item transfer is delayed or has issues, notify me. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-243 - Prevent Reversion When CheckedOut

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must prevent an item from automatically reverting to its original location when the item is checked out at the destination. This is needed for temporary transfers to a mobile library, where an item that is checked out there must remain at that destination. Items that remain unused may still be eligible for automatic reversion under configured criteria, such as a date-based period or another event-based condition. The checked-out condition must therefore take precedence over automatic reversion.

> We send items to a mobile library, and when they're checked out there, they should stay. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-244 - Process Large Transfers Efficiently

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must process large transfer operations efficiently, using smaller batches when necessary to avoid locking the database. This requirement is needed because transfer operations may involve 9.6 million items, making inefficient batch updates a concern. The utility must therefore divide processing into smaller batches as appropriate while carrying out transfer-related updates. This constraint applies to large-scale operations and is intended to reduce database locking during processing.

> One concern: with 9.6 million items, batch updates need to be efficient. We should process in smaller batches to avoid locking the database. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-245 - Retain Item Transfer History

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must retain and expose the transfer history for each item. The history must support reporting the number of times an item has been transferred during a relevant period, such as identifying repeated transfers within the past year. Staff need this information to identify items that may be located incorrectly or whose movement indicates a problem. The transfer history must therefore be available for review as part of managing item locations.

> Can we track transfer history? Like, "this item has been transferred 5 times in the past year." (`conversations/conv_pines018_item_transfer.eml`)

### REQ-246 - Share Saved Candidate Queries

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The utility must allow saved queries to be shared with other users. This capability is needed so that queries for selecting transfer candidates can be made available beyond the person who created them. Query sharing should follow the same general approach as sharing report templates. The shared queries must support the utility’s candidate-selection process for items being considered for transfer.

> 2. Save/share queries - similar to report templates. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-247 - Support Event Temporary Transfers

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must support transferring items to temporary locations for specific events or programs. This capability is needed for outreach activities, such as sending items to a community center for a genealogy workshop. Staff must be able to place items at the temporary location for the associated event or program and later return them to their original location. The temporary transfer applies to items used for the defined event or program rather than establishing a permanent location change.

> Can we transfer items to a temporary location for a specific event or program? (`conversations/conv_pines018_item_transfer.eml`)

### REQ-248 - Undo Item Transfers After Confirmation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must provide an undo function that reverses an item transfer after an accidental or incorrect action. This capability is needed when a staff member selects the wrong action or confirms an unintended transfer. Undo must reverse the transfer rather than merely display its details, so the affected items can be returned from the incorrect destination to their prior location.

> And we need an undo function! What if someone clicks the wrong button? (`conversations/conv_pines018_item_transfer.eml`)

### REQ-249 - Check Report Cancellation Signals

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The report-processing component must check for cancellation signals while processing a report. This condition is required so that cancellation requests can take effect for scheduled or running reports. The cancellation capability applies to reports that are being processed, and the processing component must perform the checks during processing rather than only before a report starts.

> The ability to cancel a scheduled or running report is technically feasible, but requires the system to check for cancellation signals during report processing. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-250 - Handle Optional Vendor Integration Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must handle vendor integration data when such data is provided. This includes data supplied through vendor websites, published APIs, or automated transfers of standard-format data files, including EDI ordering data. The system must not require vendor integration data to be present at every library, because some libraries may not receive or maintain that data.

> The reporting system needs to handle this data, but we can't rely on it being present at every library. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-251 - Provide Current Data Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must support reports that provide current data at the time of the request. This capability is needed for operational questions such as identifying what is overdue today. Staff and other reporting users must be able to obtain current information rather than only historical results, while reports that retrieve data from a specified past date are addressed separately as historical reporting.

> "Some reports need to be real-time - like 'what's overdue today,'" Robert said. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-252 - Provide Global Admin Full Access

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a Global Admin role with full system access. It must support security groups or roles that control access for individuals, workgroups, and arbitrary staff groups. The system should make permission changes easy by allowing staff access to be changed through role assignment. This role provides the highest level of access among the defined roles and is distinct from branch-level administration, report execution, and indirect patron access.

> - Global Admin: Full system access (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-253 - Provide Historical Date Reporting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must support reports that retrieve data as it existed on a specified historical date. This capability is needed for questions such as determining what the bill amount was on June 30th, rather than reporting only the current amount. The system will probably need a reporting warehouse for historical data so that staff and other reporting users can access the required past state.

> "Others are historical - 'what was the bill amount on June 30th?' We probably need a reporting warehouse for historical data." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-254 - Provide Library Manager Role

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a Library Manager role that allows library managers to run approved reports. The role must also permit limited modification of report templates, rather than unrestricted template changes or full system access. Role-based access control must support assigning this role to individuals, workgroups, or arbitrary staff groups. The system should make permissions easy to change by changing the assigned role.

> - Library Manager: Run approved reports, limited template modification (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-255 - Provide Staff Role For Report Runs

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a Staff role that allows staff to run reports within their assigned permissions. Report access must therefore be controlled through security groups or roles assigned to individuals, workgroups, or arbitrary staff groups. The system should make it easy to change a staff member’s permissions by changing the role assignment. Staff access is limited by the permissions assigned to the role and does not imply full system access.

> - Staff: Run reports within assigned permissions (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-256 - Provide Training With Data Migration

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a training environment in which staff can experiment without risking production data. It must keep development, training, and production environments distinct and support migration of configurations between them through export and import. This migration must include templates, permission settings, and saved queries, so configurations can be transferred while production data remains protected. The safeguard is needed when staff test or change reporting configurations in training rather than production.

> And the training environment needs to be safe - staff should be able to experiment without risking production data. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-257 - Query OPAC Data Read Only

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must query data from the OPAC without modifying that data. Patrons create holds and circulation transactions through the OPAC, and the reporting system must use those data for reporting while preserving the OPAC’s operational records. This read-only condition applies to OPAC data accessed by the management processes, regardless of whether EDI ordering data is available at every library.

> The reporting system queries this data, but doesn't modify it. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-258 - Read From Library Automation System

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must read data from the enterprise Library Automation System for its management processes. It must rely on the Library Automation System data structures and functionality, including those associated with Acquisitions and Cataloging. The reporting system must not manage acquisitions or cataloging functions; it is limited to reading the data.

> All our data comes from the ILS," Robert said. "The reporting system doesn't manage acquisitions or cataloging - it just reads the data. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-259 - Read OPAC Holds And Circulation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The management processes must interact with the patron-facing OPAC to access data associated with patron holds and circulation transactions. Patrons create holds and circulation transactions through the OPAC, so the reporting system must be able to query that data. The system must not modify the holds or circulation transaction data through the OPAC integration.

> DE-3: Management Processes interact with a patron interface (OPAC). (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-260 - Accrue Fines And Charges Reporting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must provide financial reports of fines and charges accrued during selectable time periods, including the last 12 months, year to date, and the last month. Reports must categorize accrued amounts by charge type, such as overdue fines, damaged item charges, and lost item charges. Staff need this information to review financial activity for the applicable period and charge category. The system must support reporting these accrued fines and charges as part of the library’s financial reporting.

> Fines and charges accrued per time period (last 12 months, YTD, last month) (`email_financial_reports.eml`)
> Fines and charges accrued per time period (last 12 months, YTD, last month) and per type of charge (overdue fines, damaged item charges, lost item charges, etc.) (`email_financial_reports.eml`)

### REQ-261 - Enforce Financial Data Retention

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must enforce applicable financial-data retention policies for data archiving. Retention must comply with state and local requirements and with auditing requirements. Financial data required for audit purposes must be retained for seven years. The system must apply these policies to ensure that required financial information remains available for compliance and audit needs.

> Some data needs to be retained for 7 years for audit purposes. The system needs to enforce retention policies. (`email_financial_reports.eml`)

### REQ-262 - Generate Item Value Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must generate reports of item values using value data from item records, such as purchase-price or equivalent data. Staff must be able to report the value of the entire collection or a user-defined portion of it. The portion must support criteria such as a specified item status or a specified collection, including longoverdue items and DVDs in the children's collection.

> Value of items report - staff should be able to get the value of items based on data in item records. This could be the entire collection, or a portion. (`email_financial_reports.eml`)
> System can generate a report of the value of items (based on data in item record) in the entire collection or a portion. (`email_financial_reports.eml`)

### REQ-263 - Join Financial Patron And Item Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must support joining financial data associated with patron records and item records when generating financial reports. This is required because fines, charges, waivers, and other financial information may be attached to both patron and item records. Staff need combined financial queries to produce reports using information from these data sources. The system should also support querying patron accounts with balances greater than a specified dollar amount so staff can identify accounts that need attention.

> The financial data is attached to patron records AND item records. So when we query for financial reports, we need to be able to join these data sources. (`email_financial_reports.eml`)

### REQ-264 - Provide Patron Account Balance Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must provide financial reports of patron account balances. These reports must support grouping or filtering by patron, the patron's home library, and the overall library system. The capability is needed for financial reporting by staff and must distinguish account-balance reporting from related reports on fines, charges, waived fines, and payments.

> Patron account balances by patron, home library, and system (`email_financial_reports.eml`)

### REQ-265 - Report Payments By Channel And Type

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must report payments made during selectable time periods and categorize them by payment channel. Supported payment channels must include the staff desk, self-check, and OPAC. Reports must also categorize payments by payment type, including cash, credit card, and check. Staff need these reports to review payment activity and support daily reconciliation of financial transactions.

> Payments made per time period and per payment method (staff desk, self-check, OPAC) (`email_financial_reports.eml`)
> Payments made per time period and per payment method (staff desk, self-check station, OPAC) (`email_financial_reports.eml`)

### REQ-266 - Track Waived Fines By Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must track waived fines by branch so that each branch’s waived-fine budget can be managed separately. It must report waived fines for specified time periods and identify the branch associated with each reported amount. Staff need this information to monitor waived-fine activity and manage branch budgets. The system must preserve the per-branch distinction in financial reports rather than combining all waived fines into one total.

> Fines waived should be tracked per library because each library has its own budget for waived fines. (`email_financial_reports.eml`)
> Fines waived per time period and per branch (`email_financial_reports.eml`)

### REQ-267 - Update Financial Information Easily

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-14  
**Sources:** `email_financial_reports.eml`

The system must allow staff to update financial information easily. This includes financial information associated with patron and item records, including fines, charges, waivers, and ecommerce transactions. The system must reflect front-desk patron payments immediately after they are made. These capabilities are needed to keep patron financial information current and to support staff queries of patron accounts with balances greater than a specified dollar amount.

> Financial information can be updated easily. (`email_financial_reports.eml`)

### REQ-268 - Control Access By Roles

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must control access according to assigned roles and permissions. Access control must support individuals, workgroups, and arbitrary staff groups through security groups and/or roles. The system should distinguish access such as full system access, branch-level reporting and configuration, approved report execution, and report access within assigned permissions, as applicable to the assigned role.

> - User permissions and role-based access (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-269 - Provide Collection Weeding Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports that support library collection weeding activities. Weeding reports are frequently used, indicating an ongoing need for them in collection management. The reports should therefore be available to support the staff activities involved in weeding the library collection.

> - Weeding reports are frequently used (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-270 - Provide Data Quality Assessment Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports for identifying and assessing data quality issues. Data quality reports are needed as part of the library’s reporting needs, allowing staff to review the quality of reported data. The system should make these reports available when data quality assessment is required.

> - Data quality reports are needed (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-271 - Provide Director-Level Financial Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide financial reporting suitable for director-level needs. Financial report requirements are understood at the director level, indicating that directors need access to financial information through the reporting function. The system should therefore make financial reports available for director-level reporting activities.

> - Financial report needs are understood at the director level (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-272 - Provide Inventory Tracking Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports for tracking library inventory. It should also support inventory and capacity reporting, since these reports are used daily by branch managers. The reporting capability is needed to support branch-level monitoring of library resources. The system should support comparison reports across branches, reflecting the identified need to compare inventory-related conditions between locations.

> - Inventory and capacity reports are used daily (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-273 - Provide Library Capacity Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports showing library capacity. Capacity reports are used daily, so branch managers need reliable access to them for recurring library reporting. The system should also support comparisons across branches, because cross-branch comparison reports are needed.

> - Inventory and capacity reports are used daily (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-274 - Provide Predefined Board Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide predefined reports for boards and executive audiences. Board and executive reports need to be predefined so that these audiences can receive established reporting outputs. The predefined reports should support the reporting needs identified for board and executive use.

> - Board/executive reports need to be pre-defined (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-275 - Provide Shelf Space Utilization

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports showing shelf space utilization. Shelf space utilization reports are important to branch managers and are needed for branch-level reporting. The system should make these reports available to support assessment of how shelf space is being used at a branch.

> - Shelf space utilization reports are important (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-276 - Provide Web Or Windows Client Access

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The management processes must be accessible through a web browser or a client compatible with Microsoft Windows. This access must accommodate libraries that prefer browser-based use without client installation and libraries that prefer a dedicated client for better performance. The requirement applies to access to the management processes regardless of which supported access method a library selects.

> Management Processes shall be accessible through a web-browser or a Windows-compatible client. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-277 - Support Demographic Program Planning Analysis

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must support demographic analysis to provide information needed for program planning. Staff, including branch managers, need this analysis when designing or evaluating library programs. The reporting capability must make demographic information available for that planning purpose without extending beyond the stated program-planning need.

> - Demographic analysis for program planning (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-278 - Support Internet Explorer And Firefox

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

When the management processes are accessed through a web browser, the system must support Microsoft Internet Explorer version 6.0 or later and Mozilla Firefox version 2.0 or later. Supporting both browsers is required because different libraries standardize on different browsers. The browser requirement applies only to web-browser-based access, not to use through a Windows-compatible client.

> If web-browser based, Management Processes shall be accessible through Microsoft Internet Explorer (v.6.0 and later) and Mozilla Firefox (v.2.0 and later). (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-279 - Support Linux Or Solaris Processing

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The management processes must operate on either a Linux server or a Solaris server. Both server operating systems are acceptable because library installations may use either platform. Report processing must support background processing or queuing so that report generation during peak hours does not slow down the circulation client.

> Management Processes shall operate on a Linux or Solaris server. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-280 - Clone Report Template Variants

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must allow staff with appropriate permissions to clone an existing report template and create a new report variant from it. Cloning must not modify the original template, because the original must remain available with its existing criteria for consistent reporting. The new variant must be distinct from modifying the existing template. Report permissions should be easy to administer through roles, so permission changes update automatically when a staff member’s role changes.

> We also need the ability to "clone" reports - take an existing template and create a new one based on it. This is different from modifying the template - it's creating a new variant. (`email_report_features.eml`)

### REQ-281 - Display Report Submission Timestamp

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must display when a report was submitted. This information must be available to staff who submit reports so they can determine when the report entered processing and understand its position in relation to other queued reports. Submission time is needed as part of queue visibility because staff require confirmation and progress information after requesting a report. The system must provide this information along with the report’s queue and processing details.

> - When their report was submitted (`email_report_features.eml`)

### REQ-282 - Indicate Report Processing Status

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must display the processing status of a report to staff. The status must indicate whether the report is waiting, running, completed, or failed. This capability is needed so staff are not left without feedback after submitting a report and can determine whether processing has started, finished successfully, or encountered a failure. Status visibility is part of the required information for monitoring queued reports.

> - Status (waiting, running, completed, failed) (`email_report_features.eml`)

### REQ-283 - Maintain Named Report Consistency

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must maintain consistent criteria for staff running the same named report template. When the same report is requested, the template must ensure that staff run the same report with the same criteria and produce consistent reports. The system should also support creating a new report variant by cloning an existing template, rather than modifying the original template.

> We want to make sure that when the director asks for "the weeding report," everyone runs the same report with the same criteria. Templates ensure this. (`email_report_features.eml`)

### REQ-284 - Preserve Report Template Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must preserve the correctness and intended results of a report when staff modify a report template. Templates must be available for staff to run as-is or modify for individual needs without changes compromising the report results. Administrators must be able to limit which filters and display fields can be altered, supporting dependable output.

> Changes shouldn't compromise results. (`email_report_features.eml`)

### REQ-285 - Provide Regex Dropdown Selection

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must provide regular expressions through a dropdown selection mechanism in the query interface. Staff must be able to use the selected regular expressions when designing queries against all record types. This capability is needed as part of a user-friendly query tool that also supports selecting fields and values from picklists.

> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)

### REQ-286 - Restrict Template Filter And Fields

**Priority:** Could - Mentioned in 2 documents. Adjusted from Should by model: Restricting template modifications improves governance; not core.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must allow administrators to restrict which report-template filters and display fields staff may alter. Templates must remain available to staff for execution as-is or modification for individual needs. These controls are needed to ensure that staff changes do not compromise the accuracy of report results and to certify dependable output. The restriction must apply to both filters and display fields that administrators designate as non-alterable.

> Administrators should be able to limit which filters and display fields can be altered, to certify a dependable output. (`early_draft_srs_galecia.txt`)
> Admins should be able to limit which filters and display fields can be altered. (`email_report_features.eml`)

### REQ-287 - Retain Transactions Per State Law

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must retain transaction data for the number of years required by state law. This transaction archive is needed for compliance with the applicable retention requirement. The system must also protect patron privacy by not retaining personally identifiable information in the archived transaction data. The retention period is therefore determined by state law, while the archive must comply with the stated privacy limitation.

> State law requires us to retain transaction data for X years, but patron privacy means we can't keep personally identifiable information. (`email_report_features.eml`)

### REQ-288 - Support Boolean Query Operators

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must support Boolean operators for combining query conditions in the query interface. Staff must be able to use these operators when designing queries against all record types. This capability is required as part of a user-friendly query tool that also provides field selection, picklists, and regular-expression support, with access controlled by administrators.

> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)
> QUERY TOOL: User-friendly interface for designing queries against all record types. Boolean operators, picklists, regex support. Admin controls access. (`email_report_features.eml`)

### REQ-289 - Update Report Permissions On Role

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must automatically update a staff member’s report permissions when the staff member’s role changes. For example, changing a staff member’s role from Staff to Manager must cause the associated report permissions to update without separate manual administration. This capability is needed to make fine-grained report permissions easy to administer and to control who can create, clone, or run reports according to role-based access.

> If I change someone from "Staff" to "Manager," their report permissions should update automatically based on the role. (`email_report_features.eml`)

### REQ-290 - Clone Existing Report Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

The system must allow users to clone existing report templates. This capability is needed because administrators create templates for staff, who may run them as-is or modify them within the permitted limits. Cloning should provide a way to create a report template based on an existing template while preserving the ability to manage access through the system’s report permissions.

> REPORT TEMPLATES: Admins create templates available to staff. Run as-is or modified. Limit alterable filters/fields. Clone capability. (`email_report_features.eml`)

### REQ-291 - Provide Query Designer Picklists

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

The system must provide picklists in the query designer so users can select query values or criteria without having to enter every value manually. This capability is needed as part of a user-friendly interface for designing queries against all record types. The system should allow administrators to control access to the query tool and its picklist-based query functions.

> QUERY TOOL: User-friendly interface for designing queries against all record types. Boolean operators, picklists, regex support. Admin controls access. (`email_report_features.eml`)

### REQ-292 - Allow Admin Manage Report Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow system administrators to create report templates that are available to staff. These templates are needed to provide dependable, shared reporting tools for staff with individual reporting needs. Administrators should be able to limit which filters and display fields staff can alter so that certified output remains dependable. The system must preserve the accuracy of results when templates are made available for staff use.

> System administrators should be able to create report templates that are available to staff. (`early_draft_srs_galecia.txt`)

### REQ-293 - Allow Admin Run System Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow Local System Administrators to run system reports. This capability is needed because these administrators oversee library processes and have elevated permissions within the system. Local System Administrators are typically library managers, who use reports for planning and evaluation while supervising organizational units and providing input to the design and implementation of library services.

> They can configure local settings and run system reports. (`early_draft_srs_galecia.txt`)

### REQ-294 - Allow Canned Display Editing

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow authorized users to edit canned reports for display purposes. Editing must support adding fields such as shelving location to the report display. This capability is needed when staff require canned reports to present additional item information, while remaining limited to display customization of the canned report.

> Ability to edit canned report for display purposes such as adding shelving location as a display (`early_draft_srs_galecia.txt`)

### REQ-295 - Allow Local System Admin Configuration

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow Local System Administrators to configure local settings. This capability is needed because these administrators oversee library processes and have elevated permissions within the system. Local System Administrators are typically library managers, who supervise organizational units and provide input to the design and implementation of library services.

> They can configure local settings and run system reports. (`early_draft_srs_galecia.txt`)

### REQ-296 - Allow Staff Report Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow staff to create reusable report templates. Templates are needed in the reports interface so that report definitions can be created once and reused for later reporting needs. The system should support these templates as a distinct reporting capability alongside saved and reusable queries, while access to creating or running reports may be controlled through permissions.

> Ability to create report templates: 81% (`survey_results_2009.txt`)

### REQ-297 - Annual Report Holds Placed Count

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide an annual report showing the number of holds placed. Staff need this report as part of the holds reporting functions used to review hold activity. The report must present the annual total rather than the other listed holds measures, such as items sent for holds, items received for holds, unfilled holds, or stale holds.

> - Annual # of holds placed (`early_draft_srs_galecia.txt`)

### REQ-298 - Breakdown Circulation Counts By Type

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must retrieve total circulation counts and present a breakdown by circulation type. The breakdown must include checkouts, renewals, and noncataloged transactions. This capability is needed when staff require circulation reporting that distinguishes the types of transactions contributing to the total count. The system should provide these results as part of report retrieval without limiting the count to a single circulation type.

> Ability to retrieve total circ including checkouts, renewals, and noncats with a breakdown displaying those circ types (`early_draft_srs_galecia.txt`)

### REQ-299 - Cataloged And Uncataloged Merge

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a total circulation report that merges cataloged and non-cataloged circulation data. The report must present a combined circulation count for staff who need an overall measure of circulation across both data types. The total circulation count must include checkouts, renewals, and non-cataloged circulation, consistent with the stated total circulation definition. This report is needed when staff require one circulation total rather than separate cataloged and non-cataloged counts.

> - Total Circulation Count (Merging both Cat and Non-Cat circulation data) (`early_draft_srs_galecia.txt`)

### REQ-300 - Combined Total Circulation Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a total circulation count combining check-outs, renewals, and circulation involving non-cataloged material. The total must merge cataloged and non-cataloged circulation data so that circulation statistics represent all listed activity rather than check-outs alone. This report is needed when staff require an overall circulation measure while retaining the separate checkout, renewal, and non-cataloged counts available in the circulation reports.

> - Circulation Count - total circ including checkouts, renewals, and noncats (`early_draft_srs_galecia.txt`)

### REQ-301 - Compare Period Values And Percentages

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must present report results with separate columns for current-period values, prior-period values, percentage differences, and corresponding prior-year values and comparisons. It must support comparisons such as last month’s circulation, the previous month’s circulation, the percentage difference, the previous year’s month, and the percentage difference between the last month and the prior-year month. This capability is needed by report users who need to compare circulation results across periods.

> Ability to determine the output results in a way such that a result could have one column for last month's circs, another for previous month's circ, a percent difference column, previous year's month column, a percent difference from last month to last year's month column (`early_draft_srs_galecia.txt`)

### REQ-302 - Control Display Field Alteration

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow administrators to control which display fields staff are permitted to alter in report templates. Staff must be able to use templates as-is or modify them for individual needs only within the display-field limits established by administrators. This control is needed to prevent template changes from compromising the accuracy of results and to support dependable output. The system must apply the restriction to display fields specifically designated by administrators.

> Administrators should be able to limit which filters and display fields can be altered, to certify a dependable output. (`early_draft_srs_galecia.txt`)

### REQ-303 - Control Fine Grained Report Permissions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The reporting interface must provide fine-grained permissions that control which staff can create or run particular reports or queries. This capability is needed when different staff require different rights over report creation and execution. Permissions must apply to both creating and running reports or queries, rather than providing only general access to the reporting interface.

> Fine-grained permissions (who can create/run what): 76% (`survey_results_2009.txt`)

### REQ-304 - Control Fine Grained Template Permissions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide fine-grained permission management and report template management. These capabilities are needed because existing reporting capabilities have significant gaps in several areas of the management processes reporting system. Permission management must support fine-grained control, and template management must support the administration of report templates. The requirement concerns the reporting system used to support management processes within management processes.

> Implement fine-grained permissions and template management (`evergreen_reference_2009.txt`)

### REQ-305 - Count Bibliographic Additions By Staff

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a count of bibliographic records added by each staff member and library. Staff need this report to distinguish additions according to both the person who added the bibliographic record and the library associated with the addition. The report must therefore support the combined reporting dimension of staff member and library, rather than only a total count of added bibliographic records.

> - Bib Records Added by user by library Count (`early_draft_srs_galecia.txt`)

### REQ-306 - Deliver Generated Reports By Email

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must support delivering generated reports by email. This capability is needed in the reports interface when staff require reports to be sent electronically rather than accessed only within the reporting interface. Email delivery applies to reports after they have been generated, and the system should provide it as a reporting output capability.

> Email delivery of reports: 45% (`survey_results_2009.txt`)

### REQ-307 - Deliver Prewritten Canned Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The product must include a predefined set of prewritten canned report templates. These templates are needed to provide generic reports that staff can run immediately or on a recurring basis. The canned reports must be delivered with the product and made available as a list from which reports can be selected.

> There should be a certain set of templates that are pre-written and delivered with the product. (`early_draft_srs_galecia.txt`)

### REQ-308 - Display OpenTemplate Attributes

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to select open-template attributes for display in report results. The selectable attributes must be associated with circulation, patrons, items, bills, and bibliographic records. This capability is needed when staff must determine which information an open-template report presents, in addition to using those attribute areas as filtering criteria.

> Open template would have all attributes associated with say circulation, patrons, items, bills, and bibs to select from for filtering and the same attributes for displaying. (`early_draft_srs_galecia.txt`)

### REQ-309 - Display Report Name And Date Range

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must display the selected date range and the report name in the report output. This information must appear at the top or bottom of the results so the selected reporting period and report identity can be seen quickly. The requirement supports reporting in which data is acquired for a given date or date range and selection criteria are clearly defined.

> Report results would include the date selection criteria at the top or bottom to quickly see date range selected along with the name of the report (`early_draft_srs_galecia.txt`)

### REQ-310 - Edit Canned Report Display Options

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must allow staff to edit the display options of canned reports. This capability is needed when the predefined report remains useful but its presentation requires adjustment for the reporting task. The editing function must apply to display options for canned reports and must not be limited to running only the predefined presentation.

> - No ability to edit canned report display options (`evergreen_reference_2009.txt`)

### REQ-311 - Edit OnDemand Report Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to modify the selection criteria and display options of preset on-demand reports. These reports are intended for situations in which pre-selected reporting content must be adjusted before execution, rather than using only fixed report settings. The capability applies to noncanned or on-demand reports and must support changes to both the data selected and the way the results are displayed.

> Noncanned or On Demand Reports - preset but have the ability to edit selection criteria and display options (`early_draft_srs_galecia.txt`)

### REQ-312 - Enhance Detailed Aged Debt Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide an enhanced detailed report of aged debt. Staff need the report to review aged debt in greater detail than the currently available reporting capability. The source identifies the aged debt detailed report as partially available and requiring enhancement, so the system must improve that existing report rather than treat the requirement as already satisfied.

> - Aged Debt detailed report (partially available, needs enhancement) (`evergreen_reference_2009.txt`)

### REQ-313 - Estimate Item Renewal Likelihood

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system should report or estimate how likely a particular item is to be renewed. This capability is needed to support understanding and prediction of patron behavior and material use. The renewal likelihood must be associated with the specified item rather than only presenting general renewal information. The result should be available as part of the system’s patron behavior and use analysis.

> - How likely is a particular book to be renewed? (`early_draft_srs_galecia.txt`)

### REQ-314 - Estimate Item Renewal Likelihood

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must support analysis that estimates how likely a book is to be renewed and identifies what percent of check-outs are renewals. This capability is needed to predict patron behavior and analyze how quickly books are returned. The analysis may use demographic data such as age ranges and geographical regions, including zip codes when useful for planning programming, but demographic statistics must be anonymized and must not contain personally identifiable information.

> We need to predict patron behavior. How likely is a book to be renewed? What percent of check-outs are renewals? (`survey_results_2009.txt`)

### REQ-315 - Exclude Last Edit From Circulation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide a last edit date that excludes the date of the last circulation activity. This distinction is needed because the existing reporting environment does not provide a last edit date that omits circulation, making the required edit information unavailable. The reported value must represent the last edit independently of the most recent circulation activity. This requirement applies when reporting dates and is intended to distinguish editing from circulation history.

> - Last edit date not including last circulation - does not exist (`evergreen_reference_2009.txt`)

### REQ-316 - Export Report Output Formats

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide report output in Excel, HTML, and CSV formats. This capability is needed so staff can obtain report results in the formats supported by the quick access interface. The available output format must be selectable or otherwise provided for report generation. The requirement applies to report output and does not limit the other report selections or scheduling choices available through the interface.

> Output would be in Excel, HTML, and CSV format (`early_draft_srs_galecia.txt`)

### REQ-317 - Export Reports Multiple File Formats

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow reports to be exported in Excel, CSV, and HTML formats. This capability is needed in the reports interface to provide multiple output formats for generated reporting results. The export requirement applies to each of the specified formats and should be available when staff need to use reports in those forms.

> Multiple output formats (Excel, CSV, HTML): 61% (`survey_results_2009.txt`)

### REQ-318 - Expose Bibliographic Report Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must make the specified bibliographic fields available in reports for bibliographic records. These fields must include identifiers such as id, fingerprint, ISBN, ISSN, UPC, and EAN; classification and record details such as record_type, edition, and language; publication information such as publisher_name, publication_date, and place_of_publication; and physical-description data. The fields are needed to report on bibliographic records and their relationships to items.

> For bibliographic_record: - id, fingerprint, scan_timestamp, record_type, edition, language, ISBN, ISSN, UPC, EAN, publisher_name, publication_date, place_of_publication, physical_description (`evergreen_reference_2009.txt`)

### REQ-319 - Expose Item Report Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must make the specified item fields available in reports. These fields must include item identifiers, barcode, label, copy_number, location, status, circulation modifier, call number, purchase date, purchase price, shelving location, age-based hold protection, and reserve information. The reports must support item reporting across identification, location, status, circulation, acquisition, shelving, hold-protection, and reserve details.

> For item: - id, barcode, label, copy_number, location (copy_location), status (acq status), circ_modifier, call_number, purchase_date, purchase_price, shelving_location, age_hold_protect, reserve_id (`evergreen_reference_2009.txt`)

### REQ-320 - Filter Reports By All Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow report users to filter reports by all relevant fields that are available. This capability is needed because users currently cannot filter by some fields that should be available. The filtering function must therefore expose every relevant available field for use in report queries.

> Can't filter by some fields that should be available (`survey_results_2009.txt`)

### REQ-321 - Filter With OpenTemplate Attributes

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to use open-template report attributes as filtering criteria. Available attributes must be associated with circulation, patrons, items, bills, and bibliographic records. This capability is needed when staff require filtering beyond the pre-selected criteria of on-demand reports, and the same attribute areas are also available for selecting report displays.

> Open template would have all attributes associated with say circulation, patrons, items, bills, and bibs to select from for filtering and the same attributes for displaying. (`early_draft_srs_galecia.txt`)

### REQ-322 - Generate Combined In-Transit Items Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must generate an in-transit item report for each branch and for the entire library system. The report must identify items that have been in transit for more than a configurable number of days. It must combine transit-to and transit-from information into one report so staff can use a single list when monitoring in-transit items.

> The system should generate a list of items that have been in-transit for more than X days (X configurable), per branch and per system. (`early_draft_srs_galecia.txt`)

### REQ-323 - Generate Consortium Wide Statistical Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow the Global System Administrator to generate statistical reports for the entire library consortium. This capability is needed because the Global System Administrator manages the ILS at the consortium level and generates statistical reports for the entire system. The reports must therefore support consortium-wide statistical reporting rather than being limited to an individual organizational unit.

> The Global System Administrator: The individual(s) who manage the ILS at the consortium level, implementing software changes and configurations, and generating statistical reports for the entire system. (`early_draft_srs_galecia.txt`)

### REQ-324 - Generate Item Use Count List

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide a list of items having a specified total use count. This report is needed to identify items according to their total recorded use. The specified count must determine which items are included in the list. The source identifies this report type as not available, so the reporting system must add support for producing it.

> - List of Items with specific Total Use Count (not available) (`evergreen_reference_2009.txt`)

### REQ-325 - High Use Threshold Item Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report listing items whose total use count exceeds a specified threshold. The report must evaluate each item’s total use count against the threshold and include items that are above it. Staff need this report to identify items with high use for collection reporting and review. The threshold must be specified for the report, so the qualifying items depend on the selected total use count limit.

> - List of Items with a > Total Use Count (`early_draft_srs_galecia.txt`)

### REQ-326 - Hold Request Placement Counting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must count all hold requests and record how each hold was placed. The placement categories must include a staff desk, a public computer inside the library, and a remote location. This information is needed for reporting on hold activity by placement method and for staff analysis of how patrons submit requests. The system must also support transaction reports covering holds placed, holds filled, and check-outs per patron, library, selected group of libraries, system, or county.

> The system counts all hold requests, including how the hold was placed: - at a staff desk - at a public computer inside the library - remotely (`early_draft_srs_galecia.txt`)

### REQ-327 - Identify Hold Placement Method

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide hold reports that identify how each hold was placed. Each hold must be distinguishable as placed at a staff desk, at a public computer, or remotely. This information is needed to analyze hold activity by placement method.

> Holds reports should show how the hold was placed - at staff desk, at public computer, or remotely (`survey_results_2009.txt`)

### REQ-328 - Include Null And Blank Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must include all null and blank fields in report results. This capability is needed because the current reporting environment may filter some nulls, whereas the reporting requirement calls for all such fields to be retained. Reports must therefore return fields regardless of whether their values are null, blank, or populated. This condition applies to report results and ensures that missing or empty values are not omitted by filtering.

> - All nulls and blank fields included in results - current system may filter some nulls (`evergreen_reference_2009.txt`)

### REQ-329 - Integrate With Enterprise ILS Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must integrate the Management Processes component with the broader ILS data structures and functionality. It must rely on the Acquisitions and Cataloging modules when supporting library administrators, managers, and staff in analyzing operations, managing collections, and making data-driven decisions. This integration is required because Management Processes operate as part of a larger enterprise-level Library Automation System and depend on the broader ILS for their data and functionality.

> They rely on the data structures and functionality of the broader ILS, including Acquisitions and Cataloging modules. (`early_draft_srs_galecia.txt`)

### REQ-330 - Item Value Collection Reporting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must generate reports showing the value of items based on data in item records. Staff must be able to report on the entire collection or a selected portion of it. Selected portions may include items with a specified status or items in a specified collection category, such as longoverdue items or DVDs in the children's collection. The report must also support determining the value of the entire collection.

> The system can generate a report of the value of items (based on data in item record) in the entire collection or a portion. (`early_draft_srs_galecia.txt`)

### REQ-331 - Last Copy Deleted Items Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to run a report on items deleted when they were the last copy owned by the library system or facility. The report must identify deleted items that satisfied the last-copy condition at the time of deletion. Staff need this report to review deletions that removed the last copy held by the relevant library system or facility. The report is limited to deleted items that were last copies, rather than deleted items generally.

> - Last Copy Report (last copy owned by a library system that was deleted) (`early_draft_srs_galecia.txt`)
> Ability to run a report on deleted items that were the last copy in the facility (`early_draft_srs_galecia.txt`)

### REQ-332 - List Barred Patrons Only

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report listing patrons whose status is barred. Staff need this patron report to identify patrons currently recorded with the barred status. The report must present a list of patrons rather than an aggregate patron count or a list based on another status. Its scope is limited to patrons identified as barred.

> - List of patrons who are BARRED (`early_draft_srs_galecia.txt`)

### REQ-333 - List Bibliographic Text-Matching Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of items whose bibliographic record contains specified text or data. The report must use the requested text or data to identify the applicable bibliographic records and their associated items. This capability belongs to the item reports and must support reporting on items with specified content in the bibliographic record.

> - List of items with XXX in bib record (`early_draft_srs_galecia.txt`)

### REQ-334 - List Deleted Last Owned Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of items deleted that were the last copies owned by the library system. The list must identify items meeting this ownership condition so the library can determine which deletions require follow-up. This capability is needed to update WorldCat after the library system deletes an item that was its last owned copy.

> Ability to get a list of items deleted that was the last copy owned by the library system in order to update WorldCat (`early_draft_srs_galecia.txt`)

### REQ-335 - List Of Items Added

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide an items report listing the items that were added. This report is needed to support review of additions beyond a count of added items, as the items-reporting requirements distinguish a list of items added from the Items Added Count report. Staff must be able to use the report when examining added items. The report should be available as a List of Items Added.

> - List of Items Added (`early_draft_srs_galecia.txt`)

### REQ-336 - List Patrons By Expiration Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of patrons organized by expiration date. The report is needed when staff must review patron records according to the dates on which patron status expires. It must be available as part of the patrons reports for examining patrons by expiration date. The source does not state additional conditions, date ranges, sorting rules, or other limits.

> - List of Patrons by Expiration Date (`early_draft_srs_galecia.txt`)

### REQ-337 - List Patrons By Notes Wording

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report listing patrons whose notes contain specified wording. Staff need this report to locate patrons based on wording recorded in patron notes. The report must support identification by the specified wording and present the matching patrons as a list. Its scope is limited to notes containing the requested wording, rather than all patron notes or another patron attribute.

> - List of Patrons with specific wording in notes (`early_draft_srs_galecia.txt`)

### REQ-338 - List Patrons By Survey Answer Filter

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of patrons grouped or filtered by survey answer. This report is needed when staff must identify patrons according to the survey answers associated with their records. The resulting patron list must support the survey-answer grouping or filtering described in the requirement. The source identifies this as a patrons report and does not state additional conditions or limits.

> - List of patrons by survey answer (`early_draft_srs_galecia.txt`)

### REQ-339 - Location And Home Library Counts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide circulation counts by circulation location, broken down by the patron's home library. Staff need this report to examine circulation activity at circulation locations in relation to patrons' home libraries. The report must retain both the circulation location and the patron home library as reporting dimensions. This capability is needed when staff require circulation counts that show where circulation occurred and the home library associated with the patron.

> - Circulation Count by Circ Location broken down by Patron Home Library (`early_draft_srs_galecia.txt`)

### REQ-340 - Long Overdue System Marked List

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report listing items that are long overdue. The report must include items marked long overdue by the system, in addition to other items identified as long overdue. Staff need this report to review long-overdue materials as part of item reporting. The report must distinguish or identify the system-marked long-overdue status where that status applies.

> - Items marked longoverdue by system (`early_draft_srs_galecia.txt`)
> - List of Long Overdue (`early_draft_srs_galecia.txt`)

### REQ-341 - Low Use Threshold Item Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report listing items whose total use count is below a specified threshold. The report must evaluate item use against the selected threshold and include items that fall below it. Staff need this report for weeding purposes and collection review. The threshold must be specified for the report, so the items listed are limited to those with a total use count lower than the selected limit.

> - List of Items with a < Total Use Count [Weeding Report] (`early_draft_srs_galecia.txt`)

### REQ-342 - Maintain Report Recipient Address Book

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide an address book for report recipients and report delivery. Staff need this capability to maintain recipient information for distributing reports through the reporting system. The address book must support the delivery process and must be provided in addition to the stated need for report delivery.

> - No address book for report delivery (`evergreen_reference_2009.txt`)

### REQ-343 - Manage Report Templates Administration

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide management of report templates within the reporting system. This capability is needed because the existing reporting environment has no report template management system. It must support the management of templates used for reporting, addressing the identified gap in reporting capabilities. The requirement applies to report template administration and is separate from the other reporting gaps identified in the source.

> - No report template management system (`evergreen_reference_2009.txt`)

### REQ-344 - Modifier Category Circulation Breakdown

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide circulation counts broken down by circulation modifier, Cat1, and Cat2 categories. The report must support category distinctions such as Adult, YA, and Juvenile so that circulation can be examined for each applicable classification. This capability is needed when staff require circulation statistics organized by circulation and catalog-related categories rather than only as an overall count.

> - Circulation Count by Circ Modifier, Cat1, and Cat2 (Adult, YA, Juv...) (`early_draft_srs_galecia.txt`)

### REQ-345 - Modify Recurring Report Selections

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to modify recurring reports by adding or removing report selections and by editing their email recipients. This capability is needed when the content or distribution of a recurring report changes after it has been configured. The system must preserve the recurring-report context while allowing both report selections and email addresses to be changed. The requirement applies to recurring reports and includes changes to the selected report data and delivery recipients.

> Ability to edit recurring reports by adding or removing report selections as well as editing the email addresses (`early_draft_srs_galecia.txt`)

### REQ-346 - Monthly Cataloged In-House Use Count

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report showing counts of cataloged in-house use. Staff need this report to review use of cataloged items within the library. The report must distinguish cataloged in-house use from non-cataloged in-house use, which is reported separately by month.

> - Cataloged In House Use Count (`early_draft_srs_galecia.txt`)

### REQ-347 - Monthly Non-Cataloged In-House Use Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a monthly report of non-cataloged in-house use. Staff need this report to review counts of non-cataloged items used in-house over each month. The report must distinguish non-cataloged in-house use from cataloged in-house use, which is identified as a separate in-house use report.

> - NonCat In House Use Count by Month (`early_draft_srs_galecia.txt`)

### REQ-348 - Patron Hold Status Display

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must display the number of check-outs and placed holds for each patron. It must subtotal holds by type, including active, frozen, and frozen-until holds. This detail is needed in transaction reports that examine patron activity and hold status. Reports must support the source-defined scopes of patron, library, selected group of libraries, system, and county, and may include holds placed, holds filled, and check-outs.

> The system displays the number of check-outs and placed holds per patron. Holds are subtotaled by type, e.g., active, frozen, and frozen-until holds. (`early_draft_srs_galecia.txt`)

### REQ-349 - Periodic Reports For Bibliographic Holds

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support periodic reports identifying bibliographic records with holds. These reports are needed to identify bibliographic records associated with holds as part of periodic reporting. The report must distinguish the affected bibliographic records so that the records with holds can be reviewed. This requirement applies to bibliographic records and does not specify a particular reporting interval or additional condition.

> Examples of periodic reports include: - Bibliographic records with holds (`early_draft_srs_galecia.txt`)

### REQ-350 - Periodic Reports For In-Transit Held Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support periodic reports identifying items that are in transit while having outstanding holds. Staff need this report to identify in-transit items associated with outstanding hold requests. The report must be available as a periodic report type alongside other operational reports, including reports for items that have been in transit for more than a specified number of days. It must focus on the combined condition of transit status and an outstanding hold.

> - In-transit items with outstanding hold (`early_draft_srs_galecia.txt`)

### REQ-351 - Periodic Reports For Inactive Checkouts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support periodic reports identifying items that have not been checked out within a specified number of days. These reports are needed to identify items with no check-out activity during the selected period. The reporting condition must use the specified number of days as the limit for determining inactivity. The requirement concerns item-level check-out history and does not specify any additional filtering or action.

> - Items that have not been checked out in X days (`early_draft_srs_galecia.txt`)

### REQ-352 - Periodic Reports For Invalid Patron Home

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support periodic reports identifying patrons with an invalid home library. Staff need this report to identify patron records whose home library is not valid. The invalid-home-library report must be available as a periodic reporting option alongside other reports covering patron, item, and bibliographic record conditions. The report must focus on patrons affected by the invalid home-library condition.

> - Patrons with invalid home library (`early_draft_srs_galecia.txt`)

### REQ-353 - Periodic Reports For Item-Level Holds

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support periodic reports identifying item-level holds. These reports are needed to distinguish holds placed on specific items from other hold-related reporting. The report must identify the items associated with item-level holds so they can be reviewed through periodic reporting. The source defines this as a report example but does not specify a reporting interval, additional selection criteria, or any required action after identification.

> - Item-level holds (`early_draft_srs_galecia.txt`)

### REQ-354 - Periodic Reports For Itemless Bibliographics

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support periodic reports identifying bibliographic records with no item records. Staff need this report to identify bibliographic records that lack associated items. The itemless-bibliographic-record report must be available as a periodic report type alongside other reports concerning data quality and operational conditions. Its scope must be limited to bibliographic records for which no item records are present.

> - Bibliographic records with no item records (`early_draft_srs_galecia.txt`)

### REQ-355 - Present Consolidated Multiple Canned Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must present the results of multiple canned reports run together within a single document. Staff need this consolidated presentation when they select several canned reports to run at the same time. The reports may use pre-written templates and data periods such as yesterday, last week, last month, or last year, while the combined results must remain available in one document.

> Canned reports can be checked off from a list to run at the same time and will be viewed within one document. (`early_draft_srs_galecia.txt`)

### REQ-356 - Prevent Excel Export Duplicate Rows

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must prevent unnecessary duplicate rows when report data is exported to Excel. This capability is needed because report users currently encounter too many duplicate rows in Excel output, making the resulting data less useful. The system must provide export results that avoid such duplication while preserving the requested report data.

> I need to export to Excel but the data has too many duplicate rows (`survey_results_2009.txt`)

### REQ-357 - Prevent Unauthorized Template Violations

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must prevent staff from modifying report templates in ways that violate administrator-defined reporting restrictions. Staff may set a call number range for a weeding report or add and remove display fields from a pick list when those changes are permitted. The system must prohibit staff from altering a template to display deleted items when that display is not allowed. These controls are needed so that reports remain accurate and dependable after permitted modifications.

> For example, front-line staff could set a call number range for a weeding report or add/remove display fields from a pick list, but they should not be able to alter the template to display deleted items. (`early_draft_srs_galecia.txt`)

### REQ-358 - Prioritize Selected Report Types

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must allow authorized users to prioritize selected report types. Staff need this capability to control the priority of reports in situations where certain report types should be processed ahead of others. The requirement addresses the current absence of an ability to prioritize certain types of reports and applies to selected report types rather than all reports by default.

> - No ability to prioritize certain types of reports (`evergreen_reference_2009.txt`)

### REQ-359 - Process Long Running Reports In Background

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must process long-running reports in the background rather than requiring them to remain in foreground processing. Staff need this capability when report execution takes substantial time, so that long-running report work can be handled separately from immediate interaction with the reporting system. Background processing must specifically support long-running reports.

> - No background processing for long-running reports (`evergreen_reference_2009.txt`)

### REQ-360 - Provide Age Range Demographic Reporting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must support demographic reporting that analyzes transactions and patron activity by age range. Age ranges are needed for demographic analysis and are considered useful for planning programming. The reporting must also support patron behavior analysis, including how quickly items are returned and renewal rates.

> I use demographic data to plan programming. Age ranges and zip codes are most useful. (`survey_results_2009.txt`)

### REQ-361 - Provide Aggregated Administrator Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide aggregated, high-level reports for Library Administrators. These reports are needed to support strategic planning and board presentations. Library Administrators are senior leadership who plan and direct library services and priorities, so the reports must present information at an aggregated, high level suitable for those activities.

> They require aggregated, high-level reports for strategic planning and board presentations. (`early_draft_srs_galecia.txt`)

### REQ-362 - Provide Board Executive Cross Tabs

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide predefined board and executive reports containing the basic statistics required by the Georgia Annual Report and Application for State Aid. These reports are needed for consumption by library boards and other external consumers. The reports should include statistics describing traffic and volume of use, including check-outs, check-ins, holds placed, and holds filled. The system should support cross-tabulation by terminal, branch, library system, hour, patron age range, patron type, and patron location.

> These should include basic statistics like those required by the Georgia Annual Report and Application for State Aid. (`early_draft_srs_galecia.txt`)

### REQ-363 - Provide Forgive Work Goods Payments

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a detailed report of forgive, work, and goods payments received. Staff need this report as part of the bills reporting functions to review these payment types separately from detailed payments received and detailed voids. The report must cover forgive, work, and goods payments received and must remain distinct from the general detailed payments received report.

> - Detailed Forgive, Work, and Goods Payments Received (`early_draft_srs_galecia.txt`)

### REQ-364 - Provide Historical Snapshot Bills Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide snapshot bills reports for historical points in time, allowing staff to see what the bills data looked like on a specific date in the past. The report must preserve the historical view even when an item’s shelving location has changed. This capability is needed for historical reporting and for examining bills data from an earlier point in time.

> Need a snapshot bills report going back in time (`survey_results_2009.txt`)

### REQ-365 - Provide Item Total Use Counts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide total use counts for items. It must also provide use counts broken down by usage date ranges, including fiscal-year and monthly periods. This capability is needed by staff who need to examine item usage overall or for a defined reporting period, while the available breakdown is limited to usage date ranges such as an FY or monthly use count.

> Ability to have a total use count on items as well as a use count broken down by usage date range such as an FY use count or monthly use count (`early_draft_srs_galecia.txt`)

### REQ-366 - Provide Manager Planning And Evaluation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide reports that Library Managers can use for organizational planning and evaluation. These reports are needed because Library Managers supervise organizational units and provide input to the design and implementation of library services. The reporting capability should support their planning and evaluation responsibilities within the library system.

> They use reports for planning and evaluation. (`early_draft_srs_galecia.txt`)

### REQ-367 - Provide Patron Fields In Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must make the specified patron fields available in reports. These fields must include patron identifiers, barcode, OPAC-visible fields, home library, patron type, email, address lines, city, state, postal code, birth date, and account creation date. The fields are needed to report patron identity, visibility, library affiliation, type, contact and address details, birth information, and account creation information.

> For patron: - id, barcode, opac (visible fields), family_lib (home library), usr_grp (patron type), em (email), address lines, city, state, zip (postal code), birth_date, create_date (`evergreen_reference_2009.txt`)

### REQ-368 - Provide Real Time Busy Period Reporting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must support real-time reporting during busy periods. This capability is needed because respondents specifically requested real-time reporting for those periods, when timely access to current report results is important. The system must provide reporting results in real time rather than limiting reporting to a later or non-current view.

> Real-time reporting for busy periods (`survey_results_2009.txt`)

### REQ-369 - Provide Recipient Email Address Book

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system should provide an address book for email addresses that are regularly used as report recipients. This capability is needed so staff can reuse commonly used recipient addresses when arranging report delivery. The address book should support the email addresses entered for sending report output. It applies to regularly used addresses and is intended to support, rather than replace, the ability to enter recipient addresses directly.

> Ability to enter email addresses for report to be sent to - would be great to have an address book of regularly used addresses (`early_draft_srs_galecia.txt`)

### REQ-370 - Provide Report Title Quick Access

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting interface must help staff find reports through quick access and descriptions associated with report titles. It must provide a quick access interface with pop-up descriptions and hover tooltips for report titles. These navigation aids are needed to make reports easier to locate and understand within the reporting interface.

> - No quick access interface with pop-up descriptions (`evergreen_reference_2009.txt`)
> - No hover tooltips for report titles (`evergreen_reference_2009.txt`)

### REQ-371 - Provide Snapshot Bills Historical Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide a snapshot bills report that can report on historical points in time. This capability is needed because reporting requirements include viewing bills as they existed at earlier points, while the existing reporting environment lacks both a historical reporting warehouse and a snapshot bills report going back in time. The report must therefore support historical bills reporting rather than only reporting current information. The requirement addresses the identified gap in historical reporting capabilities.

> - Snapshot bills report going back in time - does not exist (`evergreen_reference_2009.txt`)

### REQ-372 - Provide Weeding Collection Review

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a weeding report for collection review. The report must include each item's date of last circulation and the number of circulations for that item. It should support the item-level weeding reporting identified in the sources, including reporting based on circulation activity and items with lower total use counts.

> - Weeding report (date of last circulation and number of circs) (`early_draft_srs_galecia.txt`)

### REQ-373 - Report Actor Circulation Using Librarian Link

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must support the relationship between actors and circulation actions through the librarian link. This relationship must allow reports to connect actor information, including staff accounts and permissions, with circulation activities such as checkout, renewal, and holds. The capability is needed when staff reporting requires circulation actions to be associated with the actor linked to those actions.

> - actor -> action.circulation (through librarian link) (`evergreen_reference_2009.txt`)

### REQ-374 - Report Average Item Return Time

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system should report the average time required for a particular item to be returned. This statistic is needed to help understand and predict patron behavior and the use of materials. The report must focus on return timing for the specified item and present the average return time. The statistic should be available as part of the patron behavior and use analysis reporting.

> - How quickly is a particular book returned, on average? (`early_draft_srs_galecia.txt`)

### REQ-375 - Report Bibliographic Additions By User And Library

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide a report of bibliographic records added by user and library. The report must identify the user and library associated with the additions so staff can review activity by both dimensions. This capability is needed because reporting on bibliographic records added by user and library is identified as unavailable.

> - Bib Records Added by user by library Count (not available) (`evergreen_reference_2009.txt`)

### REQ-376 - Report Bibliographic Asset Copy Relationship

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must support the relationship between a bibliographic record and its items through asset.copy. This relationship must allow reports to connect bibliographic information, such as title, author, ISBN, publication information, and subjects, with item information, such as call number, barcode, location, and status. The relationship is needed when reporting requires bibliographic records and their associated items to be considered together.

> - bibliographic_record -> item (through asset.copy) (`evergreen_reference_2009.txt`)

### REQ-377 - Report Branch Renewals Percentage

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system should report the percentage of check-outs at a particular branch that are renewals. This statistic is needed to support analysis of patron behavior and the use of materials at the branch. The calculation must use check-outs at the specified branch and identify the portion that are renewals. The result should be available as part of the system’s patron behavior and use analysis reporting.

> - What percent of check-outs at a particular branch are renewals? (`early_draft_srs_galecia.txt`)

### REQ-378 - Report Collection Price By Call Number

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must report the price value of the collection grouped by call number. This report is needed to evaluate collection price value within call-number groupings. The grouping must use call number as the reporting dimension, and the reported measure must be collection price value. The source identifies price value of collection by call number as not available, so the system must provide this report.

> - Price value of collection by call number (not available) (`evergreen_reference_2009.txt`)

### REQ-379 - Report Collection Value By Location

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a collection value report showing the price value of the collection. Staff must be able to organize or view the reported value by call number or shelving location. This report is needed when staff require collection value information at either of those organizational levels.

> - Price value of collection by call number or shelving location (`early_draft_srs_galecia.txt`)

### REQ-380 - Report Holds Fulfillment Items Received

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide staff with a report of items received to fulfill holds. The report must support staff activities involving holds by identifying items that have been received for that purpose. This report must be provided as part of the holds reports and must remain distinct from the report of items sent for holds, unfilled holds, and stale holds.

> - Items Received for Holds (`early_draft_srs_galecia.txt`)

### REQ-381 - Report Holds Fulfillment Items Sent

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report of items sent to fulfill holds. Staff need this holds report to review items that have been sent for hold fulfillment. The report must focus on items sent for holds and distinguish them from items received for holds, holds requiring a purchase alert, unfilled holds, and stale holds. The report is limited to sent items associated with fulfilling holds.

> - Items Sent for Holds (`early_draft_srs_galecia.txt`)

### REQ-382 - Report IntraPINES Loans All Facilities

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide staff with a report of IntraPINES loans for all facilities. The report must give staff a facility-wide view of IntraPINES loan activity rather than limiting the information to a particular facility or system. This capability must be provided as part of the holds reports and must remain distinct from reports of IntraPINES loans for all systems, loans by system, and loans by facility.

> - IntraPINES Loans for all Facilities (`early_draft_srs_galecia.txt`)

### REQ-383 - Report IntraPINES Loans All Systems

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide staff with a report of IntraPINES loans for all systems. The report must give staff a system-wide view of IntraPINES loan activity rather than limiting the information to a particular system or facility. This capability must be provided as part of the holds reports and must remain distinct from reports of IntraPINES loans for all facilities, loans by system, and loans by facility.

> - IntraPINES Loans for all Systems (`early_draft_srs_galecia.txt`)

### REQ-384 - Report IntraPINES Loans Grouped By Facility

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide staff with a report of IntraPINES loans grouped by facility. The grouping must allow staff to review IntraPINES loan activity according to facility, supporting analysis of loans by that organizational level. This report must be provided among the holds reports and must remain distinct from the report of IntraPINES loans for all facilities, the report for all systems, and the report grouped by system.

> - IntraPINES Loans by Facility (`early_draft_srs_galecia.txt`)

### REQ-385 - Report IntraPINES Loans Grouped By System

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide staff with a report of IntraPINES loans grouped by system. The grouping must allow staff to review IntraPINES loan activity according to system, supporting analysis of loans by that organizational level. This report must be provided among the holds reports and must remain distinct from the report of IntraPINES loans for all systems, the report for all facilities, and the report grouped by facility.

> - IntraPINES Loans by System (`early_draft_srs_galecia.txt`)

### REQ-386 - Report Item Circulation Transaction Relationship

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must support the relationship between items and circulation actions through circulation transactions. This relationship must allow reports to connect item details, including call number, barcode, location, and status, with circulation activities such as checkout, renewal, and holds. The capability is needed when staff reporting requires circulation actions to be analyzed in relation to the items involved.

> - item -> action.circulation (through circulation transactions) (`evergreen_reference_2009.txt`)

### REQ-387 - Report Monthly Patron Additions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report showing the number of patrons added during each month. Staff need this report to review changes in patron enrollment over time. The report must organize the additions by month and present a patron count for each applicable month.

> - Patron Added Count by Month (`early_draft_srs_galecia.txt`)

### REQ-388 - Report Patron Circulation Using Patron Id

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must support the relationship between patrons and circulation actions through patron_id. This relationship must allow reports to connect patron information, including name, address, library, and patron type, with circulation activities such as checkout, renewal, and holds. The capability is needed when staff reporting requires circulation actions to be associated with the patrons connected to those actions.

> - patron -> action.circulation (through patron_id) (`evergreen_reference_2009.txt`)

### REQ-389 - Report Patron Counts By Age Demographic

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide patron counts broken down by age demographic. Staff need this report to examine the distribution of patrons across age demographics. The report must organize the count according to the available age-demographic categories rather than presenting only one combined patron count.

> - Patron Count by Age Demographic (`early_draft_srs_galecia.txt`)

### REQ-390 - Report Patron Counts By Profile Group

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a patron report that presents patron counts broken down by profile group. The report is needed when patron totals must be examined according to the profile groups associated with patrons. Staff need this report as part of the available patrons reporting capabilities. The source identifies the report by profile group but does not state additional conditions, grouping rules, or limits.

> - Patron Count by Profile Group (`early_draft_srs_galecia.txt`)

### REQ-391 - Report Patron Counts By Survey Answer

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a patron report that presents patron counts broken down by survey answer. The report is needed when staff must review the number of patrons associated with each survey answer. It must be available as part of the patrons reports so patron totals can be analyzed by the recorded survey responses. The source does not state additional conditions or limits for this count report.

> - Patron Count by survey answer (`early_draft_srs_galecia.txt`)

### REQ-392 - Report Patron Debt Using Debt Records

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must support the relationship between patrons and monetary records through debt records. This relationship must allow reports to connect patron information, including name, address, library, and patron type, with monetary activity such as fines, payments, and credits. The capability is needed when staff reporting requires monetary records to be associated with the patrons connected to those debt records.

> - patron -> money (through debt records) (`evergreen_reference_2009.txt`)

### REQ-393 - Report Previous Month Patrons Demographics

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report of patrons added during the previous month, grouped by demographic category. Staff need this report to examine the demographic composition of newly added patrons. The report is limited to patrons added during the previous month and must present the results by demographic category.

> - New Patron Count (patrons added the previous month by Demographic Category) (`early_draft_srs_galecia.txt`)

### REQ-394 - Report Sent Notice Statuses

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to run reports identifying pre-overdue, overdue, and holds notices that were sent. The reporting capability must distinguish these notice situations so that staff can retrieve the applicable sent-notice information. This is needed for reporting on notice activity associated with circulation and holds processes. The requirement concerns notices that were sent, rather than merely notices that could be sent.

> Ability to run reports for pre-overdue, overdue, and holds notices sent (`early_draft_srs_galecia.txt`)

### REQ-395 - Report Voided Transactions Detail

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a detailed report of voided transactions. This report is needed as part of the bills reporting capabilities, alongside reports for bills currently owed, payments received, and other payment-related activity. Staff must be able to access the detailed voids report through the reporting functionality.

> - Detailed Voids (`early_draft_srs_galecia.txt`)

### REQ-396 - Report Voter Survey Counts By County Week

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report showing voter survey response counts broken down by county and week. This report is needed when staff must review voter survey responses across counties over weekly periods. The report must present the counts using both county and week as the stated breakdowns. The source identifies it as a patrons report and does not state additional conditions or limits.

> - Voter Survey Responses County by Week (`early_draft_srs_galecia.txt`)

### REQ-397 - Report Voter Survey Responses

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide a report of voter survey responses. Staff need this report to review the responses collected through voter surveys. The capability is required because voter survey responses are identified as a missing report type.

> - Voter Survey Responses (not available) (`evergreen_reference_2009.txt`)

### REQ-398 - Restrict Canned Template Additions

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow additional canned reports to be added according to the user’s permission level. Permission levels must determine whether a user is authorized to add more canned reports. This capability is needed by staff who require report options beyond the existing canned reports, while restricting additions according to assigned permissions.

> Ability to add more canned reports via permission level (`early_draft_srs_galecia.txt`)

### REQ-399 - Restrict Queryable Tables And Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow administrators to control staff access to the database tables and fields used by the query tool. This access control must apply while staff design queries against bibliographic, item, patron, transaction, and financial records. The restriction is needed to govern which tables and fields staff can use when creating queries.

> Administrators should control staff access to tables and fields. (`early_draft_srs_galecia.txt`)

### REQ-400 - Retrieve Distributed MARC Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow report users to retrieve specific MARC fields even when the fields are stored across multiple rows. This capability is needed because users need specific MARC fields, but those fields are currently distributed across multiple rows. The system must combine or otherwise present the requested fields so they can be retrieved through reporting.

> Need to pull specific MARC fields but they're spread across multiple rows (`survey_results_2009.txt`)

### REQ-401 - Retrieve MARC Fields In Rows

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must retrieve MARC record fields for inclusion in report results. It must present the retrieved fields on a single row of report data rather than separating them across multiple rows. This capability is needed when reports require MARC record information in a consolidated form, supporting clear presentation of the relevant item or record data.

> Ability to pull MARC record fields so that they appear on a single row of data (`early_draft_srs_galecia.txt`)

### REQ-402 - Run Canned Reports By Interval

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to run canned reports using data from yesterday, last week, last month, or last year. This capability is needed when a canned report is run immediately or on a recurring basis and the reporting period must be based on a completed data interval. The available period selections are limited to yesterday, last week, last month, and last year.

> Will have the ability for it to run by yesterday's data, last week's, last month's, or last year's. (`early_draft_srs_galecia.txt`)

### REQ-403 - Run Preset OnDemand Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to run preset on-demand reports when reporting is needed. These reports support activities such as maintenance reporting and collections development, for which the reporting criteria are pre-selected but execution is not necessarily recurring. The system should distinguish this on-demand use from canned reports that may be set to run ASAP or on a recurring basis.

> On Demand Reports would be for pre-selected criteria but for things like maintenance reports or collections development and would be set to run on demand. (`early_draft_srs_galecia.txt`)

### REQ-404 - Run Reports By Date Time And Staff

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow reports to be run for transactions that occurred at a specified date and time. The reporting criteria must also support limiting the transactions by workstation or by staff member. This capability is needed to examine transaction activity in relation to when it occurred, where it was performed, or which staff member performed it.

> Ability to run a report on transactions that occurred on x date and time on x workstation or by x staff (`early_draft_srs_galecia.txt`)

### REQ-405 - Run Templates Without Modification

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to run available report templates without modifying them. This capability is needed when staff require a dependable report that can be used as provided by a system administrator. Templates must be runnable as-is while retaining their established reporting configuration. The system should also support individual modifications when permitted, but changes must not compromise the accuracy of results.

> These templates should be runnable as-is or modifiable for individual needs. (`early_draft_srs_galecia.txt`)

### REQ-406 - Schedule Recurring Report Execution

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow staff to schedule reports to run on a recurring basis. This capability is needed when the same reporting activity must be performed repeatedly rather than initiated separately each time. The scheduling function must apply to reports and support recurring execution, while the source does not specify a particular recurrence interval.

> Ability to schedule recurring reports: 52% (`survey_results_2009.txt`)

### REQ-407 - Select And Deselect Data Parts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to select or deselect individual parts of the available data for a report. This capability is needed when staff want to control which portions of report data are included in the output. The selection must apply to each part of the available data rather than only to the report as a whole. The selected data may be used with reports scheduled to run ASAP, hourly, daily, weekly, monthly, or yearly.

> Check off any part of data you want (`early_draft_srs_galecia.txt`)

### REQ-408 - Select Individual Records Manually

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow report users to manually select individual records from query results. This capability is needed as an administrative feature for selecting records returned by queries, and 39% of respondents identified the need to manually select from query results. The selection must apply to individual records within the query results.

> Manually select from query results: 39% (`survey_results_2009.txt`)

### REQ-409 - Select Regular Expressions From Dropdown

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to select regular expressions from a drop-down menu in the query tool. This capability is required when staff design queries against bibliographic, item, patron, transaction, and financial records. The drop-down menu must provide the regular expressions available for selection during query construction.

> - Select regular expressions from a drop-down menu (`early_draft_srs_galecia.txt`)

### REQ-410 - Separate Check In And Renewal Timestamps

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must store check-in date and time separately from renewal timestamps. This separation is needed because the current reporting information stores check-in and renewal timestamps together, preventing check-in activity from being represented independently. Reports must be able to use the check-in date and time without treating renewal timestamps as check-in events. The requirement addresses accurate reporting of circulation activity and the identified limitation in timestamp data.

> - Checkin Date/time not including renewals - checkin and renewal timestamps are stored together (`evergreen_reference_2009.txt`)

### REQ-411 - Separate Check-in From Renewals

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must ensure that reported check-in dates and times represent check-in transactions without including renewal transactions. Staff need this distinction when reviewing circulation activity and interpreting check-in reports. The system must not combine check-in and renewal timestamps in a way that prevents renewals from being excluded from check-in date and time reporting.

> Checkin date/time should not include renewals (`survey_results_2009.txt`)

### REQ-412 - Show Branch Capacity Interface

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide an interface showing the capacity of all branches. This interface is needed to support reporting on branch capacity across the library system. The capacity interface must cover all branches.

> The system should provide an interface showing the capacity of all branches. (`early_draft_srs_galecia.txt`)

### REQ-413 - Show Canned Template Hover Descriptions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must display a pop-up description when staff hover over the title of a canned report or template. This capability is needed in the quick access interface so staff can understand the report or template before selecting it. The description must be associated with each available canned report or template title and appear in response to hovering over that title.

> Ability to hover over each title of canned report/template with pop-up box with description (`early_draft_srs_galecia.txt`)

### REQ-414 - Support Core Report Categories

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must support circulation reports covering checkouts, check-ins, and renewals, as well as item reports covering inventory, weeding, and missing items. It must also support patron reports, financial reports covering fines and payments, and hold reports covering placed, filled, and stale holds. Custom or on-demand reports must be available for staff who need reporting beyond these core types.

> - Circulation reports (checkouts, check-ins, renewals): 78% - Item reports (inventory, weeding, missing): 65% - Patron reports (demographics, inactive accounts): 52% - Financial reports (fines, payments): 34% - Hold reports (placed, filled, stale): 41% - Custom/on-demand reports: 29% (`survey_results_2009.txt`)

### REQ-415 - Support Custom Locally Defined Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow report users to create or run custom and locally defined reports. These reports must support needs such as collection development, program attendance tracking, and staff productivity reporting, including time spent per transaction. This capability is needed because 38% of respondents reported using custom reports, while 62% reported not using them.

> Among those who use custom reports, the most common are: - Collection development reports - Program attendance tracking - Staff productivity reports (time spent per transaction) (`survey_results_2009.txt`)

### REQ-416 - Support Multiple Report Record Types

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must support bibliographic records, items, patrons, circulation actions, hold actions, monetary records, and actors as reportable record types. It must make bibliographic information, item details, patron information, circulation activities, hold requests, fines, payments, credits, staff accounts, and permissions available within reporting. This support is needed so reporting can address the listed library records and actions, including checkout, renewal, holds, monetary activity, and actor-related information.

> The following record types are available for reporting: - bibliographic_record: Title, author, ISBN, publication info, subjects, etc. - item: Call number, barcode, location (copy location), status, etc. - patron: Name, address, library, patron type, etc. - action_circulation: Checkout, checkout, ren... (`evergreen_reference_2009.txt`)

### REQ-417 - Total Items Count Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide an items report showing the total number of items. This report is needed to support an overall count of items within the items-reporting functions. Staff must be able to use the report when reviewing the total item collection. The report should be provided as an Items Count report, distinct from reports for items added, items deleted, or items currently checked out.

> - Items Count (`early_draft_srs_galecia.txt`)

### REQ-418 - Upload Patron Filter Identifier Text Files

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must allow staff to upload text files containing values used to filter reports. This capability is needed when filtering by lists of identifiers rather than entering each value individually. The uploaded values must support filtering for barcodes and TCNs, which are the examples specified for this function.

> - No ability to upload text files for filtering (barcodes, TCNs) (`evergreen_reference_2009.txt`)

### REQ-419 - Upload Text File For Filtering

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to upload a text file containing values such as barcodes or TCNs. The uploaded values must be available for filtering a report. This capability is needed when staff have a set of item identifiers that should determine which records are included in report results. The requirement applies specifically to text-file input used as report-filter criteria.

> Ability to upload a text file such as barcodes or TCN to use for filtering on a report (`early_draft_srs_galecia.txt`)

### REQ-420 - Use Full Boolean Operator Set

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support the full range of Boolean operators in its query tool. This capability is required for staff designing queries against bibliographic, item, patron, transaction, and financial records. The operators must be available as part of the user-friendly interface used to construct those queries.

> - Use a full range of Boolean operators (`early_draft_srs_galecia.txt`)

### REQ-421 - Weekly Report Voter Registration Responses

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a weekly report of voter registration survey response counts. The report must organize the counts by week so staff can review voter registration survey activity over time. This capability is required as part of the patron reports and must specifically address voter registration survey responses rather than general survey answers. The report is limited to response counts and does not require a list of individual patrons.

> - Voter Reg Survey Responses Count by Week (`early_draft_srs_galecia.txt`)

## Blacklist

Items found in the sources but discarded, with the reason. They are not part of the requirements above.

### BL-001 - Event-Based Reversion

**Reason (Conflicts with another requirement):** This requirement says an item may revert to its original location when checked out at the destination, while REQ-243 explicitly requires preventing automatic reversion on that event. Keep the more specific prohibition in REQ-243.  
**Conflicts with:** REQ-243  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

### BL-002 - Integrate with WorldCat

**Reason (Conflicts with another requirement):** This requests cataloging functionality for catalogers, which conflicts with the kept project-scope decision to exclude cataloging functionality from the management-reporting specification.  
**Conflicts with:** REQ-156  
**Sources:** `interview_cataloging_2009-05-08.txt`

### BL-003 - Provide Historical Reporting

**Reason (Conflicts with another requirement):** Its requirement to provide historical reporting through a reporting warehouse conflicts with the kept requirements to retain reporting data in the main relational database and avoid a denormalized warehouse requiring synchronization. The historical reporting need is retained by REQ-253.  
**Conflicts with:** REQ-084  
**Sources:** `early_draft_srs_galecia.txt`

### BL-004 - Run Reports on a Separate Database

**Reason (Conflicts with another requirement):** This requires reports to run against a separate reporting database or replica, contradicting the kept requirement that reporting data remain in the main relational database rather than requiring a separate reporting schema.  
**Conflicts with:** REQ-084  
**Sources:** `evergreen_reference_2009.txt`

### BL-005 - Adapt Existing Requirements Specification

**Reason (Too vague or not a software requirement):** This specifies how the requirements document should be developed, not behavior required of the software system.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-006 - Administer Permissions Easily

**Reason (Too vague or not a software requirement):** “Easy” is subjective and does not specify a testable level of administrative effort or usability.  
**Sources:** `early_draft_srs_galecia.txt`

### BL-007 - Assume Library Process Familiarity

**Reason (Too vague or not a software requirement):** This concerns how requirements documentation should address reader familiarity, rather than a requirement for the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-008 - Clarify Report Navigation

**Reason (Too vague or not a software requirement):** The requirement only says reports must be easy to find and navigate, without defining testable criteria for ease of use.  
**Sources:** `survey_results_2009.txt`

### BL-009 - Define Selection Criteria

**Reason (Too vague or not a software requirement):** The requirement does not specify what selection criteria must be defined or how their clarity to users can be evaluated.  
**Sources:** `early_draft_srs_galecia.txt`

### BL-010 - Ensure SRS Readability

**Reason (Too vague or not a software requirement):** This describes a quality goal for the requirements document, not a requirement for the software system.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-011 - Enterprise Infrastructure Reliance

**Reason (Too vague or not a software requirement):** It only states that management processes may rely on enterprise infrastructure and does not specify a required, testable behavior or infrastructure standard.  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

### BL-012 - Expand Report Types

**Reason (Too vague or not a software requirement):** The request to add report types sufficient to cover all identified gaps does not specify which report types are needed, so it is too vague to test.  
**Sources:** `evergreen_reference_2009.txt`

### BL-013 - Filter New Reports Development

**Reason (Too vague or not a software requirement):** This specifies a project development review process rather than a requirement for the software system.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-014 - Limit Specification Scope

**Reason (Too vague or not a software requirement):** This constrains the contents of the requirements specification, rather than stating a requirement for the software.  
**Sources:** `early_draft_srs_galecia.txt`

### BL-015 - Minimize Branch Labor

**Reason (Too vague or not a software requirement):** The requirement gives no measurable target or criterion for how much staff time must be reduced, so it is too vague to test.  
**Sources:** `interview_cataloging_2009-05-08.txt`

### BL-016 - Prioritize Functional Specification

**Reason (Too vague or not a software requirement):** This describes how the current specification effort should be conducted, rather than a testable requirement for the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-017 - Provide Developer Specificity

**Reason (Too vague or not a software requirement):** “Enough precise detail” is not defined by a measurable criterion, so the requirement is too vague to test.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-018 - Provide Management Reporting Tools

**Reason (Too vague or not a software requirement):** The statement is too broad to define a testable system requirement; it does not specify what reporting tools or capabilities are required.  
**Sources:** `early_draft_srs_galecia.txt`

### BL-019 - Provide Optimal Reports Functionality

**Reason (Too vague or not a software requirement):** “Optimal” functionality is not specified in testable terms, and the requirement does not identify concrete system behavior.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-020 - Rely on Full ILS Foundation

**Reason (Too vague or not a software requirement):** This only says the specification may rely on a full ILS, without stating a testable system requirement.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-021 - Simplify Permission Administration

**Reason (Too vague or not a software requirement):** The requirement says administration should be easy but provides no testable criteria for what constitutes easy administration.  
**Sources:** `email_staff_login.eml`

### BL-022 - Support Multiple SRS Audiences

**Reason (Too vague or not a software requirement):** This describes who should be able to use the requirements specification, not a requirement for the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-023 - Use Iterative Development

**Reason (Too vague or not a software requirement):** This specifies a software-development process, not a requirement for the software.  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

### BL-024 - Use Iterative Prototype Development

**Reason (Too vague or not a software requirement):** Specifies a development methodology rather than a testable requirement for the software.  
**Sources:** `early_draft_srs_galecia.txt`

### BL-025 - Validate Report Output

**Reason (Too vague or not a software requirement):** The requirement says output must be tested and proven reliable but specifies no testable reliability criteria or acceptance threshold.  
**Sources:** `early_draft_srs_galecia.txt`

