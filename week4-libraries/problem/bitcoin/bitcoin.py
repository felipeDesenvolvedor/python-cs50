import os
from dotenv import load_dotenv
import sys
import requests

load_dotenv()

YourApiKey = os.getenv("YourApiKey")
baseApi = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={YourApiKey}"

def main():
    print(get_number())

def get_number():
    
    try:
        if len(sys.argv) != 2:
            raise ValueError("Missing command-line argument")

        return fetch_bitcoin_cost(convert_to_float(sys.argv[1]))
    except ValueError as e:
        sys.exit(e)

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("Command-line argument is not a number")


def fetch_bitcoin_cost(numberBitcoin):
    try:
        priceBitcointUSD = float(fetch_bitcoin_price())
        totalCost = numberBitcoin * priceBitcointUSD
        return f"${totalCost:,.4f}"
    except Exception as e:
        sys.exit(e)

def fetch_bitcoin_price():
    try:
        response = requests.get(baseApi)
        return response.json()['data']['priceUsd']
    except requests.RequestException as e:
        sys.exit("Error fetching Bitcoin price:", e)

if __name__ == "__main__":
    main()