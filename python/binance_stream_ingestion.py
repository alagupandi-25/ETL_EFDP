
import json
import time
from datetime import datetime, timezone

import psycopg2
import websocket

DB_CONFIG = {
    "host": "localhost",
    "database": "efdp",
    "user": "postgres",
    "password": "postgres123",
    "port": "5432",
}

WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"


def on_open(ws):
    print("Connected to Binance live trade stream.")


def on_message(ws, message):
    try:
        event = json.loads(message)

        trade_id = int(event["t"])
        symbol = event["s"]
        price = event["p"]
        quantity = event["q"]

        trade_time = datetime.fromtimestamp(
            event["T"] / 1000,
            tz=timezone.utc
        )

        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO api_market_trades
                    (trade_id, symbol, price, quantity, trade_time)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (trade_id) DO NOTHING
                """, (
                    trade_id,
                    symbol,
                    price,
                    quantity,
                    trade_time
                ))

        print(
            f"{symbol} | Price: {price} USDT | "
            f"Quantity: {quantity} | "
            f"Trade ID: {trade_id}"
        )

    except Exception as exc:
        print("Processing error:", exc)


def on_error(ws, error):
    print("WebSocket error:", error)


def on_close(ws, status_code, message):
    print("Connection closed:", status_code, message)


while True:
    try:
        ws = websocket.WebSocketApp(
            WS_URL,
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
        )

        ws.run_forever(ping_interval=20, ping_timeout=10)

    except Exception as exc:
        print("Connection error:", exc)

    print("Reconnecting in 5 seconds...")
    time.sleep(5)
