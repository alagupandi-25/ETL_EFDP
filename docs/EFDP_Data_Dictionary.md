# EFDP Data Dictionary

## Enterprise Financial Data Platform (EFDP)

**Project Code:** UC20  
**Sprint:** Sprint 1 – Data Discovery & Ingestion  
**Database Layer:** PostgreSQL Staging Database  
**Source Domain:** SAP Financial and Enterprise Master Data

---

## 1. Purpose

This Data Dictionary documents the staging tables and fields used in the Enterprise Financial Data Platform (EFDP). It provides the table purpose, SAP business context, record grain, important identifiers, relationships, and the actual PostgreSQL column definitions implemented in the project staging database.

## 2. Scope

The dictionary covers the following 10 SAP-derived staging tables:

- `stg_bkpf` – Accounting Document Header
- `stg_bseg` – Accounting Document Line Items
- `stg_csks` – Cost Center Master Data
- `stg_cskt` – Cost Center Texts
- `stg_kna1` – Customer Master General Data
- `stg_lfa1` – Vendor Master General Data
- `stg_ska1` – G/L Account Master
- `stg_skat` – G/L Account Texts
- `stg_t001` – Company Code Master
- `stg_t002` – SAP System Languages

## 3. Data Dictionary Conventions

- **Staging table name:** PostgreSQL table created for the project.
- **SAP source table:** Corresponding SAP table represented by the dataset.
- **Data type / maximum length:** Taken from the implemented PostgreSQL staging schema.
- **Business description:** Explains the role of the field in the SAP financial or enterprise-data context.
- **Important identifiers and relationships:** Business-level key and linkage notes for understanding how the tables support integration and later warehouse design.

---

## 4. `stg_bkpf` — Accounting Document Header

**SAP Source Table:** `BKPF`  
**Business Area / Module:** FI – Financial Accounting  
**Purpose:** Stores header-level information for SAP accounting documents. One row represents an accounting document header for a company code and fiscal year.

**Record Grain:** an accounting document header for a company code and fiscal year.

**Important Identifier(s):** Important business key: company_code + accounting_document_no + fiscal_year.  
**Relationships:** Joins to stg_bseg using company_code, accounting_document_no, and fiscal_year.

### Column Definitions

| # | Column Name | PostgreSQL Data Type | Max Length | Business Description |
|---:|---|---|---:|---|
| 1 | `client_id` | character varying | 4 | SAP client/tenant identifier associated with the record. |
| 2 | `company_code` | character varying | 10 | Identifier of the SAP company code to which the record belongs. |
| 3 | `accounting_document_no` | character varying | 20 | Unique accounting document number within the relevant company code and fiscal year. |
| 4 | `fiscal_year` | integer | — | Fiscal year in which the accounting document is recorded. |
| 5 | `document_type` | character varying | 10 | Classification of the accounting document. |
| 6 | `document_date` | date | — | Date shown on the original business document. |
| 7 | `posting_date` | date | — | Date on which the document is posted to financial accounting. |
| 8 | `fiscal_period` | integer | — | Accounting period associated with the posting. |
| 9 | `entry_date` | date | — | Date on which the document or record was entered into the system. |
| 10 | `entry_time` | character varying | 8 | Time at which the document or record was entered into the system. |
| 11 | `created_by_user` | character varying | 50 | User identifier of the person or process that created the record. |
| 12 | `transaction_code` | character varying | 10 | SAP transaction code associated with the creation or processing of the document. |
| 13 | `document_currency` | character varying | 10 | Currency in which the accounting document is recorded. |
| 14 | `reference_transaction_type` | character varying | 10 | Reference transaction or business transaction type associated with the document. |
| 15 | `reference_key` | character varying | 30 | Reference identifier used to link or identify related business information. |

## 5. `stg_bseg` — Accounting Document Line Items

**SAP Source Table:** `BSEG`  
**Business Area / Module:** FI – Financial Accounting  
**Purpose:** Stores line-item-level accounting information belonging to accounting documents. One row represents a line item within an accounting document.

**Record Grain:** a line item within an accounting document.

**Important Identifier(s):** Important business key: company_code + accounting_document_no + fiscal_year + line_item_no. Links to BKPF at document level.  
**Relationships:** Connects accounting line items to stg_bkpf (document header), stg_ska1/stg_skat (G/L account data), stg_kna1 (customer), stg_lfa1 (vendor), and stg_csks/stg_cskt (cost center data), where corresponding values are available.

### Column Definitions

| # | Column Name | PostgreSQL Data Type | Max Length | Business Description |
|---:|---|---|---:|---|
| 1 | `client_id` | character varying | 10 | SAP client/tenant identifier associated with the record. |
| 2 | `company_code` | character varying | 20 | Identifier of the SAP company code to which the record belongs. |
| 3 | `accounting_document_no` | character varying | 30 | Unique accounting document number within the relevant company code and fiscal year. |
| 4 | `fiscal_year` | integer | — | Fiscal year in which the accounting document is recorded. |
| 5 | `line_item_no` | character varying | 20 | Sequential number identifying a line item within an accounting document. |
| 6 | `account_type` | character varying | 20 | Type of account involved in the line item, such as G/L, customer, or vendor. |
| 7 | `debit_credit_indicator` | character varying | 20 | Indicator showing whether the line item is a debit or credit posting. |
| 8 | `amount_local_currency` | numeric | — | Monetary amount of the line item expressed in local/company-code currency. |
| 9 | `amount_document_currency` | numeric | — | Monetary amount of the line item expressed in document currency. |
| 10 | `assignment_no` | character varying | 50 | Assignment or reference number used to group or identify related postings. |
| 11 | `line_item_text` | character varying | 500 | Descriptive text associated with the accounting line item. |
| 12 | `payment_terms` | character varying | 30 | Payment terms applicable to the relevant business transaction. |
| 13 | `cost_center_id` | character varying | 30 | Identifier of the cost center associated with the record. |
| 14 | `gl_account_no` | character varying | 30 | General Ledger account number associated with the accounting line item. |
| 15 | `customer_id` | character varying | 30 | Identifier of the customer associated with the record. |
| 16 | `vendor_id` | character varying | 30 | Identifier of the vendor associated with the record. |
| 17 | `payement_baseline_date` | character varying | 20 | Baseline date used for payment-term calculation. The staging column name is preserved exactly as implemented in the source schema. |
| 18 | `tax_code` | character varying | 30 | Code identifying the tax treatment applicable to the line item. |
| 19 | `clearing_document_number` | character varying | 30 | Accounting document number used to clear the open item. |
| 20 | `clearing_date` | character varying | 20 | Date on which the item was cleared. |
| 21 | `special_gl_indicator` | character varying | 30 | Indicator identifying a special G/L transaction. |

## 6. `stg_csks` — Cost Center Master Data

**SAP Source Table:** `CSKS`  
**Business Area / Module:** CO – Controlling  
**Purpose:** Stores master data and organizational attributes for cost centers, including validity periods and controlling-area information.

**Record Grain:** Defined by the business-level identifiers and validity/language attributes where applicable.

**Important Identifier(s):** Important business identifier: controlling_area + cost_center_id, together with the applicable validity period.  
**Relationships:** Provides cost center master attributes for cost_center_id values used in stg_bseg.

### Column Definitions

| # | Column Name | PostgreSQL Data Type | Max Length | Business Description |
|---:|---|---|---:|---|
| 1 | `client_id` | character varying | 10 | SAP client/tenant identifier associated with the record. |
| 2 | `controlling_area` | character varying | 20 | Identifier of the SAP controlling area. |
| 3 | `cost_center_id` | character varying | 30 | Identifier of the cost center associated with the record. |
| 4 | `valid_to_date` | date | — | End date of the record's validity period. |
| 5 | `valid_from_date` | date | — | Start date of the record's validity period. |
| 6 | `company_code` | character varying | 20 | Identifier of the SAP company code to which the record belongs. |
| 7 | `cost_center_category` | character varying | 30 | Classification or category assigned to the cost center. |
| 8 | `responsible_person` | character varying | 100 | Person responsible for the cost center. |
| 9 | `currency_code` | character varying | 20 | Currency associated with the cost center or record. |

## 7. `stg_cskt` — Cost Center Texts

**SAP Source Table:** `CSKT`  
**Business Area / Module:** CO – Controlling  
**Purpose:** Stores language-dependent names and descriptions for cost centers.

**Record Grain:** Defined by the business-level identifiers and validity/language attributes where applicable.

**Important Identifier(s):** Important business identifier: language_code + controlling_area + cost_center_id + valid_to_date.  
**Relationships:** Provides language-dependent cost center text for cost centers represented in stg_csks and referenced by stg_bseg.

### Column Definitions

| # | Column Name | PostgreSQL Data Type | Max Length | Business Description |
|---:|---|---|---:|---|
| 1 | `client_id` | character varying | 10 | SAP client/tenant identifier associated with the record. |
| 2 | `language_code` | character varying | 20 | Language key associated with language-dependent data. |
| 3 | `controlling_area` | character varying | 20 | Identifier of the SAP controlling area. |
| 4 | `cost_center_id` | character varying | 30 | Identifier of the cost center associated with the record. |
| 5 | `valid_to_date` | date | — | End date of the record's validity period. |
| 6 | `cost_center_name` | character varying | 200 | Short or display name of the cost center. |
| 7 | `cost_center_description` | character varying | 500 | Detailed description of the cost center. |

## 8. `stg_kna1` — Customer Master – General Data

**SAP Source Table:** `KNA1`  
**Business Area / Module:** FI – Accounts Receivable  
**Purpose:** Stores general master information for customers used in business and financial processes.

**Record Grain:** Defined by the business-level identifiers and validity/language attributes where applicable.

**Important Identifier(s):** Important business identifier: customer_id.  
**Relationships:** Provides customer master information for customer_id values used in stg_bseg.

### Column Definitions

| # | Column Name | PostgreSQL Data Type | Max Length | Business Description |
|---:|---|---|---:|---|
| 1 | `client_id` | bigint | — | SAP client/tenant identifier associated with the record. |
| 2 | `customer_id` | character varying | 20 | Identifier of the customer associated with the record. |
| 3 | `country_code` | character varying | 10 | Country identifier associated with the customer, vendor, or company. |
| 4 | `customer_name` | character varying | 100 | Primary name of the customer. |
| 5 | `customer_name_2` | character varying | 100 | Additional or secondary customer name information. |
| 6 | `city` | character varying | 100 | City associated with the address or organizational record. |
| 7 | `postal_code` | character varying | 20 | Postal or ZIP code associated with the address. |
| 8 | `regional_code` | character varying | 20 | Regional code associated with the customer address. |
| 9 | `street_address` | character varying | 150 | Street and address information. |
| 10 | `created_date` | timestamp without time zone | — | Date and time or date on which the master record was created, according to the staging schema. |
| 11 | `customer_account_group` | character varying | 20 | Account group used to classify the customer master record. |
| 12 | `language_code` | character varying | 10 | Language key associated with language-dependent data. |

## 9. `stg_lfa1` — Vendor Master – General Data

**SAP Source Table:** `LFA1`  
**Business Area / Module:** FI – Accounts Payable  
**Purpose:** Stores general master information for vendors or suppliers used in business and financial processes.

**Record Grain:** Defined by the business-level identifiers and validity/language attributes where applicable.

**Important Identifier(s):** Important business identifier: vendor_id.  
**Relationships:** Provides vendor master information for vendor_id values used in stg_bseg.

### Column Definitions

| # | Column Name | PostgreSQL Data Type | Max Length | Business Description |
|---:|---|---|---:|---|
| 1 | `client_id` | bigint | — | SAP client/tenant identifier associated with the record. |
| 2 | `vendor_id` | character varying | 20 | Identifier of the vendor associated with the record. |
| 3 | `country_code` | character varying | 10 | Country identifier associated with the customer, vendor, or company. |
| 4 | `vendor_name` | character varying | 100 | Primary name of the vendor or supplier. |
| 5 | `vendor_name2` | character varying | 100 | Additional or secondary vendor name information. |
| 6 | `city` | character varying | 100 | City associated with the address or organizational record. |
| 7 | `postal_code` | character varying | 20 | Postal or ZIP code associated with the address. |
| 8 | `region_code` | character varying | 20 | Regional code associated with the vendor address. |
| 9 | `street_address` | character varying | 150 | Street and address information. |
| 10 | `created_date` | timestamp without time zone | — | Date and time or date on which the master record was created, according to the staging schema. |
| 11 | `vendor_account_group` | character varying | 20 | Account group used to classify the vendor master record. |
| 12 | `language_code` | character varying | 10 | Language key associated with language-dependent data. |

## 10. `stg_ska1` — G/L Account Master – Chart of Accounts Level

**SAP Source Table:** `SKA1`  
**Business Area / Module:** FI – General Ledger  
**Purpose:** Stores general master data for G/L accounts at the chart-of-accounts level.

**Record Grain:** Defined by the business-level identifiers and validity/language attributes where applicable.

**Important Identifier(s):** Important business identifier: chart_of_accounts + gl_account_no.  
**Relationships:** Provides G/L account master attributes for gl_account_no values used in stg_bseg.

### Column Definitions

| # | Column Name | PostgreSQL Data Type | Max Length | Business Description |
|---:|---|---|---:|---|
| 1 | `client_id` | character varying | 10 | SAP client/tenant identifier associated with the record. |
| 2 | `gl_account_no` | character varying | 30 | General Ledger account number associated with the accounting line item. |
| 3 | `created_by_user` | character varying | 100 | User identifier of the person or process that created the record. |
| 4 | `created_date` | character varying | 20 | Date and time or date on which the master record was created, according to the staging schema. |
| 5 | `record_timestamp` | character varying | 50 | Timestamp or timestamp-like value associated with the staged source record. |
| 6 | `is_deleted` | boolean | — | Flag indicating whether the source record is marked as deleted. |
| 7 | `gl_account_group` | character varying | 50 | Account group used to classify the G/L account. |
| 8 | `operation_flag` | character varying | 20 | Operation or change indicator carried from the source or ingestion process. |
| 9 | `balance_sheet_indicator` | character varying | 20 | Indicator describing whether the G/L account is classified as a balance sheet account. |
| 10 | `chart_of_accounts` | character varying | 30 | Identifier of the chart of accounts to which the G/L account or organizational record belongs. |
| 11 | `financial_statement_type` | character varying | 100 | Financial statement classification associated with the G/L account. |

## 11. `stg_skat` — G/L Account Master Texts

**SAP Source Table:** `SKAT`  
**Business Area / Module:** FI – General Ledger  
**Purpose:** Stores language-dependent names, descriptions, and search terms for G/L accounts.

**Record Grain:** Defined by the business-level identifiers and validity/language attributes where applicable.

**Important Identifier(s):** Important business identifier: language_code + chart_of_accounts + gl_account_number.  
**Relationships:** Provides language-dependent text for G/L accounts represented by chart_of_accounts and gl_account_number.

### Column Definitions

| # | Column Name | PostgreSQL Data Type | Max Length | Business Description |
|---:|---|---|---:|---|
| 1 | `client_id` | character varying | 20 | SAP client/tenant identifier associated with the record. |
| 2 | `language_code` | character varying | 20 | Language key associated with language-dependent data. |
| 3 | `chart_of_accounts` | character varying | 30 | Identifier of the chart of accounts to which the G/L account or organizational record belongs. |
| 4 | `gl_account_number` | character varying | 30 | General Ledger account number used in the account-text record. |
| 5 | `gl_account_short_name` | character varying | 100 | Short name of the G/L account. |
| 6 | `gl_account_description` | character varying | 255 | Long name or description of the G/L account. |
| 7 | `search_term` | character varying | 100 | Search keyword or term associated with the G/L account. |
| 8 | `operation_flag` | character varying | 20 | Operation or change indicator carried from the source or ingestion process. |
| 9 | `is_deleted` | boolean | — | Flag indicating whether the source record is marked as deleted. |
| 10 | `record_timestamp` | character varying | 50 | Timestamp or timestamp-like value associated with the staged source record. |

## 12. `stg_t001` — Company Code Master

**SAP Source Table:** `T001`  
**Business Area / Module:** Enterprise Structure / FI  
**Purpose:** Stores organizational master data for company codes, including company identity, currency, language, chart of accounts, and fiscal-year settings.

**Record Grain:** Defined by the business-level identifiers and validity/language attributes where applicable.

**Important Identifier(s):** Important business identifier: company_code.  
**Relationships:** Provides company-code organizational attributes for company_code values used by financial and controlling records.

### Column Definitions

| # | Column Name | PostgreSQL Data Type | Max Length | Business Description |
|---:|---|---|---:|---|
| 1 | `client_id` | character varying | 10 | SAP client/tenant identifier associated with the record. |
| 2 | `company_code` | character varying | 20 | Identifier of the SAP company code to which the record belongs. |
| 3 | `company_name` | character varying | 500 | Name of the company or company code. |
| 4 | `city` | character varying | 200 | City associated with the address or organizational record. |
| 5 | `country_code` | character varying | 20 | Country identifier associated with the customer, vendor, or company. |
| 6 | `company_currency` | character varying | 20 | Primary currency associated with the company code. |
| 7 | `language_code` | character varying | 20 | Language key associated with language-dependent data. |
| 8 | `chart_of_accounts` | character varying | 30 | Identifier of the chart of accounts to which the G/L account or organizational record belongs. |
| 9 | `fiscal_year_variant` | character varying | 20 | Fiscal year variant used by the company code. |

## 13. `stg_t002` — System Languages

**SAP Source Table:** `T002`  
**Business Area / Module:** SAP Basis / Reference Data  
**Purpose:** Stores SAP language reference information, including SAP language codes, ISO language codes, and language hierarchy attributes.

**Record Grain:** Defined by the business-level identifiers and validity/language attributes where applicable.

**Important Identifier(s):** Important business identifier: sap_language_code.  
**Relationships:** Acts as language reference data for language_code values appearing in language-dependent tables such as stg_skat and stg_cskt.

### Column Definitions

| # | Column Name | PostgreSQL Data Type | Max Length | Business Description |
|---:|---|---|---:|---|
| 1 | `sap_language_code` | character varying | 20 | SAP-specific language key. |
| 2 | `language_specialization` | character varying | 200 | Language specialization or variant information. |
| 3 | `language_hierarchy_level` | integer | — | Hierarchy level associated with the language definition. |
| 4 | `iso_language_code` | character varying | 20 | ISO-standard language code. |
| 5 | `operation_flag` | character varying | 20 | Operation or change indicator carried from the source or ingestion process. |
| 6 | `is_deleted` | character varying | 10 | Flag indicating whether the source record is marked as deleted. |
| 7 | `record_timestamp` | character varying | 50 | Timestamp or timestamp-like value associated with the staged source record. |

---

## 14. Summary of Core Table Relationships

### Financial Transaction Flow

`stg_bkpf` (Accounting Document Header)  
→ joins with `stg_bseg` (Accounting Document Line Items)

### Master Data Enrichment

- `stg_bseg.gl_account_no` → G/L account master data in `stg_ska1` and descriptive text in `stg_skat`.
- `stg_bseg.customer_id` → customer master data in `stg_kna1`.
- `stg_bseg.vendor_id` → vendor master data in `stg_lfa1`.
- `stg_bseg.cost_center_id` → cost center master data in `stg_csks` and descriptive text in `stg_cskt`.
- `company_code` fields → organizational master information in `stg_t001`.
- Language-dependent fields in text/master tables can be interpreted using SAP language reference data in `stg_t002`.

## 15. Notes

1. The field names, data types, maximum lengths, and ordinal positions in this document are based on the project's implemented PostgreSQL staging schema.
2. SAP business purposes are used to explain the role of each SAP-derived table and field.
3. The staging column name `payement_baseline_date` is intentionally preserved exactly as implemented in the project schema.
4. Key and relationship notes are documented as business/integration identifiers; they do not assert that PostgreSQL primary-key or foreign-key constraints have already been physically created.
