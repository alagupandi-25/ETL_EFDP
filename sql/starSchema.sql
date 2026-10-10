
-- ---------------------------------------------------------------------
-- stg_bseg  (Accounting Document Line Items) -> fact_accounting_line_item
-- stg_bkpf  (Accounting Document Header)     -> dim_accounting_document
-- stg_t001  (Company Code Master)            -> dim_company_code
-- stg_ska1  (G/L Account Master)  
-- stg_skat  (G/L Account Texts)              -> dim_gl_account
-- stg_csks  (Cost Center Master)  
-- stg_cskt  (Cost Center Texts)              -> dim_cost_center
-- stg_kna1  (Customer Master)                -> dim_customer
-- stg_lfa1  (Vendor Master)                  -> dim_vendor
-- stg_t002  (System Languages)               -> dim_language
--                                            -> dim_date
-- ---------------------------------------------------------------------

CREATE SCHEMA IF NOT EXISTS dwh;
SET search_path TO dwh;

DROP TABLE IF EXISTS fact_accounting_line_item CASCADE;
DROP TABLE IF EXISTS dim_line_item_attribute   CASCADE;
DROP TABLE IF EXISTS dim_accounting_document   CASCADE;
DROP TABLE IF EXISTS dim_cost_center           CASCADE;
DROP TABLE IF EXISTS dim_gl_account            CASCADE;
DROP TABLE IF EXISTS dim_customer              CASCADE;
DROP TABLE IF EXISTS dim_vendor                CASCADE;
DROP TABLE IF EXISTS dim_company_code          CASCADE;
DROP TABLE IF EXISTS dim_language              CASCADE;
DROP TABLE IF EXISTS dim_date                  CASCADE;


CREATE TABLE dim_date (
    date_key            INTEGER      PRIMARY KEY,         
    full_date           DATE         UNIQUE,
    day_of_month        SMALLINT,
    day_of_week         SMALLINT,
    day_name            VARCHAR(10),
    month_number        SMALLINT,
    month_name          VARCHAR(10),
    quarter_number      SMALLINT,
    calendar_year       INTEGER,
    is_weekend          BOOLEAN
);

CREATE TABLE dim_language (
    language_key             SERIAL       PRIMARY KEY,
    sap_language_code        VARCHAR(20)  NOT NULL UNIQUE,
    language_specialization  VARCHAR(200),
    language_hierarchy_level INTEGER,
    iso_language_code        VARCHAR(20)
);

CREATE TABLE dim_company_code (
    company_code_key    SERIAL        PRIMARY KEY,
    client_id           VARCHAR(10),
    company_code        VARCHAR(20)   NOT NULL,
    company_name        VARCHAR(500),
    city                VARCHAR(200),
    country_code        VARCHAR(20),
    company_currency    VARCHAR(20),
    language_code       VARCHAR(20),                       
    chart_of_accounts   VARCHAR(30),
    fiscal_year_variant VARCHAR(20),
    CONSTRAINT uq_dim_company_code UNIQUE (client_id, company_code)
);


CREATE TABLE dim_gl_account (
    gl_account_key           SERIAL        PRIMARY KEY,
    client_id                VARCHAR(10),
    chart_of_accounts        VARCHAR(30)   NOT NULL,
    gl_account_no            VARCHAR(30)   NOT NULL,
    language_code            VARCHAR(20)   NOT NULL DEFAULT '',
    gl_account_group         VARCHAR(50),
    balance_sheet_indicator  VARCHAR(20),
    financial_statement_type VARCHAR(100),
    created_by_user          VARCHAR(100),
    created_date             VARCHAR(20),
    gl_account_short_name    VARCHAR(100),
    gl_account_description   VARCHAR(255),
    search_term              VARCHAR(100),
    is_deleted               BOOLEAN       DEFAULT FALSE,
    CONSTRAINT uq_dim_gl_account UNIQUE (chart_of_accounts, gl_account_no, language_code)
);


CREATE TABLE dim_cost_center (
    cost_center_key         SERIAL        PRIMARY KEY,
    client_id               VARCHAR(10),
    controlling_area        VARCHAR(20)   NOT NULL,
    cost_center_id          VARCHAR(30)   NOT NULL,
    valid_from_date         DATE,
    valid_to_date           DATE          NOT NULL DEFAULT DATE '9999-12-31',
    language_code           VARCHAR(20)   NOT NULL DEFAULT '',
    company_code            VARCHAR(20),
    cost_center_category    VARCHAR(30),
    responsible_person      VARCHAR(100),
    currency_code           VARCHAR(20),
    cost_center_name        VARCHAR(200),
    cost_center_description VARCHAR(500),
    CONSTRAINT uq_dim_cost_center UNIQUE (controlling_area, cost_center_id, valid_to_date, language_code)
);

CREATE TABLE dim_customer (
    customer_key           SERIAL        PRIMARY KEY,
    client_id              BIGINT,
    customer_id            VARCHAR(20)   NOT NULL UNIQUE,
    customer_name          VARCHAR(100),
    customer_name_2        VARCHAR(100),
    country_code           VARCHAR(10),
    city                   VARCHAR(100),
    postal_code            VARCHAR(20),
    regional_code          VARCHAR(20),
    street_address         VARCHAR(150),
    customer_account_group VARCHAR(20),
    language_code          VARCHAR(10),
    created_date           TIMESTAMP
);

CREATE TABLE dim_vendor (
    vendor_key           SERIAL        PRIMARY KEY,
    client_id            BIGINT,
    vendor_id            VARCHAR(20)   NOT NULL UNIQUE,
    vendor_name          VARCHAR(100),
    vendor_name2         VARCHAR(100),
    country_code         VARCHAR(10),
    city                 VARCHAR(100),
    postal_code          VARCHAR(20),
    region_code          VARCHAR(20),
    street_address       VARCHAR(150),
    vendor_account_group VARCHAR(20),
    language_code        VARCHAR(10),
    created_date         TIMESTAMP
);

CREATE TABLE dim_accounting_document (
    document_key               SERIAL        PRIMARY KEY,
    client_id                  VARCHAR(4),
    company_code               VARCHAR(10)   NOT NULL,
    accounting_document_no     VARCHAR(20)   NOT NULL,
    fiscal_year                INTEGER       NOT NULL,
    document_type              VARCHAR(10),
    entry_time                 VARCHAR(8),
    created_by_user            VARCHAR(50),
    transaction_code           VARCHAR(10),
    reference_transaction_type VARCHAR(10),
    reference_key              VARCHAR(30),
    CONSTRAINT uq_dim_accounting_document
        UNIQUE (company_code, accounting_document_no, fiscal_year)
);

CREATE TABLE dim_line_item_attribute (
    line_item_attribute_key SERIAL       PRIMARY KEY,
    account_type            VARCHAR(20),
    debit_credit_indicator  VARCHAR(20),
    special_gl_indicator    VARCHAR(30),
    tax_code                VARCHAR(30),
    payment_terms           VARCHAR(30),
    CONSTRAINT uq_dim_line_item_attribute
        UNIQUE (account_type, debit_credit_indicator, special_gl_indicator, tax_code, payment_terms)
);

CREATE TABLE fact_accounting_line_item (
    line_item_fact_key        BIGSERIAL    PRIMARY KEY,

    document_key              INTEGER      NOT NULL REFERENCES dim_accounting_document (document_key),
    company_code_key          INTEGER      NOT NULL REFERENCES dim_company_code (company_code_key),
    gl_account_key            INTEGER      REFERENCES dim_gl_account (gl_account_key),
    cost_center_key           INTEGER      REFERENCES dim_cost_center (cost_center_key),
    customer_key              INTEGER      REFERENCES dim_customer (customer_key),
    vendor_key                INTEGER      REFERENCES dim_vendor (vendor_key),
    line_item_attribute_key   INTEGER      REFERENCES dim_line_item_attribute (line_item_attribute_key),

    posting_date_key          INTEGER      REFERENCES dim_date (date_key),
    document_date_key         INTEGER      REFERENCES dim_date (date_key),
    entry_date_key            INTEGER      REFERENCES dim_date (date_key),
    baseline_date_key         INTEGER      REFERENCES dim_date (date_key),  
    clearing_date_key         INTEGER      REFERENCES dim_date (date_key),

    accounting_document_no    VARCHAR(30)  NOT NULL,
    fiscal_year               INTEGER      NOT NULL,
    line_item_no              VARCHAR(20)  NOT NULL,
    fiscal_period             INTEGER,
    assignment_no             VARCHAR(50),
    clearing_document_number  VARCHAR(30),
    line_item_text            VARCHAR(500),
    document_currency         VARCHAR(10),

    amount_local_currency     NUMERIC(23,2),
    amount_document_currency  NUMERIC(23,2),

    etl_load_timestamp        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uq_fact_line_item
        UNIQUE (company_code_key, accounting_document_no, fiscal_year, line_item_no)
);

CREATE INDEX ix_fact_document      ON fact_accounting_line_item (document_key);
CREATE INDEX ix_fact_company       ON fact_accounting_line_item (company_code_key);
CREATE INDEX ix_fact_gl_account    ON fact_accounting_line_item (gl_account_key);
CREATE INDEX ix_fact_cost_center   ON fact_accounting_line_item (cost_center_key);
CREATE INDEX ix_fact_customer      ON fact_accounting_line_item (customer_key);
CREATE INDEX ix_fact_vendor        ON fact_accounting_line_item (vendor_key);
CREATE INDEX ix_fact_posting_date  ON fact_accounting_line_item (posting_date_key);
CREATE INDEX ix_fact_fiscal        ON fact_accounting_line_item (fiscal_year, fiscal_period);

