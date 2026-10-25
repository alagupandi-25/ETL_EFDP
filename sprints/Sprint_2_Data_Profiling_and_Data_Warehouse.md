# Sprint 2 --- Data Profiling & Database / Data Warehouse

**Project:** UC20 --- Enterprise Financial Data Platform (EFDP)\
**Sprint:** 2 --- Data Profiling & DB / Data Warehouse\
**Status:** Profiling and quality-report work completed; cleansing and
warehouse implementation should be marked according to the latest
checked-in artifacts and database state.

## 1. Sprint Objective

Transform raw SAP-derived staging data into trusted, analytics-ready
data through Python/Pandas profiling, data-quality assessment, cleansing
and standardization, PostgreSQL modeling, and SQL reporting preparation.

## 2. Input Layer

Sprint 2 uses the ten staging tables created in Sprint 1:

`stg_bkpf`, `stg_bseg`, `stg_csks`, `stg_cskt`, `stg_kna1`, `stg_lfa1`,
`stg_ska1`, `stg_skat`, `stg_t001`, and `stg_t002`.

The staging layer is retained as the raw landing layer. Cleaning should
produce a separate downstream layer so that original ingested data
remains available for comparison and traceability.

## 3. Profiling and Data-Quality Assessment

Python/Pandas profiling was performed across the ten SAP-derived tables.
The reports covered approximately **1,465,129 total rows** across the
tables.

Reported findings include:

  ------------------------------------------------------------------------
  Table                 Reported issue                 Count / observation
  --------------------- --------------------- ----------------------------
  `stg_skat`            Exact duplicate rows                        71,924

  `stg_skat`            `chart_of_accounts`      Entire column reported as
                        fully NULL                                    NULL

  `stg_lfa1`            Duplicate rows                                 389

  `stg_t001`            Duplicate rows                                  67

  Other staging tables  Further key, NULL,         Requires table-specific
                        and business-rule                           review
                        checks                
  ------------------------------------------------------------------------

These are reported profiling findings, not proof that all listed records
should be deleted. In particular, exact duplicates, repeated business
keys, and valid repeated text/description records are different cases
and should be handled according to source semantics and validated keys.

## 4. Cleansing and Standardization Approach

The cleaning process should be reproducible and should preserve source
data. The established cleaning approach includes:

-   Standardizing whitespace and empty-string representations.
-   Profiling missing values and retaining a record of missingness.
-   Applying field renaming only through explicit mappings.
-   Parsing dates only where the source format and business meaning are
    understood.
-   Checking candidate keys and duplicate records before removing
    anything.
-   Validating row counts and key uniqueness before and after cleaning.
-   Recording quality findings and producing evidence files.
-   Loading cleaned results to separate tables only after validation.

Do not automatically fill financial amounts or delete duplicates without
a defensible business rule. Preserve the raw `stg_*` tables.

## 5. Date and Type Handling

Some date columns were loaded as strings in Sprint 1. Sprint 2 is the
appropriate stage to parse and standardize those values, with invalid or
ambiguous values reported rather than silently coerced. Warehouse
columns should use suitable PostgreSQL types such as `DATE`,
`TIMESTAMP`, numeric, and text types according to the field's meaning.

## 6. PostgreSQL Warehouse and Dimensional Modeling

The target design uses a dimensional warehouse with fact and dimension
tables, populated from validated and standardized data. The exact tables
and relationships must reflect the supplied SAP data and verified
business keys.

Potential subject areas include accounting documents/line items, G/L
accounts, company codes, customers, vendors, cost centers, and
language/text descriptions. Do not claim a fact or dimension table is
implemented until its DDL, load logic, and validation evidence exist in
the repository.

SQL reporting queries should be built on the curated layer and validated
against known totals and source records.

## 7. Validation and Evidence

Recommended validation evidence for this sprint includes:

-   Before-and-after row counts.
-   Duplicate and candidate-key checks.
-   NULL/missing-value summaries.
-   Invalid date/type conversion counts.
-   Referential-integrity checks between related tables.
-   Financial value checks where business rules and source fields
    support them.
-   SQL scripts and load logs for warehouse tables.

Any reported total should identify the source table(s), query or script,
and date of execution.

## 8. Sprint 2 Deliverables

-   Python/Pandas Data Profiling Report.
-   Data Quality Report.
-   Cleaning/standardization scripts or notebook.
-   Star Schema design.
-   PostgreSQL warehouse tables and load logic, where implemented.
-   SQL reporting scripts.
-   Git repository updates.

## 9. Outcome and Handoff

Profiling has identified data-quality issues that must be addressed
before downstream analytics. The next step is to complete and validate
the cleansing/warehouse layer, then document source-to-target mappings,
lineage, governance, reconciliation, and analytics in Sprint 3.

## 10. Items to Verify Before Submission

-   Confirm whether cleaned tables have been loaded or whether cleaning
    remains in progress.
-   Confirm the final Star Schema and which fact/dimension tables are
    populated.
-   Add exact report filenames and a reproducible summary of each
    profiling result.
-   Verify whether the `stg_skat` NULL column is genuinely absent from
    the source, introduced during ingestion, or caused by a mapping
    issue.
-   Keep reported profiling counts distinct from the number of records
    actually removed or corrected.
