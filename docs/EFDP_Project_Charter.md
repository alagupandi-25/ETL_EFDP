# Project Charter

## Enterprise Financial Data Platform (EFDP)

**Project Code:** UC20  
**Project Methodology:** Agile Scrum  
**Project Type:** Enterprise Data Engineering / Financial Analytics Platform

---

## 1. Project Purpose

The Enterprise Financial Data Platform (EFDP) is an end-to-end data engineering project designed to consolidate SAP-derived financial and enterprise master data into a structured, governed, and analytics-ready platform.

The project addresses the challenge of working with financial data distributed across heterogeneous source formats and structures. It establishes a repeatable pipeline for ingestion, staging, profiling, data quality assessment, cleansing, standardization, integration, dimensional modeling, and reporting.

The current implementation is based on 10 SAP-derived source tables and the actual transformations and analytics supported by those datasets.

---

## 2. Problem Statement

Financial transactions and supporting master data must be connected before they can be effectively used for reporting and analysis. Differences in source formats, data structures, identifiers, and data quality can increase the effort required to create reliable analytical datasets.

The EFDP addresses this by implementing a layered data platform that:

- Ingests source data using Pentaho.
- Stores raw data in PostgreSQL staging.
- Profiles and assesses data quality using Python/Pandas.
- Cleans and standardizes data.
- Integrates relevant financial and master data.
- Loads curated data into a dimensional warehouse.
- Supports SQL reporting and Power BI visualization.
- Maintains metadata, mappings, and lineage documentation.

---

## 3. Current Implementation Scope

The current project implementation uses the following SAP-derived tables:

| SAP Table | Business Purpose |
|---|---|
| BKPF | Accounting Document Header |
| BSEG | Accounting Document Line Items |
| CSKS | Cost Center Master Data |
| CSKT | Cost Center Texts |
| KNA1 | Customer Master General Data |
| LFA1 | Vendor Master General Data |
| SKA1 | G/L Account Master |
| SKAT | G/L Account Texts |
| T001 | Company Code Master |
| T002 | SAP System Languages |

The implementation focuses on the relationships and analytics supported by these datasets.

---

## 4. Project Objectives

The project objectives are to:

1. Build an end-to-end pipeline for SAP-derived financial and master data.
2. Demonstrate ingestion of the heterogeneous file formats used in the project.
3. Create PostgreSQL staging tables for raw source-derived data.
4. Perform data profiling and quality assessment.
5. Apply documented cleansing and standardization rules.
6. Integrate accounting transactions with available master and organizational data.
7. Design and implement an analytical warehouse using dimensional modeling.
8. Develop Fact and Dimension tables supported by the available data.
9. Produce SQL-based reports and analytical queries.
10. Provide curated data for Power BI dashboards.
11. Document the complete data lifecycle through project governance artifacts.
12. Maintain project artifacts using Git and GitHub.

---

## 5. Project Deliverables

### Data Discovery and Governance

- Project Charter
- Source Inventory
- Data Dictionary
- Data Profiling Report
- Data Quality Report
- Finance Business Glossary
- Source-to-Target Mapping
- Data Lineage Documentation

### Data Engineering

- Pentaho ingestion transformations
- PostgreSQL staging tables
- Cleansing and standardization transformations
- Integration transformations
- Warehouse loading transformations
- Pentaho Jobs where implemented

### Data Platform

- Bronze/Staging layer
- Silver/Cleansed and Integrated layer
- Gold/Analytical Warehouse layer
- Fact and Dimension tables

### Analytics

- SQL reporting queries
- Power BI datasets
- Power BI reports and dashboards supported by the implemented model

### Project Management

- Sprint Backlog
- Sprint deliverables
- Git/GitHub repository and version control

---

## 6. Project Scope

### In Scope

- The 10 SAP-derived source tables listed in Section 3.
- Heterogeneous file-format ingestion as implemented.
- PostgreSQL-based data storage.
- Pentaho ETL processing.
- Python/Pandas profiling.
- Data quality assessment.
- Cleansing and standardization.
- Integration of supported source entities.
- Dimensional warehouse design.
- SQL reporting.
- Power BI visualization.
- Data governance documentation.
- Agile sprint execution.

### Future Extensibility

The architecture may later incorporate additional enterprise financial domains when source data is available, such as:

- Fixed Assets
- Budgeting and Forecasting
- Treasury
- Payroll
- Tax
- Expense Management
- Additional SAP/ERP modules

These are not part of the current source-data implementation unless corresponding datasets and transformations are added.

### Out of Scope

- Replacing SAP.
- Modifying operational SAP systems.
- Building a complete ERP.
- Real-time enterprise transaction processing.
- Production deployment at full enterprise scale.
- Analytical claims unsupported by the current data.

---

## 7. High-Level Architecture

```text
SAP-Derived Source Files
        |
        v
Pentaho Data Integration
        |
        v
PostgreSQL Bronze / Staging
        |
        v
Profiling and Data Quality Analysis
        |
        v
Cleansing / Standardization / Integration
        |
        v
PostgreSQL Silver Layer
        |
        v
PostgreSQL Gold Data Warehouse
        |
        v
SQL Reporting + Power BI
```

Governance documentation and Git/GitHub support the complete lifecycle.

---

## 8. Technology Stack

| Component | Technology |
|---|---|
| Data Integration / ETL | Pentaho Data Integration (Spoon) |
| Database | PostgreSQL |
| Data Profiling | Python / Pandas |
| Data Warehouse | PostgreSQL |
| Querying | SQL |
| Visualization | Power BI |
| Version Control | Git / GitHub |
| Methodology | Agile Scrum |

---

## 9. Stakeholders

| Stakeholder | Role / Interest |
|---|---|
| Project Team | Designs and implements the platform |
| Finance / Business Users | Require reliable financial information |
| Financial Analysts | Analyze curated transaction and master data |
| Controlling Users | Analyze cost-center-related information |
| BI Users | Develop reports and dashboards |
| Data Engineering Functions | Maintain ingestion, transformation, and warehouse processes |
| Academic Evaluators | Assess project implementation and documentation |

---

## 10. Success Criteria

The project will be successful when:

1. All selected source datasets are documented.
2. The 10 SAP-derived tables are successfully staged.
3. Data profiling and quality findings are documented.
4. Cleansing and standardization rules are implemented.
5. Relevant source relationships are integrated.
6. The approved warehouse design is implemented.
7. Curated Fact and Dimension tables are loaded.
8. SQL reporting queries execute successfully.
9. Governance documentation is complete.
10. Data lineage and source-to-target mappings are maintained.
11. Curated data is used in Power BI reporting.
12. Sprint deliverables are tracked and completed.

---

## 11. Risks and Constraints

### Risks

- Source data may contain quality or consistency issues.
- Some desired business metrics may not be derivable from the supplied tables.
- Incorrect joins can duplicate or distort financial records.
- Identifier formatting must be preserved where required.
- Changes to source structures may require ETL updates.

### Constraints

- The project is developed within the academic timeline and sprint structure.
- The current implementation is limited to the supplied datasets.
- Available technologies and project environment constrain implementation choices.
- The project does not use live production SAP systems.

---

## 12. Project Principles

The EFDP will follow these principles:

- Build from the actual available source data.
- Preserve source meaning and identifier semantics.
- Profile before applying cleansing rules.
- Document transformations and assumptions.
- Separate raw, cleansed, and curated layers.
- Avoid claiming functionality that has not been implemented.
- Keep the architecture extensible for future sources.
- Maintain reproducibility through version control.

---

## 13. Approval and Review

The Project Charter should be reviewed when:

- Project scope changes.
- New source datasets are introduced.
- Major architecture changes are made.
- Sprint deliverables are re-planned.

---

## 14. Conclusion

The EFDP project provides a structured approach for converting SAP-derived financial and enterprise master data into curated analytical information. Its current implementation is grounded in the 10 available source tables while its architecture remains extensible for additional enterprise financial domains in the future.
