# Business Requirements Document (BRD)

## Enterprise Financial Data Platform (EFDP)

**Project Name:** Enterprise Financial Data Platform (EFDP)  
**Project Code:** UC20  
**Project Methodology:** Agile Scrum  
**Core Technologies:** Pentaho Data Integration (Spoon), PostgreSQL, Python/Pandas, Power BI, Git/GitHub

---

## 1. Project Title

**Enterprise Financial Data Platform (EFDP)**

---

## 2. Business Problem

Organizations generate financial and enterprise master data across multiple systems and data structures. These datasets may differ in format, structure, naming conventions, and quality, making it difficult to consolidate information for reporting and analysis.

The Enterprise Financial Data Platform (EFDP) addresses this problem by providing an end-to-end data engineering pipeline for ingesting, profiling, cleansing, standardizing, integrating, and analyzing financial data.

The current project implementation is based on SAP-derived financial and master datasets. The implemented source tables are:

- `BKPF` – Accounting Document Header
- `BSEG` – Accounting Document Line Items
- `CSKS` – Cost Center Master Data
- `CSKT` – Cost Center Texts
- `KNA1` – Customer Master General Data
- `LFA1` – Vendor Master General Data
- `SKA1` – G/L Account Master
- `SKAT` – G/L Account Texts
- `T001` – Company Code Master
- `T002` – SAP System Languages

These datasets provide the basis for integrating financial transactions with relevant organizational and master data.

---

## 3. Business Objectives

The EFDP shall:

1. Ingest SAP-derived financial and master data from heterogeneous source formats.
2. Preserve raw source data in a PostgreSQL staging layer.
3. Profile datasets to identify missing values, duplicates, data-type issues, and other applicable quality issues.
4. Clean, validate, and standardize data before analytical use.
5. Integrate financial transaction data with relevant master and organizational data.
6. Create a PostgreSQL-based analytical data warehouse using dimensional modeling.
7. Populate appropriate Fact and Dimension tables based on the available source data.
8. Support SQL-based financial reporting and analysis.
9. Maintain documentation for data sources, field definitions, transformations, source-to-target mappings, and data lineage.
10. Provide curated data for Power BI reporting and dashboards.
11. Maintain project artifacts through Git and GitHub.

The broader platform architecture is designed to be extensible to additional financial domains and enterprise sources in the future. However, only capabilities supported by the supplied datasets and actual project implementation are considered implemented.

---

## 4. Current Implementation Scope

### 4.1 In Scope

The current EFDP implementation includes:

- SAP-derived financial and enterprise master data.
- Data ingestion using Pentaho Data Integration.
- Demonstration of heterogeneous source formats, including formats such as CSV, Excel, JSON, and XML where used in the project.
- PostgreSQL staging tables.
- Data profiling using Python and Pandas.
- Data quality assessment.
- Data cleansing and standardization.
- Integration of accounting transactions with available master data.
- Dimensional warehouse design.
- Fact and Dimension table creation based on the implemented model.
- SQL-based reporting queries.
- Source-to-Target mapping.
- Data lineage documentation.
- Finance business glossary and metadata documentation.
- ETL orchestration using Pentaho Jobs where implemented.
- Data validation and reconciliation checks supported by the available data.
- Power BI reporting using curated warehouse data.
- Version control using Git and GitHub.

### 4.2 Future / Extensible Scope

The architecture may be extended to additional enterprise domains, such as:

- Accounts Payable
- Accounts Receivable
- Fixed Assets
- Budgeting and Forecasting
- Treasury
- Payroll
- Tax
- Expense Management
- Additional ERP and SAP modules

These domains are architectural extensions unless corresponding source data and transformations are implemented.

### 4.3 Out of Scope

The project does not include:

- Replacing SAP or any operational enterprise system.
- Developing a new ERP system.
- Modifying live source-system transactions.
- Real-time transaction processing.
- A production deployment of a full enterprise financial platform.
- Claims of analytical capabilities that cannot be supported by the available source data.

---

## 5. Business Requirements

### BR-01: Multi-Source Data Integration

The platform shall ingest and integrate the SAP-derived datasets selected for the project.

### BR-02: Multi-Format Data Ingestion

The platform shall demonstrate ingestion of the heterogeneous file formats used in the project through Pentaho Data Integration.

### BR-03: Raw Data Preservation

The platform shall load source data into PostgreSQL staging tables before downstream transformation.

### BR-04: Data Profiling

The platform shall use Python and Pandas to profile available datasets and identify applicable data quality issues.

### BR-05: Data Quality and Standardization

The platform shall apply appropriate cleansing, validation, and standardization rules based on profiling results and source characteristics.

### BR-06: Financial Data Integration

The platform shall integrate accounting document data with available G/L account, customer, vendor, cost center, company, and language/reference data where applicable.

### BR-07: Analytical Data Warehouse

The platform shall implement a PostgreSQL analytical warehouse using dimensional modeling.

### BR-08: Fact and Dimension Modeling

The platform shall create Fact and Dimension tables supported by the available source data and approved warehouse design.

### BR-09: Reporting and Analysis

The platform shall support SQL queries and analytical use cases that can be derived from the curated financial data.

### BR-10: Data Governance

The platform shall maintain a Source Inventory, Data Dictionary, Source-to-Target Mapping, Data Lineage documentation, and Finance Business Glossary.

### BR-11: Traceability

The platform shall document the movement of data from source datasets through staging and transformation to curated reporting datasets.

### BR-12: Business Intelligence

The platform shall provide curated data suitable for Power BI reports and dashboards based on the implemented warehouse model.

### BR-13: Version Control and Documentation

Project code, ETL artifacts, SQL scripts, profiling scripts, and technical documentation shall be maintained using Git and GitHub.

---

## 6. Functional Requirements

### 6.1 Data Ingestion

The platform shall:

- Extract data from the actual project source files.
- Support the heterogeneous file formats used in the project.
- Load source records into PostgreSQL staging tables.
- Preserve source-compatible identifiers and relevant source attributes.
- Record and handle ETL errors where implemented.

### 6.2 Data Profiling

The platform shall analyze available datasets for:

- Missing values.
- Duplicate records.
- Data types and format consistency.
- Key-field completeness and uniqueness where applicable.
- Invalid or inconsistent values detectable from the available data.
- Relationships between transaction and master data.

### 6.3 Data Processing

The platform shall:

- Apply cleansing rules derived from profiling results.
- Standardize dates, text, identifiers, and financial fields where required.
- Preserve identifier formatting, including leading zeros where applicable.
- Validate important business and integration keys.
- Transform staged data into structures required by the warehouse model.

### 6.4 Data Warehouse

The warehouse shall:

- Use PostgreSQL.
- Follow the approved dimensional design.
- Contain appropriate Fact and Dimension tables.
- Store curated datasets for analytical queries.
- Support the relationships represented by the available SAP-derived data.

### 6.5 Reporting and Visualization

The platform shall:

- Support SQL-based financial and operational analysis.
- Provide curated warehouse data to Power BI.
- Support dashboards and visualizations based on the metrics that can be calculated from the implemented data model.

---

## 7. Non-Functional Requirements

### 7.1 Data Integrity

Transformations should preserve the integrity and meaning of source records and identifiers.

### 7.2 Data Quality

Curated data should be validated against the defined quality and transformation rules.

### 7.3 Traceability

Important transformations should be traceable through documentation and source-to-target mappings.

### 7.4 Maintainability

Pentaho transformations, Jobs, SQL scripts, Python scripts, and documentation should be organized for maintenance and reuse.

### 7.5 Scalability

The architecture should allow additional SAP tables and financial data domains to be incorporated in the future.

### 7.6 Documentation

The project shall maintain documentation describing data sources, table structures, transformations, warehouse design, lineage, and business terminology.

### 7.7 Security and Data Handling

Project data and artifacts should be handled with controlled access appropriate to the academic project environment.

---

## 8. Stakeholders

| Stakeholder | Interest |
|---|---|
| Finance Department | Accurate and integrated financial information |
| Financial Analysts | Curated data for analysis and reporting |
| General Ledger Team | Accounting document and G/L analysis |
| Accounts Receivable Functions | Customer-related financial analysis where supported |
| Accounts Payable Functions | Vendor-related financial analysis where supported |
| Controlling Functions | Cost center analysis where supported |
| Executive Management | Consolidated insights and dashboards |
| Compliance / Audit Functions | Data traceability and validation evidence |
| Data Engineering Team | ETL, data integration, and warehouse implementation |
| BI / Reporting Users | SQL reports and Power BI dashboards |
| Project Team | End-to-end implementation and documentation |

---

## 9. Data Requirements

The current implementation uses the following SAP-derived entities:

| Source Table | Business Purpose |
|---|---|
| BKPF | Accounting document header information |
| BSEG | Accounting document line-item information |
| CSKS | Cost center master data |
| CSKT | Language-dependent cost center texts |
| KNA1 | Customer master general data |
| LFA1 | Vendor master general data |
| SKA1 | G/L account master data |
| SKAT | G/L account texts |
| T001 | Company code master data |
| T002 | SAP language reference data |

The data warehouse and reporting model shall be designed around relationships that are actually supported by these datasets.

---

## 10. Technology Requirements

| Component | Technology |
|---|---|
| ETL / Ingestion | Pentaho Data Integration (Spoon) |
| Database / Staging | PostgreSQL |
| Data Profiling | Python / Pandas |
| Data Warehouse | PostgreSQL |
| Reporting Queries | SQL |
| Visualization | Power BI |
| Version Control | Git / GitHub |
| Documentation | Markdown and other required project formats |
| Project Methodology | Agile Scrum |

---

## 11. Success Criteria

The project will be considered successful when:

1. The selected SAP-derived datasets are successfully ingested.
2. Source data is loaded into PostgreSQL staging tables.
3. Data profiling identifies and documents applicable quality findings.
4. Defined cleansing and standardization rules are implemented.
5. Relevant transaction and master data relationships are integrated.
6. The approved dimensional warehouse model is implemented.
7. Fact and Dimension tables are populated from supported source data.
8. SQL reporting queries run successfully on curated data.
9. Source-to-Target mappings and data lineage are documented.
10. Data validation or reconciliation checks appropriate to the available data are performed.
11. Curated data is available for Power BI reporting.
12. Project artifacts and documentation are maintained under version control.
13. Required sprint deliverables are completed.

---

## 12. Assumptions

- The supplied SAP-derived datasets are the basis for the current implementation.
- PostgreSQL is available for staging and warehouse storage.
- Pentaho Data Integration is available for ETL development.
- Python and Pandas are available for profiling and data quality analysis.
- Power BI is available for visualization.
- Git and GitHub are available for version control and collaboration.
- The project follows the required Agile sprint structure.

---

## 13. Conclusion

The Enterprise Financial Data Platform provides an end-to-end approach for transforming SAP-derived financial and enterprise master data into curated analytical datasets. The current implementation focuses on the actual supplied tables and the transformations, quality processes, warehouse structures, and reports supported by them.

The architecture remains extensible to additional enterprise financial domains, but future capabilities are clearly distinguished from the functionality implemented in the current project.
