# Source Inventory

## Enterprise Financial Data Platform (EFDP)

**Project Code:** UC20  
**Current Data Domain:** SAP-derived Financial, Controlling, Master, Organizational, and Reference Data  
**Purpose:** Identify and document the datasets currently used as source data in the EFDP implementation.

---

## 1. Purpose

This Source Inventory documents the actual SAP-derived datasets available for the current Enterprise Financial Data Platform (EFDP) implementation.

The inventory distinguishes between:

- **Current implementation sources:** datasets supplied and used in the project.
- **Future extensibility:** additional financial domains that the EFDP architecture may support later but are not currently represented by the supplied source tables.

The current implementation contains 10 SAP-derived source tables.

---

## 2. Source System Overview

| Source System | Source Type | Description |
|---|---|---|
| SAP-derived dataset | Structured enterprise data | Primary source for the current implementation |
| Project source files | CSV / Excel / JSON / XML as implemented | Physical formats used to demonstrate heterogeneous ingestion |

The original business scenario may describe a wider enterprise financial landscape. However, this inventory records only the datasets actually available and implemented in the current project.

---

## 3. Source Table Inventory

| # | SAP Table | Staging Table | Business Area | Business Purpose |
|---:|---|---|---|---|
| 1 | BKPF | `stg_bkpf` | FI – Financial Accounting | Accounting Document Header |
| 2 | BSEG | `stg_bseg` | FI – Financial Accounting | Accounting Document Line Items |
| 3 | CSKS | `stg_csks` | CO – Controlling | Cost Center Master Data |
| 4 | CSKT | `stg_cskt` | CO – Controlling | Cost Center Texts |
| 5 | KNA1 | `stg_kna1` | Customer Master / FI | Customer Master – General Data |
| 6 | LFA1 | `stg_lfa1` | Vendor Master / FI | Vendor Master – General Data |
| 7 | SKA1 | `stg_ska1` | FI – General Ledger | G/L Account Master |
| 8 | SKAT | `stg_skat` | FI – General Ledger | G/L Account Texts |
| 9 | T001 | `stg_t001` | Enterprise Structure / FI | Company Code Master |
| 10 | T002 | `stg_t002` | SAP Basis / Reference Data | SAP System Languages |

---

## 4. Source Table Details

### 4.1 BKPF – Accounting Document Header

**Business Area:** FI – Financial Accounting

**Purpose:** Stores document-level accounting information.

**Business Grain:** One record represents an accounting document header for the relevant company code and fiscal year.

**Primary Integration Role:** Provides document-level attributes used to contextualize accounting line items in BSEG.

**Key Integration Fields:** Company code, accounting document number, fiscal year.

---

### 4.2 BSEG – Accounting Document Line Items

**Business Area:** FI – Financial Accounting

**Purpose:** Stores individual accounting line items belonging to accounting documents.

**Business Grain:** One record represents one accounting line item within an accounting document.

**Primary Integration Role:** Core transaction-level dataset for the current financial model. It can be enriched using document-header, G/L account, customer, vendor, cost center, and company information where corresponding values are available.

**Key Integration Fields:** Company code, accounting document number, fiscal year, line item number.

---

### 4.3 CSKS – Cost Center Master Data

**Business Area:** CO – Controlling

**Purpose:** Stores master attributes for cost centers.

**Business Grain:** One cost center master record for the applicable controlling area and validity period.

**Primary Integration Role:** Enriches transactions associated with cost centers.

---

### 4.4 CSKT – Cost Center Texts

**Business Area:** CO – Controlling

**Purpose:** Stores language-dependent cost center names and descriptions.

**Primary Integration Role:** Provides descriptive text for cost centers represented in CSKS and referenced by transactional data.

---

### 4.5 KNA1 – Customer Master General Data

**Business Area:** Customer Master / Financial Accounting

**Purpose:** Stores general master information for customers.

**Primary Integration Role:** Enriches accounting records associated with customer identifiers.

---

### 4.6 LFA1 – Vendor Master General Data

**Business Area:** Vendor Master / Financial Accounting

**Purpose:** Stores general master information for vendors or suppliers.

**Primary Integration Role:** Enriches accounting records associated with vendor identifiers.

---

### 4.7 SKA1 – G/L Account Master

**Business Area:** FI – General Ledger

**Purpose:** Stores G/L account master information at the chart-of-accounts level.

**Primary Integration Role:** Enriches accounting line items using G/L account attributes.

**Identifier Note:** G/L account numbers are business identifiers and should be handled in a way that preserves their source representation, including leading zeros where applicable.

---

### 4.8 SKAT – G/L Account Texts

**Business Area:** FI – General Ledger

**Purpose:** Stores language-dependent names and descriptions for G/L accounts.

**Primary Integration Role:** Provides readable account descriptions for G/L accounts.

---

### 4.9 T001 – Company Code Master

**Business Area:** Enterprise Structure / FI

**Purpose:** Stores organizational master information for company codes.

**Primary Integration Role:** Provides company-level attributes for financial and related records.

---

### 4.10 T002 – SAP System Languages

**Business Area:** SAP Basis / Reference Data

**Purpose:** Stores SAP language reference information.

**Primary Integration Role:** Supports interpretation of language keys used in language-dependent datasets such as SKAT and CSKT.

---

## 5. Core Source Relationships

The principal conceptual relationships in the current source inventory are:

```text
                    T001
             Company Code Master
                    |
                    v
BKPF ------------------------------+
Accounting Document Header         |
                    |              |
                    | Document     |
                    v              |
BSEG                               |
Accounting Document Line Items     |
   |        |         |       |    |
   v        v         v       v    |
SKA1     KNA1      LFA1     CSKS   |
G/L      Customer   Vendor   Cost   |
Master   Master     Master   Center |
   |                         |     |
   v                         v     |
SKAT                       CSKT    |
G/L Texts                  Texts   |
   |
   +------ Language-dependent text ------> T002
```

Detailed field-level relationships are documented separately in the Data Dictionary and Source-to-Target Mapping.

---

## 6. Data Formats

The EFDP implementation demonstrates ingestion from the heterogeneous file formats actually used in the project. Depending on the source table and implementation, these may include:

- CSV
- Excel
- JSON
- XML

The exact physical file format for each source is documented in the relevant ingestion transformation and project repository.

---

## 7. Future Extensibility

The EFDP architecture can be extended to additional enterprise financial domains when corresponding source datasets are made available, including:

- Fixed Assets
- Budgeting and Forecasting
- Treasury
- Payroll
- Tax
- Expense Management
- Additional Accounts Payable and Accounts Receivable datasets
- Additional SAP or ERP modules

These domains are not listed as current source tables unless their corresponding datasets are actually added to the project.

---

## 8. Data Ownership and Usage

| Data Category | Current Use |
|---|---|
| Financial transaction data | Staging, cleansing, integration, warehouse loading, reporting |
| G/L master data | Transaction enrichment and account analysis |
| Customer master data | Customer-related transaction enrichment |
| Vendor master data | Vendor-related transaction enrichment |
| Cost center data | Controlling-related enrichment and analysis |
| Company code data | Organizational enrichment |
| Language reference data | Interpretation of language-dependent text |

---

## 9. Inventory Maintenance

This Source Inventory shall be updated when:

- A new source dataset is added.
- A source table is removed or replaced.
- A source file format changes.
- New integration relationships are implemented.
- Additional SAP or enterprise modules are incorporated.

---

## 10. Summary

The current EFDP implementation is based on 10 SAP-derived datasets covering accounting documents, accounting line items, G/L accounts, customers, vendors, cost centers, company codes, and language reference data.

The inventory provides the authoritative source list for the current implementation and should be used consistently by the Data Dictionary, Source-to-Target Mapping, Data Lineage, Solution Architecture, Sprint Backlog, and future warehouse documentation.
