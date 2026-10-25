# Sprint 3 --- Data Governance, Lineage & Analytics

**Project:** UC20 --- Enterprise Financial Data Platform (EFDP)\
**Sprint:** 3 --- Data Governance, Lineage & Analytics\
**Status:** Sprint scope and governance approach documented; completion
of individual deliverables must be confirmed against the repository and
running implementation.

## 1. Sprint Objective

Prepare the EFDP for traceable and reliable reporting by documenting
data movement, defining metadata and business terms, orchestrating ETL
workflows, validating data, and preparing Power BI analytics.

Sprint 3 depends on validated outputs from Sprint 2. Dashboards and
reconciliation results should use curated data rather than unvalidated
raw staging records.

## 2. Source-to-Target Mapping

The source-to-target mapping should document how each field moves from a
SAP source table/file through Pentaho and PostgreSQL staging into the
cleansed and warehouse layers.

For each mapping, record where applicable:

-   Source file/table and source column.
-   Source data type and target data type.
-   Target table and target column.
-   Transformation, standardization, or lookup rule.
-   Key and relationship assumptions.
-   Null/default handling.
-   Validation rule and rejected-record behavior.

Mappings must reflect the transformations that actually exist; do not
document a proposed transformation as though it has already been
implemented.

## 3. Data Lineage

The intended lineage path is:

``` text
SAP-derived source file/table
        |
        v
Pentaho ingestion transformation
        |
        v
PostgreSQL staging table
        |
        v
Python/Pandas profiling and cleansing
        |
        v
Curated PostgreSQL table(s)
        |
        v
Fact/dimension model and SQL reporting
        |
        v
Power BI report/dashboard
```

Lineage documentation should identify the relevant transformation/job,
input and output tables, and any quality checks performed. Where a stage
is not yet implemented, mark it as planned or in progress.

## 4. Metadata Repository and Finance Business Glossary

The metadata repository should consolidate source and target table
details, field descriptions, data types, keys, transformations, and
ownership/validation notes where known.

The Finance Business Glossary should define business terms used in
reports. Definitions should be based on the actual available fields and
agreed business meaning. Terms such as accounting document, G/L account,
company code, customer, vendor, cost center, debit/credit, and financial
period may be included where supported by the data.

## 5. Pentaho Job Orchestration

Pentaho Jobs can coordinate the end-to-end workflow, including:

1.  Source ingestion.
2.  Staging validation.
3.  Profiling or cleansing steps.
4.  Curated/warehouse loading.
5.  Post-load checks.
6.  Logging, error handling, and failure notification or status
    recording.

A job should be described as complete only when the `.kjb` file exists,
its transformations are connected correctly, and a successful execution
has been verified. Individual `.ktr` transformations do not by
themselves prove that end-to-end orchestration is complete.

## 6. Reconciliation and Validation

Reconciliation should compare appropriate source and target totals using
explicit rules. Possible checks include:

-   Source-to-staging row-count reconciliation.
-   Staging-to-curated row-count and rejection accounting.
-   Key uniqueness and referential integrity.
-   Valid date and numeric conversions.
-   Financial totals only where the source fields and business rules
    make the comparison meaningful.

Record the query/script, source and target, expected result, actual
result, and any explained variance. Do not claim reconciliation across
all enterprise systems when the implementation uses the supplied
SAP-derived extracts.

## 7. Power BI Analytics

The intended reporting layer is Power BI, connected to validated
PostgreSQL warehouse data. Candidate views include financial
performance, G/L analysis, company-code comparisons, vendor/customer
views, and other analyses supported by the populated model.

Before claiming a dashboard is complete, verify that it connects to the
curated data, measures and filters are validated, and displayed totals
agree with SQL results. If the dashboard is not yet implemented or
validated, describe it as planned or in progress.

## 8. Git Release and Final Documentation

The final project package should include:

-   Data Lineage document.
-   Source-to-Target Mapping.
-   Metadata Repository.
-   Finance Business Glossary.
-   Pentaho Jobs and relevant transformations.
-   Validation/Reconciliation Report.
-   Power BI dashboard/report artifacts, if implemented.
-   Final project report and sprint presentation.
-   Tagged Git release, after the final artifacts have been reviewed and
    committed.

## 9. Sprint 3 Deliverables

The required deliverables are Data Lineage documentation, metadata
repository, Pentaho Jobs, validation report, Power BI dashboard, final
Git release, project report, and sprint presentation.

## 10. Completion Checklist

-   [ ] Source-to-target mappings match implemented transformations.
-   [ ] Lineage identifies actual files, transformations, and target
    tables.
-   [ ] Metadata and glossary entries are based on verified fields and
    business definitions.
-   [ ] Pentaho Jobs execute end-to-end successfully.
-   [ ] Reconciliation checks are repeatable and their results are
    recorded.
-   [ ] Power BI measures and visuals reconcile to SQL results.
-   [ ] Documentation and presentation reflect the actual completion
    status.
-   [ ] Final commit and Git tag are created.

## 11. Handoff and Status Note

This file describes Sprint 3's scope and the evidence needed to claim
completion. Update the status and checklist only after verifying the
current repository and database. Do not mark planned deliverables as
completed based on architecture documentation alone.
