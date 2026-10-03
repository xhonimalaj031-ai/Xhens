import os
import time
import requests

# ==========================================
# XHENS TRADING BOT
# ==========================================

SYMBOL = "BTC/USD"
INTERVAL = 30


def get_price():
    url = "https://api.kraken.com/0/public/Ticker"
    params = {"pair": "XBTUSD"}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if data.get("error"):
        raise Exception(data["error"])

    result = data["result"]
    pair = list(result.keys())[0]

    return float(result[pair]["c"][0])


def main():
    print("================================")
    print("       XHENS TRADING BOT")
    print("================================")
    print("Bot started...")
    print("Mode: TEST")
    print("Symbol:", SYMBOL)
    print("--------------------------------")

    while True:
        try:
            price = get_price()
            print(f"BTC/USD price: ${price:,.2f}")

        except Exception as e:
            print("Error:", e)

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
