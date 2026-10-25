# UC20 — Enterprise Financial Data Platform (EFDP)

**Building a Unified Financial Reporting & Business Intelligence Platform**

## 1. Project Overview

The **Enterprise Financial Data Platform (EFDP)** is an Enterprise Data Engineering capstone project that focuses on integrating, processing, validating, and analyzing financial data from heterogeneous enterprise data sources.

Organizations often maintain financial information across multiple systems and file formats, making it difficult to consolidate transactions, maintain data quality, reconcile financial records, and generate reliable business reports.

This project addresses these challenges by developing an ETL pipeline and a PostgreSQL-based data platform using Pentaho Data Integration, Python, and SQL. The platform is designed to transform raw financial data into structured, consistent, and analytics-ready datasets that support financial reporting and business intelligence.

The project follows an Agile Scrum approach and is organized into four sprints, covering project initiation, data ingestion, data profiling and warehousing, and data governance and analytics.

## 2. Project Objectives

- Integrate financial data from multiple heterogeneous sources and file formats.
- Develop ETL pipelines using Pentaho Data Integration (Spoon).
- Load raw financial records into PostgreSQL staging tables.
- Profile datasets and identify missing values, duplicate records, inconsistencies, and data quality issues using Python and Pandas.
- Clean, standardize, and validate financial data.
- Design a dimensional data warehouse using a star schema with fact and dimension tables.
- Develop SQL queries for financial reporting and analytical use cases.
- Document data dictionaries, source-to-target mappings, metadata, and data lineage.
- Enable business intelligence and financial reporting through Power BI.
- Maintain version control and project documentation using Git and GitHub.

## 3. Technology Stack

| Component | Technology |
|---|---|
| ETL and data integration | Pentaho Data Integration (Spoon) |
| Programming and data profiling | Python, Pandas |
| Database and data warehouse | PostgreSQL |
| Query language | SQL |
| Business intelligence | Microsoft Power BI |
| Version control | Git and GitHub |
| Documentation | Markdown, Microsoft Word |
| Project methodology | Agile Scrum |

## 4. System Architecture

The platform follows a staged data engineering workflow, from source data ingestion to analytics and reporting.

```text
Heterogeneous Financial Data Sources
                  |
                  v
       Data Discovery & Inventory
                  |
                  v
      Pentaho Data Integration
          (ETL Pipelines)
                  |
                  v
       PostgreSQL Staging Layer
                  |
                  v
      Data Profiling & Validation
          (Python / Pandas)
                  |
                  v
        Data Cleaning and
          Standardization
                  |
                  v
      Dimensional Data Warehouse
            (PostgreSQL)
                  |
                  v
       SQL Queries & Analytics
                  |
                  v
          Power BI Reports
       and Financial Dashboards
```

Data governance activities, including metadata management, source-to-target mapping, data lineage, and validation documentation, support traceability and reliability across the pipeline.

*Note: The diagram represents the intended end-to-end platform workflow. Individual components may be at different stages of implementation.*

## 5. Data Sources and Formats

The project uses enterprise financial data, including SAP-related datasets, to simulate the integration challenges encountered in enterprise financial systems.

### Financial data domains

- General Ledger (GL)
- Accounts Payable (AP)
- Accounts Receivable (AR)
- Fixed Assets Management
- Budgeting and Forecasting
- Treasury Management
- Payroll
- Tax Management
- Expense Management
- Enterprise Resource Planning (ERP)

### Supported data formats

The ingestion scope includes:

- CSV — comma-separated tabular data
- Excel — spreadsheet-based data
- JSON — semi-structured data
- XML — structured hierarchical data
- SQL — relational database tables and queries

Pentaho transformations are used to extract, transform, and load data from the applicable source formats into PostgreSQL staging tables.

## 6. Project Sprints

### Sprint 0 — Project Initiation and Architecture

**Objective:** Establish the project scope, requirements, architecture, and development workflow.

Key activities:

- Analyze financial business processes and stakeholders.
- Define project requirements and scope.
- Identify financial data sources.
- Prepare the Business Requirements Document (BRD).
- Design the high-level system architecture.
- Establish the GitHub repository and project structure.
- Prepare the project charter and sprint backlog.

### Sprint 1 — Data Discovery and Ingestion

**Objective:** Build the financial data landing zone by ingesting data from heterogeneous sources.

Key activities:

- Analyze source datasets and their structures.
- Prepare the source inventory and data dictionary.
- Develop Pentaho ETL transformations for supported data formats.
- Load raw financial data into PostgreSQL staging tables.
- Implement basic logging and exception handling.
- Validate ingestion results and maintain version-controlled ETL artifacts.

### Sprint 2 — Data Profiling and Data Warehouse

**Objective:** Transform raw financial records into trusted, analytics-ready datasets.

Key activities:

- Perform exploratory data analysis and data profiling using Python and Pandas.
- Identify duplicate transactions, missing values, inconsistent records, and master data quality issues.
- Clean and standardize financial records.
- Design a star schema for analytical workloads.
- Create fact and dimension tables in PostgreSQL.
- Develop Pentaho transformations to populate warehouse tables.
- Write SQL queries for financial reporting.
- Validate row counts, data quality, and transformation results.

### Sprint 3 — Data Governance, Lineage, and Analytics

**Objective:** Improve data traceability, governance, validation, and business intelligence capabilities.

Planned activities:

- Document source-to-target mappings.
- Prepare data lineage documentation.
- Develop a finance business glossary and metadata repository.
- Implement Pentaho Jobs for ETL orchestration.
- Validate financial reconciliation across enterprise systems.
- Develop executive financial dashboards in Power BI.
- Complete technical documentation and project reporting.
- Prepare the final version-controlled project release.

## 7. Data Engineering Workflow

The platform follows these major stages:

1. **Source discovery:** Identify the source datasets, formats, structures, and business meaning of financial fields.
2. **Data ingestion:** Use Pentaho transformations to read source data and load it into PostgreSQL staging tables.
3. **Data profiling:** Use Python and Pandas to analyze data distributions, missing values, duplicates, and inconsistencies.
4. **Data cleaning:** Standardize records and apply appropriate validation and cleaning rules.
5. **Dimensional modeling:** Organize curated data into fact and dimension tables using a star schema.
6. **Warehouse loading:** Transform and load validated records into PostgreSQL warehouse tables.
7. **Data validation:** Compare source and target records, check row counts, and verify data quality rules.
8. **Analytics and reporting:** Use SQL and Power BI to support financial analysis and reporting.
9. **Governance and documentation:** Maintain data dictionaries, mappings, lineage records, and validation reports.


## 8. Database Design

PostgreSQL serves as the relational storage layer for staging data and curated analytical datasets.

### Staging layer

The staging layer stores ingested source records before downstream cleaning, standardization, and transformation.

Its purposes include:

- Preserving ingested data for subsequent processing.
- Supporting source-to-target comparisons.
- Enabling data profiling and quality checks.
- Providing a structured input for warehouse loading.

### Data warehouse layer

The warehouse is designed around dimensional modeling, using a star schema where appropriate.

- **Fact tables:** Store measurable business events and transaction-level metrics.
- **Dimension tables:** Store descriptive attributes used to categorize and filter facts.
- **SQL queries:** Support aggregations, reporting, and analytical validation.

The specific fact tables, dimension tables, primary keys, and foreign-key relationships should be documented alongside the implemented database schema.

## 9. Data Quality and Validation

Reliable financial reporting requires consistent and validated input data.

The project addresses data quality through:

- Missing-value identification and analysis.
- Duplicate-record and repeated-key detection.
- Schema and data-type consistency checks.
- Standardization of financial fields.
- Source-to-staging and staging-to-warehouse row-count comparisons.
- Validation of transformation outputs.
- SQL-based verification of loaded records.
- Documentation of data quality findings and corrective actions.

Validation results should be recorded in the relevant profiling reports, data quality reports, and project documentation.

## 10. Business Intelligence and Use Cases

The curated data is intended to support the following business use cases:

- Revenue, expense, and profitability analysis.
- Financial performance monitoring.
- Cash flow analysis.
- Budget versus actual expenditure analysis.
- Accounts payable and accounts receivable trend analysis.
- Financial reconciliation and audit support.
- Executive reporting through Power BI dashboards.

The availability of each use case depends on the source data, implemented warehouse model, and completed reporting components.

## 11. Getting Started

### Prerequisites

Install or configure the following tools:

- Git
- Pentaho Data Integration (Spoon)
- PostgreSQL
- pgAdmin or the PostgreSQL command-line client
- Python with Pandas
- Microsoft Power BI Desktop, for report development

### Step 1 — Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd EFDP
```

Replace the placeholder with the actual GitHub repository URL.

### Step 2 — Configure PostgreSQL

1. Start the PostgreSQL server.
2. Create the project database.
3. Create the required staging and warehouse schemas or tables using the repository's SQL scripts.
4. Configure the database connection details used by the Pentaho transformations.

Example database creation command:

```sql
CREATE DATABASE efdp;
```

Use the actual database name and schema definitions required by your implementation.

### Step 3 — Configure Pentaho

1. Open Pentaho Data Integration (Spoon).
2. Open the required `.ktr` transformation.
3. Verify the input file paths and PostgreSQL connection settings.
4. Ensure that the required source datasets are available locally.
5. Execute the transformation and review its execution logs.
6. Verify the loaded records in PostgreSQL.

Update any machine-specific file paths when running the project on another computer.

### Step 4 — Run data profiling

Use the Python scripts provided in the repository, if available, to inspect the source or staging datasets.

Install the core profiling dependency if needed:

```bash
pip install pandas
```

Run a profiling script using its actual filename, for example:

```bash
python <profiling_script>.py
```

Additional dependencies and execution arguments should be taken from the corresponding script or project requirements file.

### Step 5 — Verify database results

Connect to the project database and inspect the staging or warehouse tables.

```sql
SELECT COUNT(*)
FROM <schema_name>.<table_name>;
```

Replace the placeholders with the actual schema and table names.

Compare the resulting counts and data quality checks with the corresponding source files and validation reports.

## 12. Version Control and Collaboration

Git and GitHub are used to maintain project history and support collaborative development.

Recommended workflow:

```bash
git status
git add .
git commit -m "Describe the changes"
git push origin main
```

Large source datasets and machine-specific configuration files should be handled carefully. Use `.gitignore` to exclude temporary files, local credentials, generated artifacts, and other files that should not be version-controlled.

For large datasets, document the source and acquisition method rather than committing files that exceed repository limits. Never commit database passwords or other secrets.

## 13. Project Deliverables

The project deliverables are organized by sprint.

| Sprint | Key deliverables |
|---|---|
| Sprint 0 | BRD, project charter, architecture, sprint backlog |
| Sprint 1 | Source inventory, data dictionary, Pentaho transformations, staging database |
| Sprint 2 | Data profiling report, data quality report, star schema, PostgreSQL warehouse, SQL scripts |
| Sprint 3 | Data lineage documentation, metadata repository, Pentaho Jobs, validation report, Power BI dashboard, project report, final release |

The completion status of individual deliverables should be verified against the current repository.

## 14. Limitations and Future Enhancements

Potential future enhancements include:

- More comprehensive automated data quality rules.
- Centralized ETL logging and audit metadata.
- Improved failure handling and controlled pipeline reruns.
- Automated source-to-target reconciliation.
- Complete end-to-end data lineage.
- Scheduled ETL orchestration using Pentaho Jobs.
- Expanded Power BI dashboards and financial KPIs.
- Automated validation and regression testing.
- Improved deployment and environment configuration.

These enhancements depend on the remaining project scope and should not be interpreted as already implemented.

## 15. Learning Outcomes

This project provides practical experience in:

- Enterprise data integration and ETL pipeline development.
- Working with heterogeneous data formats.
- Data profiling and quality assessment using Python and Pandas.
- Relational database design and SQL.
- Dimensional modeling and data warehouse development.
- Financial data validation and reconciliation.
- Data governance, metadata, and lineage documentation.
- Version control and collaborative development.
- Business intelligence and financial reporting.

## 16. Acknowledgements

This project was developed as part of the Enterprise Data Engineering Capstone Project under UC20: Enterprise Financial Data Platform (EFDP).

---

**Project:** UC20 — Enterprise Financial Data Platform  
**Primary technologies:** Pentaho Data Integration, PostgreSQL, Python, Pandas, SQL, Power BI  
**Repository:** https://github.com/alagupandi-25/ETL_EFDP
**Project status:** Update according to the current implementation and sprint progress.
