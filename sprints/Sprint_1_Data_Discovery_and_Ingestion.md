# Sprint 1 --- Data Discovery & Ingestion

**Project:** UC20 --- Enterprise Financial Data Platform (EFDP)\
**Sprint:** 1 --- Data Discovery & Ingestion\
**Status:** Source documentation and PostgreSQL staging ingestion
substantially completed; verify all transformations and table counts
against the latest repository/database.

## 1. Sprint Objective

Build the initial data landing zone by inspecting the supplied
SAP-derived data, documenting its structure, creating Pentaho ingestion
transformations, and loading raw records into PostgreSQL staging tables.

## 2. Source Data Inventory

The implementation focuses on these ten SAP-derived tables:

  SAP table   Staging table   Domain / role
  ----------- --------------- --------------------------------
  BKPF        `stg_bkpf`      Accounting document headers
  BSEG        `stg_bseg`      Accounting document line items
  CSKS        `stg_csks`      Cost center master data
  CSKT        `stg_cskt`      Cost center text data
  KNA1        `stg_kna1`      Customer master data
  LFA1        `stg_lfa1`      Vendor master data
  SKA1        `stg_ska1`      G/L account master data
  SKAT        `stg_skat`      G/L account text data
  T001        `stg_t001`      Company-code data
  T002        `stg_t002`      Language-key data

The source package includes CSV extracts and additional format examples,
including `SKAT.xml` and `T002.xls`, used to demonstrate ingestion from
heterogeneous file formats. The core implementation is SAP-derived; it
should not be represented as live connectivity to all enterprise systems
listed in the project scenario.

## 3. Data Dictionary and Source Documentation

The Source Inventory and Data Dictionary describe source files/tables,
columns, formats, and their intended staging targets. Source identifiers
and SAP field names should be preserved unless a documented downstream
standardization rule is applied.

Important implementation notes:

-   Preserve SAP identifiers such as `MANDT`, `KTOPL`, `SAKNR`, and
    `SPRAS` where present.
-   Preserve audit/operation fields such as `operation_flag`,
    `is_deleted`, and `recordstamp` where present in the source.
-   Keep the exact source-compatible spelling `payement_baseline_date`
    in `stg_bseg` if that is the column name in the current
    implementation.
-   Validate column names and data types against the supplied files
    rather than relying only on inferred descriptions.

## 4. Pentaho Ingestion and Staging

Pentaho Data Integration (Spoon) is used to read source data and write
it to PostgreSQL staging tables. The staging layer is intended to
preserve source records before profiling and cleansing.

The documented pipeline pattern is:

1.  Read the source file using the appropriate input step.
2.  Map fields to the staging table structure.
3.  Write records to the corresponding `stg_*` table.
4.  Validate row counts and inspect execution logs.
5.  Commit the transformation and related documentation to Git.

A Sprint 1 issue was that some date values were stored as strings in
staging. This was retained as a raw-ingestion characteristic; type
conversion and standardization belong in the downstream
cleansing/warehouse process rather than silently altering the source
landing data.

## 5. Ingestion Validation Evidence

During a BKPF staging check, the following values were recorded:

  Check                            Result
  ----------------------------- ---------
  Original CSV data rows          150,057
  PostgreSQL staging rows         150,057
  Staging-to-source row ratio         1.0

This confirms row-count parity for that specific run/table. It does not,
by itself, prove that every source field or every table has been
validated.

A duplicate-key investigation also reported 451 repeated document keys
and zero repeated keys associated with multiple distinct records for the
check performed. Treat this as a check-specific result; document the
exact table, key definition, and query alongside the result in the final
evidence if available.

## 6. Git and Repository Management

ETL transformations, source documentation, SQL/Python assets, and sprint
documentation are maintained in the EFDP Git repository. Large raw
datasets may need to be handled carefully to avoid GitHub file-size
limits; keep repository history and the submitted repository structure
consistent with the team's chosen data-file policy.

## 7. Sprint 1 Deliverables

-   Source Inventory for the ten SAP-derived tables.
-   Data Dictionary.
-   Pentaho ingestion transformations.
-   PostgreSQL staging tables.
-   Git commit history for project artifacts.

## 8. Outcome and Handoff

Sprint 1 established a source-to-staging landing zone. Sprint 2 builds
on this layer by profiling the data, identifying quality issues, and
preparing cleaned and analytics-ready structures.

## 9. Items to Verify Before Submission

-   Re-run or inspect row-count checks for all ten staging tables.
-   Confirm that all `.ktr` transformations use valid relative paths or
    documented parameters.
-   Capture successful Pentaho execution logs and PostgreSQL row counts.
-   Verify the exact scope of the duplicate-key result before presenting
    it as a general data-quality conclusion.
