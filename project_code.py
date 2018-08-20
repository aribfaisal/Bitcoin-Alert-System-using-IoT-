import json
import time
import requests
from boltiot import Bolt

SELLING_PRICE = 1720.56
API_KEY = "XXXX"        # Replace with your API key
DEVICE_ID = "XXXXX"     # Replace with your Device ID

bolt = Bolt(API_KEY, DEVICE_ID)


def price_check():
    url = "https://min-api.cryptocompare.com/data/price"
    query_string = {"fsym":"BTC", "tsyms":"USD"}
    response = requests.request("GET", url, params=query_string)
    response = json.loads(response.text)
    current_price = response["USD"]
    return current_price


while True:
    market_price = price_check()
    print("Market price is :", market_price)
    print("Selling price is :", SELLING_PRICE)
    if market_price > SELLING_PRICE:
        bolt.digitalWrite("0", "HIGH")
        time.sleep(5)
        bolt.digitalWrite("0", "LOW")
        continue
    time.sleep(5)