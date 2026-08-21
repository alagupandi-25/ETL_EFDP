# Sprint Backlog

## Enterprise Financial Data Platform (EFDP)

**Project Code:** UC20  
**Methodology:** Agile Scrum  
**Current Source Scope:** 10 SAP-derived tables

---

## 1. Current Source Scope

The Sprint Backlog is based on the following confirmed project sources:

`BKPF`, `BSEG`, `CSKS`, `CSKT`, `KNA1`, `LFA1`, `SKA1`, `SKAT`, `T001`, and `T002`.

Future enterprise financial domains may be added later if corresponding source datasets become available.

---

# Sprint 1 – Data Discovery and Ingestion

## Sprint Goal

Establish the source inventory, understand the 10 SAP-derived datasets, document their structures, demonstrate ingestion from the project source formats, and load raw data into PostgreSQL staging.

### Sprint 1 Backlog

| ID | User Story / Task | Priority | Status |
|---|---|---|---|
| S1-01 | Create Project Charter | High | Completed |
| S1-02 | Create Source Inventory for all 10 SAP-derived tables | High | Completed |
| S1-03 | Analyze SAP table purpose and business relationships | High | Completed |
| S1-04 | Create Data Dictionary using actual PostgreSQL staging columns | High | Completed |
| S1-05 | Document heterogeneous source file formats used in the project | High | Completed / verify final repository evidence |
| S1-06 | Configure PostgreSQL connection in Pentaho | High | Completed |
| S1-07 | Create PostgreSQL staging tables | High | Completed |
| S1-08 | Ingest BKPF into PostgreSQL staging | High | Completed / verify |
| S1-09 | Ingest BSEG into PostgreSQL staging | High | Completed / verify |
| S1-10 | Ingest CSKS into PostgreSQL staging | High | Completed / verify |
| S1-11 | Ingest CSKT into PostgreSQL staging | High | Completed / verify |
| S1-12 | Ingest KNA1 into PostgreSQL staging | High | Completed / verify |
| S1-13 | Ingest LFA1 into PostgreSQL staging | High | Completed / verify |
| S1-14 | Ingest SKA1 into PostgreSQL staging | High | Completed / verify |
| S1-15 | Ingest SKAT into PostgreSQL staging | High | Completed / verify |
| S1-16 | Ingest T001 into PostgreSQL staging | High | Completed / verify |
| S1-17 | Ingest T002 into PostgreSQL staging | High | Completed / verify |
| S1-18 | Validate staging row counts and successful loads | High | Pending final validation |
| S1-19 | Commit Sprint 1 artifacts to Git/GitHub | Medium | In Progress |

### Sprint 1 Definition of Done

- All 10 sources are documented.
- Data Dictionary reflects the implemented staging schema.
- Source files can be ingested through the implemented Pentaho transformations.
- PostgreSQL staging contains the required source-derived tables.
- Basic load validation is documented.
- Sprint artifacts are version controlled.

---

# Sprint 2 – Data Profiling and Data Quality

## Sprint Goal

Profile the staged SAP-derived datasets, identify data quality characteristics, and define justified cleansing and validation rules.

### Sprint 2 Backlog

| ID | User Story / Task | Priority | Status |
|---|---|---|---|
| S2-01 | Build Python/Pandas profiling workflow | High | Not Started |
| S2-02 | Profile missing values across all 10 tables | High | Not Started |
| S2-03 | Check duplicate records and key uniqueness where applicable | High | Not Started |
| S2-04 | Validate data types and formats | High | Not Started |
| S2-05 | Analyze key completeness for integration fields | High | Not Started |
| S2-06 | Identify invalid or inconsistent values supported by the data | High | Not Started |
| S2-07 | Produce Data Profiling Report | High | Not Started |
| S2-08 | Define data quality rules from profiling findings | High | Not Started |
| S2-09 | Create Data Quality Report | High | Not Started |
| S2-10 | Define cleansing and standardization rules | High | Not Started |
| S2-11 | Implement cleansing transformations | High | Not Started |
| S2-12 | Document before/after validation results | Medium | Not Started |
| S2-13 | Commit Sprint 2 artifacts to Git/GitHub | Medium | Not Started |

---

# Sprint 3 – Data Integration and Silver Layer

## Sprint Goal

Create cleansed and integrated datasets by connecting accounting transactions with relevant SAP master and organizational data.

### Sprint 3 Backlog

| ID | User Story / Task | Priority | Status |
|---|---|---|---|
| S3-01 | Finalize integration keys and join rules | High | Not Started |
| S3-02 | Integrate BKPF and BSEG at accounting-document level | High | Not Started |
| S3-03 | Integrate G/L account master data | High | Not Started |
| S3-04 | Integrate G/L account text data | Medium | Not Started |
| S3-05 | Integrate customer master data where applicable | Medium | Not Started |
| S3-06 | Integrate vendor master data where applicable | Medium | Not Started |
| S3-07 | Integrate cost center master and text data where applicable | Medium | Not Started |
| S3-08 | Integrate company code data | High | Not Started |
| S3-09 | Apply language/reference logic where applicable | Low | Not Started |
| S3-10 | Create PostgreSQL Silver-layer datasets | High | Not Started |
| S3-11 | Validate joins for duplication and row-count distortion | High | Not Started |
| S3-12 | Create Source-to-Target Mapping | High | Not Started |
| S3-13 | Create Data Lineage documentation | High | Not Started |
| S3-14 | Commit Sprint 3 artifacts to Git/GitHub | Medium | Not Started |

---

# Sprint 4 – Gold Data Warehouse

## Sprint Goal

Implement the approved dimensional model and load curated Fact and Dimension tables from the integrated data.

### Sprint 4 Backlog

| ID | User Story / Task | Priority | Status |
|---|---|---|---|
| S4-01 | Finalize dimensional warehouse design | High | Not Started |
| S4-02 | Define fact grain and business keys | High | Not Started |
| S4-03 | Create Date Dimension | High | Not Started |
| S4-04 | Create Company Dimension | High | Not Started |
| S4-05 | Create G/L Account Dimension | High | Not Started |
| S4-06 | Create Customer Dimension where supported | Medium | Not Started |
| S4-07 | Create Vendor Dimension where supported | Medium | Not Started |
| S4-08 | Create Cost Center Dimension where supported | Medium | Not Started |
| S4-09 | Create central financial transaction Fact table | High | Not Started |
| S4-10 | Build Dimension loading transformations | High | Not Started |
| S4-11 | Build Fact loading transformation | High | Not Started |
| S4-12 | Validate warehouse row counts and referential consistency | High | Not Started |
| S4-13 | Document warehouse schema and loading process | High | Not Started |
| S4-14 | Commit Sprint 4 artifacts to Git/GitHub | Medium | Not Started |

---

# Sprint 5 – Reporting and Business Intelligence

## Sprint Goal

Use curated warehouse data to build SQL reports and Power BI dashboards supported by the implemented model.

### Sprint 5 Backlog

| ID | User Story / Task | Priority | Status |
|---|---|---|---|
| S5-01 | Define reporting questions supported by the data | High | Not Started |
| S5-02 | Develop SQL analytical queries | High | Not Started |
| S5-03 | Validate query results against curated warehouse data | High | Not Started |
| S5-04 | Connect Power BI to the curated data model | High | Not Started |
| S5-05 | Build financial transaction dashboard | High | Not Started |
| S5-06 | Build G/L and company analysis visuals | Medium | Not Started |
| S5-07 | Build customer/vendor analysis where supported | Medium | Not Started |
| S5-08 | Build cost-center analysis where supported | Medium | Not Started |
| S5-09 | Validate dashboard calculations | High | Not Started |
| S5-10 | Document dashboard metrics and filters | Medium | Not Started |
| S5-11 | Commit Sprint 5 artifacts to Git/GitHub | Medium | Not Started |

---

# Sprint 6 – Validation, Documentation, and Finalization

## Sprint Goal

Complete end-to-end validation, reconciliation appropriate to the implemented data model, documentation, and final project packaging.

### Sprint 6 Backlog

| ID | User Story / Task | Priority | Status |
|---|---|---|---|
| S6-01 | Perform end-to-end pipeline validation | High | Not Started |
| S6-02 | Validate source-to-staging completeness | High | Not Started |
| S6-03 | Validate Silver-layer transformations | High | Not Started |
| S6-04 | Validate Gold-layer outputs | High | Not Started |
| S6-05 | Perform reconciliation checks supported by available data | High | Not Started |
| S6-06 | Finalize Source-to-Target Mapping | High | Not Started |
| S6-07 | Finalize Data Lineage | High | Not Started |
| S6-08 | Finalize Finance Business Glossary | High | Not Started |
| S6-09 | Finalize Solution Architecture | High | In Progress |
| S6-10 | Finalize technical documentation | High | Not Started |
| S6-11 | Review repository structure and reproducibility | Medium | Not Started |
| S6-12 | Prepare final demonstration | High | Not Started |
| S6-13 | Final Git/GitHub commit and release | High | Not Started |

---

## Backlog Status Notes

Status values should be updated by the project team as work progresses.

Items marked **Completed / verify** reflect work that appears to have been completed during the current implementation but should be checked against the final transformations, database contents, and repository before formal submission.

Items marked **Pending final validation** require evidence such as successful transformation logs, row counts, or database verification.

---

## Overall Delivery Principle

The backlog is grounded in the actual 10 SAP-derived source tables. Future enterprise domains should only be added as implemented backlog items when corresponding datasets and transformations become available.
