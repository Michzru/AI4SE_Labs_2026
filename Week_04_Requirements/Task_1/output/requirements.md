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
| REQ-001 | Configure Shared Report Folders | Must | functional | 4 |
| REQ-002 | Report Missing Damaged Items By Branch | Must | functional | 4 |
| REQ-003 | Allow Staff Credential Login | Must | functional | 3 |
| REQ-004 | Authenticate Individual Staff Regardless Login | Must | functional | 1 |
| REQ-005 | Control Staff Rights Via Roles | Must | functional | 5 |
| REQ-006 | Record Authenticated Staff For Audit | Must | functional | 1 |
| REQ-007 | Provide Last Copy Items Report | Must | functional | 3 |
| REQ-008 | Include Null Patron Records | Must | functional | 5 |
| REQ-009 | Query Transfer Candidate Items | Must | functional | 4 |
| REQ-010 | Save Reusable Transfer Queries | Must | functional | 3 |
| REQ-011 | Assign Roles Access Levels | Must | functional | 2 |
| REQ-012 | Non Degrading OPAC Reporting Separation | Must | non-functional | 2 |
| REQ-013 | Provide Section 508 Accessibility | Must | non-functional | 3 |
| REQ-014 | Queue Background Report Processing | Must | non-functional | 2 |
| REQ-015 | Support Validated Server Environments | Must | constraint | 3 |
| REQ-016 | Enforce Mandatory Role Based Access | Must | functional | 1 |
| REQ-017 | Provide Cross Linked HTML Help | Must | functional | 3 |
| REQ-018 | Cancel Scheduled Running Reports | Must | functional | 4 |
| REQ-019 | Provide Real Time Reporting Results | Must | functional | 4 |
| REQ-020 | Access Management Via Web Or Client | Must | constraint | 2 |
| REQ-021 | Preserve OPAC Module Functionality | Must | constraint | 2 |
| REQ-022 | Process Reports Without Disruption | Must | non-functional | 2 |
| REQ-023 | Provide Management Process Data Specifications | Must | functional | 2 |
| REQ-024 | Control Template Allowed Filter Fields | Must | constraint | 2 |
| REQ-025 | Produce Standards Compliant Web HTML | Must | constraint | 1 |
| REQ-026 | Use Fully Relational Data Store | Must | constraint | 1 |
| REQ-027 | Allow Complex Query Construction | Should | functional | 1 |
| REQ-028 | Analyze Branch Capacity Distribution | Should | functional | 2 |
| REQ-029 | Analyze Patron Demographics Interests | Should | functional | 3 |
| REQ-030 | Analyze Staff Productivity Workflow | Should | functional | 2 |
| REQ-031 | Combine Conditions With Boolean Operators | Should | functional | 3 |
| REQ-032 | Count Non Cataloged Transactions | Should | functional | 2 |
| REQ-033 | Create Controlled Report Templates | Should | functional | 3 |
| REQ-034 | Deliver Reports Via Email | Should | functional | 2 |
| REQ-035 | Export Reports Multiple Formats | Should | functional | 3 |
| REQ-036 | Generate Consortium Statistical Reports | Should | functional | 2 |
| REQ-037 | Provide Currently Checked Out Items | Should | functional | 2 |
| REQ-038 | Provide Deleted Items Count | Should | functional | 2 |
| REQ-039 | Provide Detailed Aged Debt Categorization | Should | functional | 2 |
| REQ-040 | Provide Item Additions Canned Report | Should | functional | 2 |
| REQ-041 | Provide Management Reporting Tools | Should | functional | 2 |
| REQ-042 | Provide Outstanding Patron Bills Report | Should | functional | 2 |
| REQ-043 | Provide Patron Counts By Home | Should | functional | 2 |
| REQ-044 | Provide Renewal Count Report | Should | functional | 2 |
| REQ-045 | Provide Shelving Location Counts | Should | functional | 2 |
| REQ-046 | Provide Total Patron Count | Should | functional | 2 |
| REQ-047 | Report Detailed Payments Received | Should | functional | 2 |
| REQ-048 | Report Missing Item Records | Should | functional | 3 |
| REQ-049 | Report Overdue Items By Days | Should | functional | 2 |
| REQ-050 | Schedule Recurring Canned Reports | Should | functional | 2 |
| REQ-051 | Show Queue Status For Reports | Should | functional | 3 |
| REQ-052 | Generate Material Volume Report | Should | functional | 3 |
| REQ-053 | Report Category Holds With Counts | Should | functional | 2 |
| REQ-054 | Determine Permissions Via Security Groups | Should | functional | 1 |
| REQ-055 | Display All Branch Capacities | Should | functional | 2 |
| REQ-056 | Provide System Administrator Role | Should | functional | 1 |
| REQ-057 | Compare Shelf Space Percentages | Should | functional | 3 |
| REQ-058 | Generate Automated Shelf Space Reports | Should | functional | 2 |
| REQ-059 | Combine In Transit Report Directions | Should | functional | 3 |
| REQ-060 | Generate In Transit Items Report | Should | functional | 2 |
| REQ-061 | Audit Deletions For Multiple Record Types | Should | functional | 2 |
| REQ-062 | Audit Purge And Deletion Events | Should | functional | 3 |
| REQ-063 | Cleanup Delete Volume With Items | Should | functional | 3 |
| REQ-064 | Convert Item Statuses In Batch | Should | functional | 3 |
| REQ-065 | Delete Orphaned Itemless Records | Should | functional | 2 |
| REQ-066 | Generate Last Copy Report | Should | functional | 1 |
| REQ-067 | Identify Purge Candidates By Configured Criteria | Should | functional | 3 |
| REQ-068 | Provide Last Copy By Branch | Should | functional | 2 |
| REQ-069 | Safeguard Against Mass Collection Deletion | Should | non-functional | 1 |
| REQ-070 | Checkout Renewal Counting By Type | Should | functional | 2 |
| REQ-071 | Control Report Create Clone Permissions | Should | functional | 2 |
| REQ-072 | Cross Tabulate Multi Dimension Activity | Should | functional | 3 |
| REQ-073 | Granular Check In Counting Methods | Should | functional | 2 |
| REQ-074 | Provide Demographic Region Patron Stats | Should | functional | 2 |
| REQ-075 | Provide Patron Behavior Analytics | Should | functional | 2 |
| REQ-076 | Retain Transaction History Window | Should | functional | 2 |
| REQ-077 | Run Or Edit Report Templates | Should | functional | 3 |
| REQ-078 | Show Report Queue Position | Should | functional | 3 |
| REQ-079 | Track Record Deletions By Location | Should | functional | 3 |
| REQ-080 | Allow Grouping By Patron Characteristics | Should | functional | 3 |
| REQ-081 | Filter Patron Reports By Home Branch | Should | functional | 2 |
| REQ-082 | Limit And Group Preferred Language | Should | functional | 2 |
| REQ-083 | Configure Age Range Grouping | Should | functional | 2 |
| REQ-084 | Group And Filter Patron County | Should | functional | 2 |
| REQ-085 | Group And Filter Patron Type | Should | functional | 2 |
| REQ-086 | Group And Filter Patron Zip | Should | functional | 2 |
| REQ-087 | Generate Inactive Patrons Report | Should | functional | 2 |
| REQ-088 | Run Inactive Patron Report Levels | Should | functional | 2 |
| REQ-089 | Allow Selective Title Transfers | Should | functional | 2 |
| REQ-090 | Automatically Revert Temporary Transfers | Should | functional | 3 |
| REQ-091 | Batch Transfer Items Between Branches | Should | functional | 3 |
| REQ-092 | Identify Uncataloged Material Usage | Should | functional | 2 |
| REQ-093 | Integrate WorldCat Last Copy | Should | functional | 1 |
| REQ-094 | Report Long Transit Items By Branch | Should | functional | 2 |
| REQ-095 | Track Uncataloged Item Inventory | Should | functional | 2 |
| REQ-096 | Update Item Locations For Destinations | Should | functional | 3 |
| REQ-097 | Provide Separate Dev Training Environments | Should | functional | 4 |
| REQ-098 | Report Invalid Item Types Periodically | Should | functional | 2 |
| REQ-099 | Report Long Call Numbers Periodically | Should | functional | 2 |
| REQ-100 | Show Separate Item Last Edit Date | Should | functional | 2 |
| REQ-101 | Support Accessible HTML Standards | Should | non-functional | 2 |
| REQ-102 | Use Live Database Reporting | Should | constraint | 2 |
| REQ-103 | Provide Searchable Online Report Help | Should | functional | 3 |
| REQ-104 | Separate Reporting From OPAC | Should | constraint | 1 |
| REQ-105 | Support Environment Template Migration | Should | functional | 3 |
| REQ-106 | Centralized Enterprise Management Processes | Should | constraint | 3 |
| REQ-107 | Describe Management Process Workflows | Should | functional | 3 |
| REQ-108 | Filter By Survey Name | Should | functional | 2 |
| REQ-109 | Integrate With Enterprise Library Automation | Should | constraint | 3 |
| REQ-110 | Interface Vendor APIs And File Transfers | Should | constraint | 3 |
| REQ-111 | Management Data Specifications And Dictionaries | Should | functional | 1 |
| REQ-112 | Provide Historical Date Reporting | Should | functional | 3 |
| REQ-113 | Provide Historical Reporting Warehouse | Should | functional | 2 |
| REQ-114 | Provide Thorough Error Reporting Feedback | Should | functional | 3 |
| REQ-115 | Query OPAC Hold Circulation Data | Should | functional | 2 |
| REQ-116 | W3C Compliant Web Output | Should | non-functional | 2 |
| REQ-117 | Comply With Accounting Audit Requirements | Should | constraint | 2 |
| REQ-118 | Link Payments To Applied Charges | Should | functional | 1 |
| REQ-119 | Provide Patron Balance Financial Reports | Should | functional | 2 |
| REQ-120 | Query Balances Above Dollar Threshold | Should | functional | 2 |
| REQ-121 | Report Payments By Method Channel | Should | functional | 2 |
| REQ-122 | Report Waived Fines By Branch | Should | functional | 2 |
| REQ-123 | Track Waived Fines By Library | Should | functional | 2 |
| REQ-124 | Update Front Desk Payments Immediately | Should | non-functional | 2 |
| REQ-125 | Associate Finance With Patron Items | Should | functional | 2 |
| REQ-126 | Maintain Applied Payment Ledger | Should | functional | 2 |
| REQ-127 | Report Item Values From Records | Should | functional | 2 |
| REQ-128 | Context Sensitive Online Help | Should | functional | 1 |
| REQ-129 | Provide Admin Query Specific Feedback | Should | functional | 2 |
| REQ-130 | Relational Database Back End | Should | constraint | 1 |
| REQ-131 | Report Items Currently In Transit | Should | functional | 1 |
| REQ-132 | Support Supported Web Browsers | Should | constraint | 2 |
| REQ-133 | Archive Transactions With Privacy | Should | functional | 1 |
| REQ-134 | Control Report Access Permissions | Should | functional | 2 |
| REQ-135 | Control Report Creation And Cloning | Should | functional | 1 |
| REQ-136 | Exclude Personally Identifiable Patron Data | Should | constraint | 1 |
| REQ-137 | Manage Access Using Security Groups | Should | non-functional | 2 |
| REQ-138 | Provide Activity Traffic Volume Reports | Should | functional | 2 |
| REQ-139 | Provide Executive Board Activity Reports | Should | functional | 2 |
| REQ-140 | Retain Archives Per Legal Periods | Should | constraint | 1 |
| REQ-141 | Run Named Reports Using Templates | Should | non-functional | 1 |
| REQ-142 | Select Query Values From Picklists | Should | functional | 2 |
| REQ-143 | Select Report Display Fields | Should | functional | 2 |
| REQ-144 | Show Report Name And Criteria | Should | functional | 3 |
| REQ-145 | Update Permissions On Role Change | Should | functional | 1 |
| REQ-146 | Assign Report Queue Priorities | Should | functional | 1 |
| REQ-147 | Control Query Tool Access | Should | functional | 1 |
| REQ-148 | Design User Queries Via Interface | Should | functional | 2 |
| REQ-149 | Run And Modify Templates With Limits | Should | functional | 2 |
| REQ-150 | Allow Open Template Reporting | Should | functional | 2 |
| REQ-151 | Anonymize Demographic Reporting Data | Should | constraint | 1 |
| REQ-152 | Filter By Uploaded Identifier File | Should | functional | 2 |
| REQ-153 | Generate Pivot Table Report Results | Should | functional | 2 |
| REQ-154 | Identify Hold Placement Method | Should | functional | 2 |
| REQ-155 | Patron Behavior Renewal And Return Analysis | Should | functional | 1 |
| REQ-156 | Provide Fines-Stopped Reason Items | Should | functional | 2 |
| REQ-157 | Provide Hover Title Popups | Should | functional | 2 |
| REQ-158 | Provide Open Template Filter Attributes | Should | functional | 1 |
| REQ-159 | Report Bibliographic Additions By Staff | Should | functional | 2 |
| REQ-160 | Report Circulation By Modifiers | Should | functional | 2 |
| REQ-161 | Report Circulation Location By County | Should | functional | 2 |
| REQ-162 | Report Collection Age By Location | Should | functional | 2 |
| REQ-163 | Report Collection Price By Location | Should | functional | 2 |
| REQ-164 | Report Edited Bibliographic Records Count | Should | functional | 2 |
| REQ-165 | Report Holds With Purchase Alerts | Should | functional | 2 |
| REQ-166 | Report Inactive Patron Status | Should | functional | 2 |
| REQ-167 | Report Items Created Within Range | Should | functional | 2 |
| REQ-168 | Report Last Circulation Date And Uses | Should | functional | 2 |
| REQ-169 | Report Overdue Items Threshold Days | Should | functional | 2 |
| REQ-170 | Report Patron Geography County City ZIP | Should | functional | 2 |
| REQ-171 | Report Staff Account Dates | Should | functional | 2 |
| REQ-172 | Report Stale Holds Shelf Awaiting Pickup | Should | functional | 2 |
| REQ-173 | Report Unfilled Holds | Should | functional | 2 |
| REQ-174 | Report Voter Survey Responses By Week County | Should | functional | 2 |
| REQ-175 | Support Canned Report Definitions | Should | functional | 1 |
| REQ-176 | Support Fine Grained Reporting | Should | functional | 1 |
| REQ-177 | Use Iterative Prototype Methodology | Could | constraint | 1 |
| REQ-178 | Allow Custom Web Report Creation | Could | functional | 1 |
| REQ-179 | Allow Global Administrator Consortium Configuration | Could | functional | 1 |
| REQ-180 | Allow Local Administrator Configuration | Could | functional | 1 |
| REQ-181 | Control Report Create And Run | Could | functional | 1 |
| REQ-182 | Display Reports Indirectly To Patrons | Could | functional | 1 |
| REQ-183 | Enable Report Data Filtering | Could | functional | 1 |
| REQ-184 | Enable Report Results Sorting | Could | functional | 1 |
| REQ-185 | Enable Staff Management Report Creation | Could | functional | 1 |
| REQ-186 | Exclude Day To Day Patron Functions | Could | constraint | 1 |
| REQ-187 | Expose Field Catalog For Reporting | Could | functional | 1 |
| REQ-188 | Provide Bibliographic Record Count Report | Could | functional | 1 |
| REQ-189 | Provide Checkout Count Canned Report | Could | functional | 1 |
| REQ-190 | Provide Executive Reports Interface | Could | functional | 1 |
| REQ-191 | Schedule Multiple Reports Concurrently | Could | functional | 1 |
| REQ-192 | Support Drag Drop Field Selection | Could | functional | 1 |
| REQ-193 | Support Regular Expression Criteria | Could | functional | 1 |
| REQ-194 | Support Saved Report Reuse | Could | functional | 1 |
| REQ-195 | Track And Verify Financial Transactions | Could | functional | 1 |
| REQ-196 | Configure Item Category Breakdowns | Could | functional | 1 |
| REQ-197 | Differentiate Acquisition And Circulation | Could | functional | 1 |
| REQ-198 | Report Recent Acquisition Volume | Could | functional | 1 |
| REQ-199 | Color Code Branch Capacity Status | Could | functional | 1 |
| REQ-200 | Control Department Head Template Rights | Could | functional | 1 |
| REQ-201 | Control Front Desk Role Permissions | Could | functional | 1 |
| REQ-202 | Enable Branch Capacity Drilldown | Could | functional | 1 |
| REQ-203 | Export Branch Capacity CSV | Could | functional | 1 |
| REQ-204 | Show Branch Capacity Trend Data | Could | functional | 1 |
| REQ-205 | Sort Filter Branch Capacity Overview | Could | functional | 1 |
| REQ-206 | Calculate Circulation Percent By Category | Could | functional | 1 |
| REQ-207 | Calculate Collection Percent By Category | Could | functional | 1 |
| REQ-208 | Compare Branch Results With Average | Could | functional | 1 |
| REQ-209 | Estimate Shelf Space From Item Data | Could | functional | 1 |
| REQ-210 | Filter Shelf Space By DateRange | Could | functional | 1 |
| REQ-211 | Side By Side Library Comparison | Could | functional | 1 |
| REQ-212 | Include Condition Notes Per Item | Could | functional | 1 |
| REQ-213 | Merge Transit To And From | Could | functional | 1 |
| REQ-214 | Produce In Transit Report Scope | Could | functional | 1 |
| REQ-215 | Provide Default Transit Threshold | Could | constraint | 1 |
| REQ-216 | Report Missing And Damaged Items | Could | functional | 1 |
| REQ-217 | Restrict Missing Damage By DateRange | Could | functional | 1 |
| REQ-218 | Sort In Transit Report By Due Date | Could | functional | 1 |
| REQ-219 | Combine Purge Criteria In Selection | Could | functional | 1 |
| REQ-220 | Combine Purge Criteria With Logical AND | Could | functional | 1 |
| REQ-221 | Configure Purge By Last Circulation Interval | Could | functional | 1 |
| REQ-222 | Configure Purge By Status Duration Months Years | Could | functional | 1 |
| REQ-223 | Configure Purge Criteria By Item Attributes | Could | functional | 1 |
| REQ-224 | Provide Purge Candidate Read Only | Could | functional | 1 |
| REQ-225 | Require Purge Deletion Confirmation | Could | functional | 1 |
| REQ-226 | Schedule Purge Utility Automatic Runs | Could | functional | 1 |
| REQ-227 | Provide Purge Selection And Status Conversion Report | Could | functional | 1 |
| REQ-228 | Separate Purge Candidates From Deletions | Could | functional | 1 |
| REQ-229 | Aggregate Deletions By Location And Branch | Could | functional | 1 |
| REQ-230 | Aggregate Deletions By Record Type | Could | functional | 1 |
| REQ-231 | Aggregate Deletions By Staff Member | Could | functional | 1 |
| REQ-232 | Aggregate Deletions By System Scope | Could | functional | 1 |
| REQ-233 | Filter Deletion Audit By Reporting Period | Could | functional | 1 |
| REQ-234 | Provide Deletion Audit Query Interface | Could | functional | 1 |
| REQ-235 | Rank Deleting Staff By Count | Could | functional | 1 |
| REQ-236 | Report Total Deletions By Period | Could | functional | 1 |
| REQ-237 | Track Denied Deletion Attempts | Could | functional | 1 |
| REQ-238 | Count Holds By Placement Method | Could | functional | 1 |
| REQ-239 | Report Holds And Checkouts Counts | Could | functional | 1 |
| REQ-240 | Apply Multiple Patron Filters Together | Could | functional | 1 |
| REQ-241 | Calculate Age Range From Birthdate | Could | functional | 1 |
| REQ-242 | Combine Circulation And Demographics | Could | functional | 1 |
| REQ-243 | Configure Patron Age Range Boundaries | Could | functional | 1 |
| REQ-244 | Filter And Group Patrons By ZIP Code | Could | functional | 1 |
| REQ-245 | Limit And Group Patron Reports By Age Range | Could | functional | 1 |
| REQ-246 | Provide Checkout Period Patron Filters | Could | functional | 1 |
| REQ-247 | Report Patron County Of Residence | Could | functional | 1 |
| REQ-248 | Report Patron Type As Characteristic | Could | functional | 1 |
| REQ-249 | Support Null Demographic Values | Could | functional | 1 |
| REQ-250 | Combine Filters With AND Or | Could | functional | 1 |
| REQ-251 | Filter Patron By Home Branch | Could | functional | 1 |
| REQ-252 | Group Results By Home Branch | Could | functional | 1 |
| REQ-253 | Separate Age Brackets Per Report | Could | functional | 1 |
| REQ-254 | Cache Inactive Report Results | Could | non-functional | 1 |
| REQ-255 | Configure Inactivity Threshold Days | Could | functional | 1 |
| REQ-256 | Count Electronic Activity For Inactivity | Could | functional | 1 |
| REQ-257 | Count Inactive Patrons By Branch | Could | functional | 1 |
| REQ-258 | Determine Most Recent Electronic Activity | Could | functional | 1 |
| REQ-259 | Exclude Patron Categories From Report | Could | functional | 1 |
| REQ-260 | Export Inactive Report CSV | Could | functional | 1 |
| REQ-261 | Generate Inactive Reports Background | Could | non-functional | 1 |
| REQ-262 | Include Inactive Patron Mailing Address | Could | functional | 1 |
| REQ-263 | Track Inactive Patrons With Fines | Could | functional | 1 |
| REQ-264 | Support Level Reports With Extras | Could | functional | 1 |
| REQ-265 | Include Uncataloged Item Circulation | Could | functional | 1 |
| REQ-266 | Retain Deletion Reasons Audit | Could | functional | 1 |
| REQ-267 | Migrate Report Configurations Between Environments | Could | functional | 1 |
| REQ-268 | Queue Background Complex Reports | Could | functional | 1 |
| REQ-269 | Use PostgreSQL Relational Joins | Could | constraint | 2 |
| REQ-270 | Execute Transaction Safe Batch Updates | Could | non-functional | 1 |
| REQ-271 | Generate Printable Transfer Pull Lists | Could | functional | 1 |
| REQ-272 | Generate Printable Transit Labels | Could | functional | 1 |
| REQ-273 | Keep Items Checked Out At Destination | Could | functional | 1 |
| REQ-274 | Log Transfer Activity History | Could | functional | 1 |
| REQ-275 | Manually Select Items For Transfer | Could | functional | 1 |
| REQ-276 | Notify Designated Transfer Exceptions | Could | functional | 1 |
| REQ-277 | Preview And Confirm Transfer Changes | Could | functional | 1 |
| REQ-278 | Process Large Transfers In Batches | Could | non-functional | 1 |
| REQ-279 | Restrict Transfer Roles Authorization | Could | constraint | 1 |
| REQ-280 | Revert Transfers On Status Change | Could | functional | 1 |
| REQ-281 | Share Saved Transfer Queries | Could | functional | 1 |
| REQ-282 | Support Temporary Event Transfers | Could | functional | 1 |
| REQ-283 | Undo Transfer Operation Effect | Could | functional | 1 |
| REQ-284 | CSV Report Export Results | Could | functional | 1 |
| REQ-285 | Cancel Scheduled And Running Reports | Could | functional | 1 |
| REQ-286 | Cancellation Signal Checks During Processing | Could | constraint | 1 |
| REQ-287 | Complete Current Consolidated Branch Data | Could | non-functional | 1 |
| REQ-288 | Enterprise Infrastructure Dependency | Could | constraint | 1 |
| REQ-289 | Excel Report Export Results | Could | functional | 1 |
| REQ-290 | Global Admin Role Access | Could | functional | 1 |
| REQ-291 | HTML Report Output Results | Could | functional | 1 |
| REQ-292 | Indirect Patron Access Via OPAC | Could | functional | 1 |
| REQ-293 | Library Manager Limited Template Changes | Could | functional | 1 |
| REQ-294 | Optional Vendor Integration Data Handling | Could | constraint | 1 |
| REQ-295 | Query Specific Error Feedback | Could | functional | 1 |
| REQ-296 | Read Only Enterprise Data Interface | Could | constraint | 1 |
| REQ-297 | Read Only OPAC Transaction Querying | Could | constraint | 1 |
| REQ-298 | Separated Training Environment | Could | non-functional | 1 |
| REQ-299 | Staff Role Permission Restricted Reporting | Could | functional | 1 |
| REQ-300 | Survey Name To ID Resolution | Could | functional | 1 |
| REQ-301 | Calculate Item Value From Purchase Price | Could | functional | 1 |
| REQ-302 | Enforce Archived Data Retention | Could | constraint | 1 |
| REQ-303 | Join Patron And Item Financial Data | Could | functional | 1 |
| REQ-304 | Report Accrued Fines By Period | Could | functional | 1 |
| REQ-305 | Track Payments By Collecting Branch | Could | functional | 1 |
| REQ-306 | Compare Data Across Branches | Could | functional | 1 |
| REQ-307 | OPAC And Vendor Data Integration | Could | functional | 1 |
| REQ-308 | PINES Reports Templates Provision | Could | functional | 1 |
| REQ-309 | Process Reports In Background | Could | functional | 1 |
| REQ-310 | Provide Board Predefined Reports | Could | functional | 1 |
| REQ-311 | Provide Collection Weeding Reports | Could | functional | 1 |
| REQ-312 | Provide Data Quality Assessment Reports | Could | functional | 1 |
| REQ-313 | Provide Director Level Financial Reports | Could | functional | 1 |
| REQ-314 | Provide Inventory And Capacity Reports | Could | functional | 1 |
| REQ-315 | Provide Shelf Space Utilization | Could | functional | 1 |
| REQ-316 | Reliable Network Connectivity | Could | non-functional | 1 |
| REQ-317 | Report Missing Damaged Items By Branch | Could | functional | 1 |
| REQ-318 | Server OS Compatibility | Could | constraint | 1 |
| REQ-319 | Clone Report Template Preserve Original | Could | functional | 1 |
| REQ-320 | Display Report Submission Timestamp | Could | functional | 1 |
| REQ-321 | Provide Universal Record Query Interface | Could | functional | 1 |
| REQ-322 | Select Regular Expressions From Dropdown | Could | functional | 1 |
| REQ-323 | Show Report Queue Processing Position | Could | functional | 1 |
| REQ-324 | Clone Templates With Restricted Changes | Could | functional | 1 |
| REQ-325 | Enable Regex In Query Builder | Could | functional | 1 |
| REQ-326 | Provide Query Picklists By Record | Could | functional | 1 |
| REQ-327 | Allow Add Canned Reports By Permission | Could | functional | 1 |
| REQ-328 | Allow Authorized Ad Hoc Reports | Could | functional | 1 |
| REQ-329 | Allow Email Report Delivery | Could | functional | 1 |
| REQ-330 | Allow Local Admin Reports | Could | functional | 1 |
| REQ-331 | Allow Partial Data Selection | Could | functional | 1 |
| REQ-332 | Archive Transactions With Patron Privacy | Could | constraint | 1 |
| REQ-333 | Assist Batch Status Conversion | Could | functional | 1 |
| REQ-334 | Combine Canned Report Outputs | Could | functional | 1 |
| REQ-335 | Control Selected Item Transfers | Could | functional | 1 |
| REQ-336 | Cross Row MARC Field Retrieval | Could | functional | 1 |
| REQ-337 | Custom Locally Defined Report Support | Could | functional | 1 |
| REQ-338 | Display Patron Checkouts Holds | Could | functional | 1 |
| REQ-339 | Display Query Criteria With Results | Could | functional | 1 |
| REQ-340 | Display Report Selection Criteria | Could | non-functional | 1 |
| REQ-341 | Edit Canned Report Display Fields | Could | functional | 1 |
| REQ-342 | Edit Canned Report Display Options | Could | functional | 1 |
| REQ-343 | Edit Recurring Report Configurations | Could | functional | 1 |
| REQ-344 | Enable Elevated Local Administrator Config | Could | functional | 1 |
| REQ-345 | Excel Export Duplicate Row Prevention | Could | functional | 1 |
| REQ-346 | Exclude Renewal From Checkin | Could | functional | 1 |
| REQ-347 | Fine Grained Report Permission Control | Could | functional | 1 |
| REQ-348 | Flatten MARC Fields In Row | Could | functional | 1 |
| REQ-349 | Generate Hold And Checkout Reports | Could | functional | 1 |
| REQ-350 | Generate Pivot Table Reports | Could | functional | 1 |
| REQ-351 | Group Transactions By Hour | Could | functional | 1 |
| REQ-352 | Group Transactions By System | Could | functional | 1 |
| REQ-353 | Group Transactions By Terminal | Could | functional | 1 |
| REQ-354 | Identify Bibliographic MARC Missing Fields | Could | functional | 1 |
| REQ-355 | Identify Inactive Patron Accounts | Could | functional | 1 |
| REQ-356 | Implement Consortium Level ILS Changes | Could | functional | 1 |
| REQ-357 | Indicate Last Circulation Date | Could | functional | 1 |
| REQ-358 | Integrate Online Help With Reports | Could | functional | 1 |
| REQ-359 | Keep Archived Data Demographically Usable | Could | functional | 1 |
| REQ-360 | List Items By Total Use Count | Could | functional | 1 |
| REQ-361 | List Last Copy Owned Deletions | Could | functional | 1 |
| REQ-362 | List Patrons By Expiration Date | Could | functional | 1 |
| REQ-363 | List Patrons By Survey Answer | Could | functional | 1 |
| REQ-364 | List Patrons With Barred Status | Could | functional | 1 |
| REQ-365 | Manage Report Delivery Recipients | Could | functional | 1 |
| REQ-366 | Manage Report Templates | Could | functional | 1 |
| REQ-367 | Manual Record Selection From Results | Could | functional | 1 |
| REQ-368 | Merge Cataloged Non Cataloged Circulation | Could | functional | 1 |
| REQ-369 | Preserve Report Accuracy After Edits | Could | non-functional | 1 |
| REQ-370 | Prioritize Reports Execution Queue | Could | functional | 1 |
| REQ-371 | Prioritize Selected Report Types | Could | functional | 1 |
| REQ-372 | Process Long Running Reports Background | Could | functional | 1 |
| REQ-373 | Provide Added Items Listing | Could | functional | 1 |
| REQ-374 | Provide Bills Snapshot Reports | Could | functional | 1 |
| REQ-375 | Provide Canned Report Templates | Could | functional | 1 |
| REQ-376 | Provide Check In Count Report | Could | functional | 1 |
| REQ-377 | Provide Checkout Count Report | Could | functional | 1 |
| REQ-378 | Provide Circulation By Dewey | Could | functional | 1 |
| REQ-379 | Provide Circulation Modifier Counts | Could | functional | 1 |
| REQ-380 | Provide Circulation Totals By Type | Could | functional | 1 |
| REQ-381 | Provide Claims Returned Report | Could | functional | 1 |
| REQ-382 | Provide Dewey Breakdown Circulation | Could | functional | 1 |
| REQ-383 | Provide Edited Items Aggregate Count | Could | functional | 2 |
| REQ-384 | Provide Email Address Book | Could | functional | 1 |
| REQ-385 | Provide Executive Georgia Annual Reports | Could | functional | 1 |
| REQ-386 | Provide Fines And Payments Reports | Could | functional | 1 |
| REQ-387 | Provide Item Use Totals And Ranges | Could | functional | 1 |
| REQ-388 | Provide Last Circulation Date | Could | functional | 1 |
| REQ-389 | Provide MARC Data Counts | Could | functional | 1 |
| REQ-390 | Provide MARC Filtered Circulation Counts | Could | functional | 1 |
| REQ-391 | Provide Period Comparison Columns | Could | functional | 1 |
| REQ-392 | Provide Snapshot Bills Reports | Could | functional | 1 |
| REQ-393 | Provide Total Circulation Merged | Could | functional | 1 |
| REQ-394 | Provide Total Items Aggregate Count | Could | functional | 1 |
| REQ-395 | Record Transaction Categories | Could | functional | 1 |
| REQ-396 | Report Accrued Charges By Type | Could | functional | 1 |
| REQ-397 | Report Annual Holds Placed Count | Could | functional | 1 |
| REQ-398 | Report Bibliographic Holds Periodically | Could | functional | 1 |
| REQ-399 | Report Bibliographic Missing MARC Fields | Could | functional | 1 |
| REQ-400 | Report Bibliographic Records Count | Could | functional | 1 |
| REQ-401 | Report Branch Renewal Percentage | Could | functional | 1 |
| REQ-402 | Report Cataloged In House Use Counts | Could | functional | 1 |
| REQ-403 | Report Claims Returned Items | Could | functional | 1 |
| REQ-404 | Report Deleted Last-Copy Items | Could | functional | 1 |
| REQ-405 | Report Detailed Voi ded Transactions | Could | functional | 1 |
| REQ-406 | Report In Transit Items With Holds | Could | functional | 1 |
| REQ-407 | Report IntraPINES Loans By Facility | Could | functional | 1 |
| REQ-408 | Report IntraPINES Loans By System | Could | functional | 1 |
| REQ-409 | Report Inventory Weeding Missing Items | Could | functional | 1 |
| REQ-410 | Report Item Level Holds Periodically | Could | functional | 1 |
| REQ-411 | Report Item Renewal Likelihood | Could | functional | 1 |
| REQ-412 | Report Item Return Average | Could | functional | 1 |
| REQ-413 | Report Items By Bibliographic Text | Could | functional | 1 |
| REQ-414 | Report Items In Transit By Branch | Could | functional | 1 |
| REQ-415 | Report Last Copy Deleted | Could | functional | 1 |
| REQ-416 | Report Location Counts By Home Library | Could | functional | 1 |
| REQ-417 | Report Marked Long Overdue Items | Could | functional | 1 |
| REQ-418 | Report Monthly Noncataloged In House Use | Could | functional | 1 |
| REQ-419 | Report Patron Additions By Month | Could | functional | 1 |
| REQ-420 | Report Patron Counts By Profile Group | Could | functional | 1 |
| REQ-421 | Report Patron Counts By Survey Answer | Could | functional | 1 |
| REQ-422 | Report Patrons With Invalid Branches | Could | functional | 1 |
| REQ-423 | Report Patrons With Note Wording | Could | functional | 1 |
| REQ-424 | Report Previous Month Patron Additions | Could | functional | 1 |
| REQ-425 | Report Received Items For Holds | Could | functional | 1 |
| REQ-426 | Report Records Missing Attached Volumes | Could | functional | 1 |
| REQ-427 | Report Sent Items For Holds | Could | functional | 1 |
| REQ-428 | Report Sent Notice Activity | Could | functional | 1 |
| REQ-429 | Report Total Use Exceeds Threshold | Could | functional | 1 |
| REQ-430 | Report Weeding Below Use Threshold | Could | functional | 1 |
| REQ-431 | Report X Days Not Checked Out | Could | functional | 1 |
| REQ-432 | Restrict Query Tables And Fields | Could | functional | 1 |
| REQ-433 | Reusable Report Template Creation | Could | functional | 1 |
| REQ-434 | Reusable Saved Query Storage | Could | functional | 1 |
| REQ-435 | Revert Item To Origin | Could | functional | 1 |
| REQ-436 | Run Canned Reports Historical Periods | Could | functional | 1 |
| REQ-437 | Run Preset Reports On Demand | Could | functional | 1 |
| REQ-438 | Run Transaction Reports By Time | Could | functional | 1 |
| REQ-439 | Scheduled Recurring Report Execution | Could | functional | 1 |
| REQ-440 | Select Multiple Canned Reports | Could | functional | 1 |
| REQ-441 | Select Regular Expressions From Dropdown | Could | functional | 1 |
| REQ-442 | Separate Checkin And Renewal | Could | constraint | 1 |
| REQ-443 | Separate Reporting From Production | Could | constraint | 1 |
| REQ-444 | Separate Reporting Interfaces By Type | Could | functional | 1 |
| REQ-445 | Show Report Queue Position For Staff | Could | functional | 1 |
| REQ-446 | Show Report Title Hover Tooltips | Could | functional | 1 |
| REQ-447 | Subtotal Holds By Hold Type | Could | functional | 1 |
| REQ-448 | Support Diverse Report Data Sources | Could | functional | 1 |
| REQ-449 | Total Transactions By Patron And Branch | Could | functional | 1 |
| REQ-450 | Track And Verify Financial Transactions | Could | functional | 1 |
| REQ-451 | Transaction Reports Grouping By Dimensions | Could | functional | 1 |
| REQ-452 | Traverse Documented Relationship Joins | Could | functional | 1 |
| REQ-453 | Validate Report Output Reliability | Could | non-functional | 1 |

## Must requirements

### REQ-001 - Configure Shared Report Folders

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The system must provide shared folders for organizing and accessing reports. System administrators must be able to configure each shared folder to allow or disallow staff from running specific reports. This control is needed so staff can access only the reports permitted for them, while administrators can also run ad hoc reports on specific sets of data. The system must preserve the distinction between staff changes to permitted criteria or display fields and changes that would alter restricted report content.

> Shared folders to allow/disallow staff from running specific reports. (`survey_results_2009.txt`)
> Admins can create shared folders to allow or disallow staff from running specific reports, and/or to run ad hoc reports on specific sets of data. (`email_report_features.eml`)

### REQ-002 - Report Missing Damaged Items By Branch

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide periodic reports identifying missing and damaged items, organized by branch and showing counts for auditing. The missing-items report must include items with a system status of missing and items with a system status of lost. Staff need these reports to track collection health and identify patterns in missing or damaged items. The reports must support review by branch so that conditions at individual library locations can be examined.

> - List of Items with a status of Missing (`early_draft_srs_galecia.txt`)
> - List of Items with Missing Status (`evergreen_reference_2009.txt`)

### REQ-003 - Allow Staff Credential Login

**Priority:** Must - Mentioned in 3 documents. Adjusted from Should by model: Staff authentication must support individual identity across login methods.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `early_draft_srs_galecia.txt`, `email_staff_login.eml`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must allow staff to log in with individual username-and-password credentials and should support an optional streamlined method such as swiping an employee card or RFID badge. The system must not require card-based or other streamlined-login hardware, and it must not require either login method, so branches can use supported alternatives. Login rights and privileges must be controlled through security groups or roles, with access control for individuals, workgroups, and arbitrary staff groups.

> 1. System supports (but does not require) streamlined staff login methods, e.g. card swipe or individual login/password. (`email_staff_login.eml`)
> For example, a staff member could swipe a card (like an RFID employee badge) to log in, or alternatively use individual login credentials (username and password). (`early_draft_srs_galecia.txt`)

### REQ-004 - Authenticate Individual Staff Regardless Login

**Priority:** Must - Mentioned in 1 document; strong wording (must). Adjusted from Should by model: Individual staff authentication prevents shared identity/audit breakdown.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must authenticate the specific individual staff member regardless of the login method used. A card swipe or another streamlined method may conveniently identify a staff member, but it must not bypass individual authentication. The system must support streamlined staff login methods without requiring them, because some smaller branches may not have the infrastructure for card readers. Individual authentication is needed to ensure that staff activity is associated with the correct person.

> The system must track WHICH staff member is logged in for audit purposes. The card is just a convenient way to identify the person, but it shouldn't bypass individual authentication entirely. (`email_staff_login.eml`)

### REQ-005 - Control Staff Rights Via Roles

**Priority:** Must - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `early_draft_srs_galecia.txt`, `email_staff_login.eml`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must control staff rights and privileges through assignable security groups or roles for individuals, workgroups, and arbitrary staff groups. Administrators must be able to administer access by assigning or changing a staff member’s role rather than editing individual permissions, so changing permissions is a simple role-assignment change. After login, the system must determine the staff member’s permissions from the assigned role. The role system must support flexible role-based access control.

> CO-4: User rights and privileges will be controlled through security groups and or "roles" that allow access control for individuals, workgroups, and arbitrary staff groups. (`early_draft_srs_galecia.txt`)
> we need user rights and privileges to be controlled through security groups and/or "roles." This would allow access control for individuals, workgroups, and arbitrary staff groups. (`email_staff_login.eml`)

### REQ-006 - Record Authenticated Staff For Audit

**Priority:** Must - Mentioned in 1 document; strong wording (must). Adjusted from Should by model: Recording login identity is necessary for auditing and accountability.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must record which individual staff member is logged in so that staff activity can be audited. This identity must be recorded regardless of whether the staff member uses a card swipe or another login method. A card may provide a convenient way to identify the person, but it must not replace individual authentication or prevent the system from tracking the specific staff member.

> The system must track WHICH staff member is logged in for audit purposes. (`email_staff_login.eml`)

### REQ-007 - Provide Last Copy Items Report

**Priority:** Must - Mentioned in 3 documents; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a last-copy report identifying items that are the last copies at the library-system or consortium level. Staff, particularly catalogers, need this report before deleting items or performing catalog maintenance, including edits to WorldCat entries. The report must help prevent accidental deletion of a system or consortium’s last copy and support review of these items before maintenance.

> - Items that are the last copy in the system (`early_draft_srs_galecia.txt`)
> This is all great. One more thing - the "last copy report" should definitely be available per system, not just per library. We need to make sure no one accidentally deletes the last copy at the consortium level. (`conversations/conv_pines021_item_purging.eml`)

### REQ-008 - Include Null Patron Records

**Priority:** Must - Mentioned in 5 documents; strong wording (must).  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The system must include records with null or blank relevant fields in patron queries and reports, including patrons whose optional characteristics are missing. Missing values must be represented as null where applicable rather than being omitted. This inclusion must apply regardless of the fields being filtered or displayed, so staff receive complete results when limiting or grouping reports.

> Null values should be included in results (`conversations/conv_pines023_patron_characteristics.eml`)
> All nulls and blank fields must be included in the results no matter what is being filtered or displayed (`early_draft_srs_galecia.txt`)

### REQ-009 - Query Transfer Candidate Items

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The system must allow staff to query for items that are candidates for transfer between branches. Query criteria must support relevant characteristics such as section and circulation inactivity, including identifying items in a children’s section that have not circulated in 6 months. This capability is needed when staff prepare batches of items for destinations such as a mobile library unit or an outreach program collection.

> Query for candidate materials (`conversations/conv_pines018_item_transfer.eml`)
> - Ability to query for candidate materials (`early_draft_srs_galecia.txt`)

### REQ-010 - Save Reusable Transfer Queries

**Priority:** Must - Mentioned in 3 documents; strong wording (crucial).  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must allow staff to save transfer queries for repeated use in transfer operations. Saved queries are needed for recurring collection-balancing and special-program activities, including monthly transfers of items in a specified genre that have not circulated in 6 months. The saved queries must support repeated selection of transfer candidates without requiring staff to recreate the query each time.

> The "save queries for repeated use" is crucial. We do this monthly - move all items in genre X that haven't circulated in 6 months. (`conversations/conv_pines018_item_transfer.eml`)
> - Ability to save queries for repeated use (`conversations/conv_pines018_item_transfer.eml`)

### REQ-011 - Assign Roles Access Levels

**Priority:** Must - Mentioned in 2 documents. Adjusted from Should by model: RBAC and branch-level admin access; security-critical permissions.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must control access through roles or security groups that can be assigned to individuals, workgroups, and arbitrary staff groups. Access levels must include Patron, Staff, Local Admin, and Global Admin, with Global Admin having full system access and Staff operating within assigned permissions. Local Admins, who serve as branch managers, must have branch-level reporting and configuration access, and changing permissions should be achievable by changing a role assignment.

> The permission system needs to be controlled through security groups and/or "roles." (`interview_sysadmin_2009-05-10.txt`)
> - Local Admin: Branch-level reporting and configuration (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-012 - Non Degrading OPAC Reporting Separation

**Priority:** Must - Mentioned in 2 documents; strong wording (must). Adjusted from Should by model: Must not degrade OPAC performance; critical system performance isolation.  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The management reporting system must remain separate from the public catalog and must not constrain or slow down the OPAC. Large or resource-intensive reporting queries must not degrade patrons’ fast, responsive access to the catalog. This requirement applies whenever the reporting system is running a report, including when it is performing a big query.

> "We absolutely cannot constrain the OPAC," Robert emphasized. "The management reporting system is separate from the public catalog. If a report is running, it should not slow down the OPAC." (`meeting_tech_subcommittee_2009-06-30.txt`)
> The management reporting system must not constrain the OPAC in any way. These are separate concerns. Patrons need fast, responsive access to the catalog. (`interview_sysadmin_2009-05-10.txt`)

### REQ-013 - Provide Section 508 Accessibility

**Priority:** Must - Marked as priority in the source document.  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must meet applicable accessibility requirements, including Section 508, and must work with screen-reading software, screen-magnification software, and other assistive technology programs. It must support screen readers such as JAWS and NVDA and screen magnification software such as ZoomText. HTML output must be properly structured with alt tags, ARIA labels, semantic HTML, and standards-compliant HTML. This capability is needed so staff, including blind staff members, can run reports and use the system.

> OE-5: The system must be accessible with screen-reading software, screen- magnification software, and other assistive technology programs designed to increase accessibility. (`early_draft_srs_galecia.txt`)
> As a public institution, we MUST comply with Section 508 accessibility requirements. (`interview_sysadmin_2009-05-10.txt`)

### REQ-014 - Queue Background Report Processing

**Priority:** Must - Marked as priority in the source document.  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_sysadmin_2009-05-10.txt`

The system must process searches and reports during open hours without disrupting other system functions, including circulation operations. This capability is needed because complex reports may otherwise tie up the database and slow the circulation client during peak hours. The system should support background processing or queuing, or otherwise provide processing that prevents report generation from affecting circulation operations. Staff need this capability to run searches and reports while library services remain operational.

> It is highly desirable that searches and reports can be processed during open hours without disrupting other system functions. (`early_draft_srs_galecia.txt`)
> The key requirement is that searches and reports can be processed during open hours without disrupting other system functions. (`interview_sysadmin_2009-05-10.txt`)

### REQ-015 - Support Validated Server Environments

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must operate in the validated server environments, including Linux and Solaris, with support for Red Hat Enterprise Linux and Solaris 10 on SPARC hardware. It must also support Microsoft Internet Explorer version 6.0 and later and Mozilla Firefox version 2.0 and later when browser access is used. This requirement is needed because the library environment includes both Linux and Solaris servers and locations using different browser standards. Staff need access through the browsers retained in those library environments.

> OE-2: The system must operate on a Linux or Solaris server environment. (`early_draft_srs_galecia.txt`)
> So any reporting system needs to work on both Linux and Solaris. (`interview_sysadmin_2009-05-10.txt`)

### REQ-016 - Enforce Mandatory Role Based Access

**Priority:** Must - Mentioned in 1 document; strong wording (essential). Adjusted from Should by model: Role-based access enforcement restricts data/functionality; core security.  
**Type:** functional  
**First mentioned:** 2009-05-12  
**Sources:** `interview_sysadmin_2009-05-10.txt`

The system must enforce role-based access control so that functionality or data is restricted according to the patron or staff role assigned. Access restrictions must be applied as an essential control rather than treated as optional functionality. The system must therefore ensure that each role receives only the functionality or data permitted for that role.

> - Role-based access control is confirmed as essential (`interview_sysadmin_2009-05-10.txt`)

### REQ-017 - Provide Cross Linked HTML Help

**Priority:** Must - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-05-12  
**Sources:** `early_draft_srs_galecia.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide online help in HTML, organized hierarchically and containing cross-links between related topics to support navigation. The help must describe and illustrate all system functions, including major processes and standard reports. It must be available within the system so staff can find documentation without leaving the system, and it must work with screen readers.

> Also, the help system needs to be online, hierarchical, and cross-linked. (`interview_sysadmin_2009-05-10.txt`)
> UD-3: The system must provide an online, hierarchical, and cross-linked help system in HTML that describes and illustrates all system functions. (`early_draft_srs_galecia.txt`)

### REQ-018 - Cancel Scheduled Running Reports

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The system must allow staff or authorized processes to cancel a report that has been scheduled to run or is currently running. This capability is needed when a scheduled or active report should no longer continue processing. For a running report, the system must check for cancellation signals during report processing so that cancellation can take effect. The cancellation function must apply to both scheduled reports and reports already in progress.

> Ability to cancel a report that has already been scheduled to run or is currently running (`early_draft_srs_galecia.txt`)
> - No ability to cancel a running report (`evergreen_reference_2009.txt`)

### REQ-019 - Provide Real Time Reporting Results

**Priority:** Must - Mentioned in 4 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The system must provide real-time reporting against current data so that report results reflect current conditions. Staff need this capability for situations such as determining what is overdue today and for reporting during busy periods. Real-time reporting must be available in addition to historical reporting, which may require a reporting warehouse for obtaining data from a given date or date range. The system must also include null and blank fields in results regardless of filtering or display selections.

> - No real-time reporting (all reports are run on current data) (`evergreen_reference_2009.txt`)
> "Some reports need to be real-time - like 'what's overdue today,'" Robert said. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-020 - Access Management Via Web Or Client

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must make Management Processes accessible through a web browser or through a client compatible with Microsoft Windows. This flexibility is needed because some libraries prefer browser-based access that requires no client installation, while others prefer a dedicated client for better performance. The access method must therefore accommodate both library preferences. Staff and other authorized personnel who perform Management Processes need to be able to access them through one of these supported approaches.

> OE-3: The system must be accessible through a web browser or a Windows-compatible client. (`early_draft_srs_galecia.txt`)
> Management Processes shall be accessible through a web-browser or a Windows-compatible client. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-021 - Preserve OPAC Module Functionality

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The Management Processes requirements and implementation must not constrain or reduce the functionality or features of the Online Public Access Catalog module. Management reporting and related changes must remain separate from the public-facing catalog. The system must therefore ensure that changes to management reporting do not affect patron access to the Online Public Access Catalog.

> CO-5: These requirements must not constrain functionality or features of the Online Public Access Catalog (OPAC) module. (`early_draft_srs_galecia.txt`)
> These requirements shall not constrain functionality or features of the Online Public Access Catalog (OPAC) module. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-022 - Process Reports Without Disruption

**Priority:** Must - Marked as priority in the source document.  
**Type:** non-functional  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The management processes must support a library consortium with 286 locations, 17 million annual circulations, and the purchasing and processing of more than 900,000 items per year. The system should allow searches and reports to be processed during open hours without disrupting other system functions. This capacity is needed to support the management needs of a large, multiple-system library consortium. The requirement applies to management processes across the consortium.

> OE-1: The system must support a library consortium with 286 locations, 17 million annual circulations, and purchasing/processing over 900,000 items per year. (`early_draft_srs_galecia.txt`)
> Management Processes must support the needs of a large, multiple-system library consortium. Specifically, the system must support a library consortium with 286 locations, 17 million annual circulations, purchasing and processing over 900,000 items per year. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-023 - Provide Management Process Data Specifications

**Priority:** Must - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The developer must provide complete data specifications for records maintained or accessed by the Management Processes. The specifications must cover authority records, bibliographic records, order records, item records, hold/request records, and other applicable records. The documentation should include data dictionaries so staff can understand the data structures and write effective queries.

> UD-1: The developer must provide complete data specifications for authority records, bibliographic records, order records, item records, hold/request records, and other records maintained or accessed by the Management Processes. (`early_draft_srs_galecia.txt`)
> UD-1: The software developer shall provide complete data specifications for authority records, bibliographic records, order records, item records, hold/request records, and other records maintained or accessed by Management Processes. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-024 - Control Template Allowed Filter Fields

**Priority:** Must - Mentioned in 2 documents. Adjusted from Should by model: Prevents prohibited content and deleted-item leakage; legal/content integrity risk.  
**Type:** constraint  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must allow administrators to create report templates that staff can run as-is or modify for individual needs. Administrators must be able to limit which filters and display fields staff may alter so that template changes do not compromise result accuracy. Staff may adjust permitted options, such as a call number range or display fields from a pick list. Staff must not be able to modify a template to expose prohibited content, including deleted items.

> Front-line staff can set a call number range for a weeding report or add/remove display fields from a pick list, but can't alter the template to display deleted items. (`email_report_features.eml`)
> For example, front-line staff could set a call number range for a weeding report or add/remove display fields from a pick list, but they should not be able to alter the template to display deleted items. (`early_draft_srs_galecia.txt`)

### REQ-025 - Produce Standards Compliant Web HTML

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

Web-based system components must produce HTML that complies with applicable standards. This requirement applies to all web-based components and includes the HTML output they produce. Standards-compliant HTML is required as a high-priority design and implementation constraint. The requirement affects web output for report display, the help system, and other web-based user interface components.

> CO-2: The system must produce standards-compliant HTML output for web-based components. (`early_draft_srs_galecia.txt`)

### REQ-026 - Use Fully Relational Data Store

**Priority:** Must - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must use a fully relational database as its back-end data store. This is a design and implementation constraint for the system. The requirement is marked high priority and applies to the back-end data store used by the system. The system must therefore provide a fully relational backend rather than a backend that does not meet this specified constraint.

> CO-1: The system must use a fully relational database back-end. (`early_draft_srs_galecia.txt`)


## Should requirements

### REQ-027 - Allow Complex Query Construction

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Complex query building materially impacts report usefulness.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must support construction of complex queries rather than limiting staff to simple query definitions. This is needed when the basic filtering and sorting capabilities of the report writer are insufficient for the required report criteria. Complex query construction must be available through the report writer used to create custom reports. The source identifies difficulty constructing complex queries and the absence of Boolean operators beyond simple filters as limitations that this requirement addresses.

> - Complex queries are difficult to construct (`evergreen_reference_2009.txt`)

### REQ-028 - Analyze Branch Capacity Distribution

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must provide management reports and analysis tools for analyzing branch capacity and determining the optimal distribution of the collection across branches. This capability is needed to support management of library services, programs, and policies and to inform planning and oversight. Managers and administrators need the analysis to evaluate how collection resources are distributed among branches. The requirement is limited to management activities and presupposes the general data structures and functionality of a full-fledged ILS.

> Analyzing branch capacity and optimal distribution of the collection. (`early_draft_srs_galecia.txt`)
> - Analyzing branch capacity and optimal distribution of the collection (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-029 - Analyze Patron Demographics Interests

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must support analysis of patron demographics and interests. This capability is needed to support management of library services, programs, and policies and to inform library program planning. Managers and administrators need the resulting analysis to evaluate patron characteristics and interests when planning services and programs. The requirement covers management activities and presupposes the general data structures and functionality of a full-fledged ILS.

> Analyzing the demographics and interests of patrons. (`early_draft_srs_galecia.txt`)
> - Analyzing demographics and interests of patrons (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-030 - Analyze Staff Productivity Workflow

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must provide management reports and analysis tools for analyzing staff productivity and workflow. This capability is needed to support management of library services, programs, and policies and to inform organizational planning and oversight. Managers and administrators need the analysis to evaluate staff productivity and workflow. The requirement is limited to management activities and presupposes the general data structures and functionality of a full-fledged ILS.

> Analyzing staff productivity and workflow. (`early_draft_srs_galecia.txt`)
> - Analyzing staff productivity and workflow (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-031 - Combine Conditions With Boolean Operators

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`

The query tool must support Boolean operators for combining query conditions, including AND and OR. This capability is needed by staff designing queries across bibliographic, item, patron, transaction, and financial records. The interface must provide these operators as part of user-friendly query construction, alongside field selection, picklist values, and regular-expression selection.

> - Use a full range of Boolean operators (`early_draft_srs_galecia.txt`)
> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)

### REQ-032 - Count Non Cataloged Transactions

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must count transactions involving non-cataloged material and include those transactions in circulation statistics and reports. It must provide a circulation report showing the count of non-cataloged transactions, alongside total circulation information that includes cataloged and non-cataloged circulation data. This capability is needed to report the use of materials such as paperback books and children’s board books that are distributed without individual catalog records.

> Ability to count transactions and include in circulation statistics and reports. (`early_draft_srs_galecia.txt`)
> - Non-Cat Count (`early_draft_srs_galecia.txt`)

### REQ-033 - Create Controlled Report Templates

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`

The system must enable administrators to create report templates and make those templates available to staff. Each template must be runnable as-is or modifiable for individual reporting needs. Administrators must be able to restrict which filters and display fields individual staff may alter. These restrictions are required to certify dependable output and ensure that template changes do not compromise result accuracy.

> System administrators should be able to create report templates that are available to staff. (`early_draft_srs_galecia.txt`)
> Admins need to create report templates that are available to staff. (`email_report_features.eml`)

### REQ-034 - Deliver Reports Via Email

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The system must support delivering generated reports by email, including reports that are scheduled to run at regular intervals. Staff must be able to receive reports through email rather than being limited to downloading them from the web interface. This capability is needed for scheduled reporting, although the available scheduling intervals are limited to daily, weekly, and monthly in the stated situation.

> - No email delivery of reports (`evergreen_reference_2009.txt`)
> - No email delivery (reports can only be downloaded from the web interface) (`evergreen_reference_2009.txt`)

### REQ-035 - Export Reports Multiple Formats

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The reporting system must generate and export reports in multiple formats, including Excel, CSV, and HTML. Staff need these formats to select an appropriate output when using reports and report templates. The system should support these formats for report results and saved or recurring report use, consistent with the requirement for multiple output formats.

> Provide multiple output formats and scheduling options (`evergreen_reference_2009.txt`)
> Output would be in Excel, HTML, and CSV format (`early_draft_srs_galecia.txt`)

### REQ-036 - Generate Consortium Statistical Reports

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must allow the global system administrator to generate statistical reports for the entire library consortium. The global system administrator manages the ILS at the consortium level and is responsible for generating statistical reports for the entire system. These reports are needed by library administrators and library directors, who require aggregated, high-level information for strategic planning, service priorities, and board presentations. The reporting scope must cover the consortium as a whole.

> The individual(s) who manage the ILS at the consortium level, implementing software changes and configurations, and generating statistical reports for the entire system. (`early_draft_srs_galecia.txt`)
> Global System Administrator: Manages PINES at the consortium level, implementing software changes and configurations, and generating statistical reports for PINES as a whole. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-037 - Provide Currently Checked Out Items

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide an items report listing items that are currently checked out. This report is needed when staff must review the items presently checked out. The system may also provide a count of currently checked-out items, in addition to the item listing.

> - Items Currently Checked Out (`early_draft_srs_galecia.txt`)

### REQ-038 - Provide Deleted Items Count

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a predefined report showing the number of items deleted. This report is needed for staff to review item deletion activity as part of item reporting. The report must present a count rather than a list of deleted items. Items deleted must be treated as a distinct report category from items added, edited, or otherwise counted.

> - Items Deleted Count (`early_draft_srs_galecia.txt`)

### REQ-039 - Provide Detailed Aged Debt Categorization

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a detailed report categorizing debt by age. Staff need this report to review bills currently owed by patrons and to analyze aged debt as part of bills reporting. The report must provide sufficient detail to distinguish debt according to its age rather than presenting only an undifferentiated debt total. This capability is identified as partially available and must be enhanced to support the detailed aged-debt reporting requirement.

> - Aged Debt detailed report (partially available, needs enhancement) (`evergreen_reference_2009.txt`)
> - Aged Debt (`early_draft_srs_galecia.txt`)

### REQ-040 - Provide Item Additions Canned Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a predefined item report showing the number of items added. The report should be available among the item reports used for library reporting. Staff need this report to review item additions as part of the available reporting functions. If item reporting is scheduled, scheduling is limited to daily, weekly, or monthly intervals, and reports can only be downloaded from the web interface.

> - Items Added Count (`evergreen_reference_2009.txt`)

### REQ-041 - Provide Management Reporting Tools

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must provide management reports and analysis tools for managers, administrators, and staff to evaluate organizational performance and support planning and oversight. Reports must support analysis of the collection and its use by patrons, branch capacity and collection distribution, patron demographics and interests, staff productivity and workflow, and financial transactions. Library managers need reports for planning and evaluation, while library administrators require aggregated, high-level reports for strategic planning and board presentations. The global system administrator must be able to generate statistical reports for the entire system.

> Analyzing the Library collection and its use by patrons. (`early_draft_srs_galecia.txt`)
> - Analyzing the Library collection and its use by patrons (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-042 - Provide Outstanding Patron Bills Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report listing bills currently owed by patrons. Staff need this report to review outstanding patron bills as part of the available bills reporting functions. The bills reports also include detailed payments received, detailed forgive, work, and goods payments received, detailed voids, and aged debt. If the report is scheduled, scheduling is limited to daily, weekly, or monthly intervals, with no hourly scheduling or email delivery; reports can only be downloaded from the web interface.

> - Bills Currently Owed by Patrons (`evergreen_reference_2009.txt`)
> - Bills currently Owed by Patrons (`early_draft_srs_galecia.txt`)

### REQ-043 - Provide Patron Counts By Home

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report showing patron counts grouped by home library or home branch. Staff need this report to examine patron counts according to the patron’s associated library location. Queries and reports may be limited or grouped by patron characteristics, including home branch, age range, zip code, county of residence, patron type, and preferred language. The report should therefore support home library grouping as a patron reporting characteristic.

> - Patron Count by Home Library (`evergreen_reference_2009.txt`)

### REQ-044 - Provide Renewal Count Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a predefined report showing the number of renewals. The renewal count must be available as a distinct circulation report rather than being combined with checkout counts or total circulation counts. The reporting sources identify limitations including no report queue visibility, no ability to prioritize or cancel reports, no scheduling choices, and no email delivery of reports.

> - Renewals Count (`early_draft_srs_galecia.txt`)

### REQ-045 - Provide Shelving Location Counts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide circulation counts organized by shelving location. Staff need this report to examine circulation activity according to where items are shelved within the library collection. The report must be available as a circulation report alongside checkout counts, renewal counts, non-cataloged counts, and total circulation counts. The source also lists circulation by shelving location among the predefined circulation reports, while noting general limitations on complex queries and available field selection.

> - Circulation Count by Shelving Location (`early_draft_srs_galecia.txt`)

### REQ-046 - Provide Total Patron Count

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report showing the number of patrons. This report is needed for patron reporting and must be available alongside patron counts by home library. Staff need the report to determine the overall number of patrons, independently of breakdowns by location. The source also indicates that some reports may be scheduled to run at regular daily, weekly, or monthly intervals, but scheduling options are limited.

> - Patron Count (`early_draft_srs_galecia.txt`)

### REQ-047 - Report Detailed Payments Received

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide detailed reports of payments received by the library. These reports must include payments received through forgive, work, and goods payment methods, in addition to detailed payments received generally. Staff need these reports as part of bills reporting to review payment activity and related patron account information. Reports may be scheduled at regular intervals, but scheduling is limited to daily, weekly, or monthly intervals, with no hourly scheduling or email delivery.

> - Detailed Payments Received (`early_draft_srs_galecia.txt`)
> - Detailed Forgive, Work, and Goods Payments Received (`early_draft_srs_galecia.txt`)

### REQ-048 - Report Missing Item Records

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide reports identifying bibliographic records that have no associated item records or attached volumes. These reports are needed to support data quality review and maintain data integrity by revealing incomplete bibliographic records. Cataloging staff and other authorized staff must be able to use the reports to identify records requiring attention.

> Data quality reports - items with invalid item type, items with long call numbers, bibliographic records with no item records. (`interview_cataloging_2009-05-08.txt`)
> - Bibliographic records with no item records (`early_draft_srs_galecia.txt`)

### REQ-049 - Report Overdue Items By Days

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report identifying items overdue by a specified number of days. The report must support the overdue-by-X-days condition and include information for daily use, shelf reading, and patron contact. Staff need this circulation report to identify overdue items and support the listed daily, shelf-reading, and patron-contact activities.

> - Items overdue by X days (daily, shelf reading, patron contact info) (`early_draft_srs_galecia.txt`)
> - Items Overdue by X Days (`evergreen_reference_2009.txt`)

### REQ-050 - Schedule Recurring Canned Reports

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must let staff schedule canned reports to run immediately or on a recurring basis. Scheduling options must include hourly, daily, weekly, monthly, and yearly runs, so staff can obtain reports at the required interval without manually initiating each run. The system must support the canned-report interface for generic reports that staff select for immediate or recurring execution. These options address the stated limitation of existing scheduling, which lacks hourly runs.

> Provide multiple output formats and scheduling options (`evergreen_reference_2009.txt`)
> a) Canned reports - generic reports set to run by the individual either ASAP or recurring (`early_draft_srs_galecia.txt`)

### REQ-051 - Show Queue Status For Reports

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `email_report_features.eml`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The reporting interface must allow staff to view reports in the processing queue and see the submitted report’s position or current processing status. It must indicate whether a report is waiting, running, completed, or failed, and may also show its status and priority as part of queue visibility. This capability is needed because staff require feedback after submitting reports and must be able to monitor processing rather than receive no response.

> Status (waiting, running, completed, failed) (`email_report_features.eml`)
> REPORTS QUEUING: See position in queue, status, priority. (`email_report_features.eml`)

### REQ-052 - Generate Material Volume Report

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must generate a material-volume report for a specified library that counts all items assigned to that library, including items checked in and checked out. The report must account for new acquisitions, items on the shelf, and items out in circulation, and must support reporting the volume as of a selected point in time. Staff need this report for collection management, monthly board reporting, and historical comparison without manually combining information from multiple screens. The report must support category-based volume reporting.

> Quick question - how do I get a report that tells me how many items we have at Dalton-Whitman at any given moment? Not just total count, but broken down by categories. (`conversations/conv_pines014_material_volume.eml`)
> The volume should include: 1. New acquisitions (items recently added) 2. Items on the shelf (checked in) 3. Items out in circulation (checked out) (`conversations/conv_pines014_material_volume.eml`)

### REQ-053 - Report Category Holds With Counts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`, `early_draft_srs_galecia.txt`

The system must provide category breakdowns in the material-volume report for a specified library, including total items in the library, holds, adult fiction, and board books. For each applicable category, the report must show the number of holds as well as the category’s item count. The report should group items by categories such as fiction, non-fiction, or format and support reporting at a selected point in time. Staff need these breakdowns for collection management and historical comparisons.

> Shows breakdowns with holds count per category (`conversations/conv_pines014_material_volume.eml`)
> The report should allow breaking down volume in categories such as: - Total items in library - Number of holds - Number of adult fiction - Number of board books (`conversations/conv_pines014_material_volume.eml`)

### REQ-054 - Determine Permissions Via Security Groups

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Manage security groups enables scalable access control.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must allow administrators to create and manage security groups used to control staff access. When a staff member logs in by any method, the system must determine that staff member’s permissions from the assigned security group or role. Security groups support role-based access and must therefore be administered by authorized administrators. Streamlined staff login methods may be supported but must not be required for security-group-based permission determination.

> Administrators should be able to create and manage these groups. (`email_staff_login.eml`)

### REQ-055 - Display All Branch Capacities

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`, `early_draft_srs_galecia.txt`

The system must provide an interface that displays the capacity of every branch simultaneously. Staff need a high-level view of all branches at once to review branch capacity across the library system. The interface must present the branches together rather than requiring staff to inspect each branch separately. It should support the stated all-branch capacity overview while allowing the capacity of the branches to be viewed in the same interface.

> The system should provide an interface showing the capacity of all branches. This should include: - High-level overview of all branches' capacity at once (`conversations/conv_pines015_capacity_interface.eml`)
> The system should provide an interface showing the capacity of all branches. (`early_draft_srs_galecia.txt`)

### REQ-056 - Provide System Administrator Role

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Administrator full access is core to manage system, but role exists.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must provide a system administrator role managed through security groups or roles. System administrators must have full access to all reports and permissions. Access control must support assignment to individuals, workgroups, and arbitrary staff groups, and administration of roles and permissions must be easy.

> System administrators (full access to all reports and permissions) (`email_staff_login.eml`)

### REQ-057 - Compare Shelf Space Percentages

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a shelf-space report that compares, for each genre and format, the percentage of total circulations, the percentage of the collection, and the percentage of total shelf space. This comparison is needed to support collection management and decisions about where to allocate resources. The report must be available for an individual library and for the entire library system.

> What percentage of total shelf space it occupies (`conversations/conv_pines016_shelf_space.eml`)
> The system should provide, for each genre and format of material, the ability to compare: - The percentage of total circulations - The percentage of the collection - The percentage of total shelf space (`conversations/conv_pines016_shelf_space.eml`)

### REQ-058 - Generate Automated Shelf Space Reports

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`, `early_draft_srs_galecia.txt`

The system must generate shelf-space reports without requiring staff to compile the information manually in separate reports or spreadsheets. The reports must compare circulation, collection, and shelf-space percentages for each genre and format so staff can use actual data when considering whether to reallocate space from low-circulation genres to high-circulation genres. Results must be available for an individual library and aggregated for the entire library system.

> Currently I pull reports manually and make spreadsheets. It's tedious. (`conversations/conv_pines016_shelf_space.eml`)
> The report should be able to run per library and per system. (`early_draft_srs_galecia.txt`)

### REQ-059 - Combine In Transit Report Directions

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a single in-transit report that combines information about items traveling to locations and items traveling from locations. The report must identify items that have been in transit for more than a configurable number of days, with seven days as the probable default. It is needed because items can be lost during delivery or transfer between branches, and front-line staff need one report rather than separate transit-to and transit-from reports. The report must support staff monitoring of these items.

> And the report should merge transit-to and transit-from so front-line staff don't have to run two reports. (`conversations/conv_pines019_020_missing_intransit.eml`)
> It should merge the transit-to and transit-from into one report for ease of use. (`interview_cataloging_2009-05-08.txt`)

### REQ-060 - Generate In Transit Items Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`

The system must generate a report listing items that have remained in transit longer than a configurable number of days. Results must be available per branch and for the entire system so staff can investigate delivery problems at a local or system-wide level. The report must combine transit-to and transit-from information into one report for ease of use by front-line staff. This capability is needed because items may be lost in delivery trucks and require review when transit exceeds the configured threshold.

> I need to see what's been in-transit for more than X days (X should be configurable, probably 7 days default). (`conversations/conv_pines019_020_missing_intransit.eml`)
> System generates a list of items that have been in-transit for more than X days (X configurable), per branch and per system. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-061 - Audit Deletions For Multiple Record Types

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `conversations/conv_pines022_deletions.eml`

The system must retain an audit trail for deletions of item records, patron records, and bibliographic records. Each audit record must identify the record type, record identifier, staff member who performed the deletion, deletion timestamp, and location where the deletion occurred. This information is needed for accountability, troubleshooting, and tracking deletions by location and system.

> Fields: record_type, record_id, deleted_by, deleted_at, location (`conversations/conv_pines022_deletions.eml`)
> We need to track who purged what and when. This is for accountability and troubleshooting. (`conversations/conv_pines021_item_purging.eml`)

### REQ-062 - Audit Purge And Deletion Events

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `conversations/conv_pines022_deletions.eml`, `survey_results_2009.txt`

The system must maintain an audit trail for purge and record deletion operations using database triggers that write deletion events to an audit table. Each event must record the deleted record type, deletion timestamp, deleting user, the user’s location, and the relevant location and system scope. The audit trail should optionally capture the record’s pre-deletion status or associated reason, provide a report interface for querying deletions, and support counting and tracking them.

> 3. Audit trail for all purges (`conversations/conv_pines021_item_purging.eml`)
> A trigger in the database that logs deletions to an audit table (`conversations/conv_pines022_deletions.eml`)

### REQ-063 - Cleanup Delete Volume With Items

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a quick, effective cleanup operation that deletes volume entries together with their associated item entries and also deletes records with no items attached. This capability is needed to reduce the time staff spend removing orphaned records and maintaining collection data. The operation should support cleanup of volume and item records as a single action.

> - Provide a quick effective method for deleting volume entries along with copy entries, as well as records with no items attached (`conversations/conv_pines021_item_purging.eml`)
> The system should provide a quick effective method of deleting volume entries along with copy entries, as well as records with no items attached. (`early_draft_srs_galecia.txt`)

### REQ-064 - Convert Item Statuses In Batch

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a report-assisted workflow that allows staff to convert the statuses of multiple items in a single batch operation. This capability is needed when staff must change a group of items from one status to another, such as changing items from missing to discard/weed. The report must assist staff in identifying or managing the items included in the conversion. The workflow must support batch conversion rather than requiring each item to be changed individually.

> - Provide a report to assist in the conversion of items from one status to another (`conversations/conv_pines021_item_purging.eml`)
> The system should have a report to assist in the conversion of items from one status to another. (`early_draft_srs_galecia.txt`)

### REQ-065 - Delete Orphaned Itemless Records

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `interview_cataloging_2009-05-08.txt`

The system must provide a quick and effective operation for deleting records that have no items attached. This capability is needed during cleanup because orphaned records take substantial time to remove manually. Staff responsible for catalog maintenance need the operation to efficiently remove itemless records while managing related record cleanup. The system should support this operation as part of the broader process for deleting obsolete volume and item entries.

> We also need a quick way to delete volume entries along with copy entries, and delete records with no items attached. (`conversations/conv_pines021_item_purging.eml`)
> There also needs to be a quick, effective method for deleting volume entries along with copy entries, as well as records with no items attached. (`interview_cataloging_2009-05-08.txt`)

### REQ-066 - Generate Last Copy Report

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must generate a last copy report that identifies item records representing the only copy within a selected scope, such as a library or system. The report must flag these items so catalogers can review them before deleting or purging records. This is needed to help catalogers update WorldCat entries and avoid accidentally deleting the only copy held by the library system or consortium.

> CRITICAL: We need a "last copy report" that identifies our library system's last copies. This helps catalogers update WorldCat entries so we don't accidentally delete the only copy in the consortium. (`conversations/conv_pines021_item_purging.eml`)

### REQ-067 - Identify Purge Candidates By Configured Criteria

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a utility and reports that identify item records for potential purging according to configurable criteria. Criteria must support item status, including missing, discard/weed, and damaged, as well as how long an item has remained in a status and how long ago it was last circulated. This capability is needed for staff who prepare weeding and purging activities and require flexible identification of item records. The system must support the specified status-based, time-based, and activity-based conditions when selecting records.

> I want the customizable criteria for purging to include: (`conversations/conv_pines021_item_purging.eml`)
> The system should provide a utility and reports for identifying item records to purge, based on customizable criteria such as: (`early_draft_srs_galecia.txt`)

### REQ-068 - Provide Last Copy By Branch

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`, `evergreen_reference_2009.txt`

The system must provide a last-copy report that identifies whether an item is the only copy at an individual branch or across the entire PINES system. Staff need both views when cleaning the database, removing orphaned records, converting statuses, and identifying last copies before deletion. The report must support decisions about deleting the last item at a branch separately from deleting the last item in the entire system, and the partially available capability must be enhanced to provide these views.

> - Last Copy Report (partially available, needs enhancement) (`evergreen_reference_2009.txt`)
> For the last copy report - is this per library or per system? I think we need both views. (`conversations/conv_pines021_item_purging.eml`)

### REQ-069 - Safeguard Against Mass Collection Deletion

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Mass-deletion safeguards; baseline Could but safety suggests Should.  
**Type:** non-functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must provide safeguards that reduce the risk of staff accidentally deleting an entire collection during cleanup or purging. These safeguards are needed when customizable criteria are used to identify records for deletion, because an overly broad cleanup operation could affect the full collection. The system must therefore support safe handling of purge activities so that staff can avoid unintended mass deletion. The requirement applies specifically to cleanup and purging operations.

> "Customizable criteria" is great, but we need to make sure the system is safe - we don't want someone accidentally deleting their entire collection. (`conversations/conv_pines021_item_purging.eml`)

### REQ-070 - Checkout Renewal Counting By Type

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must count checkout and renewal types separately and cumulatively. It must distinguish staff checkout, self checkout, staff renewal, self checkout renewal, online renewal, and OPAC renewal. The resulting transaction reports are needed to examine checkout activity by method and may be grouped by hour, terminal, branch, and system. This reporting must preserve both individual method counts and cumulative totals.

> Check-out types should be counted separately - staff checkout, self checkout, staff renewal, self checkout renewal, online renewal, OPAC renewal (`survey_results_2009.txt`)
> The system counts all types of check-out individually and cumulatively: - staff check-out - self check-out - staff renewal - self checkout renewal - online renewal - OPAC renewal (`early_draft_srs_galecia.txt`)

### REQ-071 - Control Report Create Clone Permissions

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must provide distinct, fine-grained permission levels controlling who may create and clone reports. These permissions are needed to restrict report creation and cloning while allowing authorized staff to perform those activities. System administrators must be able to administer the permissions easily, including limiting staff capabilities so that permitted report modifications do not extend to altering the underlying template.

> Fine-grained permissions limit who can create and clone reports. (`survey_results_2009.txt`)
> The system should provide distinct, fine-grained permission levels that limit who can create and clone reports. (`early_draft_srs_galecia.txt`)

### REQ-072 - Cross Tabulate Multi Dimension Activity

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `survey_results_2009.txt`

The system must support grouping and cross-tabulating transaction and activity data by terminal, branch, system, hour, patron age range, patron type, and patron location. The reports must cover activity such as check-outs, check-ins, holds placed, and holds filled, and this cross-tabulation capability must also be available in predefined reports for library boards and other external consumers. Transaction history is retained for a configurable number of days, while monthly and annual aggregates are retained indefinitely.

> Transactions can be grouped by hour, terminal, branch, and system. (`early_draft_srs_galecia.txt`)
> It should be possible to cross-tabulate per terminal, per branch, per library system, per hour, per patron age range, per patron type, and per patron location. (`early_draft_srs_galecia.txt`)

### REQ-073 - Granular Check In Counting Methods

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must count all types of check-in individually and cumulatively. It must distinguish book-drop, terminal, and user-initiated or self-service check-ins, and report each category individually and cumulatively. These reports are needed to examine transaction activity by check-in method and can be grouped by hour, terminal, branch, and system. Transaction history is retained for a configurable number of days, while monthly and annual aggregates are retained indefinitely.

> I need to see check-in counts broken down by method - book drop vs terminal vs self-service (`survey_results_2009.txt`)
> The system counts all types of check-in individually and cumulatively: - book-drop - by terminal - by user or self-service (`early_draft_srs_galecia.txt`)

### REQ-074 - Provide Demographic Region Patron Stats

**Priority:** Should - Mentioned in 2 documents; strong wording (must).  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must provide patron counts and demographic statistics for transactions by geographic region, including county, city, and ZIP code, and by age range. These reports are needed to analyze patron behavior and to use demographic data for programming planning. The system must exclude personally identifiable information from demographic reports, and the underlying data used to produce them must be anonymized so that a patron cannot be identified.

> The system should produce useful demographic statistics, including transactions by geographical regions, age ranges, etc. (`early_draft_srs_galecia.txt`)
> Transactions by geographical regions - Transactions by age ranges (`survey_results_2009.txt`)

### REQ-075 - Provide Patron Behavior Analytics

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must produce statistics that support understanding and prediction of patron behavior and the use of materials. These statistics must include analysis such as the average speed at which a particular item is returned, the likelihood that a particular item is renewed, and the percentage of check-outs at a particular branch that are renewals. The results must support library analysis and planning, including the use of demographic data for programming.

> The system should produce statistics that can be used to understand and predict patron behavior and use of materials. (`early_draft_srs_galecia.txt`)
> System produces statistics to understand/predict patron behavior and use of materials. (`survey_results_2009.txt`)

### REQ-076 - Retain Transaction History Window

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must retain transaction history for a configurable number of days. It must preserve monthly and annual aggregate transaction information indefinitely after the detailed history period ends. Retained transactions may include check-ins, check-outs, fines collected, and patron registrations, and must support grouping by hour, terminal, branch, and system. Staff need this retained information for transaction reporting by all transactions or by transaction type.

> Transaction history is maintained for X days (X is configurable). (`early_draft_srs_galecia.txt`)
> Monthly and annual aggregate information is maintained indefinitely. (`early_draft_srs_galecia.txt`)

### REQ-077 - Run Or Edit Report Templates

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `survey_results_2009.txt`

The system must allow staff to run an available report template as-is or modify it before execution. For on-demand reporting, staff must be able to edit selection criteria and display options, such as setting a call number range or adding and removing display fields. Modifications must not compromise report results, and administrators should be able to limit which filters and display fields staff may alter. The system must support templates for reporting on circulation, items, patrons, bills, and bibliographic records.

> Report templates can be created by administrators and run as-is or modified. (`survey_results_2009.txt`)
> b) Noncanned or On Demand Reports - preset but have the ability to edit selection criteria and display options (`early_draft_srs_galecia.txt`)

### REQ-078 - Show Report Queue Position

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `email_report_features.eml`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `survey_results_2009.txt`

The system must allow staff to view the report queue’s status or contents, including the current position of their report in the queue. This visibility is needed because report queue status is important when reports are being processed. The system should show where a report is in the queue and may also show its status, priority, and other queue information.

> - Report queue visibility is important (`meeting_minutes/meeting_2009-07-20_minutes.txt`)
> Ability to see where your report is in the queue. (`survey_results_2009.txt`)

### REQ-079 - Track Record Deletions By Location

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-27  
**Sources:** `conversations/conv_pines022_deletions.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must count and track deletions of item and patron records by location and across the entire library system. Tracking must identify the record type, timestamp, staff member who performed the deletion, and the location of that staff member. This capability is needed for auditing, so directors can determine how many records were deleted and why, and for troubleshooting when catalog information goes missing. The system should also track denied deletion attempts to support compliance and troubleshooting.

> Yes, we need to count and track record deletions per location and per system. (`interview_cataloging_2009-05-08.txt`)
> The system should count and track record deletions (e.g., item records, patron records) per location and per system. (`conversations/conv_pines022_deletions.eml`)

### REQ-080 - Allow Grouping By Patron Characteristics

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must allow report results and activity measures, including circulation, checkout, and patron counts, to be grouped by supported patron characteristics. Supported groupings must include age demographics and may include characteristics such as home library when available. Staff need these groupings for program planning, such as examining activity among patrons in a particular age range. The system must support grouping both circulation activity and patron counts by the applicable characteristic.

> - Circulation Count by Age Demographic (`early_draft_srs_galecia.txt`)
> - Circulation Count by Age Demographic (not available) (`evergreen_reference_2009.txt`)

### REQ-081 - Filter Patron Reports By Home Branch

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must allow staff to limit or group patron queries and reports by the patron’s home branch. This capability is needed when staff run reports on patrons grouped by characteristics and need to distinguish patrons according to their associated branch. Home branch must be available as one of the patron characteristics used in reporting. The requirement applies to patron records and supports both restricting report results and organizing them into groups.

> - Home branch (`conversations/conv_pines023_patron_characteristics.eml`)
> Queries and reports can be limited or grouped by various patron characteristics, including: - home branch (`early_draft_srs_galecia.txt`)

### REQ-082 - Limit And Group Preferred Language

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must support preferred language as a patron reporting characteristic. Staff must be able to limit patron queries and reports by preferred language and group results according to that characteristic. This capability is needed for reports on patrons grouped by characteristics, alongside age range, zip code, county of residence, home branch, and patron type.

> - Preferred language (`conversations/conv_pines023_patron_characteristics.eml`)
> Queries and reports can be limited or grouped by various patron characteristics, including: - preferred language (`early_draft_srs_galecia.txt`)

### REQ-083 - Configure Age Range Grouping

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must allow patron queries and reports to be limited by age range and must allow patron results to be grouped by age range. Age range is one of the patron characteristics that may be used for filtering or aggregation, along with ZIP code, county of residence, home branch, patron type, and preferred language. Filters may be combined with AND or OR logic, null values must be included in results, and age ranges must be configurable per report.

> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Age range (`conversations/conv_pines023_patron_characteristics.eml`)
> Queries and reports can be limited or grouped by various patron characteristics, including: - age range (`early_draft_srs_galecia.txt`)

### REQ-084 - Group And Filter Patron County

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must allow staff to filter patron queries and reports by county of residence. It must also allow staff to group patron query and report results by county of residence. This capability is needed for reports organized around patron characteristics, including county of residence. County-based filtering and grouping must be available as part of the patron reporting functions.

> - County of residence (`conversations/conv_pines023_patron_characteristics.eml`)
> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - County of residence (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-085 - Group And Filter Patron Type

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must allow staff to filter patron queries and reports by patron type. It must also allow staff to group patron query and report results by patron type. Patron type is one of the patron characteristics needed for reports organized around patron populations. The capability must support both limiting results to selected patron types and aggregating results by patron type.

> - Patron type (`conversations/conv_pines023_patron_characteristics.eml`)
> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Patron type (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-086 - Group And Filter Patron Zip

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`

The system must allow staff to group patron query and report results by zip code. It must also allow staff to limit patron queries and reports to specified zip codes. Zip code must be supported as a patron characteristic for both grouping and filtering, alongside other characteristics used in patron reporting. Filters may be combined using AND or OR logic, and null values should be included in results.

> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Zip code (`conversations/conv_pines023_patron_characteristics.eml`)
> Queries and reports can be limited or grouped by various patron characteristics, including: - zip code (`early_draft_srs_galecia.txt`)

### REQ-087 - Generate Inactive Patrons Report

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`, `early_draft_srs_galecia.txt`

The system must generate a list of patrons with no circulation or electronic activity during a configurable number of preceding days. Electronic activity includes OPAC login, online hold placement, and online renewals. Staff must be able to configure the report at the system, home library, county, or other needed level, so inactivity can be reviewed at different organizational levels.

> We need a report that shows patrons with no circulation or electronic activity in the last X days. (`conversations/conv_pines024_inactive_patrons.eml`)
> The system should generate a list of patrons with no circulation or electronic activity in the last X days (X configurable). (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-088 - Run Inactive Patron Report Levels

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`, `early_draft_srs_galecia.txt`

The system must allow staff to generate the inactive-patron report at configurable organizational levels. Supported levels must include the system, home library, and county where applicable, with other levels available as needed. This capability is needed to support different reporting and outreach contexts across the organization. The report concerns patrons with no circulation or electronic activity during the configured inactivity period.

> The list should be configurable to different levels - System, Home Library, County, etc. (`conversations/conv_pines024_inactive_patrons.eml`)
> The list should be configurable to System, Home Library, County, etc. (`early_draft_srs_galecia.txt`)

### REQ-089 - Allow Selective Title Transfers

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The item-transfer utility must allow staff to manually select titles from query results for targeted transfers. It should support querying candidate materials and saving queries for repeated use before staff make their selections. This capability is needed when batches of items are moved between branches, including transfers to a mobile library unit or an outreach program collection. The utility must support selective transfer rather than requiring all query results to be moved.

> - Ability to manually select titles from query results (`early_draft_srs_galecia.txt`)
> Third, we need to manually select titles from query results if we want to be more targeted. (`interview_cataloging_2009-05-08.txt`)

### REQ-090 - Automatically Revert Temporary Transfers

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must automatically return transferred items to their original locations after a configured period or when configured time or status criteria are met. This capability is needed for temporary transfers, such as items sent to a mobile library or a book sale and later returned to base. A scheduled task must check transferred items and apply the configured reversion conditions. The system should support date-based reversion, such as reverting after a specified number of days, and status- or event-based reversion.

> Auto-revert mechanism - a scheduled task that checks transferred items and reverts them based on time or status criteria. (`conversations/conv_pines018_item_transfer.eml`)
> Revert after X days (date-based) (`conversations/conv_pines018_item_transfer.eml`)

### REQ-091 - Batch Transfer Items Between Branches

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a utility for transferring multiple items in a single batch between branches and other locations, including mobile libraries, outreach collections, and just-in-time warehouses. Staff must be able to query candidate materials, save queries for repeated use, and manually select titles from query results. The utility must change the records of selected items to the new location, using mechanisms such as changing the location field or generating pull lists. It must also support reverting items to their original location after a set period or based on other criteria.

> We often need to move batches of items between branches - for example, sending books to a mobile library unit or to an outreach program collection. (`interview_cataloging_2009-05-08.txt`)
> I need a utility for transferring batches of items between branches. We often need to move books to a mobile library, to an outreach program, or to a "just-in-time" warehouse. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-092 - Identify Uncataloged Material Usage

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide a way to identify how uncataloged materials are being used. This capability is needed for materials such as paperback books and children’s board books that are distributed quickly without individual catalog records. The system should count transactions involving these materials and include the resulting information in circulation statistics and reports, while requiring minimal branch labor.

> - Ability to identify how the material is being used (`early_draft_srs_galecia.txt`)
> The requirements are: quick distribution (we need to process these fast), minimal branch labor (we can't spend a lot of time per item), and ability to identify how the material is being used. (`interview_cataloging_2009-05-08.txt`)

### REQ-093 - Integrate WorldCat Last Copy

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `interview_cataloging_2009-05-08.txt`

The system must integrate with WorldCat and provide a last-copy report that identifies a library system’s last copies. This capability is needed when catalogers review, edit, or process records and must avoid deleting the last copy of a rare or other significant item without checking WorldCat. Catalogers also need the report to assist with editing WorldCat entries. The system should support this review in conjunction with processing items whose statuses may need to be changed, including batch status changes where applicable.

> And the last copy report is CRITICAL. This singles out a library system's last copies, to assist catalogers who need to edit WorldCat entries. (`interview_cataloging_2009-05-08.txt`)
> The last copy report and WorldCat integration are critical (`interview_cataloging_2009-05-08.txt`)

### REQ-094 - Report Long Transit Items By Branch

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must report items that have remained in transit longer than a specified, configurable number of days. Results must be available by branch and across the entire system so staff can track items transferred between branches and identify items that may have been lost. The report should merge transit-to and transit-from information into one report for ease of use.

> - Items that have been in-transit for more than X days (`early_draft_srs_galecia.txt`)
> The report should show items that have been in-transit for more than X days (configurable), per branch and per system. (`interview_cataloging_2009-05-08.txt`)

### REQ-095 - Track Uncataloged Item Inventory

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must track uncataloged materials as inventory before individual catalog records are created. This capability is needed for shipments such as paperback books and children’s board books that arrive without individual catalog records. It must support quick distribution, minimal branch labor, and transaction counting so staff can manage and report on these materials while they remain uncataloged.

> Ability to control inventory of uncataloged material, such as paperback books and children's board books. (`early_draft_srs_galecia.txt`)
> We need to be able to track these as inventory even though they're not fully cataloged. (`interview_cataloging_2009-05-08.txt`)

### REQ-096 - Update Item Locations For Destinations

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `conversations/conv_pines018_item_transfer.eml`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The transfer utility must allow authorized staff to change the records and related location data of selected items so that the items are assigned to a new location. It must support transfers between branches and other destinations such as a mobile library, an outreach program, or a just-in-time warehouse. The location field may be changed as a mechanism for moving items, and the utility should support generating pull lists. The system must permit items to be reverted to their original location after a set period of time or based on other criteria.

> Change records of selected items to new location - Mechanisms: changing location field, generating pull lists (`conversations/conv_pines018_item_transfer.eml`)
> - Ability to change records of selected items to move to new location (`conversations/conv_pines018_item_transfer.eml`)

### REQ-097 - Provide Separate Dev Training Environments

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide separate development, training, and production environments. Developers must be able to test new reports without affecting production, and new staff members must be able to practice running reports in a training environment without worrying about making mistakes. Configurations developed in development or training must be migratable to production through export and import functionality. This migration must include report templates, permission settings, and other configuration.

> CO-3: The system must provide a development and training environment with the ability to migrate configurations to a production environment. (`early_draft_srs_galecia.txt`)
> - No development/training environment separation (`evergreen_reference_2009.txt`)

### REQ-098 - Report Invalid Item Types Periodically

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide periodic data-quality reports identifying items with invalid item types. Staff need these reports to maintain data integrity and identify records requiring correction. The reporting capability should support this report as part of broader data-quality review, which also includes items with long call numbers and bibliographic records with no item records.

> - Items with invalid item type (`early_draft_srs_galecia.txt`)
> Data quality reports - items with invalid item type, items with long call numbers, bibliographic records with no item records. (`interview_cataloging_2009-05-08.txt`)

### REQ-099 - Report Long Call Numbers Periodically

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system must provide periodic reports identifying items with call numbers that exceed the permitted length. Staff must be able to use these reports as data quality reports to help maintain data integrity. The reporting capability must include long call numbers among the periodic report examples and must identify the affected items.

> - Items with a long call number (`early_draft_srs_galecia.txt`)
> Data quality reports - items with invalid item type, items with long call numbers, bibliographic records with no item records. (`interview_cataloging_2009-05-08.txt`)

### REQ-100 - Show Separate Item Last Edit Date

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `evergreen_reference_2009.txt`, `interview_cataloging_2009-05-08.txt`

The system must show an item's last edit date separately from its last circulation date. The last edit date must represent editing of the item and must not include circulation activity. This capability is needed for data quality reporting and item maintenance because the current reporting data combines these dates, preventing staff from identifying the actual last edit date.

> - Last edit date not including last circulation - does not exist (`evergreen_reference_2009.txt`)
> I need to be able to see the last edit date on reports, but it should be only when the item is edited and not include the last circulation. The current system combines these dates. (`interview_cataloging_2009-05-08.txt`)

### REQ-101 - Support Accessible HTML Standards

**Priority:** Should - Mentioned in 2 documents.  
**Type:** non-functional  
**First mentioned:** 2009-05-10  
**Sources:** `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`

The reporting interfaces and capabilities must support accessibility and applicable HTML standards. The system must enable staff using screen readers, screen magnification software, and other assistive technology to run reports, including blind staff members. HTML output must use alt tags, ARIA labels, and proper semantic structure, and must be standards-compliant. This requirement is needed because the library, as a public institution, must comply with Section 508 accessibility requirements.

> Implement accessibility compliance (`evergreen_reference_2009.txt`)
> - No accessibility support for report interface (`evergreen_reference_2009.txt`)

### REQ-102 - Use Live Database Reporting

**Priority:** Should - Mentioned in 2 documents.  
**Type:** constraint  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system should use the main relational database as the source for reporting data. It should avoid requiring a separate denormalized reporting schema or synchronized reporting warehouse because maintaining synchronization with the live database creates additional problems. Reporting must work with the fully relational structure and support complex analytical queries within that structure.

> I'd prefer to keep everything in the main relational database. (`interview_sysadmin_2009-05-10.txt`)
> "I strongly recommend against denormalization for reporting," Robert said. "Maintaining sync between a reporting warehouse and the live database creates more problems than it solves." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-103 - Provide Searchable Online Report Help

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-05-12  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide online HTML help that staff can use for routine instructions, including instructions for running reports, without contacting IT. The help must be searchable, easy to navigate, hierarchical, and cross-linked so staff can locate related guidance within the system. It must comprehensively describe and illustrate all system functions, including major processes and standard reports. The help must also be accessible to screen-reader users.

> Also, the help system needs to be online, hierarchical, and cross-linked. Staff shouldn't have to call IT every time they want to know how to run a report. (`interview_sysadmin_2009-05-10.txt`)
> The HTML help needs to be searchable and easy to navigate. (`interview_sysadmin_2009-05-10.txt`)

### REQ-104 - Separate Reporting From OPAC

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** constraint  
**First mentioned:** 2009-05-12  
**Sources:** `interview_sysadmin_2009-05-10.txt`

The system must keep reporting functionality separate from the OPAC. This separation is needed to protect patrons’ fast, responsive access to the catalog when reporting activities are performed. A reporting query, including a large query, must not constrain or slow down the OPAC, because reporting and catalog access are separate concerns.

> - Separation of reporting from OPAC is critical (`interview_sysadmin_2009-05-10.txt`)

### REQ-105 - Support Environment Template Migration

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-05-12  
**Sources:** `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide separate development, training, and production environments. It must support exporting and importing templates, permission settings, saved queries, and other relevant configuration between these environments. This capability is needed so staff can migrate configurations while developing, training, and operating the reporting system. The training environment must allow staff to experiment safely without risking production data.

> - No configuration migration between environments (`evergreen_reference_2009.txt`)
> Provide a development/training environment with migration capability (`evergreen_reference_2009.txt`)

### REQ-106 - Centralized Enterprise Management Processes

**Priority:** Should - Mentioned in 3 documents.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must consolidate management processes at a central location while accepting input from and providing services to multiple library locations. It must support the enterprise-level Library Automation System context and use the broader system’s data structures and functionality, including Acquisitions and Cataloging modules. Centralization is needed to provide consistent reporting and a single source of truth, while data from all locations must be complete and current.

> AS-2: Management Processes are consolidated at a central location, and accept input and provide services to multiple locations. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)
> AS-2: Management Processes are consolidated at a central location, and accept input and provide services to multiple locations. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-107 - Describe Management Process Workflows

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The developer must provide a thorough high-level description of major Management Processes for staff who need to understand and use them. The documentation must cover bibliographic record import and export, validation of bibliographic records against internal and external authority sources, and standard reports. These process descriptions must be sufficiently clear to support staff understanding of the processes and their relationship to reporting and data use.

> UD-2: The developer must provide a thorough high-level description of major processes, including bibliographic record import and export, validation of bibliographic records against internal and external authority sources, and standard reports. (`early_draft_srs_galecia.txt`)
> UD-2: The software developer shall provide a thorough high-level description of major processes, including bibliographic record import and export, validation of bibliographic records against internal and external authority sources, and standard reports. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-108 - Filter By Survey Name

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must allow staff to filter reports or survey queries by selecting a survey name rather than entering a survey ID. The system must resolve the selected survey name to its corresponding ID internally so that the filtering operation can be performed. This capability is needed when staff select a survey for filtering and should not require them to know or provide the survey ID.

> Ability to select the survey name and not have to enter the survey id for filtering (`early_draft_srs_galecia.txt`)
> The ability to filter by survey name rather than survey ID requires the system to resolve names to IDs internally. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-109 - Integrate With Enterprise Library Automation

**Priority:** Should - Mentioned in 3 documents.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must operate as part of an enterprise-level Library Automation System and rely on its data structures and functionality, including the Acquisitions and Cataloging modules. Management Processes must use the enterprise system as their source of reported data rather than managing acquisitions or cataloging themselves. The system must support processes consolidated at a central location that accepts input and provides services to multiple branches. Centralized operation supports consistent reporting, but requires good network connectivity and complete, current data from all locations.

> DE-1: Management Processes rely on the data structures and functionality of an enterprise-level Library Automation System, including Acquisitions and Cataloging modules. (`early_draft_srs_galecia.txt`)
> AS-1: Management Processes are part of an enterprise-level Library Automation System. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-110 - Interface Vendor APIs And File Transfers

**Priority:** Should - Mentioned in 3 documents.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must interface with a variety of vendor websites through published APIs or automated transfers of standard-format data files. Supported standard formats must include formats such as USMARC21 and EDIFACT. The system is needed because some branches use external vendors for certain functions and reporting must handle data from those sources. Vendor data may not be present at every branch, so the system must accommodate its absence where applicable.

> DE-2: Management Processes interface with a variety of vendor websites, via published APIs and/or automated transfer of standard-format data files (e.g., USMARC21, EDIFACT). (`early_draft_srs_galecia.txt`)
> DE-2: Management Processes interface with a variety of vendor websites, via published APIs and/or automated transfer of standard-format data files (e.g., USMARC21, EDIFACT). (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-111 - Management Data Specifications And Dictionaries

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide complete data specifications for authority, bibliographic, order, item, hold/request, and other records maintained or accessed by Management Processes. Each specification must identify field names, data types, and relationships where applicable. Staff need these data structures and data dictionaries to write effective queries. The specifications must cover all records relevant to Management Processes, including records accessed from the enterprise Library Automation System.

> The developer must provide complete data specifications for: - Authority records (`meeting_tech_subcommittee_2009-06-30.txt`)
> The developer must provide complete data specifications for: - Bibliographic records (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-112 - Provide Historical Date Reporting

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The system must provide historical reporting that shows data as it existed on a specified date or within a specified date range. This capability is needed for reports such as determining what a bill amount was on a past date or what a shelving location was at that time, even when the value has since changed. The system must use a reporting warehouse or equivalent historical data source to acquire the requested past data. Historical reporting must coexist with real-time reporting for information such as what is overdue today.

> Ability to have historical reporting - a reporting warehouse such that data can be acquired on a given date or date range (`early_draft_srs_galecia.txt`)
> "Others are historical - 'what was the bill amount on June 30th?' We probably need a reporting warehouse for historical data." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-113 - Provide Historical Reporting Warehouse

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a historical reporting warehouse or an equivalent repository for reporting on historical data. This capability is needed for reports that must answer what the data was at a past date, such as determining a bill amount on June 30th, rather than reporting only current data. The system should support historical reporting separately from real-time reporting, which is needed for situations such as identifying what is overdue today.

> - Historical reporting warehouse - does not exist (`evergreen_reference_2009.txt`)
> - No historical reporting warehouse (`evergreen_reference_2009.txt`)

### REQ-114 - Provide Thorough Error Reporting Feedback

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide thorough, high-level error reporting and feedback when operations or reports fail. Error messages must provide meaningful information so staff can understand why a report or operation failed rather than receiving only a generic failure message. The feedback must be available through the system interface and support staff in identifying the nature of the problem.

> UD-4: The system must provide thorough high-level error reporting and feedback, and shall allow low-level query-specific feedback for Local and Global System Administrators from the front-end interface. (`early_draft_srs_galecia.txt`)
> UD-4: The system shall provide thorough high-level error reporting and feedback and shall allow low-level query-specific feedback for Local and Global System Administrators from the front-end interface. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-115 - Query OPAC Hold Circulation Data

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must interact with the patron-facing Online Public Access Catalog to access data generated through patron holds and circulation transactions. Patrons create these holds and circulation transactions through the OPAC, and the reporting system must query the resulting data for reporting purposes. The system must read or query this OPAC data without modifying the holds or circulation transactions.

> DE-3: Management Processes interact with a patron interface, also known as an Online Public Access Catalog (OPAC). (`early_draft_srs_galecia.txt`)
> DE-3: Management Processes interact with a patron interface (OPAC). "Patrons create holds and circulation transactions through the OPAC," Robert said. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-116 - W3C Compliant Web Output

**Priority:** Should - Mentioned in 2 documents.  
**Type:** non-functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system must produce standards-compliant HTML for web output, including the help system and report output. All HTML output must validate against W3C standards so that it remains compatible with different browsers and assistive technologies. This requirement applies to report display, help, and other web-based interface components.

> "We need to make sure all HTML output validates against W3C standards," Robert noted. (`meeting_tech_subcommittee_2009-06-30.txt`)
> "We need to make sure all HTML output validates against W3C standards," Robert noted. "This isn't just about looks - it's about compatibility with different browsers and assistive technologies." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-117 - Comply With Accounting Audit Requirements

**Priority:** Should - Mentioned in 2 documents; strong wording (must).  
**Type:** constraint  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must ensure that all reports and archived data comply with standard accounting practices and applicable state, county, and municipal auditing requirements. This condition applies to financial reporting and data archiving used by staff. The reporting context includes patron account balances, fines and charges accrued, fines waived, and payments made, with reports organized by the specified patron, time-period, branch, home library, system, or payment-method dimensions where applicable. The system must also maintain a ledger of patron payments, including the charges to which payments are applied, to facilitate reconciliation.

> All reports and data archiving must comply with standard accounting practice and state, county, and municipal auditing requirements. (`early_draft_srs_galecia.txt`)
> Compliance - all reports and data archiving must comply with standard accounting practice and state, county, and municipal auditing requirements. (`email_financial_reports.eml`)

### REQ-118 - Link Payments To Applied Charges

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must maintain a financial audit trail that links every patron payment to the specific charge or charges to which it was applied. Finance staff need this traceability to follow payment application and reconcile accounts properly. The ledger must preserve the payment-to-charge relationship rather than recording only an unapplied or aggregate payment amount.

> The financial audit trail is CRITICAL for our finance department. They need to be able to trace every payment back to the specific charge it was applied to. (`email_financial_reports.eml`)

### REQ-119 - Provide Patron Balance Financial Reports

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must provide financial reports of patron account balances organized by patron, home library, and the overall library system. Staff need these reports to review financial information at the individual patron level and in aggregated views for libraries and the system. The reporting capability must support the balance dimensions specified by the financial reporting requirements.

> Patron account balances by patron, home library, and system (`email_financial_reports.eml`)
> patron account balances by patron, home library, and system (`early_draft_srs_galecia.txt`)

### REQ-120 - Query Balances Above Dollar Threshold

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must allow staff to query patron accounts whose balances exceed a specified dollar threshold, so accounts needing attention can be identified efficiently. Financial reports must show payments by method, distinguishing cash, credit card, check, and other applicable methods to support daily reconciliation. The system must also track fines waived per library because each library has its own budget for waived fines.

> The financial reports need to show payments by method - cash, credit card, check, etc. This helps with daily reconciliation. (`email_financial_reports.eml`)
> As an example, a staff user can easily query patron accounts with balances greater than X dollars. (`early_draft_srs_galecia.txt`)

### REQ-121 - Report Payments By Method Channel

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must report payments for selected time periods, categorized by payment method and payment channel. Supported payment methods include cash, credit card, and check, while supported channels include the staff desk, self-check station, and OPAC. Staff need these reports for financial reporting and daily reconciliation. The system must also support payment tracking by library so branch-level payment activity can be reviewed.

> payments made per time period and per payment method (e.g., staff desk, self-check station, OPAC) (`early_draft_srs_galecia.txt`)
> Payments made per time period and per payment method (staff desk, self-check, OPAC) (`email_financial_reports.eml`)

### REQ-122 - Report Waived Fines By Branch

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must report fines waived for selected time periods and by branch. Supported time periods include the last twelve months, year to date, and last month. Staff need these reports to monitor waived-fine activity for each branch and support financial reporting. The system must present waived fines separately by branch because waived-fine budgets are maintained independently for each library.

> fines waived per time period and per branch (`early_draft_srs_galecia.txt`)
> Fines waived per time period and per branch (`email_financial_reports.eml`)

### REQ-123 - Track Waived Fines By Library

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must track fines waived and payments made for each library, with fines, charges, waivers, and transactions attached to patron and item records. It must record waived fines separately by library because each library has its own budget for waived fines. Staff need this information to support independent budget management, daily reconciliation, and financial reporting. Financial reports must comply with standard accounting practice and state, county, and municipal auditing requirements.

> System tracks fines waived and payments made per library. (`early_draft_srs_galecia.txt`)
> Fines waived should be tracked per library because each library has its own budget for waived fines. (`email_financial_reports.eml`)

### REQ-124 - Update Front Desk Payments Immediately

**Priority:** Should - Mentioned in 2 documents.  
**Type:** non-functional  
**First mentioned:** 2009-07-13  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must allow staff to update financial information easily and must immediately reflect a patron payment made at the front desk. It must support querying patron accounts with balances greater than a specified amount to identify accounts needing attention. Payments must be tracked by library so each branch can see the payments collected at its location for end-of-month reports. Financial reports and archived data must comply with standard accounting practice and applicable state, county, and municipal auditing requirements.

> Financial information can be updated easily. (`early_draft_srs_galecia.txt`)
> Financial information needs to be easily updatable. When a patron makes a payment at the front desk, we need the system to reflect that immediately. (`email_financial_reports.eml`)

### REQ-125 - Associate Finance With Patron Items

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-14  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must associate fines, charges, waivers, and ecommerce transactions with patron and item records. It must track fines waived and payments made per branch so staff can review financial activity in the relevant library context. Financial information must be easy to update, and staff must be able to query patron accounts with balances greater than a specified dollar amount. These financial records and transactions must support the reporting and archiving requirements for standard accounting practices and state, county, and municipal audits.

> Fines, charges, waivers, and ecommerce transactions are attached to patron and item records. (`early_draft_srs_galecia.txt`)
> Fines, charges, waivers, and ecommerce transactions are attached to patron and item records. (`email_financial_reports.eml`)

### REQ-126 - Maintain Applied Payment Ledger

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-14  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must maintain a ledger of patron payments that identifies the charges to which each payment is applied. This ledger is required to support financial reconciliation and provide an audit trail for payment activity. The ledger must relate payments to the applicable fines or charges attached to patron and item records. Financial reports and archived data must comply with standard accounting practice and state, county, and municipal auditing requirements.

> The system maintains a ledger of patron payments, including which charges payments are applied to, to facilitate reconciliation. (`early_draft_srs_galecia.txt`)
> The system maintains a ledger of patron payments, including which charges payments are applied to, to facilitate reconciliation. (`email_financial_reports.eml`)

### REQ-127 - Report Item Values From Records

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-14  
**Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system must generate reports of item values using data recorded in item records. Staff must be able to report on the entire collection or on a selected portion of it. The selected portion may be defined by the item status or collection information represented in the records, such as all items with longoverdue status or all DVDs in the children's collection. The system must also support reporting the value of the entire collection.

> The system can generate a report of the value of items (based on data in item record) in the entire collection or a portion. (`early_draft_srs_galecia.txt`)
> System can generate a report of the value of items (based on data in item record) in the entire collection or a portion. Examples: value of all items with status of "longoverdue", value of all DVDs in children's collection, value of entire collection. (`email_financial_reports.eml`)

### REQ-128 - Context Sensitive Online Help

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide online, hierarchical, and cross-linked help in HTML that describes and illustrates all system functions. Help must be context-sensitive so staff can access relevant documentation from the system without leaving it. The system must also provide thorough high-level error reporting and feedback, while allowing low-level, query-specific feedback through the front-end interface for Local and Global System Administrators.

> [Discussion: Context-sensitive help is critical. Staff shouldn't have to leave the system to find documentation.] (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-129 - Provide Admin Query Specific Feedback

**Priority:** Should - Marked as priority in the source document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide Local and Global System Administrators with low-level, query-specific feedback through the front-end interface. This feedback is needed when reports fail so administrators can understand the cause rather than receiving a generic error message. The information should identify relevant details such as the affected table, field, and type of error.

> UD-4: The system must provide thorough high-level error reporting and feedback, and shall allow low-level query-specific feedback for Local and Global System Administrators from the front-end interface. (`early_draft_srs_galecia.txt`)
> UD-4: The system shall provide thorough high-level error reporting and feedback and shall allow low-level query-specific feedback for Local and Global System Administrators from the front-end interface. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-130 - Relational Database Back End

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Fully relational DB backend; core data integrity but less emphasized.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The management processes must use a fully relational database as their back-end. This is required so the reporting layer works properly with the relational structure used for management data. Staff need reliable reporting based on data stored in that relational back-end. The database requirement applies to the management processes and requires a fully relational implementation rather than a non-relational back-end.

> Management Processes shall use a fully relational database back-end. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-131 - Report Items Currently In Transit

**Priority:** Should - Mentioned in 1 document; strong wording (critical).  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports on items currently in transit to support delivery coordination. These reports are critical for staff coordinating deliveries between branches. The system should identify items that are in transit so staff can use the information when managing delivery activities.

> - In-transit item reports are critical for delivery coordination (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-132 - Support Supported Web Browsers

**Priority:** Should - Marked as priority in the source document.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

When Management Processes are accessed through a web browser, the system must support Microsoft Internet Explorer version 6.0 and later and Mozilla Firefox version 2.0 and later. This requirement is needed because different libraries standardize on different browsers, and Internet Explorer 6.0 remains in use in some library environments. The browser requirement applies specifically to web-browser access; the broader access requirement also permits a Windows-compatible client. Staff using either supported browser must be able to access Management Processes.

> OE-4: If web-browser based, the system must be accessible through Microsoft Internet Explorer (version 6.0 and later) and Mozilla Firefox (version 2.0 and later). (`early_draft_srs_galecia.txt`)
> If web-browser based, Management Processes shall be accessible through Microsoft Internet Explorer (v.6.0 and later) and Mozilla Firefox (v.2.0 and later). (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-133 - Archive Transactions With Privacy

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: State-law privacy protections for archived transaction data are critical.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must archive transaction data with privacy protections required by applicable state law. The archive must retain information sufficient to produce useful demographic statistics, including analysis by age range, patron type, and patron location. This capability is needed for board and activity reporting that examines library use while protecting patron privacy.

> Transactions archived protecting patron privacy per State Law, while providing useful demographic statistics. (`email_report_features.eml`)
> TRANSACTION ARCHIVE: Archive with privacy protection per State Law. (`email_report_features.eml`)

### REQ-134 - Control Report Access Permissions

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`, `evergreen_reference_2009.txt`

The reporting system must provide fine-grained permissions governing access to reporting capabilities, reports, and data. It must support distinct permission levels that limit who may create, run, modify, or clone reports, while allowing administrators to manage access through roles and shared folders. Administrators must be able to make specific reports available to staff or restrict staff from running them and from performing ad hoc reporting on specified sets of data. These controls are needed to manage reporting access across staff responsibilities.

> Implement fine-grained permissions and template management (`evergreen_reference_2009.txt`)
> We need distinct, fine-grained permission levels limiting who can create and clone reports. (`email_report_features.eml`)

### REQ-135 - Control Report Creation And Cloning

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Controls ad hoc data exposure via shared-folder permissions; important security.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must support distinct, fine-grained permission levels that control who may create and clone reports. Administrators must be able to create shared folders whose permissions determine whether staff may run specific reports or ad hoc reports. These shared-folder permissions must also control whether staff may run ad hoc reports against specified sets of data. The capability is needed to restrict access to reports and data according to administrative decisions.

> Admins can create shared folders to allow or disallow staff from running specific reports, and/or to run ad hoc reports on specific sets of data. (`email_report_features.eml`)

### REQ-136 - Exclude Personally Identifiable Patron Data

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: No patron PII in archives; strong privacy/security requirement.  
**Type:** constraint  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must exclude personally identifiable information about patrons from archived transaction data. This protection is required because transaction data must be retained for compliance while patron privacy prevents retaining identifying information. The archive must therefore preserve only information that can support required transaction retention and useful reporting without identifying individual patrons.

> State law requires us to retain transaction data for X years, but patron privacy means we can't keep personally identifiable information. (`email_report_features.eml`)

### REQ-137 - Manage Access Using Security Groups

**Priority:** Should - Mentioned in 2 documents.  
**Type:** non-functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`, `email_staff_login.eml`

The system must make roles and permissions easy for authorized administrators to manage. It must support controlling rights and privileges through security groups or roles and provide access control for individuals, workgroups, and arbitrary staff groups. This capability is needed to administer report access without requiring complex management of each permission assignment.

> The permissions need to be easy to administer. (`email_report_features.eml`)
> 4. Easy administration of roles and permissions. (`email_staff_login.eml`)

### REQ-138 - Provide Activity Traffic Volume Reports

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must provide activity reports showing traffic and volume of use for check-outs, check-ins, holds placed, and holds filled. These reports are needed by library boards and other external consumers as part of the predefined reporting provided by the system. The system should support cross-tabulation by terminal, branch, library system, hour, patron age range, patron type, and patron location, subject to staff permissions for running reports and accessing specific data.

> Activity reports should indicate traffic and volume of use, displaying statistics on check-outs, check-ins, holds placed, and holds filled. (`early_draft_srs_galecia.txt`)
> Activity reports showing traffic and volume of use - checkouts, check-ins, holds placed, holds filled. (`email_report_features.eml`)

### REQ-139 - Provide Executive Board Activity Reports

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must provide predefined executive reports suitable for library boards and other external consumers. These reports must include basic statistics required by the Georgia Annual Report and Application for State Aid, including activity measures for checkouts, check-ins, holds placed, and holds filled. Activity reports must support cross-tabulation by terminal, branch, library system, hour, patron age range, patron type, and patron location. The reports are intended to show traffic and volume of use for external reporting needs.

> Pre-defined reports for library boards with basic statistics (Georgia Annual Report requirements). (`email_report_features.eml`)
> BOARD REPORTS: Pre-defined reports for boards. (`email_report_features.eml`)

### REQ-140 - Retain Archives Per Legal Periods

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Retention for required period is legal compliance and cannot be optional.  
**Type:** constraint  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must retain archived transaction data for the period required by applicable state law. This retention is needed to support compliance with legal requirements for transaction archives. The system must apply the required retention period while also respecting the separate requirement that personally identifiable information about patrons is not retained.

> State law requires us to retain transaction data for X years, but patron privacy means we can't keep personally identifiable information. (`email_report_features.eml`)

### REQ-141 - Run Named Reports Using Templates

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Consistency reduces errors and disputes; important for report reliability.  
**Type:** non-functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must use report templates to ensure that staff running the same named report apply the same criteria and produce consistent results. Templates are needed when the director requests a report by name, such as the weeding report, so that everyone runs the same defined report. The system should support templates that are available to staff and can be run as-is or modified within permitted limits.

> We want to make sure that when the director asks for "the weeding report," everyone runs the same report with the same criteria. Templates ensure this. (`email_report_features.eml`)

### REQ-142 - Select Query Values From Picklists

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The query tool must allow staff to select query values from predefined picklists of possible values. This capability is needed to support user-friendly query design across bibliographic, item, patron, transaction, and financial records. Picklist selection must be available alongside field selection, regular-expression selection, and Boolean operators when staff construct queries.

> - Select values from a picklist of possible values (`early_draft_srs_galecia.txt`)
> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)

### REQ-143 - Select Report Display Fields

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The query and open-template reporting interfaces must allow staff to select the fields displayed in reports. Available display attributes must include circulation, patron, item, bill, and bibliographic information. For open-template reporting, these attributes must also be available for filtering, while administrators may limit which display fields and filters staff can alter in templates.

> Staff should be able to: - Select fields to query (`early_draft_srs_galecia.txt`)
> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)

### REQ-144 - Show Report Name And Criteria

**Priority:** Should - Mentioned in 3 documents.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`

The system must display the report name and the selections or criteria used to produce report results. When a date range is applicable, the results must show the selected date range at the top or bottom so staff can quickly identify the period used. The system should provide this information with the results for reports and queries, ensuring that the applied criteria are clearly defined.

> Report results would include the date selection criteria at the top or bottom to quickly see date range selected along with the name of the report (`early_draft_srs_galecia.txt`)
> QUERY SELECTIONS: Show criteria with results. (`email_report_features.eml`)

### REQ-145 - Update Permissions On Role Change

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Role-based permissions with automatic updates; security/administration important.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must provide fine-grained report permissions that authorized administrators can manage through roles. Report permissions must update automatically when a staff member's role changes, such as when the staff member moves from Staff to Manager. This capability is needed to keep access aligned with assigned roles while supporting shared folders and permissions that are easy to administer.

> If I change someone from "Staff" to "Manager," their report permissions should update automatically based on the role. (`email_report_features.eml`)
> Easy administration through roles. (`email_report_features.eml`)

### REQ-146 - Assign Report Queue Priorities

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Priority queue improves throughput for important reports; operational enhancement.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

The system must allow authorized users to assign priorities to reports in the report queue. Important reports must be able to move ahead of lower-priority reports when their assigned priority requires it. The queue must also show a report’s position, status, and priority so authorized users can understand how reports are being processed.

> PRIORITY: Important reports can jump queue. (`email_report_features.eml`)

### REQ-147 - Control Query Tool Access

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Admin control of query tool access is security governance.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

The system must allow administrators to control access to the query tool. The query tool should provide a user-friendly interface for designing queries against all record types, including Boolean operators, picklists, and regex support. Administrative access control is required so that the query tool is available only according to administrator decisions, while its supported query features remain usable when access is granted.

> Admin controls access. (`email_report_features.eml`)

### REQ-148 - Design User Queries Via Interface

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must provide staff with a user-friendly interface for designing queries across bibliographic, item, patron, transaction, and financial records. Staff must be able to select fields to query, choose values from picklists, select regular expressions from a drop-down menu, and use Boolean operators. Administrative controls must govern access to the query tool and related reporting capabilities.

> The system should provide a user-friendly interface for designing queries against all record types (bibliographic, item, patron, transaction, financial). (`early_draft_srs_galecia.txt`)
> QUERY TOOL: User-friendly interface for designing queries against all record types. (`email_report_features.eml`)

### REQ-149 - Run And Modify Templates With Limits

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`

The system must enable staff to run report templates without modification when the provided definition meets their reporting needs. It must also allow staff to modify available templates for individual reporting needs. Any modification must remain subject to the filters and display fields that administrators permit staff to alter. The system must preserve dependable results while supporting these staff-specific changes.

> These templates should be runnable as-is or modifiable for individual needs. (`early_draft_srs_galecia.txt`)
> Run as-is or modified. (`email_report_features.eml`)

### REQ-150 - Allow Open Template Reporting

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must support open-template reporting through an interface that allows staff to select reporting attributes for filtering and display. Available attributes must include those associated with circulation, items, patrons, bills, and bibs. This capability is needed when staff require reports beyond canned or preset on-demand reports. The open-template interface is distinct from canned and noncanned interfaces, and the sources identify open-template reporting as a capability that does not currently exist.

> c) Open Template Reporting - all attributes associated with circulation, items, patrons, bills, and bibs to select from for filtering and display (`early_draft_srs_galecia.txt`)
> - Open Template Reporting - does not exist (`evergreen_reference_2009.txt`)

### REQ-151 - Anonymize Demographic Reporting Data

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must anonymize data used to produce demographic statistics. Anonymization must delete information that could be used to identify a patron, including personally identifiable information. This condition applies to demographic reporting on transactions by geographic region and age range, ensuring that the resulting statistics can be used for analysis without identifying individual patrons.

> The data used to produce these statistics must be anonymized - information that could be used to identify a patron is deleted. (`early_draft_srs_galecia.txt`)

### REQ-152 - Filter By Uploaded Identifier File

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must allow staff to upload a text file containing values such as barcodes or TCNs. The uploaded values must be usable as filtering criteria for a report. This capability is needed when staff need to restrict report results according to a supplied list of item identifiers rather than entering each filtering value individually.

> Ability to upload a text file such as barcodes or TCN to use for filtering on a report (`early_draft_srs_galecia.txt`)
> - No ability to upload text files for filtering (barcodes, TCNs) (`evergreen_reference_2009.txt`)

### REQ-153 - Generate Pivot Table Report Results

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reporting system must generate report results in pivot-table format. This capability is needed by staff who require pivot tables for analyzing report data and was identified as a missing reporting feature. Pivot-table output must be available as a result format for generated reports. The output should be provided as part of the reporting system rather than requiring staff to create the pivot table separately.

> Pivot table output (`early_draft_srs_galecia.txt`)
> - No pivot table output (`evergreen_reference_2009.txt`)

### REQ-154 - Identify Hold Placement Method

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

The system must identify the placement method for each hold in hold reports. The reported methods must distinguish holds placed at a staff desk, at a public computer inside the library, and remotely. This information is needed for reports covering holds placed, holds filled, and check-outs, including reports organized per patron, per library, per selected group of libraries, per system, or per county.

> The system counts all hold requests, including how the hold was placed: - at a staff desk - at a public computer inside the library - remotely (`early_draft_srs_galecia.txt`)
> Holds reports should show how the hold was placed - at staff desk, at public computer, or remotely (`survey_results_2009.txt`)

### REQ-155 - Patron Behavior Renewal And Return Analysis

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The reporting system must analyze patron behavior by reporting how quickly items are returned, renewal rates, the likelihood that an item will be renewed, and the percentage of checkouts that are renewals. This analysis is needed to predict patron behavior and support demographic analysis of transaction activity. Any demographic statistics used with this analysis must be anonymized and must not include personally identifiable information.

> Patron behavior analysis (how quickly books are returned, renewal rates) - Demographic statistics (must be anonymized - no personally identifiable info) (`survey_results_2009.txt`)

### REQ-156 - Provide Fines-Stopped Reason Items

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide an items report that lists items grouped or filtered by the reason fines were stopped. The report is needed when staff must review items according to the applicable fines-stopped reason. It must preserve the relationship between each item and its fines-stopped reason so that reporting can be organized by that criterion.

> - List of Items by Fines Stopped Reason (`early_draft_srs_galecia.txt`)
> - List of Items by Fines Stopped Reason (not available) (`evergreen_reference_2009.txt`)

### REQ-157 - Provide Hover Title Popups

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The reports interface must provide quick access to canned reports and templates and display a pop-up description when staff hover over a report or template title. The description must be available from each applicable title so staff can understand the report or template before selecting it. This capability addresses the stated need for a quick access interface with pop-up descriptions and hover tooltips for report titles.

> Ability to hover over each title of canned report/template with pop-up box with description (`early_draft_srs_galecia.txt`)
> - No quick access interface with pop-up descriptions (`evergreen_reference_2009.txt`)

### REQ-158 - Provide Open Template Filter Attributes

**Priority:** Should - Mentioned in 1 document. Adjusted from Could by model: Expose all relevant attribute filters; broadens usability significantly.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The open template reporting interface must provide attributes associated with circulation, patrons, items, bills, and bibliographic records for selection as report filters. The same attributes must also be available for display in the report results. This capability is needed when reports require filtering and displaying information from these library record areas.

> Open template would have all attributes associated with say circulation, patrons, items, bills, and bibs to select from for filtering and the same attributes for displaying. (`early_draft_srs_galecia.txt`)

### REQ-159 - Report Bibliographic Additions By Staff

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report the number of bibliographic records added by each staff member and by each library. Staff need this report to review additions by the person responsible and by library. The report must distinguish additions by staff member and by library, as specified for the bibliographic records report. The source identifies this report as not available, so implementation must address that stated availability limitation.

> - Bib Records Added by user by library Count (`early_draft_srs_galecia.txt`)
> - Bib Records Added by user by library Count (not available) (`evergreen_reference_2009.txt`)

### REQ-160 - Report Circulation By Modifiers

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide circulation counts organized by circulation modifier, Cat1, and Cat2 categories. The report must support categories such as Adult, YA, and Juv. Circulation count by circulation modifier is identified as partially available, while the requirement also lists category-based circulation reporting as a needed circulation report for staff review.

> - Circulation Count by Circ Modifier, Cat1, and Cat2 (Adult, YA, Juv...) (`early_draft_srs_galecia.txt`)
> - Circulation Count by Circ Modifier (partially available) (`evergreen_reference_2009.txt`)

### REQ-161 - Report Circulation Location By County

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report circulation counts by circulation location, broken down by the patron’s county. Staff need this report to examine circulation activity at each circulation location in relation to patron county. It must be provided as a distinct report alongside circulation counts by patron home library and age demographic. The source identifies this report type as unavailable in the referenced Evergreen report set, so the system must provide the required capability despite that limitation.

> - Circulation Count by Circ Location broken down by Patron County (`early_draft_srs_galecia.txt`)
> - Circulation Count by Circ Location broken down by Patron County (not available) (`evergreen_reference_2009.txt`)

### REQ-162 - Report Collection Age By Location

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report the age of the collection by call number or shelving location. Staff need this report to assess collection age within either of these organizational categories. The report must support collection-age reporting using call number or shelving location as the stated basis. The source also identifies the age-of-collection report by call number as not available, so implementation must address that stated availability limitation.

> - Age of collection by call number or shelving location (`early_draft_srs_galecia.txt`)
> - Age of collection by call number (not available) (`evergreen_reference_2009.txt`)

### REQ-163 - Report Collection Price By Location

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report the price value of the collection by call number or shelving location. Staff need this report to review collection value within either of these organizational categories. The report must support price-value reporting using call number or shelving location as the stated basis. The source identifies the price-value report as not available, so implementation must address that stated availability limitation.

> - Price value of collection by call number or shelving location (`early_draft_srs_galecia.txt`)
> - Price value of collection by call number (not available) (`evergreen_reference_2009.txt`)

### REQ-164 - Report Edited Bibliographic Records Count

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must report the number of bibliographic records edited. Staff need this report to determine the volume of bibliographic-record editing activity. The report must provide the count of edited bibliographic records as a bibliographic records report. The source identifies this report as not available, so implementation must address that stated availability limitation.

> - Bib Records Edited Count (`early_draft_srs_galecia.txt`)
> - Bib Records Edited Count (not available) (`evergreen_reference_2009.txt`)

### REQ-165 - Report Holds With Purchase Alerts

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report of purchase alerts associated with holds. This report is needed within the holds-reporting area to identify holds that have purchase alerts associated with them. The referenced reporting information lists Holds Purchase Alert among report types that are not available, so the system must address this stated availability limitation while providing the required report.

> - Holds Purchase Alert (`early_draft_srs_galecia.txt`)
> - Holds Purchase Alert (not available) (`evergreen_reference_2009.txt`)

### REQ-166 - Report Inactive Patron Status

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report listing patrons whose status is inactive. This report is needed as part of the patron reports so inactive patron records can be identified separately from other patron lists, including barred patrons and patrons listed by expiration date. The inactive-patron report is also identified as not available in the referenced reporting information, so its availability is a stated limitation that the system must address.

> - List of Patrons with inactive status (`early_draft_srs_galecia.txt`)
> - List of Patrons with inactive status (not available) (`evergreen_reference_2009.txt`)

### REQ-167 - Report Items Created Within Range

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide an items report listing items whose creation dates fall within a specified date range. Staff need this report to identify items created during a selected period. The report must use the item creation date as its filtering criterion and include items whose dates fall within the specified range. The listed reference materials indicate that this report type was not available, so the reporting system must provide the required capability.

> - List of Items by Creation Date Range (`early_draft_srs_galecia.txt`)
> - List of Items by Creation Date Range (not available) (`evergreen_reference_2009.txt`)

### REQ-168 - Report Last Circulation Date And Uses

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a weeding report showing each item’s last circulation date and number of circulations. Staff need this information to evaluate item use when conducting collection weeding. The report must present both circulation measures for each item, including items with different circulation histories. The source indicates that reporting the last circulation date was only partially available, so the system must provide the complete required capability.

> - Weeding report (date of last circulation and number of circs) (`early_draft_srs_galecia.txt`)
> - Weeding report with date of last circulation (partially available) (`evergreen_reference_2009.txt`)

### REQ-169 - Report Overdue Items Threshold Days

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report listing items overdue by more than a specified number of days. Staff must be able to use configurable thresholds so the report identifies items exceeding the selected overdue period. The report must include patron contact information and support reporting on long-overdue items as well as items exceeding the specified threshold.

> - Items more than XX days overdue (Overdue Materials Report) (`early_draft_srs_galecia.txt`)
> - List of Long Overdue (`early_draft_srs_galecia.txt`)

### REQ-170 - Report Patron Geography County City ZIP

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide patron counts organized by county, city, and ZIP code. Staff need this geographic report to review the distribution of patrons across these locations, in addition to separate counts by county and home library. The source identifies this report type as not available in the reference material, establishing a stated availability limitation. The required geographic breakdown is limited to county, city, and ZIP code.

> - Patron Count by County (`early_draft_srs_galecia.txt`)
> - Patron Count by County (not available) (`evergreen_reference_2009.txt`)

### REQ-171 - Report Staff Account Dates

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report listing staff accounts together with each account’s last password-change date and account expiration date. This report is needed within the patron-reporting area to show account-related dates for staff accounts. The referenced reporting information identifies the staff-account report with the last password-change date as not available, so availability of this reporting capability is a stated limitation that the system must address.

> - List of Staff Accounts with date of last password change and account expiration (`early_draft_srs_galecia.txt`)
> - Staff Accounts with date of last password change (not available) (`evergreen_reference_2009.txt`)

### REQ-172 - Report Stale Holds Shelf Awaiting Pickup

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report of holds that remain on the hold shelf awaiting pickup beyond the permitted period. Staff need this holds report to identify stale holds requiring review because they have waited too long for pickup. The report must be distinct from the report of unfilled holds and other holds reports. The source also identifies Stale Holds as not available in the referenced system, establishing the need for this capability.

> - Stale Holds (holds sitting on hold shelf waiting for pickup for too long) (`early_draft_srs_galecia.txt`)
> - Stale Holds (not available) (`evergreen_reference_2009.txt`)

### REQ-173 - Report Unfilled Holds

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report identifying holds that remain unfilled. Staff need this holds report to review holds for which fulfillment has not occurred. The report must be available as a distinct holds report alongside reports for items sent for holds, items received for holds, annual holds placed, and stale holds. The source also identifies Unfilled Holds as not available in the referenced system, establishing the need for this capability.

> - Unfilled Holds (`early_draft_srs_galecia.txt`)
> - Unfilled Holds (not available) (`evergreen_reference_2009.txt`)

### REQ-174 - Report Voter Survey Responses By Week County

**Priority:** Should - Mentioned in 2 documents.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report of voter registration survey responses, including response counts by week and county. This report is needed within the patron reports for reviewing voter registration survey activity across those time and geographic groupings. Staff must be able to use the report when those response counts are required. The source also identifies Voter Survey Responses as not available, so the report may be subject to an availability limitation.

> - Voter Survey Responses County by Week (`early_draft_srs_galecia.txt`)
> - Voter Reg Survey Responses Count by Week (`early_draft_srs_galecia.txt`)

### REQ-175 - Support Canned Report Definitions

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support the reporting definitions specified in the report examples attached as Appendix A. Staff must be able to use reporting capabilities that conform to those canned report definitions. Support is required for the definitions described in Appendix A, as stated for the reporting system.

> The system must be able to support the reporting definitions as described in the attached report examples (see Appendix A). (`early_draft_srs_galecia.txt`)

### REQ-176 - Support Fine Grained Reporting

**Priority:** Should - Mentioned in 1 document; strong wording (must).  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support the fine-grained reporting requirements specified in the attached Appendix B specification. Staff must be able to use reporting capabilities that conform to those fine-grained requirements. Support is required for the requirements described in Appendix B, in addition to the reporting definitions specified in Appendix A.

> The system must be able to support the fine-grained reports requirements as described in the attached specification (see Appendix B). (`early_draft_srs_galecia.txt`)


## Could requirements

### REQ-177 - Use Iterative Prototype Methodology

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-01-27  
**Sources:** `early_draft_srs_galecia.txt`

The system must use an iterative, prototype-oriented methodology to further specify and develop the data structures and user interfaces for reporting and management tools. This approach is needed because the requirements describe functional aspects of an Integrated Library System while the data structures and interfaces still require additional development. The resulting tools should support the reporting and management processes of large, urban, multiple-branch, centralized library systems.

> The requirements cover functional aspects only; data structures and user interfaces will require further specification and development using an iterative, prototype-oriented methodology. (`early_draft_srs_galecia.txt`)

### REQ-178 - Allow Custom Web Report Creation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must allow staff to create custom reports through a web-based report writer interface. The interface must provide the reporting capabilities needed for staff to define reports, including field selection, basic filtering and sorting, and saving and reusing report definitions. Reports must support the available output formats of CSV, HTML, and sometimes Excel.

> Evergreen includes a report writer that allows staff to create custom reports using a web-based interface. (`evergreen_reference_2009.txt`)

### REQ-179 - Allow Global Administrator Consortium Configuration

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must allow the global system administrator to implement software changes and configurations for the PINES consortium. This role manages PINES at the consortium level and is performed by the PINES central IT team. The capability is needed to administer the consortium as a whole rather than an individual branch. The global system administrator also generates statistical reports for PINES as a whole, as part of consortium-level management.

> Global System Administrator: Manages PINES at the consortium level, implementing software changes and configurations, and generating statistical reports for PINES as a whole. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-180 - Allow Local Administrator Configuration

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must allow local system administrators to configure it for their local library processes. These administrators are management staff who oversee library processes and configure the system locally. The capability is needed by branch managers and assistant directors. Configuration must support local process management without changing the administrators’ role as local, rather than consortium-level, managers.

> They configure the system locally. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-181 - Control Report Create And Run

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The permission model must provide fine-grained control over which staff may create reports and which staff may run reports. This separation is needed because the current permission model does not distinguish permissions to create reports from permissions to run them. Staff may currently run any report they can access, but the required model must control creation and execution separately. The source also identifies the absence of shared folders and limits on which filters staff can use as current permission limitations.

> - No fine-grained control over who can create vs. run reports (`evergreen_reference_2009.txt`)

### REQ-182 - Display Reports Indirectly To Patrons

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system should support making report information available to patrons indirectly through displays or screens at libraries. Patrons are residents of the State of Georgia who use the resources of a PINES member library, whether or not they possess a library card. Patrons interact through the OPAC, so the management processes system should not treat them as direct report creators or primary operators. Staff remain the primary creators of reports that may be presented in this indirect manner.

> [Note from Katherine: Patrons interact through OPAC; they may use reports indirectly through displays/screens at libraries] (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-183 - Enable Report Data Filtering

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must allow staff to apply filters to report data through the report writer’s web-based interface. This is needed when staff create custom reports and need to restrict the data included in the results. Filtering must use the basic filter capability described for the report writer. The system is not required by this source to provide Boolean operators beyond simple filters, regular expression support, or access to every database field.

> - Basic filtering and sorting (`evergreen_reference_2009.txt`)

### REQ-184 - Enable Report Results Sorting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must allow staff to sort report results through the report writer’s web-based interface. This capability is needed when staff create custom reports and need the resulting data arranged for review or use. Sorting must be provided as a basic report-writer function alongside field selection and filtering. The source limits the report writer by noting that complex queries are difficult to construct and that not all database fields are available.

> - Basic filtering and sorting (`evergreen_reference_2009.txt`)

### REQ-185 - Enable Staff Management Report Creation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must support staff as the primary creators of management reports. This includes paid employees of PINES member libraries involved in designing and providing services, including front-line circulation staff and supervisors. Staff need report creation capabilities to support the development of management information. Patrons may interact with reports indirectly through displays or screens at libraries, but staff remain the primary content creators.

> [Jenny: Staff are our primary content creators for reports] (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-186 - Exclude Day To Day Patron Functions

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system must focus on management processes, including reports and analysis tools used for planning, evaluation, and oversight. It must exclude day-to-day patron-facing functions from its scope. Those functions belong to the OPAC and circulation client rather than the management processes system. Library managers, administrators, and staff need the included capabilities for management and operational oversight.

> She clarified that this does NOT include day-to-day patron-facing functions (those are part of the OPAC and circulation client). (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-187 - Expose Field Catalog For Reporting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must expose relevant database fields for report field selection, including the documented sample fields for bibliographic metadata, item and copy details, and patron information. It should support drag-and-drop field selection, basic filtering and sorting, multiple output formats including CSV and HTML and sometimes Excel, and saving and reusing report definitions. Field availability is limited because not all database fields are exposed; complex queries, Boolean operators beyond simple filters, regular expressions, and query queue visibility are not supported.

> 3.3 AVAILABLE FIELDS (SAMPLE) For bibliographic_record: - id, fingerprint, scan_timestamp, record_type, edition, language, ISBN, ISSN, UPC, EAN, publisher_name, publication_date, place_of_publication, physical_description For item: - id, barcode, label, copy_number, location (copy_location), status ... (`evergreen_reference_2009.txt`)
> - Limited field selection (not all database fields are available) (`evergreen_reference_2009.txt`)

### REQ-188 - Provide Bibliographic Record Count Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must provide a predefined report showing the number of bibliographic records. The report should be available as a bibliographic-record report alongside reporting on bibliographic records with no volumes attached. Staff need this report to review the count of bibliographic records through the reporting functions. The source places this report within the set of predefined reports available to the library.

> - Bib Records Count (`evergreen_reference_2009.txt`)

### REQ-189 - Provide Checkout Count Canned Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must provide a predefined report showing checkout counts. This report is needed as part of the report writer’s canned reports for circulation reporting. The predefined report must be available as the Checkout Count report alongside other listed circulation reports, including Renewals Count and Non-Cataloged Count. This requirement concerns a predefined report rather than construction of a custom query, within the stated set of available canned reports.

> - Checkout Count (`evergreen_reference_2009.txt`)

### REQ-190 - Provide Executive Reports Interface

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system shall provide an Executive Reports Interface with reports functionality to support library management and administrative oversight. The reports functionality must be developed and evaluated through the Reports testing group, which filters new Reports development. The system must also support the reports needed for the Executive Reports Interface and the templates needed for all PINES libraries.

> Compile a list of reports needed for an Executive Reports Interface. (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-191 - Schedule Multiple Reports Concurrently

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The scheduling system must allow staff to select multiple reports and schedule them to run at the same time. This capability is needed because the stated scheduling limitations include no ability to check multiple reports to run at the same time. Scheduled reports may run at regular daily, weekly, or monthly intervals. The scheduling system must not imply hourly scheduling, and reports can only be downloaded from the web interface because email delivery is not available.

> - No ability to check multiple reports to run at the same time (`evergreen_reference_2009.txt`)

### REQ-192 - Support Drag Drop Field Selection

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The web-based report writer must support selecting report fields through drag-and-drop. This capability is needed to allow staff to create custom reports using the report writer interface. Field selection remains limited to the database fields made available by the system, and the report writer does not need to support complex queries, Boolean operators beyond simple filters, regular expressions, or query queue visibility.

> - Drag-and-drop field selection (`evergreen_reference_2009.txt`)

### REQ-193 - Support Regular Expression Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must support regular expression criteria in report queries and filters. This capability is needed when staff require criteria beyond the basic filtering available in the report writer while creating custom reports. Regular expressions must be usable as query or filter criteria within the report-writing interface. The source identifies the lack of regular expression support as a limitation, so this requirement specifically removes that limitation while retaining the report writer’s reporting context.

> - No regular expression support (`evergreen_reference_2009.txt`)

### REQ-194 - Support Saved Report Reuse

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `evergreen_reference_2009.txt`

The system must allow staff to save report definitions for later reuse. This is needed when staff create custom reports that may need to be run again without reconstructing the field selections, filters, and sorting. Saved definitions must support reuse through the report writer’s web-based interface. The source does not require support for complex queries, Boolean operators beyond simple filters, regular expressions, or fields that are not available through the report writer.

> - Ability to save and reuse report definitions (`evergreen_reference_2009.txt`)

### REQ-195 - Track And Verify Financial Transactions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-03-15  
**Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system shall track and verify financial transactions for management oversight. This capability is within the management-related scope of the reporting requirements, alongside analysis of collections, branches, patrons, and staff productivity and workflow. The requirements presuppose the general data structures and functionality of a full-fledged ILS, while separate specifications address Acquisitions and Cataloging modules.

> - Tracking and verifying financial transactions (`meeting_minutes/meeting_2009-03-15_minutes.txt`)

### REQ-196 - Configure Item Category Breakdowns

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`

The system must break material-volume counts down by item category, including categories such as adult fiction and board books. Authorized users must be able to configure standard and additional categories so each library can apply its own classifications and reporting needs. The report should support categories for total items, holds, and other classifications selected by the library. This configuration is needed because different libraries may require different breakdowns for assessment and collection management.

> Also, the breakdown by categories is important. We need things like: - Total items - Number of holds - Number of adult fiction - Number of board books - Maybe other categories too (`conversations/conv_pines014_material_volume.eml`)
> At Twin Lakes we need this for our quarterly assessment. Can we make the categories customizable? Different libraries might want different breakdowns. (`conversations/conv_pines014_material_volume.eml`)

### REQ-197 - Differentiate Acquisition And Circulation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`

The system must show separate counts for new acquisitions, checked-in items, and checked-out items in the material-volume report, together with an overall total. These distinctions are needed for collection management so staff can understand how the total volume is distributed among recently added, available, and circulating items. The report should present these counts for the specified library and retain the ability to include category breakdowns such as holds, adult fiction, and board books.

> I think Maria is asking for all three counts separately plus a total. That makes sense for collection management. (`conversations/conv_pines014_material_volume.eml`)

### REQ-198 - Report Recent Acquisition Volume

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-06  
**Sources:** `conversations/conv_pines014_material_volume.eml`

The system must use item acquisition dates to report the volume added during a selectable recent period. The report must support periods of 30, 60, and 90 days so staff can assess recent additions to a library’s collection. This capability is needed for collection assessment and for understanding how much material has been added over time. The report should base the recent-acquisition volume on items whose acquisition dates fall within the selected period.

> It would be helpful to see how much volume has been added in the last 30/60/90 days. (`conversations/conv_pines014_material_volume.eml`)

### REQ-199 - Color Code Branch Capacity Status

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-08  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system should use color coding to communicate each branch's capacity status in the capacity interface. Green must indicate a branch is under capacity, yellow must indicate that it is getting full or nearing capacity, and red must indicate that it is at or over capacity. This visual distinction is needed to help staff assess status across the high-level view of all branches and identify branches requiring attention.

> Maybe color-coding - green for under capacity, yellow for getting full, red for at/over capacity (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-200 - Control Department Head Template Rights

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must provide a department head role managed through security groups or roles. This role must allow department heads to create and modify report templates. Access control must support assignment to individuals, workgroups, and arbitrary staff groups, allowing department head privileges to be administered for the appropriate staff groups.

> Department heads (can create and modify templates) (`email_staff_login.eml`)

### REQ-201 - Control Front Desk Role Permissions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `email_staff_login.eml`

The system must provide a front desk staff role managed through security groups or roles. This role must allow front desk staff to run basic reports and apply limited filters. Access control must support assignment to individuals, workgroups, and arbitrary staff groups, so front desk permissions can be administered according to branch staffing needs.

> Front desk staff (can run basic reports, limited filters) (`email_staff_login.eml`)

### REQ-202 - Enable Branch Capacity Drilldown

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must provide a high-level capacity overview for all branches and allow a user to select an individual branch for detailed capacity information. This drill-down is needed when the overview does not provide enough detail to assess a particular branch. The capability should support staff reviewing branch capacity alongside the broader view of all branches and their key metrics.

> - Ability to drill down into individual branches (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-203 - Export Branch Capacity CSV

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must allow users to export branch capacity information in CSV format. This capability is needed for directors who want to work with the information in spreadsheets. The export should apply to the branch capacity data presented by the system, including information used in the all-branch capacity overview. Users should be able to obtain the data in CSV rather than being limited to viewing it within the interface.

> - Export to CSV (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-204 - Show Branch Capacity Trend Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must display trend data for branch capacity or load, indicating whether the relevant measure is growing or shrinking over time. This information is needed in the capacity interface so staff can review patterns in addition to current branch capacity. Trend information should be available as part of the overview that presents capacity for all branches and supports more detailed branch review.

> - Trend data (growth/shrink patterns) (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-205 - Sort Filter Branch Capacity Overview

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-09  
**Sources:** `conversations/conv_pines015_capacity_interface.eml`

The system must provide a capacity overview showing all branches and allow users to sort and filter the overview by region, library type, and current load. These capabilities are needed to organize the branch information and focus on locations or capacity conditions of interest. The interface should support staff reviewing the capacity of all branches at once, subject to any technical constraints associated with displaying 286 locations.

> - Sorting and filtering capabilities (region, type, load) (`conversations/conv_pines015_capacity_interface.eml`)

### REQ-206 - Calculate Circulation Percent By Category

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must report, for each genre and format, the percentage of total circulations attributable to that category. This information is needed by staff assessing whether shelf space is being used efficiently. The report should present the circulation percentage separately for each genre and format, so it can be considered alongside the percentage of the collection and the percentage of total shelf space occupied by that category.

> What percentage of total circulations it has (`conversations/conv_pines016_shelf_space.eml`)

### REQ-207 - Calculate Collection Percent By Category

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must report, for each genre and format, the percentage of the collection represented by that category. The report should present this measure in the context of collection and shelf-space analysis, where staff need to understand how each category relates to the overall collection. The result must support evaluation of how collection space is being used efficiently.

> What percentage of the collection it is (`conversations/conv_pines016_shelf_space.eml`)

### REQ-208 - Compare Branch Results With Average

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must allow branch managers to view shelf-space results for their local library and compare those results with the system average. The comparison must cover, for each genre and format, the percentage of total circulations, the percentage of the collection, and the percentage of total shelf space. This capability is needed to show branch managers their local situation in relation to the broader library system.

> This way branch managers can see their local situation AND see how they compare to the system average. (`conversations/conv_pines016_shelf_space.eml`)

### REQ-209 - Estimate Shelf Space From Item Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must estimate shelf space for each genre and format because shelf space is not directly tracked in the database. It should derive the estimate from item dimensions or use item count as a proxy. The report must use item counts to determine the percentage of the collection, checkout totals to determine the percentage of circulations, and the shelf-space estimate to determine the percentage of shelf space.

> Shelf space isn't directly tracked in the database. We'd need to estimate based on item dimensions or use item count as a proxy. (`conversations/conv_pines016_shelf_space.eml`)

### REQ-210 - Filter Shelf Space By DateRange

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must allow staff to filter shelf-space utilization results by a specified date range. The filter should support comparisons between periods such as the first and second quarters so staff can examine how shelf-space utilization changes over time. The capability is needed because seasonal collection patterns may affect decisions about collection distribution across branches and the system.

> Can we also filter by date range? Like, what was the shelf space utilization in Q1 vs. Q2? (`conversations/conv_pines016_shelf_space.eml`)

### REQ-211 - Side By Side Library Comparison

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-13  
**Sources:** `conversations/conv_pines016_shelf_space.eml`

The system must provide a comparison view that displays each library’s breakdown side by side. It must support breakdowns both per library and per system so directors can review the data from either perspective. The comparison view is needed for quarterly reviews and must make it easier to identify outliers.

> Also, can we include a "comparison" view that shows each library's breakdown side by side? That would make it easy to spot outliers. (`conversations/conv_pines016_shelf_space.eml`)

### REQ-212 - Include Condition Notes Per Item

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The missing and damaged items report must include condition notes associated with each reported item. These notes must describe the item condition or the cause of damage when that information is available, including examples such as water damage or vandalism. The report remains organized per branch so staff can maintain accountability and investigate patterns in missing or damaged items. The notes are needed to help staff understand possible root causes.

> Also, can the report include item condition notes? Like "water damage" or "vandalism"? (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-213 - Merge Transit To And From

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The system must combine items traveling to a branch and items traveling from a branch in one in-transit report. The report must merge transit-to and transit-from information instead of requiring separate reports for the two directions. This combined presentation is needed to make in-transit reporting easier for front-line staff. The report must cover items that have been in transit for more than a configurable number of days and support reporting per branch and per system.

> The report merges transit-to and transit-from into one report for ease of front-line staff. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-214 - Produce In Transit Report Scope

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The system must allow the in-transit report to be produced by branch and by system. This scope is needed for monitoring items transferred between branches and for reviewing in-transit activity at the system level. The report must retain the requirement to list items that have been in transit for more than a configurable number of days. Staff need these reporting scopes to identify and follow up on items that may have been lost during transfer.

> System generates a list of items that have been in-transit for more than X days (X configurable), per branch and per system. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-215 - Provide Default Transit Threshold

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The system must provide a default threshold of seven days for identifying items that have remained in transit too long. Staff must be able to configure this threshold when a different transit period is required. The threshold is used by the in-transit items report to identify items exceeding the permitted duration. This default supports the stated need to review items in transit for more than the expected delivery period.

> I need to see what's been in-transit for more than X days (X should be configurable, probably 7 days default). (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-216 - Report Missing And Damaged Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The system must generate a report of items marked as missing or damaged, organized per branch. The report is needed to support inventory auditing and collection management after staff identify missing or damaged items during shelf reading. Staff need an accessible way to review all such items for each branch instead of compiling the information manually. The reporting scope must include both missing items and damaged items.

> Right now I have no easy way to generate a report of all these items per branch. I need this for my inventory audit and for collection management. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-217 - Restrict Missing Damage By DateRange

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The missing and damaged items report must allow staff to restrict results to a specified date range. The date range is needed to support trending and review of items reported during a particular period. The system should support periods such as the last 30 days or the last quarter, as well as other specified ranges. The date-range restriction applies to the missing and damaged items report.

> The missing/damaged report can include date ranges (e.g., last 30 days, last quarter, etc.) which would be useful for trending. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-218 - Sort In Transit Report By Due Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-16  
**Sources:** `conversations/conv_pines019_020_missing_intransit.eml`

The system must allow staff to sort the in-transit report by due date. This sorting is needed so front-line staff can identify and pursue the oldest in-transit items first. The sorting capability applies to the in-transit report, which lists items that have been in transit for more than a configurable number of days and combines transit-to and transit-from information. The report must continue to support the stated branch and system reporting scopes.

> Also, for the in-transit report - can we sort by due date? Front-line staff need to chase the oldest items first. (`conversations/conv_pines019_020_missing_intransit.eml`)

### REQ-219 - Combine Purge Criteria In Selection

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must allow users to combine multiple purge criteria in a single selection. Combinations must be supported across circulation history, item status, and item condition, including conditions such as an item being damaged and not circulated for a specified period. The criteria must remain customizable so users can identify items according to different collection management needs. This capability is needed to support purging workflows and reduce the manual effort involved in reviewing item records.

> The system should let us combine criteria. (`conversations/conv_pines021_item_purging.eml`)

### REQ-220 - Combine Purge Criteria With Logical AND

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must allow staff to combine multiple purge criteria through logical conditions such as AND. This must support selections that require an item to satisfy more than one condition, such as having a missing status for a specified period and having not circulated for another specified period. The capability is needed to make purge selection more precise and support safety in item record decisions. The combined conditions must be applied together when identifying records that meet the configured purge requirements.

> Can we combine these? Like "items with status 'missing' for more than 6 months AND haven't circulated in 2 years"? (`conversations/conv_pines021_item_purging.eml`)

### REQ-221 - Configure Purge By Last Circulation Interval

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must allow staff to configure purge criteria based on the elapsed time since an item was last circulated. The configurable period must be expressible in days, months, or years, allowing staff to identify items whose circulation activity is older than the selected period. This capability is needed for activity-based weeding and purging decisions. The system must use the configured last-circulation interval when selecting item records for possible purging.

> - Activity-based criteria (last circulated X days/months/years ago) (`conversations/conv_pines021_item_purging.eml`)

### REQ-222 - Configure Purge By Status Duration Months Years

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must allow staff to configure purge criteria based on the length of time an item has remained in a specified status. The configurable period must be expressed in months or years, so staff can identify items such as those that have remained missing beyond a selected period. This capability is needed when staff prepare item records for purging and require time-based control over the selection. The system must apply the configured duration to the selected item status.

> - Time-based criteria (in status for X months/years) (`conversations/conv_pines021_item_purging.eml`)

### REQ-223 - Configure Purge Criteria By Item Attributes

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must allow users to define customizable criteria for identifying item records to purge. Criteria must include item status, circulation history, and item condition, with status options including missing, discard or weed, and damaged items. Users must also be able to specify time-based conditions, such as how long an item has remained in a status or how long it has been since the item was last circulated. This capability is needed for annual weeding and collection management reporting.

> I need to identify item records to purge based on customizable criteria. For example: - Item has been in status "missing" for more than X months - Item has status "discard/weed" (`conversations/conv_pines021_item_purging.eml`)
> - Status-based criteria (missing, discard/weed, damaged) (`conversations/conv_pines021_item_purging.eml`)

### REQ-224 - Provide Purge Candidate Read Only

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must provide a read-only report that identifies item records selected as candidates for purging. Staff must be able to review the reported candidates before any deletion occurs, and generating or viewing the report must not modify or delete records. This separation is needed to make cleanup safer and to prevent customizable purge criteria from unintentionally affecting an entire collection. Actual deletions must be handled separately from candidate identification.

> 1. Reports show candidates for purging (read-only) (`conversations/conv_pines021_item_purging.eml`)
> - Read-only reports for identifying candidates (`conversations/conv_pines021_item_purging.eml`)

### REQ-225 - Require Purge Deletion Confirmation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must require a separate confirmation step before executing purge deletions. Reports that identify purge candidates must not themselves perform the deletion, allowing staff to review the proposed records before removal. This control is needed because customizable criteria could otherwise cause someone to delete an entire collection accidentally. The confirmation requirement applies to actual purge deletions after the candidate-reporting stage.

> 2. A separate confirmation step for actual deletions (`conversations/conv_pines021_item_purging.eml`)

### REQ-226 - Schedule Purge Utility Automatic Runs

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-21  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The purging utility must support scheduled or automatic execution of purge operations. Staff should be able to configure recurring runs, including execution at the end of each year. This capability is needed to perform routine purging without requiring staff to start every run manually.

> Also wondering - can the purging utility be scheduled? Like, run automatically at the end of each year? (`conversations/conv_pines021_item_purging.eml`)

### REQ-227 - Provide Purge Selection And Status Conversion Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-22  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must provide a utility and reports that identify item records meeting configured purge criteria. Staff need this capability to locate items for purging based on conditions such as remaining missing for a specified period or having a discard/weed status. The system must also provide a report to assist with converting items from one status to another, as part of the staff workflow surrounding item purging. The identified records must be presented through the utility or reports for staff review and action.

> The system should provide a utility and reports for identifying item records to purge, based on customizable criteria such as: (`conversations/conv_pines021_item_purging.eml`)

### REQ-228 - Separate Purge Candidates From Deletions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-22  
**Sources:** `conversations/conv_pines021_item_purging.eml`

The system must present purge candidates in read-only reports and require a separate confirmation step before performing any actual deletions. This control is needed to prevent staff from accidentally deleting an entire collection when using customizable purge criteria. The system should keep the identification of candidates distinct from authorization of the deletion.

> - Separate confirmation step for actual deletions (`conversations/conv_pines021_item_purging.eml`)

### REQ-229 - Aggregate Deletions By Location And Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

Deletion reports must show deletions by library location or branch and support aggregation using those locations. The reports must use the recorded deletion information, including record type, record identifier, staff member, deletion timestamp, and location. This capability is needed to track and review deletion activity for each branch or other location.

> The report should show deletions per location and per system. (`conversations/conv_pines022_deletions.eml`)

### REQ-230 - Aggregate Deletions By Record Type

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must allow staff to query or aggregate deletion records by record type. The report must support applicable types including item, patron, bibliographic, and other record types. This capability is needed for administrative review of what kinds of records are being deleted. The type-based reporting must use the deletion audit records and operate alongside the stated date-range, deleting-staff-member, location, and system reporting dimensions.

> We can aggregate by date range, by user, by record type. (`conversations/conv_pines022_deletions.eml`)

### REQ-231 - Aggregate Deletions By Staff Member

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must allow staff to query or aggregate deletion records according to the staff member who performed each deletion. The report interface must use the deletion audit records so that administrative staff can review activity associated with a particular deleting staff member. This capability is needed to identify and analyze deletion activity by the person responsible for the action. The system must support aggregation by the deleting staff member in addition to the other stated deletion-report criteria.

> We can aggregate by date range, by user, by record type. (`conversations/conv_pines022_deletions.eml`)

### REQ-232 - Aggregate Deletions By System Scope

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must provide deletion reports that show and support aggregation of deletion records by system. The reports must also show deletions per location and provide an interface for querying the audit records. This capability is needed for administrative review of deletion activity across systems and locations. The report may aggregate records by date range, by the staff member who performed the deletion, and by record type.

> The report should show deletions per location and per system. (`conversations/conv_pines022_deletions.eml`)

### REQ-233 - Filter Deletion Audit By Reporting Period

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must allow staff to query or aggregate deletion records for a specified date range. The reporting capability must support reporting periods expressed as months, quarters, and years. This is needed when administrative staff review deletion activity for a selected reporting period. The date filtering must operate on deletion records held in the audit records used by the report interface.

> We can aggregate by date range, by user, by record type. (`conversations/conv_pines022_deletions.eml`)

### REQ-234 - Provide Deletion Audit Query Interface

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must provide a report interface that allows staff to query deletion audit data. The interface must support reporting on recorded deletions by location and system and aggregation by date range, staff member, and record type. This capability is needed to review and investigate deletions after the system has recorded them.

> A report interface to query this audit table (`conversations/conv_pines022_deletions.eml`)

### REQ-235 - Rank Deleting Staff By Count

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must provide administrative reports that identify the staff members who deleted the greatest number of records. The report must rank deleting staff members according to their deletion totals so that the staff members with the highest counts can be identified. This capability is needed for administrative review of deletion activity. The ranking must be based on deletion records and may be considered with reporting by period, type, and location.

> Top users who delete the most records (`conversations/conv_pines022_deletions.eml`)

### REQ-236 - Report Total Deletions By Period

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must provide administrative reports showing the total number of deletions for a selected reporting period. The reports must support monthly, quarterly, and annual periods. They must also support reporting deletions by type and by location, so administrative staff can review totals in the required categories. The reports must include item, patron, and other applicable deletion types as specified for administrative deletion reporting.

> Total deletions per period (month, quarter, year) (`conversations/conv_pines022_deletions.eml`)

### REQ-237 - Track Denied Deletion Attempts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-24  
**Sources:** `conversations/conv_pines022_deletions.eml`

The system must record deletion attempts that are denied, including activity involving records that the requester is not authorized or permitted to delete. Staff must be able to use these records to identify attempts to delete inappropriate items or patron records. This tracking is needed for compliance and troubleshooting, including situations where libraries must demonstrate that data handling follows retention schedules. The recorded denied attempts should support audits of deletion activity.

> Can we also track attempted deletions that were denied? That would tell us if someone is trying to delete things they shouldn't. (`conversations/conv_pines022_deletions.eml`)

### REQ-238 - Count Holds By Placement Method

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `survey_results_2009.txt`

The system must count holds according to their placement method. It must distinguish holds placed at a staff desk, public computer, and remotely, so reports can show counts for each stated method. Staff need this breakdown to analyze hold placement activity by method. The requirement concerns placement-method counts and does not state that the methods should be combined into a single undifferentiated total.

> Holds counted with method of placement: at staff desk, public computer, or remotely. (`survey_results_2009.txt`)

### REQ-239 - Report Holds And Checkouts Counts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-25  
**Sources:** `survey_results_2009.txt`

The system must provide transaction reports showing holds placed, holds filled, and check-outs by patron, library, group of libraries, system, and county. These reports are needed to present transaction activity at each stated reporting level. The system must also support individual and cumulative counting of the listed check-out types, including staff checkout, self checkout, staff renewal, self checkout renewal, online renewal, and OPAC renewal. Demographic statistics must include transactions by geographical regions and age ranges, with the data anonymized.

> Transactions report can show holds placed, holds filled, and check-outs per patron, per library, per group of libraries, per system, per county. (`survey_results_2009.txt`)

### REQ-240 - Apply Multiple Patron Filters Together

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow multiple patron characteristics to be applied together as filters in the same report. Staff need this capability to identify a specific population, such as juvenile patrons in a specified ZIP code, while also considering the characteristics relevant to library services. The filters may include patron type, ZIP code, preferred language, and other available patron characteristics.

> Can we combine demographic filters? Like "show me all Juvenile patrons in zip code 30505 who haven't checked anything out in 6 months"? (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-241 - Calculate Age Range From Birthdate

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must calculate patron age ranges at query time from the birth date field. Staff must be able to use these calculated age ranges when limiting or grouping patron queries and reports. The age brackets must be created within the query rather than relying on a separately stored age value, because the age range is derived from birth date.

> The "age range" is calculated from the birth_date field, which means we need to compute it at query time. (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-242 - Combine Circulation And Demographics

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The reporting system must allow circulation-activity criteria and demographic filters to be used together in the same report query. Staff need this capability to identify a defined patron population, such as juvenile patrons living in a specified ZIP code who have not checked out materials within a defined period. The combined query must therefore support patron characteristics and checkout activity as simultaneous filtering criteria.

> Can we combine demographic filters? Like "show me all Juvenile patrons in zip code 30505 who haven't checked anything out in 6 months"? (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-243 - Configure Patron Age Range Boundaries

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow report users to configure the boundaries of age ranges used in patron reports. This configuration is needed because reports may require different groupings, such as 0–5, 6–10, and 11–15 or other ranges that suit the report. The configured age ranges must support reporting patron characteristics by grouping results according to age range.

> The age ranges need to be configurable too. Like, 0-5, 6-10, 11-15, etc. Or 0-6, 7-12, 13-17, 18-24, 25-34... Whatever makes sense for the report. (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-244 - Filter And Group Patrons By ZIP Code

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must support patron reports that use ZIP code as a reporting characteristic. Staff must be able to limit report results to selected ZIP code values, such as showing only patrons in a specified ZIP code. The system should also allow ZIP code to be used for grouping when staff need to organize patron-related report results by that characteristic. This capability is needed for reports that limit or group patrons by their characteristics.

> I need to be able to both LIMIT and GROUP BY patron characteristics. For example: - Limit: Show me only patrons in zip code 30501 (`conversations/conv_pines023_patron_characteristics.eml`)
> - Zip code (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-245 - Limit And Group Patron Reports By Age Range

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow staff to limit patron queries and reports by age range. It should also support grouping patron reports by age range when staff need to examine patron characteristics or related activity. This capability is needed for demographic reporting that includes age range among the requested characteristics. The age-range criterion must be available as a patron characteristic for both reporting use and query limitation.

> The fields I need: - Age range (`conversations/conv_pines023_patron_characteristics.eml`)
> - Age range (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-246 - Provide Checkout Period Patron Filters

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow reports to filter patrons according to whether they have checked out materials within a specified period. This capability is needed to identify circulation activity or inactivity among patrons, including patrons who have not checked anything out in six months. Staff need this information when examining patron characteristics together with borrowing activity.

> Can we combine demographic filters? Like "show me all Juvenile patrons in zip code 30505 who haven't checked anything out in 6 months"? (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-247 - Report Patron County Of Residence

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must support reports that use a patron’s county of residence as a reporting characteristic. Staff must be able to include county of residence when running reports on patrons grouped by characteristics. This capability is needed for demographic reporting requested alongside age range, ZIP code, home branch, patron type, and preferred language. The county criterion applies to patron reporting and must represent the patron’s residence information.

> - County of residence (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-248 - Report Patron Type As Characteristic

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must support reports that use patron type as a reporting characteristic. Staff must be able to include patron type when running reports on patrons grouped by characteristics. This capability is needed for demographic or patron-characteristic reporting that also considers age range, ZIP code, county of residence, home branch, and preferred language. The patron type criterion must be available for reporting on patron records.

> - Patron type (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-249 - Support Null Demographic Values

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-29  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The reporting capability must address patrons whose demographic fields are not populated consistently. For a characteristic such as ZIP code or county of residence, the system must support showing a null value for missing data or excluding records with missing data. This behavior is needed so staff can choose how incomplete patron demographic information is handled in a report.

> Should the report show nulls for missing data, or exclude those records? (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-250 - Combine Filters With AND Or

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow staff to combine patron-characteristic filters with both AND and OR logic when limiting queries and reports. It must support both limiting results and grouping results by characteristics, including age range, zip code, county of residence, home branch, patron type, and preferred language. Null values must remain included in results, and age ranges must be configurable for each report.

> - Filters can be combined with AND/OR logic (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-251 - Filter Patron By Home Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow staff to filter patron queries and reports by the patron’s home branch. This capability is needed when staff prepare reports based on patron characteristics, including home branch. Home branch must therefore be available as a limitation criterion for patron reporting. The requirement concerns filtering results by home branch and does not state that home branch grouping is required.

> - Home branch (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-252 - Group Results By Home Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow staff to group patron results by home branch. Grouping should support reports that show patron counts by home branch and other results organized by this patron characteristic. This capability is needed for program planning, such as evaluating patrons relevant to a targeted summer reading program. Staff must be able to use home branch as a grouping field in patron reports.

> The system should allow queries and reports to be limited or grouped by various patron characteristics, including: - Home branch (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-253 - Separate Age Brackets Per Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-04-30  
**Sources:** `conversations/conv_pines023_patron_characteristics.eml`

The system must allow staff to configure the age brackets used for age-range reporting separately for each report. Reports must support using these configured age ranges to limit or group patron results by age range. This capability is needed when staff prepare reports based on differing age categories for particular reporting needs.

> - Age ranges should be configurable per report (`conversations/conv_pines023_patron_characteristics.eml`)

### REQ-254 - Cache Inactive Report Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must cache the results of generated inactive patron reports for later retrieval. Caching is needed because producing the report requires a combined query across different tables that may be slow for a large patron population. Staff retrieving an already generated report should receive the cached results without repeatedly executing the potentially slow query.

> We should run it as a background report and cache results. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-255 - Configure Inactivity Threshold Days

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must allow staff to configure the inactivity threshold to any number of days rather than restricting the report to a fixed period. This supports recurring checks over periods such as 30, 90, 180, or 365 days while allowing other durations when needed. The configurable threshold applies to identifying patrons with no circulation or electronic activity during the selected preceding period.

> Can we make it fully customizable? Like any number of days? (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-256 - Count Electronic Activity For Inactivity

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must count specified electronic activity when determining whether a patron is inactive. This activity must include logging into the OPAC or patron account, placing holds online, renewing items online, and accessing integrated digital collections. The activity must be considered together with circulation activity when identifying patrons with no activity during the configured inactivity period. Inactive patrons who still owe fines must be tracked separately because those accounts need different handling.

> 3. Renewing items online (`conversations/conv_pines024_inactive_patrons.eml`)
> "Electronic activity" should include: 1. Logging into OPAC/patron account (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-257 - Count Inactive Patrons By Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

At the system level, the system must show the count of inactive patrons for each branch. Staff need these branch-level counts to identify which branches have the most inactive patrons and to assign database-cleanup tasks to specific branches. The report must support this view when staff run it at the system level. The report is intended to help address inactive records that contribute to database growth and slower performance.

> At the system level, I can see which branches have the most inactive patrons. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-258 - Determine Most Recent Electronic Activity

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must determine a patron’s most recent electronic activity by considering OPAC login events, online hold placements, online renewals, and logged access to digital resources. It must combine these activity types when identifying the patron’s latest electronic activity. Staff need this combined activity measure to filter patrons whose last activity is more than the configured number of days ago. Digital resource access must be included when it is logged.

> For "electronic activity," we track: - OPAC login events - Online hold placements - Online renewals - Digital resource access (if logged) (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-259 - Exclude Patron Categories From Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must allow staff to exclude specified patron categories from the inactive patron report. Exclusion options must include patrons marked do not disturb, VIP patrons, staff members, and patrons who have opted out of communications. This capability is needed so outreach lists do not include patron types for whom inactive-account contact is inappropriate or not permitted.

> One more thing - we should be able to EXCLUDE certain patrons from the inactive report. For example: - Patrons with "do not disturb" flags - VIP patrons - Staff members - Patrons who have opted out of communications (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-260 - Export Inactive Report CSV

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must provide the inactive patron report in a CSV format that can be exported by staff. The export is needed to upload the report to an outreach system for contacting inactive patrons. The exported report should preserve the information required for that outreach, including the applicable inactive-patron results and any separate handling identified for patrons with outstanding fines.

> Also, the report should be exportable. We upload it to our outreach system. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-261 - Generate Inactive Reports Background

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must generate inactive patron reports as background processes rather than requiring the report query to run interactively. This is needed because the combined query uses data stored in different tables and may be slow for a large patron population, including 3.5 million patrons. Background processing must allow staff to continue using the system while report generation is in progress.

> We should run it as a background report and cache results. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-262 - Include Inactive Patron Mailing Address

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must include each inactive patron’s current mailing address in the inactive-patrons report. Staff need this information to conduct outreach and mail postcards to patrons who have not visited in a while. The address must be included regardless of the report’s configured organizational level, such as system, home library, or county. The report should also support separately tracking inactive patrons with outstanding fines because those patrons require different handling.

> We mail postcards to inactive patrons, so the report needs to include current mailing addresses. (`conversations/conv_pines024_inactive_patrons.eml`)
> Additional considerations: - Include current mailing addresses for outreach (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-263 - Track Inactive Patrons With Fines

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-05  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must identify inactive patrons who have outstanding fines and track them separately from other inactive patrons. This separation is needed because those accounts require different handling during inactive-patron outreach and related follow-up. The inactive-patron list should support configuration by system, home library, county, or other levels as needed, while retaining the separate treatment of accounts with outstanding fines.

> - Track inactive patrons with outstanding fines separately (`conversations/conv_pines024_inactive_patrons.eml`)
> And yes, we should track inactive patrons who still owe fines separately. Those accounts need different handling. (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-264 - Support Level Reports With Extras

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-06  
**Sources:** `conversations/conv_pines024_inactive_patrons.eml`

The system must allow staff to configure the inactive-patron report at the System, Home Library, and County levels. It must also support additional organizational levels as needed. The configured report must identify patrons with no circulation or electronic activity during the specified number of days, with that period configurable. The report should support current mailing addresses, separate tracking of patrons with outstanding fines, exclusion of selected patron types, CSV export, and background processing for performance.

> The list should be configurable to: - System - Home Library - County - (Other levels as needed) (`conversations/conv_pines024_inactive_patrons.eml`)

### REQ-265 - Include Uncataloged Item Circulation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `interview_cataloging_2009-05-08.txt`

The system must count transactions involving uncataloged materials and include those transactions in circulation statistics and reports. This is needed when large shipments of paperback books and children’s board books arrive without individual catalog records but must still be tracked as inventory and monitored for use. Staff need to process this material quickly, with minimal branch labor, while retaining the ability to identify how it is being used. The statistics and reports must therefore include transactions even when the materials are not fully cataloged.

> We also need to count transactions and include them in circulation statistics and reports. (`interview_cataloging_2009-05-08.txt`)

### REQ-266 - Retain Deletion Reasons Audit

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-08  
**Sources:** `interview_cataloging_2009-05-08.txt`

The system must retain the reason for each record deletion. This information is needed to support auditing by showing why records were removed and to assist troubleshooting when something goes missing from the catalog. Staff and directors need deletion reasons associated with the deletion activity for records such as item or patron records. The retained reason must remain available as part of the system’s deletion-tracking information.

> our directors want to know how many records we've deleted and why. It also helps with troubleshooting if something goes missing from the catalog. (`interview_cataloging_2009-05-08.txt`)

### REQ-267 - Migrate Report Configurations Between Environments

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`

The system must provide export and import functionality for migrating report configurations between development or training environments and production. The migration capability must include report templates, permission settings, and other configuration. Separate environments are needed so developers can test reports and new staff can practice running them without affecting production or making operational mistakes.

> The key is that configurations developed in training/dev need to be migratable to production. We need export/import functionality for report templates, permission settings, and other configuration. (`interview_sysadmin_2009-05-10.txt`)

### REQ-268 - Queue Background Complex Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`

The system must support queuing and background processing for complex reports. This is required because running a complex report can tie up the database and slow the circulation client, particularly during peak or open hours. Report processing must therefore allow searches and reports to run without disrupting circulation or other system functions.

> We need to make sure reports can be queued and processed in the background. (`interview_sysadmin_2009-05-10.txt`)

### REQ-269 - Use PostgreSQL Relational Joins

**Priority:** Could - Mentioned in 2 documents; strong wording (must). Adjusted from Should by model: Use existing PostgreSQL relational database; implementation constraint.  
**Type:** constraint  
**First mentioned:** 2009-05-10  
**Sources:** `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The reporting system must operate with the existing fully relational PostgreSQL database structure and support complex relational joins. It must work with the relational structure rather than against it, so reporting can use the database's relational capabilities. The system must remain compatible with PostgreSQL and must not require denormalization that could create synchronization issues.

> The reporting system needs to work with the relational structure, not fight against it. (`interview_sysadmin_2009-05-10.txt`)
> - Database architecture needs are clear (relational, PostgreSQL-compatible) (`interview_sysadmin_2009-05-10.txt`)

### REQ-270 - Execute Transaction Safe Batch Updates

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must perform batch updates to item location fields with transaction safety. Transfer changes must be reliably committed or rolled back so that a partial or unsuccessful update does not leave the selected items in an unreliable state. This requirement applies when staff change the records of selected items to move them to a new location. Batch location updates should support the transfer utility’s need to change multiple selected items while preserving transaction integrity.

> 3. Batch update of location field - straightforward database update with transaction safety. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-271 - Generate Printable Transfer Pull Lists

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must generate a printable pull list identifying items selected for transfer between branches. Staff need the list to gather the items that will be moved to destinations such as a mobile library, an outreach program, or a just-in-time warehouse. Pull list generation must support transfers based on manually selected titles from candidate-material queries. The list is a mechanism for moving items and must identify the items that need to be gathered.

> Pull list generation - create a printable list of items to be moved. (`conversations/conv_pines018_item_transfer.eml`)
> - Mechanisms: changing location field, generating pull lists (`conversations/conv_pines018_item_transfer.eml`)

### REQ-272 - Generate Printable Transit Labels

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must generate printable transit labels for items being transferred between branches or other locations. Each label must include a barcode for the item so staff can identify and handle transferred items during transit. This capability is needed for transfers to locations such as a mobile library and for the broader movement of selected items to a new location. The labels must be available in a printable form.

> Also, can we generate transit labels? Like, printable barcodes for the items being transferred? (`conversations/conv_pines018_item_transfer.eml`)
> - Printable transit labels (`conversations/conv_pines018_item_transfer.eml`)

### REQ-273 - Keep Items Checked Out At Destination

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must use checkout activity at the destination as a condition for transfer reversion. Transferred items that are checked out at the destination must remain there, as occurs when items sent to a mobile library are used. Items that remain unused must be eligible to return to their original location. This event-based behavior is needed to distinguish items that have been used at the destination from items that merely remain there.

> Revert when item is checked out at the destination (event-based) (`conversations/conv_pines018_item_transfer.eml`)
> We send items to a mobile library, and when they're checked out there, they should stay. But if they just sit there unused, they come back. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-274 - Log Transfer Activity History

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must record item transfer activity so staff can audit transfers and review each item’s transfer history. The history must support determining how many times an item was transferred during a specified period, such as identifying an item transferred five times in the past year. Transfer logging is needed to reveal possible problems with an item being in the wrong location. The record must cover all transfers, including activity associated with temporary movement and reversion.

> 6. Logging - track all transfers for audit purposes. (`conversations/conv_pines018_item_transfer.eml`)
> Can we track transfer history? Like, "this item has been transferred 5 times in the past year." (`conversations/conv_pines018_item_transfer.eml`)

### REQ-275 - Manually Select Items For Transfer

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The transfer utility must allow staff to manually select individual items from query results for inclusion in a transfer. This is needed when a query returns more candidate items than staff want to move, such as selecting only 25 items from a result containing 100 candidates. Selection must allow staff to identify which returned items to include in the batch transferred between branches.

> Manually select titles from query results (`conversations/conv_pines018_item_transfer.eml`)
> I should be able to check boxes and select which ones to include. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-276 - Notify Designated Transfer Exceptions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must notify designated users when an item transfer is delayed or encounters an issue. The alert must apply to transfers that are not proceeding on time as well as transfers with other reported problems. This capability is needed so the responsible recipient can identify and respond to transfer exceptions without relying solely on routine transfer review. Notifications must be directed to the designated recipients rather than issued without an identified audience.

> If an item transfer is delayed or has issues, notify me. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-277 - Preview And Confirm Transfer Changes

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The utility must show staff a preview of the items selected for transfer and the resulting locations before applying any changes. It must request confirmation after displaying the proposed transfer, including which items will move and where they will go. This safeguard is needed so staff can review the operation before execution and avoid unintended changes. The preview and confirmation apply before the transfer is committed.

> Also, the utility should show a preview before making changes. "If you run this now, 25 items will be moved from Dalton-Whitman to Mobile Library Unit 3. Confirm?" (`conversations/conv_pines018_item_transfer.eml`)

### REQ-278 - Process Large Transfers In Batches

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must process large transfer operations efficiently by dividing them into smaller batches. This processing approach is required to avoid locking the database while many items are being updated. It must support staff who perform large-scale item transfers and ensure that batch updates remain practical for operations involving a very large number of items. The requirement applies specifically to large transfer operations rather than ordinary individual transfers.

> One concern: with 9.6 million items, batch updates need to be efficient. We should process in smaller batches to avoid locking the database. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-279 - Restrict Transfer Roles Authorization

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must restrict item transfer operations to authorized staff roles rather than making them available to every staff member. The permitted roles must include managers, administrators, and transfer coordinators. This restriction is needed because transfers between branches require controlled permissions. Staff without one of these authorized roles must not be allowed to perform such transfers.

> Not every staff member should be able to transfer items between branches. This should be limited to certain roles (managers, administrators, transfer coordinators). (`conversations/conv_pines018_item_transfer.eml`)

### REQ-280 - Revert Transfers On Status Change

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must support reverting a transferred item when its configured status changes. This is needed for temporary transfers, including items sent to a book sale, where an item may need to return to its original location when its status becomes sold. The system should also support a status change such as returned as a reversion condition. Reversion must apply to the item’s original location when the configured status criterion is met.

> Can we also revert "based on other criteria"? Like, if the item's status changes to "sold" at the book sale, automatically revert it? (`conversations/conv_pines018_item_transfer.eml`)

### REQ-281 - Share Saved Transfer Queries

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must allow staff to share saved transfer queries with other staff involved in transfer operations. Shared queries should support collaborative selection of candidate items for transfers between branches. The sharing capability may follow the approach used for report templates, while the query itself supports candidate selection through the query builder.

> 2. Save/share queries - similar to report templates. (`conversations/conv_pines018_item_transfer.eml`)

### REQ-282 - Support Temporary Event Transfers

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The system must support transferring items to temporary locations for specific events or programs. This capability is needed when staff move a group of items to a community center or another temporary location for an activity such as a genealogy workshop. The system must support returning the items to their original location after the event or program. The temporary transfer applies to the items selected for that specific use.

> Also, for the outreach program use case - can we transfer items to a temporary location for a specific event or program? (`conversations/conv_pines018_item_transfer.eml`)

### REQ-283 - Undo Transfer Operation Effect

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-05-11  
**Sources:** `conversations/conv_pines018_item_transfer.eml`

The utility must provide an undo function that allows staff to reverse a transfer operation initiated incorrectly. This capability is needed when a staff member selects the wrong action or otherwise applies an unintended transfer. Undo must address the transfer operation itself so the affected items can be returned from the incorrect change. The function is an additional safeguard alongside preview and confirmation.

> And we need an undo function! What if someone clicks the wrong button? (`conversations/conv_pines018_item_transfer.eml`)

### REQ-284 - CSV Report Export Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must support exporting report results in CSV format. This capability is needed because CSV is identified as the most reliable format for data export. Staff and other report recipients need CSV when transferring report results for subsequent use outside the reporting system. CSV output must be provided alongside the required Excel and HTML formats, including for reports that serve real-time or historical reporting needs.

> Excel, HTML, and CSV formats are required. Robert noted that CSV is the most reliable for data export, Excel is preferred by business users for pivot tables, and HTML is needed for web display. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-285 - Cancel Scheduled And Running Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must allow authorized processes to cancel scheduled or running reports. This capability is needed when a report is no longer required or should not continue processing, including reports serving real-time or historical reporting needs. Staff or authorized processes need the ability to stop report execution. Cancellation is technically feasible only when the system checks for cancellation signals during report processing.

> The ability to cancel a scheduled or running report is technically feasible, but requires the system to check for cancellation signals during report processing. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-286 - Cancellation Signal Checks During Processing

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must check for cancellation signals during report processing. This is required to enable cancellation of scheduled or running reports. Staff or authorized processes depend on these checks to stop report execution after a cancellation request. The checks must occur while processing so that the cancellation capability can operate for both scheduled and running reports.

> The ability to cancel a scheduled or running report is technically feasible, but requires the system to check for cancellation signals during report processing. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-287 - Complete Current Consolidated Branch Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must ensure that data centrally consolidated from all library locations is complete and current. This is needed to provide a single source of truth for reporting across multiple locations. Staff relying on centralized management processes need confidence that consolidated reports reflect data from every branch. The system must support the enterprise-level Library Automation System data structures and functionality on which these management processes rely.

> The challenge is making sure data from all locations is complete and current. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-288 - Enterprise Infrastructure Dependency

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system may rely on enterprise-level infrastructure because Management Processes are part of an enterprise-level Library Automation System. This infrastructure may include redundant servers, backup systems, and network connectivity rather than capabilities that the reporting system provides itself. Management Processes are consolidated at a central location and accept input and provide services to multiple branches. The system must therefore operate within that enterprise infrastructure assumption.

> Robert: "This means we can rely on the infrastructure - redundant servers, backup systems, network connectivity." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-289 - Excel Report Export Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must support exporting report results in Excel format. This capability is needed by business users who prefer Excel for pivot-table analysis. Staff and other business users need the format when analyzing report data beyond the reporting system. Excel export must be provided alongside the required HTML and CSV output formats.

> Excel, HTML, and CSV formats are required. Robert noted that CSV is the most reliable for data export, Excel is preferred by business users for pivot tables, and HTML is needed for web display. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-290 - Global Admin Role Access

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a Global Admin role with full system access. Role-based access control must support access management for individuals, workgroups, and arbitrary staff groups, and permissions should be changeable by changing a role assignment. This role is needed for staff who require unrestricted access to the reporting system and its configuration.

> - Global Admin: Full system access (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-291 - HTML Report Output Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must produce report results in HTML format for web display. This capability is needed when reports must be presented through the web. Staff and other report recipients need a format suitable for viewing report results in that context. HTML output must be provided alongside the required Excel and CSV formats, while reports may support either real-time or historical reporting needs.

> Excel, HTML, and CSV formats are required. Robert noted that CSV is the most reliable for data export, Excel is preferred by business users for pivot tables, and HTML is needed for web display. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-292 - Indirect Patron Access Via OPAC

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must support patron access indirectly through OPAC displays rather than by granting patrons direct access to the management reporting system. Patrons therefore need to receive applicable reporting information through the public catalog. Direct management-system access must remain limited to the staff roles and permissions defined for the reporting environment.

> - Patron: Indirect access through OPAC displays (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-293 - Library Manager Limited Template Changes

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a Library Manager role that permits staff to run approved reports and make only limited modifications to report templates. Role-based access control must allow permissions to be assigned through roles for individuals, workgroups, and arbitrary staff groups. The Library Manager role must therefore restrict template changes while allowing the approved reporting activities specified for this role.

> - Library Manager: Run approved reports, limited template modification (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-294 - Optional Vendor Integration Data Handling

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must handle vendor integration data when such data is available, including data supplied through published APIs or automated transfers of standard-format data files. This capability is needed for vendor information such as EDI ordering data. The system must not require vendor integration data to be present at every branch, because some vendors provide it while others may not. Vendor data handling must therefore remain optional according to its availability.

> "The reporting system needs to handle this data, but we can't rely on it being present at every library." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-295 - Query Specific Error Feedback

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide administrators with low-level, query-specific feedback when a report or query fails. This feedback must identify relevant error details, including the affected table, field, and type of error. The system should also provide thorough high-level error reporting and feedback so that failures are understandable rather than reported only as a generic query failure. Related help must be accessible with screen readers.

> and shall allow low-level query-specific feedback for administrators. "When a report fails, we need to know WHY," Robert said. "Generic error messages like 'query failed' are useless. We need specifics - which table, which field, what kind of error." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-296 - Read Only Enterprise Data Interface

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must read data from the enterprise Library Automation System, including data structures and functionality associated with Acquisitions and Cataloging modules. It must use that enterprise data for reporting and must not manage acquisitions or cataloging activities. The system must interface with the enterprise data on a read-only basis for those activities, while vendor websites may be accessed through published APIs or automated transfers of standard-format data files.

> "All our data comes from the ILS," Robert said. "The reporting system doesn't manage acquisitions or cataloging - it just reads the data." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-297 - Read Only OPAC Transaction Querying

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must query data from the patron interface, or OPAC, without modifying that data. This includes data created when patrons place holds and perform circulation transactions through the OPAC. The reporting system must use these records for reporting while preserving the OPAC data as read-only. The requirement applies to data accessed from the OPAC and prohibits the reporting system from changing those patron holds or circulation transactions.

> "The reporting system queries this data, but doesn't modify it." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-298 - Separated Training Environment

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a separate training environment in which staff can experiment without risking or modifying production data. It must support migration of configurations between the development, training, and production environments through export and import of templates, permission settings, and saved queries. This separation is required so that configuration and reporting experiments can be performed safely before changes are applied to production.

> "And the training environment needs to be safe - staff should be able to experiment without risking production data." (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-299 - Staff Role Permission Restricted Reporting

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must provide a Staff role that permits staff to run reports only within their assigned permissions. Access must be controlled through roles that can be assigned to individuals, workgroups, and arbitrary staff groups. The system should make it easy to change a staff member’s permissions by changing the assigned role, while preventing reporting activity outside those permissions.

> - Staff: Run reports within assigned permissions (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-300 - Survey Name To ID Resolution

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-06-30  
**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`

The system must accept a survey filter specified by survey name and resolve that name internally to the corresponding survey ID. This capability is needed when reports are filtered by survey name rather than survey ID, so the report can apply the requested survey filter. The name resolution must occur within the system rather than requiring the filtering specification to provide the survey ID before report filtering is performed.

> The ability to filter by survey name rather than survey ID requires the system to resolve names to IDs internally. (`meeting_tech_subcommittee_2009-06-30.txt`)

### REQ-301 - Calculate Item Value From Purchase Price

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must calculate and report the value of items using purchase-price data from item records. Staff must be able to obtain the value for the entire collection or for a filtered portion of it. The filtering capability must support subsets such as items with a specified status, items in a specified format, or items in a specified collection. Examples include valuing all longoverdue items, all DVDs in the children's collection, or the entire collection.

> Value of items report - staff should be able to get the value of items based on data in item records. This could be the entire collection, or a portion. (`email_financial_reports.eml`)

### REQ-302 - Enforce Archived Data Retention

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must enforce data-retention policies for archived data. Archiving must follow applicable state and local requirements, including retaining designated data for seven years when it is required for audit purposes. This capability is needed to support compliance with audit-related retention obligations and must apply the retention periods established by those policies.

> Some data needs to be retained for 7 years for audit purposes. The system needs to enforce retention policies. (`email_financial_reports.eml`)

### REQ-303 - Join Patron And Item Financial Data

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must support financial reporting queries that join financial data attached to patron records with financial data attached to item records. Staff need this combined view because financial information is maintained in both record types. The joined data must be available when querying financial reports, including reports involving fines and charges associated with patron accounts and items.

> The financial data is attached to patron records AND item records. So when we query for financial reports, we need to be able to join these data sources. (`email_financial_reports.eml`)

### REQ-304 - Report Accrued Fines By Period

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must report fines and charges accrued during selectable time periods, including the last twelve months, year to date, and the last month. Reports must categorize accrued amounts by type of charge, including overdue fines, damaged item charges, and lost item charges. Staff need this information as part of the financial reports used to review accrued patron charges over defined periods.

> Fines and charges accrued per time period (last 12 months, YTD, last month) (`email_financial_reports.eml`)
> Fines and charges accrued per time period (last 12 months, YTD, last month) and per type of charge (overdue fines, damaged item charges, lost item charges, etc.) (`email_financial_reports.eml`)

### REQ-305 - Track Payments By Collecting Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-13  
**Sources:** `email_financial_reports.eml`

The system must track each payment according to the library or branch where staff collected it. Each branch must be able to view the payments collected at its location for end-of-month reporting. The system must also update financial information immediately when a patron makes a payment at the front desk, so that collected-payment information remains current.

> Payments tracking by library is important for our end-of-month reports. Each branch needs to be able to see what payments were collected at their location. (`email_financial_reports.eml`)

### REQ-306 - Compare Data Across Branches

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must support reports that compare data across library branches. Cross-branch comparison reports are needed to support reporting across the library and were identified as a requirement by branch managers. The comparisons should allow relevant branch data to be examined together rather than only as separate branch reports.

> - Need for cross-branch comparison reports (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-307 - OPAC And Vendor Data Integration

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The Management Processes system must interact with the patron-facing Online Public Access Catalog (OPAC) to query data created through the patron interface. This data includes holds and circulation information, which patrons create through the OPAC and which reports need to use. The system must also handle data from external vendor websites when those sources support published APIs or automated transfers of standard-format data files.

> DE-3: Management Processes interact with a patron interface, also known as an Online Public Access Catalog (OPAC). (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-308 - PINES Reports Templates Provision

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The Reports functionality must provide templates that meet the needs of all PINES libraries. These templates are needed as part of the Reports Working Group’s responsibility to determine and create templates for all libraries. The functionality should support the group’s broader work of documenting optimal Reports functionality, testing new Reports development, and compiling reports needed for an Executive Reports Interface.

> Determine and create templates needed for all PINES libraries. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-309 - Process Reports In Background

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must process searches and reports in the background or through queuing. This capability is needed so report generation during open or peak hours does not slow down circulation clients or disrupt other system functions. Staff must be able to request reports without making circulation operations unavailable or unresponsive. The requirement applies to a large, multiple-system library consortium, where report processing must be separated from active operational processing when necessary.

> It is highly desirable that searches and reports can be processed during open hours without disrupting other system functions. We need background processing/queuing to prevent report generation from slowing down the circulation client. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-310 - Provide Board Predefined Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide predefined reports for boards and executive stakeholders. These reports are needed because board and executive reporting needs to be established in advance for review by those stakeholders. The predefined reports should support the board and executive reporting identified by library staff and directors.

> - Board/executive reports need to be pre-defined (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-311 - Provide Collection Weeding Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports that support collection weeding activities. These reports are needed because branch managers identified weeding reports as frequently used in managing collections. Staff responsible for collection management must be able to use the reports when determining which items should be considered during weeding activities. The system must make this reporting capability available as part of its management reporting functions.

> - Weeding reports are frequently used (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-312 - Provide Data Quality Assessment Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports for identifying and assessing data quality issues. These reports are needed because data quality reports were identified as a reporting need during discussions with branch managers and a director. The system should make data quality information available to the staff responsible for reviewing library data.

> - Data quality reports are needed (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-313 - Provide Director Level Financial Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide financial reports suitable for review by library directors. These reports are needed because financial reporting needs are understood at the director level. The system should make the reports available for director-level review as part of the library’s reporting activities.

> - Financial report needs are understood at the director level (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-314 - Provide Inventory And Capacity Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide inventory and capacity reports for operational use. These reports are needed because branch managers use them daily. The system should support the operational need for comparing information across branches, as cross-branch comparison reports were identified as needed. Inventory and capacity reporting is therefore required for branch-level operational oversight and related management analysis.

> - Inventory and capacity reports are used daily (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-315 - Provide Shelf Space Utilization

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports showing shelf space utilization. These reports are needed because shelf space utilization was identified as important to branch management. Staff, including branch managers, must be able to use the reports to assess how shelf space is being used in support of collection and facility planning. The system must present shelf space utilization as a distinct reporting capability within its management processes.

> - Shelf space utilization reports are important (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-316 - Reliable Network Connectivity

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The Management Processes system must support reliable network connectivity between its central location and the multiple library locations it serves. This connectivity is required because management processes are consolidated centrally while accepting input from and providing services to multiple locations. Reliable connectivity supports consistent reporting across locations within the enterprise-level Library Automation System.

> Centralization enables consistent reporting but requires good network connectivity. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-317 - Report Missing Damaged Items By Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system must provide reports identifying missing and damaged items at the branch level. These reports are needed because branch managers identified missing and damaged item reporting as an operational need. Staff at each branch must be able to use the reports to monitor item status and support branch-level management activities. The reports must distinguish the branch context so that missing and damaged items can be reviewed for the appropriate location.

> - Missing/damaged item reports are needed per branch (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-318 - Server OS Compatibility

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** 2009-07-20  
**Sources:** `meeting_minutes/meeting_2009-07-20_minutes.txt`

The management processes must operate on a server running either Linux or Solaris. Both operating systems are acceptable environments for the system. This requirement supports library installations that use Linux as well as larger systems that use Solaris. The server platform must therefore be compatible with either of these operating systems, without requiring one specific choice between them.

> Management Processes shall operate on a Linux or Solaris server. (`meeting_minutes/meeting_2009-07-20_minutes.txt`)

### REQ-319 - Clone Report Template Preserve Original

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must allow staff with appropriate permissions to clone an existing report template and create a new report variant from it. The cloning operation must preserve the original template without modifying it. This capability is needed when staff require a variation of an established report while the original template remains available for consistent reporting.

> We also need the ability to "clone" reports - take an existing template and create a new one based on it. This is different from modifying the template - it's creating a new variant. (`email_report_features.eml`)

### REQ-320 - Display Report Submission Timestamp

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The reporting interface must show staff when a report was submitted. The submission time must be available for reports that staff have placed in the processing queue. This information is needed to help staff track their submitted reports and understand their place and progress while waiting for processing.

> When their report was submitted (`email_report_features.eml`)

### REQ-321 - Provide Universal Record Query Interface

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must provide a user-friendly query interface that supports queries against every record type in the system. Staff must be able to select fields to query, choose values from picklists, select regular expressions from a dropdown, and combine query conditions with Boolean operators. This capability is needed to let staff design reports and queries across the full range of available records.

> We need a user-friendly interface for designing queries against all record types. (`email_report_features.eml`)
> QUERY TOOL: User-friendly interface for designing queries against all record types. (`email_report_features.eml`)

### REQ-322 - Select Regular Expressions From Dropdown

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The system must allow staff to choose regular expressions from a dropdown while constructing queries. This capability must be available within the query interface used to design queries against record types. Providing selectable regular expressions will support the requested user-friendly query construction process without requiring staff to enter them manually.

> Staff should be able to select fields to query, select values from picklists, use regular expressions from a dropdown, and use Boolean operators. (`email_report_features.eml`)

### REQ-323 - Show Report Queue Processing Position

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-27  
**Sources:** `email_report_features.eml`

The reporting interface must show staff that a submitted report is in the processing queue. It must also show how many reports are ahead of the submitted report. This information is needed because staff require confirmation and queue visibility after submitting a report rather than receiving no indication of its progress.

> They need to see: - That their report is in the queue - How many reports are ahead of theirs (`email_report_features.eml`)

### REQ-324 - Clone Templates With Restricted Changes

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

The system must allow users to clone report templates. Administrators must be able to create templates that are available to staff, and staff must be able to run those templates as-is or modify them within the permitted limits. When a template is modified or cloned, the system must respect restrictions on which filters and fields may be altered.

> Clone capability. (`email_report_features.eml`)

### REQ-325 - Enable Regex In Query Builder

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

The query tool must support regular expressions when staff construct queries against all record types. Regular-expression support is needed as a query-construction capability within the user-friendly query interface for designing reports. Administrative controls must govern access to the query tool.

> Boolean operators, picklists, regex support. (`email_report_features.eml`)

### REQ-326 - Provide Query Picklists By Record

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** 2009-07-28  
**Sources:** `email_report_features.eml`

The query tool must provide picklists for constructing queries against all record types. Picklists are needed as part of a user-friendly query-design interface so staff can select available query values when building reports. Access to the query tool must remain subject to administrative control.

> Boolean operators, picklists, regex support. (`email_report_features.eml`)

### REQ-327 - Allow Add Canned Reports By Permission

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow authorized staff to add additional canned reports. Access to this capability must be controlled according to the staff member’s permission level. This capability is needed to extend the available set of canned reports beyond those already provided, while limiting report creation or addition to staff whose permissions authorize it.

> Ability to add more canned reports via permission level (`early_draft_srs_galecia.txt`)

### REQ-328 - Allow Authorized Ad Hoc Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow authorized staff to run ad hoc reports against specific sets of data. System administrators must be able to use shared folders to allow or disallow staff from running specific reports or running ad hoc reports on defined data sets. Access must be governed by distinct, fine-grained permissions that are easy to administer, with controls limiting who can create or clone reports.

> System administrators should be able to create shared folders to allow or disallow staff from running specific reports, and/or to run ad hoc reports on specific sets of data. (`early_draft_srs_galecia.txt`)

### REQ-329 - Allow Email Report Delivery

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow report users to enter email addresses for delivery of report output. This capability is needed when a user configures a report for transmission by email rather than relying only on on-screen or other output handling. The entered addresses must be associated with the report being sent, and the system should support their use when reports are scheduled to run ASAP, hourly, daily, weekly, monthly, or yearly.

> Ability to enter email addresses for report to be sent to - would be great to (`early_draft_srs_galecia.txt`)

### REQ-330 - Allow Local Admin Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow Local System Administrators to run system reports. Local System Administrators are individuals, typically library managers, who oversee library processes and have elevated permissions within the system; they can also configure local settings. This reporting capability is needed by library managers because they use reports for planning and evaluation. The capability must support their responsibilities for overseeing local library processes and evaluating library services.

> They can configure local settings and run system reports. (`early_draft_srs_galecia.txt`)

### REQ-331 - Allow Partial Data Selection

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow users to select individual parts of the available data for inclusion in a report. This selection must support checking off any desired part of the data rather than requiring all available data to be included. The capability applies to the report data choices provided through the reporting interface.

> Check off any part of data you want (`early_draft_srs_galecia.txt`)

### REQ-332 - Archive Transactions With Patron Privacy

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must archive transaction data in a form that protects patron privacy in accordance with applicable state law. This capability is needed to retain transaction information while limiting disclosure of patron-related information. The archived data must still support useful demographic statistics.

> Transactions should be archived in a form that protects patron privacy as defined by State Law, while providing useful demographic statistics. (`early_draft_srs_galecia.txt`)

### REQ-333 - Assist Batch Status Conversion

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report that assists with the batch conversion of statuses. This capability is needed when report users need support for converting statuses in batches rather than handling status changes only as individual actions. The report must be available as part of the reporting capabilities and must assist with the batch conversion activity. The source does not state a required output format, schedule, recipient configuration, or permission condition for this report.

> The system provides a report to assist in the batch conversion of statuses (`early_draft_srs_galecia.txt`)

### REQ-334 - Combine Canned Report Outputs

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must present the output of canned reports selected for simultaneous execution within a single document. This allows the results of multiple canned reports checked off from the report list to be viewed together rather than as separate documents. The combined document applies to canned reports that are run at the same time.

> Canned reports can be checked off from a list to run at the same time and will be viewed within one document. (`early_draft_srs_galecia.txt`)

### REQ-335 - Control Selected Item Transfers

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The item-transfer utility must let staff move selected items by changing their location records and by generating pull lists. These mechanisms support transfers of batches of items between branches, including movement to a mobile library unit or an outreach program collection. The utility should also support reverting items to their original location after a set period of time. The transfer methods apply to items selected from query results.

> - Ability to change records of selected items to move to new location (`early_draft_srs_galecia.txt`)
> - Mechanisms for moving items: changing location field, generating pull lists (`early_draft_srs_galecia.txt`)

### REQ-336 - Cross Row MARC Field Retrieval

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The reporting system must retrieve and report specific MARC fields even when those fields are stored across multiple rows. This capability is needed because staff currently need to pull particular MARC fields, but the fields may be spread across multiple rows. Staff preparing reports need the system to locate and present those requested fields despite that storage arrangement, and the source does not state which MARC fields are required or impose additional retrieval conditions.

> Need to pull specific MARC fields but they're spread across multiple rows (`survey_results_2009.txt`)

### REQ-337 - Custom Locally Defined Report Support

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow staff to create or use custom and locally defined reports. These reports must support local reporting needs such as collection development, program attendance tracking, and staff productivity reporting, including time spent per transaction. This capability is needed because 38% of respondents use custom reports, while reported reporting issues include unavailable filters, difficult access to needed reports, duplicate rows in exported data, and MARC fields spread across multiple rows.

> Among those who use custom reports, the most common are: - Collection development reports - Program attendance tracking - Staff productivity reports (time spent per transaction) (`survey_results_2009.txt`)

### REQ-338 - Display Patron Checkouts Holds

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must display the number of check-outs and placed holds for each patron. This information must be available within transaction reporting so staff can review individual patron activity. The display must distinguish check-outs from placed holds and support the transaction report context that can be organized per patron, branch, selected group of branches, system, or county. The requirement applies to all counted hold requests, regardless of whether they were placed at a staff desk, a public computer inside the library, or remotely.

> The system displays the number of check-outs and placed holds per patron. (`early_draft_srs_galecia.txt`)

### REQ-339 - Display Query Criteria With Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must display the query selections together with the corresponding report results. Staff must be able to see which criteria were used to generate each report. This display must accompany the results so the report criteria remain clear when staff review the report.

> The system should provide the query selections along with the results, so users can see what criteria were used to generate the report. (`early_draft_srs_galecia.txt`)

### REQ-340 - Display Report Selection Criteria

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must present report selection criteria in a clearly defined manner. This is needed so staff can quickly identify the parameters used for a report and understand the scope of its results. Report results must display the selected date criteria at the top or bottom, including the selected date range and the report name. The displayed criteria must correspond to the selections used to generate the report.

> Selection criteria is clearly defined (`early_draft_srs_galecia.txt`)

### REQ-341 - Edit Canned Report Display Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow report users to edit canned reports for display purposes. Such editing must include the ability to add a field such as shelving location as a displayed value. This capability is needed when the standard display of a canned report does not include all information required by report users. The system should support modifying the report’s displayed fields while retaining the canned report as the basis for the report.

> Ability to edit canned report for display purposes such as adding shelving location as a display (`early_draft_srs_galecia.txt`)

### REQ-342 - Edit Canned Report Display Options

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must allow staff to edit the display options of canned reports. This capability is needed when a canned report must present information according to staff-selected display preferences rather than only its existing presentation. The system must apply this editing capability to the display options of canned reports, while the source identifies the absence of that capability as a reporting-system gap.

> - No ability to edit canned report display options (`evergreen_reference_2009.txt`)

### REQ-343 - Edit Recurring Report Configurations

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow report users to edit recurring reports after they have been configured. Editing must include adding or removing report selections and changing the email addresses associated with delivery. This capability is needed when the contents or recipients of a recurring report change while its recurring delivery remains required. The system must apply these edits to the recurring report configuration rather than limiting changes to a single report run.

> Ability to edit recurring reports by adding or removing report selections as well as editing the email addresses (`early_draft_srs_galecia.txt`)

### REQ-344 - Enable Elevated Local Administrator Config

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide Local System Administrators with elevated permissions to configure local system settings. Local System Administrators are typically library managers who oversee library processes and require these permissions within the system. They also need the ability to run system reports as part of their responsibilities. The configuration capability must be available to this administrative role while remaining associated with its elevated permissions.

> They can configure local settings and run system reports. (`early_draft_srs_galecia.txt`)

### REQ-345 - Excel Export Duplicate Row Prevention

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must produce Excel exports without unnecessary duplicate rows in the exported data. This is needed because staff currently need to export data to Excel but encounter too many duplicate rows in the result. Staff who use Excel exports need clean output for their reporting work, and the stated condition is that unnecessary duplication must be avoided; the source does not specify other export formats or data-cleaning rules.

> I need to export to Excel but the data has too many duplicate rows (`survey_results_2009.txt`)

### REQ-346 - Exclude Renewal From Checkin

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must report check-in dates and times while excluding renewal transactions from those values. This is needed to ensure check-in time reporting represents check-in activity rather than renewals, as requested as an additional reporting feature. The exclusion applies specifically to renewal transactions; the requirement does not state that other transaction types should be omitted. No further exclusion condition is specified for the check-in date and time reporting.

> Checkin date/time should not include renewals (`survey_results_2009.txt`)

### REQ-347 - Fine Grained Report Permission Control

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide fine-grained permissions that control which report users can create particular reports and which report users can run them. This is needed when access to report creation or execution must be controlled separately for different reports. Staff responsible for managing report access need this capability, and the source does not state additional conditions or limits on how the permissions must be configured.

> Fine-grained permissions (who can create/run what): 76% (`survey_results_2009.txt`)

### REQ-348 - Flatten MARC Fields In Row

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must retrieve MARC record fields for inclusion in report results. It must present the retrieved MARC fields on a single row of data rather than separating them across multiple rows. This capability is needed when staff require MARC record information in a flattened report format.

> Ability to pull MARC record fields so that they appear on a single row of data (`early_draft_srs_galecia.txt`)

### REQ-349 - Generate Hold And Checkout Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must generate transaction reports covering holds placed, holds filled, and check-outs. Reports must support views per patron, per branch, per selected group of branches, per system, and per county, so staff can review activity at the required organizational level. The system must count all hold requests, including requests placed at a staff desk, at a public computer inside the library, or remotely. These reports are needed to summarize circulation and hold activity across the specified reporting scopes.

> The system can generate a report of transactions (holds placed, holds filled, and check-outs) per patron, per library, per selected group of libraries, per system, per county. (`early_draft_srs_galecia.txt`)

### REQ-350 - Generate Pivot Table Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must support generating report results in pivot table format. This output is needed when staff require an alternative way to organize and analyze reporting data, including during the additional reporting and feature requests identified by respondents. Pivot table output is one of the requested report capabilities, alongside historical reporting, real-time reporting for busy periods, cancellation of scheduled or running reports, and inclusion of null and blank fields.

> Pivot table output would be great (`survey_results_2009.txt`)

### REQ-351 - Group Transactions By Hour

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support grouping transaction statistics by hour to show activity during different periods. This capability is needed for analyzing transaction activity, including check-ins, check-outs, fines collected, and patron registrations, either across all transactions or by transaction type. The system must apply this grouping to transaction history maintained for the configurable retention period, while monthly and annual aggregate information remains available indefinitely.

> Transactions can be grouped by hour, terminal, branch, and system. (`early_draft_srs_galecia.txt`)

### REQ-352 - Group Transactions By System

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support grouping transaction statistics by system. This capability is needed to analyze transactions across the library system, including check-ins, check-outs, fines collected, and patron registrations. Staff must be able to query the results for all transactions or for a selected transaction type, subject to the stated transaction-history retention period and the indefinite retention of monthly and annual aggregates.

> Transactions can be grouped by hour, terminal, branch, and system. (`early_draft_srs_galecia.txt`)

### REQ-353 - Group Transactions By Terminal

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support grouping transaction statistics by terminal. This capability is needed to analyze activity associated with terminals, including check-ins, check-outs, fines collected, and patron registrations. Staff must be able to query the grouped information across all transactions or by transaction type, subject to the stated retention of transaction history and indefinite retention of monthly and annual aggregates.

> Transactions can be grouped by hour, terminal, branch, and system. (`early_draft_srs_galecia.txt`)

### REQ-354 - Identify Bibliographic MARC Missing Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must identify bibliographic records that are missing specified MARC fields. Staff need this report to locate records whose bibliographic data does not contain required or selected MARC fields. The reporting function must allow the relevant MARC fields to be specified so that records can be identified according to the selected criteria. This capability is required because reporting on bibliographic records missing specific MARC fields is currently not available.

> - Bib Records missing specific MARC fields (not available) (`evergreen_reference_2009.txt`)

### REQ-355 - Identify Inactive Patron Accounts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide patron reports that identify inactive accounts. These reports are needed because patron reports include demographics and inactive accounts among report types used from the current Evergreen system. Staff need patron-focused reporting to identify inactive accounts as part of patron reporting. The requirement covers identification of inactive accounts; it does not state a threshold, time period, or additional action for accounts identified.

> - Patron reports (demographics, inactive accounts): 52% (`survey_results_2009.txt`)

### REQ-356 - Implement Consortium Level ILS Changes

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow Global System Administrators to implement software changes and configurations for the ILS at the consortium level. Global System Administrators manage the ILS across the consortium and are responsible for implementing software changes and configurations. This capability must support administration of the system at the consortium level rather than only within an individual branch or organizational unit. The requirement applies to the global administration of the ILS.

> * Global System Administrator: The individual(s) who manage the ILS at the consortium level, implementing software changes and configurations, and generating statistical reports for the entire system. (`early_draft_srs_galecia.txt`)

### REQ-357 - Indicate Last Circulation Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

Item reports must indicate the last circulation date for each item. Staff need this information when reviewing item reporting and assessing an item's circulation history. The requested field is specifically the last circulation date, and it is separate from the additional requirement that checkin date and time should not include renewals.

> Ability to indicate last circulation date on item reports (`survey_results_2009.txt`)

### REQ-358 - Integrate Online Help With Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide an online help system integrated with reports. Help must be available within the reporting context so staff can obtain guidance while working with reports. This capability is required because the existing reporting system lacks online help integrated with reports.

> - No online help system integrated with reports (`evergreen_reference_2009.txt`)

### REQ-359 - Keep Archived Data Demographically Usable

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must preserve archived transaction data in a form that remains usable for producing useful demographic statistics. This capability is needed when transaction information is archived while patron privacy must be protected. The system must therefore support demographic reporting without removing the usefulness of the archived data.

> Transactions should be archived in a form that protects patron privacy as defined by State Law, while providing useful demographic statistics. (`early_draft_srs_galecia.txt`)

### REQ-360 - List Items By Total Use Count

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must list items having a specified total use count. This report type is needed because a list of items with a specific total use count is identified as unavailable. The system must allow the total use count to be specified as the condition used to produce the item list.

> - List of Items with specific Total Use Count (not available) (`evergreen_reference_2009.txt`)

### REQ-361 - List Last Copy Owned Deletions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of items deleted when each item was the last copy owned by the library system. The list must support staff activities related to updating WorldCat after such deletions occur. The system should distinguish this last-copy deletion condition so that the resulting report identifies the items relevant to those updates.

> Ability to get a list of items deleted that was the last copy owned by the library system in order to update WorldCat (`early_draft_srs_galecia.txt`)

### REQ-362 - List Patrons By Expiration Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of patrons that can be filtered or organized by expiration date. This list is needed as part of the patron reports for locating or reviewing patrons according to the expiration date associated with their patron records. Staff must be able to use the list when expiration-date-based patron information is required. The source does not specify date ranges, additional filters, sorting behavior, timing, or other limits for the list.

> - List of Patrons by Expiration Date (`early_draft_srs_galecia.txt`)

### REQ-363 - List Patrons By Survey Answer

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of patrons grouped or filtered by survey answer. This list is needed as part of the patron reports for identifying patrons associated with particular survey answers or reviewing patrons by their responses. Staff must be able to use the list when patron-level survey-answer information is required. The source does not define additional fields, filtering criteria beyond survey answer, sorting, timing, or other limits.

> - List of patrons by survey answer (`early_draft_srs_galecia.txt`)

### REQ-364 - List Patrons With Barred Status

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of patrons whose status is barred. This list is needed as part of the patron reports for identifying patrons with barred status. Staff must be able to use the list when information about barred patrons is required. The source does not specify additional filtering, sorting, fields, timing, or conditions for producing the list beyond the patron's barred status.

> - List of patrons who are BARRED (`early_draft_srs_galecia.txt`)

### REQ-365 - Manage Report Delivery Recipients

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide an address book for managing recipients used for report delivery. Staff must be able to use this address book when reports are delivered, including reports delivered by email. The capability is needed because report delivery currently has no address book, and the requirement applies specifically to recipients for report delivery rather than to general reporting information.

> - No address book for report delivery (`evergreen_reference_2009.txt`)

### REQ-366 - Manage Report Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide capabilities for managing report templates. Staff who create or maintain reports need these capabilities to support the reporting system’s template-management processes. Template management is required as part of addressing identified reporting gaps, alongside fine-grained permissions, report queue visibility, multiple output formats, scheduling options, accessibility compliance, and separation of reporting from production operations.

> - No report template management system (`evergreen_reference_2009.txt`)
> Implement fine-grained permissions and template management (`evergreen_reference_2009.txt`)

### REQ-367 - Manual Record Selection From Results

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow staff to manually select individual records from query results. This capability is needed as an administrative feature when staff review query results and identify particular records for further action. The source reports that 39% of respondents need manual selection from query results, alongside related needs to query for candidate materials and save queries for repeated use.

> Manually select from query results: 39% (`survey_results_2009.txt`)

### REQ-368 - Merge Cataloged Non Cataloged Circulation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a total circulation report that merges cataloged and non-cataloged circulation data. The report must present the combined circulation count needed for staff to assess overall circulation activity across both data types. The circulation reporting scope includes checkouts, renewals, and non-cataloged circulation, so the merged total should account for these circulation activities. This report must remain distinct from separate checkout, renewal, and non-cataloged counts.

> - Total Circulation Count (Merging both Cat and Non-Cat circulation data) (`early_draft_srs_galecia.txt`)

### REQ-369 - Preserve Report Accuracy After Edits

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must preserve the accuracy of report results when staff modify a report template. Administrators must be able to limit which filters and display fields can be altered so that permitted changes do not compromise dependable output. This requirement applies when templates are adapted for individual reporting needs rather than run as-is. The resulting report must remain accurate after the allowed modifications.

> Changes to templates should not compromise the accuracy of results. (`early_draft_srs_galecia.txt`)

### REQ-370 - Prioritize Reports Execution Queue

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow certain report types to be prioritized in the report execution queue. Prioritized reports must be placed ahead of resource-consuming reports so they can reach the top of the queue. This capability is needed when staff require selected report types to receive precedence over reports that may consume substantial resources.

> Ability to prioritize certain types of reports so they will pop to the top of the queue over resource-consuming reports (`early_draft_srs_galecia.txt`)

### REQ-371 - Prioritize Selected Report Types

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must allow authorized users to prioritize selected types of reports. This capability is needed when certain report types require preferential processing compared with other reports. Prioritization must apply to selected report types rather than being limited to an undifferentiated report queue. The requirement addresses the stated absence of any ability to prioritize certain types of reports.

> - No ability to prioritize certain types of reports (`evergreen_reference_2009.txt`)

### REQ-372 - Process Long Running Reports Background

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must process long-running reports in the background. This capability is needed when a report requires extended processing, so that long-running report processing is handled separately from the immediate reporting interaction. The requirement addresses an architectural gap in which background processing for long-running reports is absent, and it applies specifically to long-running reports rather than all reporting activity.

> - No background processing for long-running reports (`evergreen_reference_2009.txt`)

### REQ-373 - Provide Added Items Listing

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of items that were added. This report is needed for staff to review the items added to the library collection or item records. The result must identify individual added items rather than provide only an aggregate count. The system must provide this report as a list within the item reports, separately from the items added count.

> - List of Items Added (`early_draft_srs_galecia.txt`)

### REQ-374 - Provide Bills Snapshot Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide snapshot bills reports for historical points in time. Staff need this capability to review bills data as it existed at an earlier point rather than only viewing the current state. The requested report must support going back in time for bills snapshots, consistent with the broader request for historical reporting that shows what the data looked like on a specific date even if the shelving location has changed.

> Need a snapshot bills report going back in time (`survey_results_2009.txt`)

### REQ-375 - Provide Canned Report Templates

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The product must include a defined set of prewritten canned report templates. Staff must be able to use these generic reports either as soon as possible or on a recurring basis. The templates must be delivered with the product rather than created only when a report is requested. Canned reports must also support use of yesterday’s, last week’s, last month’s, or last year’s data, and selected canned reports can be run together and viewed within one document.

> There should be a certain set of templates that are pre-written and delivered with the product. (`early_draft_srs_galecia.txt`)

### REQ-376 - Provide Check In Count Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a Check-In Count report showing the number of items checked in. The report must distinguish check-ins from the other listed circulation reports, including checkout counts, renewals counts, non-cataloged counts, and total circulation counts. Staff need this report to review check-in activity as part of the available circulation reporting.

> - Check in Count (`early_draft_srs_galecia.txt`)

### REQ-377 - Provide Checkout Count Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a Checkout Count report showing the number of item checkouts. The report must include checkouts only and must exclude renewals and other circulation activity. Staff need this separate circulation report to distinguish checkout activity from broader circulation counts that include renewals, non-cataloged circulation, or other circulation data.

> - Checkout Count (includes checkouts only) (`early_draft_srs_galecia.txt`)

### REQ-378 - Provide Circulation By Dewey

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide circulation counts organized by Dewey classification. Staff need this report to examine circulation activity according to the Dewey organization of items. The report must be available as a circulation report alongside counts organized by circulation modifier, shelving location, MARC data, circulation location, patron county, patron home library, and age demographic. The source identifies circulation by Dewey as a required report type even though it was listed as unavailable in the referenced Evergreen report set.

> - Circulation Count by Dewey (`early_draft_srs_galecia.txt`)

### REQ-379 - Provide Circulation Modifier Counts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide circulation counts organized by circulation modifier. Staff need this report to review circulation activity according to the modifier associated with each circulation record or item. It must be provided as a distinct circulation report in addition to reports organized by Dewey classification, shelving location, and MARC data. The reporting set also identifies circulation counts by circulation modifier, Cat1, and Cat2, including categories such as Adult, YA, and Juv.

> - Circulation Count by Circ Modifier (`early_draft_srs_galecia.txt`)

### REQ-380 - Provide Circulation Totals By Type

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must retrieve total circulation and provide a breakdown by circulation type. The total must include checkouts, renewals, and noncataloged transactions. This capability is needed by staff who require both an overall circulation figure and separate visibility into the included transaction types when reviewing circulation reports.

> Ability to retrieve total circ including checkouts, renewals, and noncats with a breakdown displaying those circ types (`early_draft_srs_galecia.txt`)

### REQ-381 - Provide Claims Returned Report

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide a claims-returned report. This report is needed to identify items associated with claims that they have been returned, supporting library reporting activities related to item and patron accounts. The claims-returned report must be available as a reporting function because this report type is identified as not available in the current reporting capabilities.

> - Claims Returned report (not available) (`evergreen_reference_2009.txt`)

### REQ-382 - Provide Dewey Breakdown Circulation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide circulation counts broken down by Dewey classification. This report type is needed because circulation count by Dewey is identified as a missing report type. The system must make the Dewey breakdown available for reporting rather than leaving this circulation analysis unavailable.

> - Circulation Count by Dewey (not available) (`evergreen_reference_2009.txt`)

### REQ-383 - Provide Edited Items Aggregate Count

**Priority:** Could - Mentioned in 2 documents. Adjusted from Should by model: Items edited count supports auditing but is relatively narrow.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

The system must provide a report showing the number of items edited. This report is needed for staff to monitor item maintenance activity through item reporting. The result must present an aggregate count of edited items rather than a list of individual items. The source also identifies this report type as not available in a reference report inventory, so its availability is a stated reporting limitation to address.

> - Items Edited Count (`early_draft_srs_galecia.txt`)
> - Items Edited Count (not available) (`evergreen_reference_2009.txt`)

### REQ-384 - Provide Email Address Book

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system should provide an address book for email addresses that are regularly used as report recipients. This capability is needed to make report delivery easier when the same addresses are used repeatedly. Report users should be able to use the stored addresses when entering recipients for report delivery and when managing recurring reports. The address book applies to email addresses used for reports and does not replace the ability to enter addresses directly.

> have an address book of regularly used addresses (`early_draft_srs_galecia.txt`)

### REQ-385 - Provide Executive Georgia Annual Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide predefined executive reports containing basic statistics required by the Georgia Annual Report and Application for State Aid. These reports are needed for library boards and other external consumers. The reports should include activity statistics that can be cross-tabulated by terminal, branch, library system, hour, patron age range, patron type, and patron location.

> These should include basic statistics like those required by the Georgia Annual Report and Application for State Aid. (`early_draft_srs_galecia.txt`)

### REQ-386 - Provide Fines And Payments Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide financial reports covering fines and payments. These reports are needed because financial reports are among the report types used from the current Evergreen system, with 34% selecting them in the survey. Staff need financial reporting that includes both stated financial areas. The requirement does not specify additional financial categories, calculations, or reporting frequency.

> - Financial reports (fines, payments): 34% (`survey_results_2009.txt`)

### REQ-387 - Provide Item Use Totals And Ranges

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide total use counts for items and use counts divided by configurable usage date ranges. The date-range breakdown must support periods such as a fiscal-year period or a monthly period. This reporting capability is needed by staff who need to examine overall item use as well as usage within selected reporting periods.

> Ability to have a total use count on items as well as a use count broken down by usage date range such as an FY use count or monthly use count (`early_draft_srs_galecia.txt`)

### REQ-388 - Provide Last Circulation Date

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide the last circulation date as a separate reportable field. Staff need this field to identify and report when an item was most recently circulated, independently of the last edit date. The system must not require staff to infer the last circulation date from another date or combine it with other circulation information.

> - Ability to indicate last circulation date - not available as separate field (`evergreen_reference_2009.txt`)

### REQ-389 - Provide MARC Data Counts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide circulation counts organized by MARC data. Staff need this report to review circulation activity according to MARC information associated with the circulated items. The report must be available as a distinct circulation report alongside reports organized by Dewey classification, circulation modifier, and shelving location. The source specifically identifies circulation counts by MARC as a required reporting category and notes that circulation counts by MARC fields were not available in the referenced Evergreen report set.

> - Circulation Count by MARC (`early_draft_srs_galecia.txt`)

### REQ-390 - Provide MARC Filtered Circulation Counts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must provide circulation counts grouped or filtered by MARC fields. This report type is needed because circulation count by MARC fields is identified as unavailable. The system must therefore support MARC fields as reporting criteria for organizing or restricting circulation-count results.

> - Circulation Count by MARC fields (not available) (`evergreen_reference_2009.txt`)

### REQ-391 - Provide Period Comparison Columns

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support report results that compare current and prior periods in separate columns. A result may include one column for last month’s circulation, another for the previous month’s circulation, a percentage difference column, a column for the corresponding month from the previous year, and a percentage difference from last month to last year’s month. This capability is needed by report users who require period-to-period and year-over-year comparisons in the report output.

> Ability to determine the output results in a way such that a result could have one column for last month's circs, another for previous month's circ, a percent difference column, previous year's month column, a percent difference from last month to last year's month column (`early_draft_srs_galecia.txt`)

### REQ-392 - Provide Snapshot Bills Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide snapshot bills reports for dates in the past. These reports are needed to determine bill information as it existed at a specified historical date rather than only reflecting current data. The capability must address the identified absence of snapshot bills reporting that goes back in time. Historical reporting support is therefore required for this report type.

> - Snapshot bills report going back in time - does not exist (`evergreen_reference_2009.txt`)

### REQ-393 - Provide Total Circulation Merged

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a total circulation report that includes checkout activity, renewal activity, and non-cataloged circulation. The report must combine these circulation types into a total rather than presenting only checkout counts or only renewal counts. It must also represent the listed total circulation concept of merging cataloged and non-cataloged circulation data.

> - Circulation Count - total circ including checkouts, renewals, and noncats (`early_draft_srs_galecia.txt`)

### REQ-394 - Provide Total Items Aggregate Count

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report showing the number of items. This report is needed for staff to review the overall quantity of items through item reporting. The result must present an aggregate item count rather than a list or a count limited to items added, deleted, edited, or currently checked out. It must remain distinct from the other item reports listed in the source.

> - Items Count (`early_draft_srs_galecia.txt`)

### REQ-395 - Record Transaction Categories

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must record transaction categories including check-ins, check-outs, fines collected, and patron registrations. It must allow staff to query transaction information across all recorded transactions or restrict a query to a selected transaction type. The transaction history must be maintained for a configurable number of days, while monthly and annual aggregate information must be maintained indefinitely.

> Transactions include check-ins, check-outs, fines collected, patron registrations, etc., and can be queried by all transactions or by type of transaction. (`early_draft_srs_galecia.txt`)

### REQ-396 - Report Accrued Charges By Type

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must report fines and charges accrued for selected time periods, including the last twelve months, year to date, and last month. Reports must categorize accrued charges by charge type, including overdue fines, damaged item charges, and lost item charges. Staff need these reports to review financial activity over defined periods and distinguish the types of charges incurred. The reports must include charges attached to patron and item records.

> fines and charges accrued per time period (e.g., last twelve months, YTD, last month) and per type of charge (overdue fines, damaged item charges, lost item charges, etc.) (`early_draft_srs_galecia.txt`)

### REQ-397 - Report Annual Holds Placed Count

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must report the annual number of holds placed. Staff need this holds report to review holds activity for the year. The report must present an annual count rather than the separate reports for unfilled holds, stale holds, or IntraPINES loans. The source lists Annual # of holds placed among the required holds reports.

> - Annual # of holds placed (`early_draft_srs_galecia.txt`)

### REQ-398 - Report Bibliographic Holds Periodically

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must provide periodic reports identifying bibliographic records with holds. This report is needed to identify bibliographic records associated with outstanding holds as part of periodic library reporting. It should be available alongside other periodic reports concerning items, in-transit items, missing items, and patrons with invalid home libraries.

> - Bibliographic records with holds (`early_draft_srs_galecia.txt`)

### REQ-399 - Report Bibliographic Missing MARC Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report identifying bibliographic records that are missing specified MARC fields. Staff need this report to locate records with incomplete or deficient MARC data during bibliographic record reporting. The report should allow the missing fields to be specified so that records can be identified according to the required MARC-field criteria. The source also lists this report type as not available in the reference material, which establishes an availability limitation.

> - Bib Records missing specific MARC fields (`early_draft_srs_galecia.txt`)

### REQ-400 - Report Bibliographic Records Count

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report showing the number of bibliographic records. Staff need this report to determine the count of bibliographic records. The report must present the bibliographic-record count as a bibliographic records report. The source does not state a required breakdown, filtering condition, or limitation for this count.

> - Bib Records Count (`early_draft_srs_galecia.txt`)

### REQ-401 - Report Branch Renewal Percentage

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must report the percentage of check-outs at a particular branch that are renewals. This statistic is required to support analysis and prediction of patron behavior and material use. The report must calculate the renewal proportion for the specified branch’s check-outs so that branch-level renewal patterns can be examined.

> What percent of check-outs at a particular branch are renewals? (`early_draft_srs_galecia.txt`)

### REQ-402 - Report Cataloged In House Use Counts

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report showing counts of cataloged in-house use. Staff need this report to monitor use of cataloged items within the library without circulation. The report must distinguish cataloged in-house use from the separate noncataloged in-house use count by month. The requirement applies to in-house use reporting and does not specify additional filtering, scheduling, or delivery conditions.

> - Cataloged In House Use Count (`early_draft_srs_galecia.txt`)

### REQ-403 - Report Claims Returned Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report of items marked as claims returned. Staff need this items report to identify items whose circulation status has been recorded as claims returned. The report must include items carrying that designation and must distinguish them from other item conditions or statuses. It should be available as a distinct claims returned report within the items reporting functions.

> - Claims returned (`early_draft_srs_galecia.txt`)

### REQ-404 - Report Deleted Last-Copy Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to run reports on items deleted when they were the last copy in the facility. This reporting capability is needed to identify deleted items that no longer had another copy available at the facility. The report facility must support this deletion condition as a selectable reporting subject.

> Ability to run a report on deleted items that were the last copy in the facility (`early_draft_srs_galecia.txt`)

### REQ-405 - Report Detailed Voi ded Transactions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a detailed report of voided transactions. Staff need this report within bills reporting to review transactions that have been voided. The report must present void information in detailed form rather than only providing a general count. The sources do not specify additional filtering, scheduling, delivery, or historical-data conditions for this report.

> - Detailed Voids (`early_draft_srs_galecia.txt`)

### REQ-406 - Report In Transit Items With Holds

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support periodic reports identifying in-transit items with outstanding holds. Staff need this information to locate transferred items that have unresolved hold requirements. The report must specifically combine the conditions of being in transit and having an outstanding hold.

> - In-transit items with outstanding hold (`early_draft_srs_galecia.txt`)

### REQ-407 - Report IntraPINES Loans By Facility

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report of IntraPINES loans covering all facilities and organize the results by facility. Staff need this holds report to review loan activity across the facilities included in the reporting scope. The report must be available as an IntraPINES loan report distinct from reports covering all systems or loans organized by system. The source lists this capability among the required holds reports.

> - IntraPINES Loans for all Facilities (`early_draft_srs_galecia.txt`)
> - IntraPINES Loans by Facility (`early_draft_srs_galecia.txt`)

### REQ-408 - Report IntraPINES Loans By System

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report of IntraPINES loans covering all systems and organize the results by system. Staff need this holds report to review loan activity across the systems included in the reporting scope. The report must be available as an IntraPINES loan report distinct from reports covering all facilities or loans organized by facility. The source lists this capability among the required holds reports.

> - IntraPINES Loans for all Systems (`early_draft_srs_galecia.txt`)
> - IntraPINES Loans by System (`early_draft_srs_galecia.txt`)

### REQ-409 - Report Inventory Weeding Missing Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide item reports supporting inventory, weeding, and missing-item activities. These reports are needed because item reports are a commonly used report type, with 65% selecting them in the survey. Staff need a report that covers each of the stated item-related purposes. The system should not limit item reporting to only one or two of these activities.

> - Item reports (inventory, weeding, missing): 65% (`survey_results_2009.txt`)

### REQ-410 - Report Item Level Holds Periodically

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support periodic reports identifying item-level holds. These reports must distinguish holds placed on individual items from other periodic report categories, such as bibliographic records with holds. Staff need this information to review and manage item-level hold activity.

> - Item-level holds (`early_draft_srs_galecia.txt`)

### REQ-411 - Report Item Renewal Likelihood

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must report how likely a particular item is to be renewed. This measure is required to support understanding and prediction of patron behavior and material use. The renewal-likelihood result must be available for analysis of the specified item and for planning based on patron behavior.

> How likely is a particular book to be renewed? (`early_draft_srs_galecia.txt`)

### REQ-412 - Report Item Return Average

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must report the average time taken for a particular item to be returned. This measure is required as part of patron behavior and material-use analysis, so that the return patterns of items can be understood and used to support prediction. The report must present the return speed as an average for the specified item.

> How quickly is a particular book returned, on average? (`early_draft_srs_galecia.txt`)

### REQ-413 - Report Items By Bibliographic Text

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of items whose bibliographic records contain a specified value or text. Staff need this report to identify items based on content within their bibliographic records. The report must support the listed case of finding items with a specified value or text in the bibliographic record. The requirement does not state any additional restriction on the value, text, or report scope.

> - List of items with XXX in bib record (`early_draft_srs_galecia.txt`)

### REQ-414 - Report Items In Transit By Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report of items in transit, organized by both the sending library and the destination library. Staff need this report to monitor the movement of items between library locations. The report must identify the destination for items sent in transit and the sending library for items dispatched in transit. Reporting must preserve both organizational views rather than presenting only an undifferentiated list of items.

> - List of Items in Transit by both sending library and destination library (`early_draft_srs_galecia.txt`)
> - Items In Transit to Destination Library (`early_draft_srs_galecia.txt`)

### REQ-415 - Report Last Copy Deleted

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a Last Copy Report identifying the last item owned by a library system that was deleted. Staff need this report to determine when deletion removed the final item held by the library system. The report must apply specifically to deleted items that were the library system’s last owned item, rather than to all deleted items. It should be available as an items report for collection reporting.

> - Last Copy Report (last copy owned by a library system that was deleted) (`early_draft_srs_galecia.txt`)

### REQ-416 - Report Location Counts By Home Library

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide circulation counts by circulation location and break down each result by the patron’s home library. This report is needed to show how circulation activity at each circulation location relates to patrons’ home libraries. Staff need this information for circulation reporting and comparison across locations. The report must retain circulation location and patron home library as the reporting dimensions.

> - Circulation Count by Circ Location broken down by Patron Home Library (`early_draft_srs_galecia.txt`)

### REQ-417 - Report Marked Long Overdue Items

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report listing items marked long overdue by the system. This report is needed when staff must identify items that have received the system’s long-overdue marking. The report must be limited to items with that marking and must distinguish them from items identified only as currently checked out or overdue.

> - Items marked longoverdue by system (`early_draft_srs_galecia.txt`)

### REQ-418 - Report Monthly Noncataloged In House Use

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide monthly counts of non-cataloged in-house use. Staff need this in-house use report to review non-cataloged use by month. The report must count non-cataloged in-house use and must remain distinct from the Cataloged In House Use Count report. The required reporting period is monthly, as specified by the Monthly Non-Cataloged Use requirement.

> - NonCat In House Use Count by Month (`early_draft_srs_galecia.txt`)

### REQ-419 - Report Patron Additions By Month

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report showing patron additions by month. Staff need this report to review when patrons were added and to analyze patron additions across monthly periods. The report belongs to the patron reports and is distinct from the new-patron report based on the previous month and demographic category. The requirement is limited to reporting patron additions by month and does not specify additional demographic or geographic breakdowns.

> - Patron Added Count by Month (`early_draft_srs_galecia.txt`)

### REQ-420 - Report Patron Counts By Profile Group

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report showing counts of patrons grouped by profile group. This report is needed as part of the patron reports for examining the distribution of patrons across profile groups. Staff must be able to use the report when patron counts by profile group are required. The source does not state additional filtering, sorting, timing, or availability conditions for this report.

> - Patron Count by Profile Group (`early_draft_srs_galecia.txt`)

### REQ-421 - Report Patron Counts By Survey Answer

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report showing counts of patrons grouped by survey answer. This report is needed as part of the patron reports for reviewing how many patrons provided each survey answer. Staff must be able to use the report when patron totals organized by survey answer are required. The source does not specify particular survey questions, filtering options, sorting, timing, or other limits for the report.

> - Patron Count by survey answer (`early_draft_srs_galecia.txt`)

### REQ-422 - Report Patrons With Invalid Branches

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support periodic reports identifying patrons whose home libraries are invalid. Staff must be able to use these reports to identify patron records requiring data quality attention. The report must specifically address invalid home library values and must be available as a periodic report.

> - Patrons with invalid home library (`early_draft_srs_galecia.txt`)

### REQ-423 - Report Patrons With Note Wording

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a list of patrons whose notes contain specified wording. This report is needed when staff must identify patron records based on text recorded in patron notes rather than by demographic, location, expiration, or status information. The report must use the specified wording as the basis for selecting patrons and must present the matching patrons in a list.

> - List of Patrons with specific wording in notes (`early_draft_srs_galecia.txt`)

### REQ-424 - Report Previous Month Patron Additions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report showing the number of patrons added during the previous month, organized by demographic category. Staff need this report to identify recent patron additions and compare those additions according to the available demographic categories. The report is distinct from the general patron-added count by month because it is restricted to patrons added during the previous month. The source does not define the specific demographic categories or provide further reporting conditions.

> - New Patron Count (patrons added the previous month by Demographic Category) (`early_draft_srs_galecia.txt`)

### REQ-425 - Report Received Items For Holds

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report of items received to fulfill holds. This report is needed within the holds-reporting area to identify items received in response to holds. It must distinguish received items from other holds-related information, including items sent for holds, unfilled holds, stale holds, and holds purchase alerts. The report concerns fulfillment activity for holds and must list the relevant items.

> - Items Received for Holds (`early_draft_srs_galecia.txt`)

### REQ-426 - Report Records Missing Attached Volumes

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report identifying bibliographic records that have no volumes attached. This report is needed to support bibliographic record reporting alongside overall bibliographic record counts, edited-record counts, and records added by staff by library. Staff need the report to locate records lacking attached volumes. The report is limited to bibliographic records without attached volumes and does not describe item-level conditions.

> - Bib Records with No Volumes attached (`early_draft_srs_galecia.txt`)

### REQ-427 - Report Sent Items For Holds

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report of items sent to fulfill holds. This report is needed within the holds-reporting area to identify items that have been sent in response to holds. It must distinguish sent items from other holds-related information, including items received for holds, unfilled holds, stale holds, and holds purchase alerts. The report concerns fulfillment activity for holds and must list the relevant items.

> - Items Sent for Holds (`early_draft_srs_galecia.txt`)

### REQ-428 - Report Sent Notice Activity

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support reports identifying pre-overdue, overdue, and holds notices that were sent. This capability is needed by staff to review notice activity and use it as reportable information. The notice reports must be available through the reporting system alongside its other report functions. Report results must be suitable for staff use and may be generated in the supported reporting output formats.

> Ability to run reports for pre-overdue, overdue, and holds notices sent (`early_draft_srs_galecia.txt`)

### REQ-429 - Report Total Use Exceeds Threshold

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a report listing items whose total use count exceeds a configurable threshold. Staff must be able to use the report to identify items with total use above the selected threshold. The threshold must be configurable so the report can reflect different high-use reporting requirements.

> - List of Items with a > Total Use Count (`early_draft_srs_galecia.txt`)

### REQ-430 - Report Weeding Below Use Threshold

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must provide a weeding report listing items whose total use count is below a configurable threshold. Staff need this report when reviewing items for weeding based on limited use. The threshold must be configurable, and the report must identify items according to the selected lower total-use limit.

> - List of Items with a < Total Use Count [Weeding Report] (`early_draft_srs_galecia.txt`)

### REQ-431 - Report X Days Not Checked Out

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support periodic reports identifying items that have not been checked out for a specified number of days. Staff must be able to use these reports to review item activity and support collection management. The report criteria must allow the number of days to be specified, as represented by the X-days reporting condition.

> - Items that have not been checked out in X days (`early_draft_srs_galecia.txt`)

### REQ-432 - Restrict Query Tables And Fields

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow administrators to control staff access to the database tables and fields used by the query tool. This control is needed because the query tool supports queries across bibliographic, item, patron, transaction, and financial records. Staff should be able to select query fields, picklist values, regular expressions, and Boolean operators only within the tables and fields to which they have access.

> Administrators should control staff access to tables and fields. (`early_draft_srs_galecia.txt`)

### REQ-433 - Reusable Report Template Creation

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow report users to create reusable report templates through the reports interface. This capability is needed so staff who prepare reports can define a report structure for reuse when the same reporting need occurs again. The requirement covers creating and reusing templates, while the source does not state limits on the number, contents, or permissions associated with those templates.

> Ability to create report templates: 81% (`survey_results_2009.txt`)

### REQ-434 - Reusable Saved Query Storage

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow report users to save queries and reuse them later through the reports interface. This capability is needed when staff need to run the same query again without recreating it each time. The requirement applies to saving and later reuse of queries, while the source does not specify limits on how many queries may be saved, how long they remain available, or who may access them.

> Ability to save and reuse queries: 73% (`survey_results_2009.txt`)

### REQ-435 - Revert Item To Origin

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow staff to revert items to their original location. This capability is needed as an administrative feature when items have been moved to a new location and must be returned to the location from which they originated. The source identifies reverting items to their original location as a requested administrative function, with 18% of respondents indicating this need.

> Revert items to original location: 18% (`survey_results_2009.txt`)

### REQ-436 - Run Canned Reports Historical Periods

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to run canned reports using historical periods defined as yesterday, last week, last month, or last year. This capability is needed when staff want recurring or immediate canned reports based on a specified prior period rather than only current data. Canned reports are generic reports that may be run as soon as possible or recurring. Staff can select canned reports to run at the same time and view them within one document.

> Will have the ability for it to run by yesterday's data, last week's, last month's, or last year's. (`early_draft_srs_galecia.txt`)

### REQ-437 - Run Preset Reports On Demand

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must support running preset reports on demand. These reports must include reports for maintenance and collections development, which use pre-selected criteria and are intended to be set to run when requested. The system should also provide pre-written canned report templates delivered with the product, while allowing canned reports to be run either ASAP or on a recurring basis.

> On Demand Reports would be for pre-selected criteria but for things like maintenance reports or collections development and would be set to run on demand. (`early_draft_srs_galecia.txt`)

### REQ-438 - Run Transaction Reports By Time

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must allow staff to run reports on transactions that occurred at a specified date and time. Transaction reports must also support selection by workstation or by staff member. These criteria are needed to identify transactions associated with a particular time, workstation, or staff member.

> Ability to run a report on transactions that occurred on x date and time on x workstation or by x staff (`early_draft_srs_galecia.txt`)

### REQ-439 - Scheduled Recurring Report Execution

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must allow report users to schedule reports to run repeatedly on a recurring basis. This capability is needed when staff require reports to be produced again according to an ongoing recurrence rather than initiated individually each time. The requirement covers recurring report execution, while the source does not define particular recurrence intervals, scheduling conditions, or limits on the number of scheduled reports.

> Ability to schedule recurring reports: 52% (`survey_results_2009.txt`)

### REQ-440 - Select Multiple Canned Reports

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The reporting system must allow users to select multiple canned reports from a list and run them at the same time. Canned reports are generic, pre-written templates delivered with the product and may be configured to run ASAP or on a recurring basis. The system should support selecting the applicable reporting period, including yesterday’s data, last week’s data, last month’s data, or last year’s data.

> Canned reports can be checked off from a list to run at the same time and will be viewed within one document. (`early_draft_srs_galecia.txt`)

### REQ-441 - Select Regular Expressions From Dropdown

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The query tool must allow staff to select regular expressions from a drop-down menu when designing queries. This capability must be available for queries across bibliographic, item, patron, transaction, and financial records. The interface should provide this selection together with query field selection, picklist values, and Boolean operators to support user-friendly query construction.

> - Select regular expressions from a drop-down menu (`early_draft_srs_galecia.txt`)

### REQ-442 - Separate Checkin And Renewal

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must store checkin date and time separately from renewal timestamps. Staff need to distinguish an item's actual checkin from renewals when creating or reviewing reports. The system must therefore prevent checkin and renewal timestamps from being stored together in a way that prevents separate reporting.

> - Checkin Date/time not including renewals - checkin and renewal timestamps are stored together (`evergreen_reference_2009.txt`)

### REQ-443 - Separate Reporting From Production

**Priority:** Could - Mentioned in 1 document.  
**Type:** constraint  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must separate reporting operations from production operations so that reporting activities do not depend on or interfere with production operations. This separation is needed as part of expanding the reporting system beyond its basic capabilities and addressing identified management-process reporting gaps. Staff need reporting functions that can operate independently of production activities. The system should preserve this separation while supporting other reporting improvements, including report types, permissions, queue visibility, output formats, scheduling, accessibility, and development or training environments with migration capability.

> Separate reporting from production operations (`evergreen_reference_2009.txt`)

### REQ-444 - Separate Reporting Interfaces By Type

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The system must provide separate reporting interfaces for canned reports, on-demand reports, and open-template reports. These interfaces must support the distinct reporting approaches identified for the reporting system rather than providing only the basic canned interface. The open-template interface is required because it does not currently exist, while the available reporting capability is limited to basic canned reports.

> - Three interfaces (canned, on-demand, open template) - only basic canned exists (`evergreen_reference_2009.txt`)

### REQ-445 - Show Report Queue Position For Staff

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must enable staff to view the position of their report in the queue of reports waiting to run. This capability is needed when a report has not yet run and staff need to know where it stands among waiting reports. The system must show the report’s place in that queue.

> Staff should be able to see where their report is in the queue of reports waiting to run. (`early_draft_srs_galecia.txt`)

### REQ-446 - Show Report Title Hover Tooltips

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting interface must provide hover tooltips for report titles. Staff must be able to obtain tooltip information by hovering over a report title while using the reporting interface. This capability is needed because hover tooltips for report titles are identified as a missing reporting-interface feature, and the requirement is limited to report titles rather than other interface elements.

> - No hover tooltips for report titles (`evergreen_reference_2009.txt`)

### REQ-447 - Subtotal Holds By Hold Type

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must subtotal holds by hold type in transaction reports. At minimum, the subtotals must include active holds, frozen holds, and frozen-until holds. This allows staff to distinguish the categories of holds while reviewing reports of holds placed and holds filled. Hold counts must include requests placed at a staff desk, at a public computer inside the library, and remotely.

> Holds are subtotaled by type, e.g., active, frozen, and frozen-until holds. (`early_draft_srs_galecia.txt`)

### REQ-448 - Support Diverse Report Data Sources

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must support reports based on bibliographic records, items, patrons, circulation actions, hold actions, monetary records, and actors. These reportable structures must provide information such as bibliographic metadata, item details, patron information, circulation and hold activity, fines and payments, and staff accounts and permissions. The supported report types must therefore cover the listed record categories and their associated reporting data.

> The following record types are available for reporting: - bibliographic_record: Title, author, ISBN, publication info, subjects, etc. - item: Call number, barcode, location (copy location), status, etc. - patron: Name, address, library, patron type, etc. - action_circulation: Checkout, checkout, ren... (`evergreen_reference_2009.txt`)

### REQ-449 - Total Transactions By Patron And Branch

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The system must provide a total transaction report with counts per patron, per library, and per system. This report is needed to show overall transaction volume at each requested level for reporting and analysis. Transaction reporting may also group transactions by hour, terminal, branch, and system, supporting the broader transaction views in which these totals are needed.

> Need total transactions report - per patron, per library, per system (`survey_results_2009.txt`)

### REQ-450 - Track And Verify Financial Transactions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must support tracking and verification of financial transactions. This capability is needed as part of the management processes for library services, programs, and policies. Managers, administrators, and staff need the information to monitor and verify financial activity. The requirement addresses financial transaction tracking and verification as a management activity.

> Tracking and verifying financial transactions. (`early_draft_srs_galecia.txt`)

### REQ-451 - Transaction Reports Grouping By Dimensions

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `survey_results_2009.txt`

The reporting system must support transaction reports for check-ins, check-outs, fines collected, patron registrations, and other transaction types. Reports should allow transactions to be grouped by hour, terminal, branch, and system. This support is needed for transaction reporting that includes method-specific check-in and checkout details, hold-placement methods, and total transactions per patron, library, or system for analysis.

> Transactions include check-ins, check-outs, fines collected, patron registrations, etc. (`survey_results_2009.txt`)

### REQ-452 - Traverse Documented Relationship Joins

**Priority:** Could - Mentioned in 1 document.  
**Type:** functional  
**First mentioned:** unknown  
**Sources:** `evergreen_reference_2009.txt`

The reporting system must allow reports to traverse documented relationships among bibliographic records, items, circulation transactions, patrons, monetary records, and actors. It must support the relationship from bibliographic records to items through asset.copy, items to circulation actions through circulation transactions, and patrons to circulation actions through patron_id. It must also support patron-to-money relationships through debt records and actor-to-circulation relationships through the librarian link.

> 3.2 KEY RELATIONSHIPS - bibliographic_record -> item (through asset.copy) - item -> action.circulation (through circulation transactions) - patron -> action.circulation (through patron_id) - patron -> money (through debt records) - actor -> action.circulation (through librarian link) (`evergreen_reference_2009.txt`)

### REQ-453 - Validate Report Output Reliability

**Priority:** Could - Mentioned in 1 document.  
**Type:** non-functional  
**First mentioned:** unknown  
**Sources:** `early_draft_srs_galecia.txt`

The system must test report output and establish that it is reliable before providing the output to staff. This requirement is needed to ensure that staff receive report results they can use with confidence. Reliability applies to reports generated by the reporting system, including reports with filtering or displayed fields. The results must also include null and blank fields regardless of what is being filtered or displayed.

> Tested and proven output (`early_draft_srs_galecia.txt`)

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

