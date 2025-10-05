# Fetch BTC price from CoinGecko API

import requests

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data["bitcoin"]["usd"]

if __name__ == "__main__":
    print(f"Current BTC price: ${get_btc_price()}")
