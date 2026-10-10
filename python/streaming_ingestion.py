
import time
import random
import uuid
import psycopg2
from datetime import datetime, timezone

# Connect to the existing EFDP database
conn = psycopg2.connect(
    host="localhost",
    database="efdp",
    user="postgres",
    password="postgres123",
    port="5432"
)

cursor = conn.cursor()

print("Financial streaming ingestion started...")

try:
    while True:
        # Simulate an incoming financial event
        transaction_ref = str(uuid.uuid4())[:12]
        account_id = f"ACC{random.randint(1000, 9999)}"
        transaction_type = random.choice(
            ["CREDIT", "DEBIT"]
        )
        amount = round(random.uniform(100, 50000), 2)
        event_timestamp = datetime.now(timezone.utc)

        # Insert the event into PostgreSQL
        cursor.execute("""
            INSERT INTO stream_financial_transactions
            (transaction_ref, account_id, transaction_type,
             amount, event_timestamp)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            transaction_ref,
            account_id,
            transaction_type,
            amount,
            event_timestamp
        ))

        conn.commit()

        print(
            f"Received: {transaction_ref} | "
            f"{transaction_type} | ₹{amount:.2f}"
        )

        # Wait before receiving the next event
        time.sleep(2)

except KeyboardInterrupt:
    print("\nStreaming stopped.")

finally:
    cursor.close()
    conn.close()
