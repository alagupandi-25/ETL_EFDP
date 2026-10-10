import os

import psycopg2
from psycopg2.extras import execute_values

SOURCE_DB = {
    "host": "localhost",
    "port": 5432,
    "dbname": "efdp_staging",
    "user": "postgres",
    "password": os.environ.get("EFDP_SOURCE_PASSWORD", "your_password_here"),
}

TARGET_DB = {
    "host": "localhost",
    "port": 5432,
    "dbname": "efdp_dwh",
    "user": "postgres",
    "password": os.environ.get("EFDP_TARGET_PASSWORD", "your_password_here"),
}

BATCH_SIZE = 5000
FACT_CHUNK_SIZE = 50000


DIMENSION_JOBS = [
    {
        "name": "dim_language",
        "target": "dwh.dim_language",
        "columns": ["sap_language_code", "language_specialization",
                    "language_hierarchy_level", "iso_language_code"],
        "conflict": ["sap_language_code"],
        "extract": """
            SELECT DISTINCT ON (sap_language_code)
                   sap_language_code, language_specialization,
                   language_hierarchy_level, iso_language_code
            FROM public.stg_t002
            WHERE sap_language_code IS NOT NULL
              AND UPPER(COALESCE(is_deleted, '')) NOT IN ('X', 'TRUE', 'T', '1', 'Y')
            ORDER BY sap_language_code, record_timestamp DESC NULLS LAST
        """,
    },
    {
        "name": "dim_company_code",
        "target": "dwh.dim_company_code",
        "columns": ["client_id", "company_code", "company_name", "city", "country_code",
                    "company_currency", "language_code", "chart_of_accounts",
                    "fiscal_year_variant"],
        "conflict": ["client_id", "company_code"],
        "extract": """
            SELECT DISTINCT ON (client_id, company_code)
                   client_id, company_code, company_name, city, country_code,
                   company_currency, language_code, chart_of_accounts, fiscal_year_variant
            FROM public.stg_t001
            WHERE company_code IS NOT NULL
            ORDER BY client_id, company_code
        """,
    },
    {
        "name": "dim_gl_account",
        "target": "dwh.dim_gl_account",
        "columns": ["client_id", "chart_of_accounts", "gl_account_no", "language_code",
                    "gl_account_group", "balance_sheet_indicator", "financial_statement_type",
                    "created_by_user", "created_date",
                    "gl_account_short_name", "gl_account_description", "search_term",
                    "is_deleted"],
        "conflict": ["chart_of_accounts", "gl_account_no", "language_code"],
        "extract": """
            SELECT DISTINCT ON (k.chart_of_accounts, k.gl_account_no, COALESCE(s.language_code, ''))
                   k.client_id, k.chart_of_accounts, k.gl_account_no,
                   COALESCE(s.language_code, ''),
                   k.gl_account_group, k.balance_sheet_indicator, k.financial_statement_type,
                   k.created_by_user, k.created_date,
                   s.gl_account_short_name, s.gl_account_description, s.search_term,
                   COALESCE(s.is_deleted, k.is_deleted, FALSE)
            FROM public.stg_ska1 k
            LEFT JOIN public.stg_skat s
                   ON s.chart_of_accounts = k.chart_of_accounts
                  AND s.gl_account_number = k.gl_account_no
            WHERE k.chart_of_accounts IS NOT NULL
              AND k.gl_account_no     IS NOT NULL
            ORDER BY k.chart_of_accounts, k.gl_account_no, COALESCE(s.language_code, ''),
                     s.record_timestamp DESC NULLS LAST, k.record_timestamp DESC NULLS LAST
        """,
    },
    {
        "name": "dim_cost_center",
        "target": "dwh.dim_cost_center",
        "columns": ["client_id", "controlling_area", "cost_center_id", "valid_from_date",
                    "valid_to_date", "language_code", "company_code", "cost_center_category",
                    "responsible_person", "currency_code", "cost_center_name",
                    "cost_center_description"],
        "conflict": ["controlling_area", "cost_center_id", "valid_to_date", "language_code"],
        "extract": """
            SELECT DISTINCT ON (k.controlling_area, k.cost_center_id,
                                COALESCE(k.valid_to_date, DATE '9999-12-31'),
                                COALESCE(t.language_code, ''))
                   k.client_id, k.controlling_area, k.cost_center_id, k.valid_from_date,
                   COALESCE(k.valid_to_date, DATE '9999-12-31'),
                   COALESCE(t.language_code, ''),
                   k.company_code, k.cost_center_category, k.responsible_person,
                   k.currency_code, t.cost_center_name, t.cost_center_description
            FROM public.stg_csks k
            LEFT JOIN public.stg_cskt t
                   ON t.controlling_area = k.controlling_area
                  AND t.cost_center_id   = k.cost_center_id
                  AND t.valid_to_date IS NOT DISTINCT FROM k.valid_to_date
            WHERE k.controlling_area IS NOT NULL
              AND k.cost_center_id   IS NOT NULL
            ORDER BY k.controlling_area, k.cost_center_id,
                     COALESCE(k.valid_to_date, DATE '9999-12-31'),
                     COALESCE(t.language_code, '')
        """,
    },
    {
        "name": "dim_customer",
        "target": "dwh.dim_customer",
        "columns": ["client_id", "customer_id", "customer_name", "customer_name_2",
                    "country_code", "city", "postal_code", "regional_code", "street_address",
                    "customer_account_group", "language_code", "created_date"],
        "conflict": ["customer_id"],
        "extract": """
            SELECT DISTINCT ON (customer_id)
                   client_id, customer_id, customer_name, customer_name_2,
                   country_code, city, postal_code, regional_code, street_address,
                   customer_account_group, language_code, created_date
            FROM public.stg_kna1
            WHERE customer_id IS NOT NULL
            ORDER BY customer_id, created_date DESC NULLS LAST
        """,
    },
    {
        "name": "dim_vendor",
        "target": "dwh.dim_vendor",
        "columns": ["client_id", "vendor_id", "vendor_name", "vendor_name2",
                    "country_code", "city", "postal_code", "region_code", "street_address",
                    "vendor_account_group", "language_code", "created_date"],
        "conflict": ["vendor_id"],
        "extract": """
            SELECT DISTINCT ON (vendor_id)
                   client_id, vendor_id, vendor_name, vendor_name2,
                   country_code, city, postal_code, region_code, street_address,
                   vendor_account_group, language_code, created_date
            FROM public.stg_lfa1
            WHERE vendor_id IS NOT NULL
            ORDER BY vendor_id, created_date DESC NULLS LAST
        """,
    },
    {
        "name": "dim_accounting_document",
        "target": "dwh.dim_accounting_document",
        "columns": ["client_id", "company_code", "accounting_document_no", "fiscal_year",
                    "document_type", "entry_time", "created_by_user", "transaction_code",
                    "reference_transaction_type", "reference_key"],
        "conflict": ["company_code", "accounting_document_no", "fiscal_year"],
        "extract": """
            SELECT DISTINCT ON (company_code, accounting_document_no, fiscal_year)
                   client_id, company_code, accounting_document_no, fiscal_year,
                   document_type, entry_time, created_by_user, transaction_code,
                   reference_transaction_type, reference_key
            FROM public.stg_bkpf
            WHERE company_code IS NOT NULL
              AND accounting_document_no IS NOT NULL
              AND fiscal_year IS NOT NULL
            ORDER BY company_code, accounting_document_no, fiscal_year,
                     entry_date DESC NULLS LAST
        """,
    },
]


LINE_ITEM_COLUMNS = [
    "client_id", "company_code", "accounting_document_no", "fiscal_year", "line_item_no",
    "account_type", "debit_credit_indicator", "amount_local_currency",
    "amount_document_currency", "assignment_no", "line_item_text", "payment_terms",
    "cost_center_id", "gl_account_no", "customer_id", "vendor_id",
    "payement_baseline_date", "tax_code", "clearing_document_number", "clearing_date",
    "special_gl_indicator",
    "posting_date", "document_date", "entry_date", "fiscal_period", "document_currency",
]

SQL_EXTRACT_LINE_ITEMS = """
WITH hdr AS (
    SELECT DISTINCT ON (company_code, accounting_document_no, fiscal_year)
           company_code, accounting_document_no, fiscal_year,
           posting_date, document_date, entry_date, fiscal_period, document_currency
    FROM public.stg_bkpf
    ORDER BY company_code, accounting_document_no, fiscal_year, entry_date DESC NULLS LAST
),
lines AS (
    SELECT DISTINCT ON (company_code, accounting_document_no, fiscal_year, line_item_no) *
    FROM public.stg_bseg
    ORDER BY company_code, accounting_document_no, fiscal_year, line_item_no
)
SELECT b.client_id, b.company_code, b.accounting_document_no, b.fiscal_year, b.line_item_no,
       b.account_type, b.debit_credit_indicator, b.amount_local_currency,
       b.amount_document_currency, b.assignment_no, b.line_item_text, b.payment_terms,
       b.cost_center_id, b.gl_account_no, b.customer_id, b.vendor_id,
       b.payement_baseline_date, b.tax_code, b.clearing_document_number, b.clearing_date,
       b.special_gl_indicator,
       h.posting_date, h.document_date, h.entry_date, h.fiscal_period, h.document_currency
FROM lines b
JOIN hdr h
  ON  h.company_code           = b.company_code
  AND h.accounting_document_no = b.accounting_document_no
  AND h.fiscal_year            = b.fiscal_year
"""

SQL_SAFE_DATE_FUNCTION = r"""
CREATE OR REPLACE FUNCTION dwh.safe_to_date(txt text) RETURNS date AS $$
DECLARE
    result date;
BEGIN
    IF txt IS NULL OR btrim(txt) = '' THEN
        RETURN NULL;
    END IF;
    IF btrim(txt) ~ '^[0-9]{8}$' THEN
        result := to_date(btrim(txt), 'YYYYMMDD');
    ELSE
        result := left(btrim(txt), 10)::date;
    END IF;
    IF result < DATE '1900-01-01' OR result > DATE '2100-12-31' THEN
        RETURN NULL;
    END IF;
    RETURN result;
EXCEPTION WHEN others THEN
    RETURN NULL;
END;
$$ LANGUAGE plpgsql IMMUTABLE;
"""

SQL_CREATE_TMP_LINE_ITEM = """
CREATE TEMP TABLE tmp_line_item (
    row_id                   bigserial,
    client_id                text,
    company_code             text,
    accounting_document_no   text,
    fiscal_year              integer,
    line_item_no             text,
    account_type             text,
    debit_credit_indicator   text,
    amount_local_currency    numeric(23, 9),
    amount_document_currency numeric(23, 9),
    assignment_no            text,
    line_item_text           text,
    payment_terms            text,
    cost_center_id           text,
    gl_account_no            text,
    customer_id              text,
    vendor_id                text,
    payement_baseline_date   text,
    tax_code                 text,
    clearing_document_number text,
    clearing_date            text,
    special_gl_indicator     text,
    posting_date             date,
    document_date            date,
    entry_date               date,
    fiscal_period            integer,
    document_currency        text
) ON COMMIT DROP;
"""

SQL_DATE_RANGE = """
WITH all_dates AS (
    SELECT posting_date  AS d FROM tmp_line_item
    UNION ALL SELECT document_date FROM tmp_line_item
    UNION ALL SELECT entry_date    FROM tmp_line_item
    UNION ALL SELECT dwh.safe_to_date(payement_baseline_date) FROM tmp_line_item
    UNION ALL SELECT dwh.safe_to_date(clearing_date)          FROM tmp_line_item
)
SELECT MIN(d), MAX(d)
FROM all_dates
WHERE d BETWEEN DATE '1900-01-01' AND DATE '2100-12-31';
"""

SQL_LOAD_DIM_DATE = """
INSERT INTO dwh.dim_date
    (date_key, full_date, day_of_month, day_of_week, day_name,
     month_number, month_name, quarter_number, calendar_year, is_weekend)
SELECT  to_char(g.d, 'YYYYMMDD')::int,
        g.d::date,
        EXTRACT(DAY     FROM g.d)::smallint,
        EXTRACT(ISODOW  FROM g.d)::smallint,
        btrim(to_char(g.d, 'Day')),
        EXTRACT(MONTH   FROM g.d)::smallint,
        btrim(to_char(g.d, 'Month')),
        EXTRACT(QUARTER FROM g.d)::smallint,
        EXTRACT(YEAR    FROM g.d)::int,
        EXTRACT(ISODOW  FROM g.d) >= 6
FROM generate_series(%s::date, %s::date, interval '1 day') AS g(d)
ON CONFLICT (date_key) DO NOTHING;
"""

SQL_LOAD_DIM_LINE_ITEM_ATTRIBUTE = """
INSERT INTO dwh.dim_line_item_attribute
    (account_type, debit_credit_indicator, special_gl_indicator, tax_code, payment_terms)
SELECT DISTINCT
       COALESCE(account_type, ''),
       COALESCE(debit_credit_indicator, ''),
       COALESCE(special_gl_indicator, ''),
       COALESCE(tax_code, ''),
       COALESCE(payment_terms, '')
FROM tmp_line_item
ON CONFLICT (account_type, debit_credit_indicator, special_gl_indicator, tax_code, payment_terms)
DO NOTHING;
"""

SQL_TRUNCATE_FACT = "TRUNCATE TABLE dwh.fact_accounting_line_item RESTART IDENTITY;"

SQL_LOAD_FACT = """
INSERT INTO dwh.fact_accounting_line_item
    (document_key, company_code_key, gl_account_key, cost_center_key,
     customer_key, vendor_key, line_item_attribute_key,
     posting_date_key, document_date_key, entry_date_key,
     baseline_date_key, clearing_date_key,
     accounting_document_no, fiscal_year, line_item_no, fiscal_period,
     assignment_no, clearing_document_number, line_item_text, document_currency,
     amount_local_currency, amount_document_currency)
SELECT  d.document_key,
        c.company_code_key,
        gl.gl_account_key,
        cc.cost_center_key,
        cu.customer_key,
        v.vendor_key,
        a.line_item_attribute_key,
        COALESCE(to_char(b.posting_date,  'YYYYMMDD')::int, -1),
        COALESCE(to_char(b.document_date, 'YYYYMMDD')::int, -1),
        COALESCE(to_char(b.entry_date,    'YYYYMMDD')::int, -1),
        COALESCE(to_char(dwh.safe_to_date(b.payement_baseline_date), 'YYYYMMDD')::int, -1),
        COALESCE(to_char(dwh.safe_to_date(b.clearing_date),          'YYYYMMDD')::int, -1),
        b.accounting_document_no,
        b.fiscal_year,
        b.line_item_no,
        b.fiscal_period,
        b.assignment_no,
        b.clearing_document_number,
        b.line_item_text,
        b.document_currency,
        b.amount_local_currency,
        b.amount_document_currency
FROM tmp_line_item b
JOIN dwh.dim_accounting_document d
  ON  d.company_code           = b.company_code
  AND d.accounting_document_no = b.accounting_document_no
  AND d.fiscal_year            = b.fiscal_year
JOIN dwh.dim_company_code c
  ON  c.company_code = b.company_code
  AND c.client_id    = b.client_id
LEFT JOIN LATERAL (
    SELECT g.gl_account_key
    FROM dwh.dim_gl_account g
    WHERE g.chart_of_accounts = c.chart_of_accounts
      AND g.gl_account_no     = b.gl_account_no
    ORDER BY (g.language_code = c.language_code) DESC,
             (g.language_code = 'E') DESC,
             g.gl_account_key
    LIMIT 1
) gl ON TRUE
LEFT JOIN LATERAL (
    SELECT k.cost_center_key
    FROM dwh.dim_cost_center k
    WHERE k.cost_center_id = b.cost_center_id
      AND (k.company_code = b.company_code OR k.company_code IS NULL)
      AND b.posting_date BETWEEN COALESCE(k.valid_from_date, DATE '0001-01-01') AND k.valid_to_date
    ORDER BY (k.language_code = c.language_code) DESC,
             (k.language_code = 'E') DESC,
             k.valid_to_date DESC,
             k.cost_center_key
    LIMIT 1
) cc ON TRUE
LEFT JOIN dwh.dim_customer cu ON cu.customer_id = NULLIF(b.customer_id, '')
LEFT JOIN dwh.dim_vendor   v  ON v.vendor_id    = NULLIF(b.vendor_id, '')
LEFT JOIN dwh.dim_line_item_attribute a
  ON  a.account_type           = COALESCE(b.account_type, '')
  AND a.debit_credit_indicator = COALESCE(b.debit_credit_indicator, '')
  AND a.special_gl_indicator   = COALESCE(b.special_gl_indicator, '')
  AND a.tax_code               = COALESCE(b.tax_code, '')
  AND a.payment_terms          = COALESCE(b.payment_terms, '')
WHERE b.row_id BETWEEN %s AND %s
ON CONFLICT (company_code_key, accounting_document_no, fiscal_year, line_item_no) DO NOTHING;
"""

SQL_INDEX_TMP_LINE_ITEM = """
CREATE INDEX ix_tmp_line_item_row_id ON tmp_line_item (row_id);
ANALYZE tmp_line_item;
"""


def build_upsert_sql(target, columns, conflict):
    sql = "INSERT INTO {} ({}) VALUES %s".format(target, ", ".join(columns))
    update_cols = [c for c in columns if c not in conflict]
    if update_cols:
        assignments = ", ".join("{0} = EXCLUDED.{0}".format(c) for c in update_cols)
        sql += " ON CONFLICT ({}) DO UPDATE SET {}".format(", ".join(conflict), assignments)
    else:
        sql += " ON CONFLICT ({}) DO NOTHING".format(", ".join(conflict))
    return sql


def copy_rows(src_conn, tgt_cur, cursor_name, extract_sql, insert_sql):
    src_cur = src_conn.cursor(name=cursor_name)
    src_cur.itersize = BATCH_SIZE
    try:
        src_cur.execute(extract_sql)
        while True:
            rows = src_cur.fetchmany(BATCH_SIZE)
            if not rows:
                break
            execute_values(tgt_cur, insert_sql, rows, page_size=BATCH_SIZE)
    finally:
        src_cur.close()


def load_fact(tgt_cur):
    tgt_cur.execute("SELECT MIN(row_id), MAX(row_id), COUNT(*) FROM tmp_line_item")
    min_id, max_id, total = tgt_cur.fetchone()
    if not total:
        return

    chunk_start = min_id
    while chunk_start <= max_id:
        chunk_end = chunk_start + FACT_CHUNK_SIZE - 1
        tgt_cur.execute(SQL_LOAD_FACT, (chunk_start, chunk_end))
        chunk_start = chunk_end + 1


def main():
    src_conn = psycopg2.connect(**SOURCE_DB)
    tgt_conn = psycopg2.connect(**TARGET_DB)
    src_conn.set_session(readonly=True)

    try:
        with tgt_conn.cursor() as tgt_cur:
            tgt_cur.execute(SQL_SAFE_DATE_FUNCTION)

            for job in DIMENSION_JOBS:
                insert_sql = build_upsert_sql(job["target"], job["columns"], job["conflict"])
                copy_rows(src_conn, tgt_cur, "cur_" + job["name"],
                          job["extract"], insert_sql)

            tgt_cur.execute(SQL_CREATE_TMP_LINE_ITEM)
            line_insert_sql = "INSERT INTO tmp_line_item ({}) VALUES %s".format(
                ", ".join(LINE_ITEM_COLUMNS))
            copy_rows(src_conn, tgt_cur, "cur_line_items",
                      SQL_EXTRACT_LINE_ITEMS, line_insert_sql)
            tgt_cur.execute(SQL_INDEX_TMP_LINE_ITEM)

            tgt_cur.execute(SQL_DATE_RANGE)
            min_date, max_date = tgt_cur.fetchone()
            if min_date is not None:
                tgt_cur.execute(SQL_LOAD_DIM_DATE, (min_date, max_date))

            tgt_cur.execute(SQL_LOAD_DIM_LINE_ITEM_ATTRIBUTE)

            tgt_cur.execute(SQL_TRUNCATE_FACT)
            load_fact(tgt_cur)

        tgt_conn.commit()
    except Exception:
        tgt_conn.rollback()
        raise
    finally:
        src_conn.close()
        tgt_conn.close()


if __name__ == "__main__":
    main()
