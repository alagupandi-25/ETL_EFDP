# Sprint 0 --- Project Initiation & Architecture

**Project:** UC20 --- Enterprise Financial Data Platform (EFDP)\
**Sprint:** 0 --- Project Initiation & Architecture\
**Status:** Foundation and planning documentation prepared

## 1. Sprint Objective

Establish the business context, scope, architecture, collaboration
workflow, and delivery plan for the Enterprise Financial Data Platform
before implementing data pipelines.

The platform is intended to bring financial data into a consistent
PostgreSQL-based environment, improve data quality and traceability, and
prepare curated data for SQL reporting and Power BI analytics.

## 2. Business Context

The project scenario describes ABC Global Enterprises Ltd., a
multinational organization whose finance function works across multiple
business domains. Fragmented data structures and formats make it
difficult to consolidate financial information, reconcile accounts,
analyze profitability, and produce reliable reporting.

The implementation uses the supplied SAP-derived financial and
master-data extracts. The architecture is designed to be extensible, but
the current implementation should not be described as having integrated
every enterprise system listed in the scenario.

## 3. Scope Defined

The project scope includes:

-   Ingesting the supplied SAP-derived data into PostgreSQL staging.
-   Maintaining a source inventory and data dictionary.
-   Profiling, validating, cleaning, and standardizing data.
-   Preparing a PostgreSQL warehouse model for analytics.
-   Maintaining technical documentation and version control in
    Git/GitHub.
-   Preparing source-to-target mapping, lineage, governance artifacts,
    and reporting as later sprint work.

## 4. Stakeholders and Business Needs

The requirements consider finance and reporting stakeholders, including
General Ledger, Accounts Payable, Accounts Receivable, treasury,
budgeting, tax, payroll, expense management, executive management, and
audit/compliance. These represent the broader business scenario; the
available implementation data is SAP-derived.

Key needs include consistent financial data, traceability, data-quality
validation, reporting-ready structures, and a maintainable ETL process.

## 5. Solution Architecture

The documented target architecture is:

``` text
SAP-derived source files
        |
        v
Pentaho Data Integration (Spoon)
        |
        v
PostgreSQL Bronze / Staging
        |
        v
Python / Pandas profiling and data-quality checks
        |
        v
Silver cleansing and standardization
        |
        v
PostgreSQL warehouse / Gold layer
        |
        v
Fact and dimension models + SQL reporting
        |
        v
Power BI analytics
```

The layers express the intended flow. Do not imply every downstream
layer or dashboard is complete unless verified by the current
repository.

## 6. Technology Stack

  -----------------------------------------------------------------------
  Area                    Technology              Purpose
  ----------------------- ----------------------- -----------------------
  ETL                     Pentaho Data            Data ingestion and
                          Integration (Spoon)     transformations

  Database                PostgreSQL              Staging and warehouse
                                                  storage

  Data profiling          Python / Pandas         Profiling and quality
                                                  assessment

  Version control         Git / GitHub            Collaboration and
                                                  change history

  Reporting               Power BI                Planned financial
                                                  reporting and
                                                  dashboards

  Documentation           Markdown / MS Word      Technical and sprint
                                                  documentation

  Methodology             Agile Scrum             Sprint-based delivery
  -----------------------------------------------------------------------

## 7. Repository and Planning Artifacts

The project repository was organized to separate source datasets, ETL
work, Python/SQL assets, documentation, and sprint deliverables.
Existing planning artifacts include the Business Requirements Document
(BRD), Solution Architecture, Source Inventory, Sprint Backlog, and
Project Charter.

Repository paths can vary by local clone; use the actual checked-in
folder names when referencing files in a submission.

## 8. Sprint 0 Deliverables

-   Business requirements and project scope documentation.
-   High-level solution architecture.
-   Project Charter and Sprint/Product Backlog.
-   Git/GitHub repository and project folder structure.
-   Initial identification of the supplied SAP-derived source data.

## 9. Outcome and Handoff

Sprint 0 established the project baseline and a layered architecture for
the implementation. Sprint 1 used this foundation to document the source
tables and build ingestion pipelines into PostgreSQL staging.

## 10. Items to Verify Before Submission

-   Confirm that the final BRD, Project Charter, backlog, and
    architecture files are committed to the repository.
-   Add the current repository URL to the submission package.
-   Ensure slides and documents describe Power BI as a downstream
    analytics target unless a completed EFDP dashboard is available.
