# Solution Architecture

## Enterprise Financial Data Platform (EFDP)

**Project Code:** UC20  
**Architecture Style:** Layered Data Engineering Architecture  
**Core Technologies:** Pentaho Data Integration, PostgreSQL, Python/Pandas, SQL, Power BI, Git/GitHub

---

## 1. Architecture Overview

The Enterprise Financial Data Platform (EFDP) uses a layered data architecture to move SAP-derived financial and enterprise master data from source files to curated analytical datasets.

The current implementation is based on 10 SAP-derived datasets:

- BKPF – Accounting Document Header
- BSEG – Accounting Document Line Items
- CSKS – Cost Center Master Data
- CSKT – Cost Center Texts
- KNA1 – Customer Master General Data
- LFA1 – Vendor Master General Data
- SKA1 – G/L Account Master
- SKAT – G/L Account Texts
- T001 – Company Code Master
- T002 – SAP System Languages

Pentaho Data Integration is used for ingestion and ETL processing. PostgreSQL stores the project's Bronze/Staging, Silver/Integrated, and Gold/Warehouse layers. Python/Pandas supports profiling and data-quality analysis, while Power BI consumes curated data for reporting.

The architecture is extensible to additional financial domains, but only the datasets and capabilities supported by the current implementation are treated as implemented.

---

## 2. High-Level Architecture

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SOURCE DATA LAYER                                   │
│                                                                             │
│   SAP-Derived Financial & Master Data                                       │
│   BKPF • BSEG • SKA1 • SKAT • KNA1 • LFA1 • CSKS • CSKT • T001 • T002       │
│   CSV / Excel / JSON / XML                                                  │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       DATA INGESTION & ETL                                  │
│                                                                             │
│                  Pentaho Data Integration (Spoon)                           │
│        Extract • Format Handling • Validation • Load • Error Logging        │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    POSTGRESQL DATA PLATFORM                                 │
│                                                                             │
│  ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────────┐   │
│  │ BRONZE / STAGING │ →  │ SILVER / CLEANSED│ →  │ GOLD / DATA WAREHOUSE│   │
│  │                  │    │ & INTEGRATED     │    │                      │   │
│  │ Raw SAP Data     │    │ Standardized     │    │ Fact Tables          │   │
│  │ stg_* Tables     │    │ Validated        │    │ Dimension Tables     │   │
│  └──────────────────┘    └──────────────────┘    └──────────────────────┘   │
└───────────────────────────────────────────────────────────┬─────────────────┘
                                                            │
                                                            ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ANALYTICS & REPORTING                                 │
│                                                                             │
│                  SQL Queries  ──────────►      Power BI                     │
│                                      Financial Reports & Dashboards         │
└─────────────────────────────────────────────────────────────────────────────┘


       ┌───────────────────────────────────────────────────────────────┐
       │              CROSS-CUTTING DATA GOVERNANCE                    │
       │                                                               │
       │ Python/Pandas Profiling • Data Quality • Metadata             │
       │ Data Dictionary • Source-to-Target Mapping • Data Lineage     │
       │ Validation & Reconciliation • Git/GitHub                      │
       └───────────────────────────────────────────────────────────────┘
```

Git/GitHub supports version control across ETL transformations, Jobs, SQL, Python scripts, and documentation.

---

## 3. Source Layer

The source layer contains the SAP-derived datasets supplied for the project.

### Financial Transaction Tables

- **BKPF** stores accounting document header information.
- **BSEG** stores individual accounting document line items.

### Master and Reference Tables

- **SKA1** stores G/L account master information.
- **SKAT** stores language-dependent G/L account descriptions.
- **KNA1** stores customer master general information.
- **LFA1** stores vendor master general information.
- **CSKS** stores cost center master information.
- **CSKT** stores language-dependent cost center descriptions.
- **T001** stores company code organizational information.
- **T002** stores SAP language reference information.

The project also demonstrates heterogeneous data ingestion using the file formats actually used in the implementation.

---

## 4. Bronze Layer – PostgreSQL Staging

The Bronze layer is implemented within PostgreSQL as the staging layer.

Its purpose is to retain source-derived data before major analytical transformation.

The implemented staging tables are:

| Staging Table | Source |
|---|---|
| `stg_bkpf` | BKPF |
| `stg_bseg` | BSEG |
| `stg_csks` | CSKS |
| `stg_cskt` | CSKT |
| `stg_kna1` | KNA1 |
| `stg_lfa1` | LFA1 |
| `stg_ska1` | SKA1 |
| `stg_skat` | SKAT |
| `stg_t001` | T001 |
| `stg_t002` | T002 |

The Bronze/Staging layer preserves source-compatible fields and provides a controlled location for downstream profiling and transformation.

---

## 5. Data Profiling and Data Quality Analysis

Python and Pandas are used to analyze staged data and identify quality characteristics relevant to the supplied datasets.

Analysis may include:

- Missing-value analysis.
- Duplicate detection.
- Data-type and format checks.
- Key completeness and uniqueness checks.
- Invalid-value or consistency checks supported by the data.
- Distribution and descriptive analysis.
- Relationship checks between transaction and master data.

Profiling findings are used to define and justify cleansing and standardization rules.

---

## 6. Silver Layer – Cleansed and Integrated Data

The Silver layer is implemented in PostgreSQL as the cleansed, standardized, and integrated layer.

Pentaho transformations perform processing such as:

1. Reading staged source data.
2. Applying profiling-driven cleansing rules.
3. Standardizing data types and formats.
4. Standardizing dates and text fields where required.
5. Preserving identifier semantics and formatting.
6. Validating important integration keys.
7. Integrating accounting transactions with relevant master data.
8. Producing cleansed datasets for warehouse loading.

### Identifier Handling

Business identifiers such as G/L account numbers should be handled as identifiers rather than ordinary numeric measures. Character/string storage is used where necessary to preserve source formatting, including leading zeros.

---

## 7. Core Data Integration Relationships

The main integration relationships are based on the available SAP-derived data.

### Accounting Documents

`BKPF` provides accounting document header information.

`BSEG` provides the corresponding line items and is associated with document-level information using the relevant accounting document identifiers.

### G/L Accounts

Accounting line items can be associated with:

- `SKA1` for G/L account master attributes.
- `SKAT` for G/L account descriptions.

### Customers and Vendors

Where populated in the transaction data:

- Customer identifiers connect to `KNA1`.
- Vendor identifiers connect to `LFA1`.

### Cost Centers

Where populated:

- Cost center identifiers connect to `CSKS`.
- Language-dependent cost center descriptions are obtained from `CSKT`.

### Company and Language Reference Data

- Company-related information is enriched using `T001`.
- Language-dependent text can be interpreted using `T002` where applicable.

The exact join conditions and transformation rules are documented separately in the Source-to-Target Mapping and Data Lineage documents.

---

## 8. Gold Layer – Financial Data Warehouse

The Gold layer is implemented in PostgreSQL as the curated analytical warehouse.

It contains the approved Fact and Dimension structures derived from the available source data.

Typical warehouse components may include dimensions for:

- Date
- Company
- G/L Account
- Customer
- Vendor
- Cost Center
- Other supported reference entities

The central fact structure is based on the accounting transaction grain supported by the integrated BKPF/BSEG data and the approved dimensional model.

Only warehouse tables and metrics supported by the actual project design and source data should be populated.

---

## 9. ETL and Orchestration Layer

Pentaho Data Integration (Spoon) is used to build ETL transformations.

The processing flow is:

1. Extract source data.
2. Load data into PostgreSQL staging.
3. Profile and assess data quality.
4. Apply cleansing and standardization rules.
5. Integrate relevant transaction and master data.
6. Load Silver-layer datasets.
7. Load warehouse Dimensions.
8. Load Fact tables.
9. Execute validation checks.
10. Make curated data available for reporting.

Pentaho Jobs may orchestrate multiple transformations where implemented.

---

## 10. Data Governance and Metadata

The project supports governance and traceability through:

- Source Inventory.
- Data Dictionary.
- Data Profiling Report.
- Data Quality Report.
- Cleansing and Standardization rules.
- Warehouse design documentation.
- Source-to-Target Mapping.
- Data Lineage.
- Finance Business Glossary.
- Validation and reconciliation documentation.

These artifacts describe how source data is understood, transformed, and delivered to reporting.

---

## 11. Data Lineage

The end-to-end lineage is:

```text
SAP-Derived Source Dataset
        |
        v
Pentaho Ingestion Transformation
        |
        v
PostgreSQL Staging / Bronze
        |
        v
Profiling and Data Quality Analysis
        |
        v
Cleansing / Standardization Transformation
        |
        v
PostgreSQL Silver / Integrated Data
        |
        v
Dimension and Fact Loading
        |
        v
PostgreSQL Gold / Financial Warehouse
        |
        v
SQL Reporting
        |
        v
Power BI
```

Detailed field-level transformations are maintained separately in the Source-to-Target Mapping document.

---

## 12. Reporting and Analytics Layer

Curated Gold-layer data is used for:

- SQL reporting queries.
- Financial transaction analysis.
- G/L account analysis.
- Company-level analysis.
- Customer-related analysis where supported.
- Vendor-related analysis where supported.
- Cost center analysis where supported.
- Power BI dashboards based on the implemented data model.

The project does not claim reporting capabilities for domains whose source data and warehouse structures have not been implemented.

---

## 13. Security and Data Handling

The academic project architecture supports responsible data handling through:

- Controlled access to project databases and files.
- Preservation of source-derived identifiers.
- ETL error logging where implemented.
- Validation before warehouse loading.
- Documentation of transformations.
- Controlled Git/GitHub access to project artifacts.

---

## 14. Version Control

Git and GitHub are used to manage:

- Pentaho transformations.
- Pentaho Jobs.
- SQL scripts.
- Python/Pandas profiling scripts.
- Data Dictionary.
- Source Inventory.
- Solution Architecture.
- Source-to-Target Mapping.
- Data Lineage documentation.
- Finance Business Glossary.
- Other sprint documentation and project artifacts.

---

## 15. Architecture Summary

The final EFDP architecture is:

**SAP-Derived Sources**  
↓  
**Pentaho Data Integration**  
↓  
**PostgreSQL Bronze / Staging**  
↓  
**Python/Pandas Profiling and Data Quality Analysis**  
↓  
**Pentaho Cleansing, Validation, Standardization and Integration**  
↓  
**PostgreSQL Silver Layer**  
↓  
**PostgreSQL Gold Financial Data Warehouse**  
↓  
**Fact and Dimension Tables**  
↓  
**SQL Reporting**  
↓  
**Power BI Dashboards**

This architecture provides a technically consistent separation between raw/staged data, cleansed/integrated data, and curated warehouse data while remaining aligned with the SAP-derived datasets actually implemented in the project.
