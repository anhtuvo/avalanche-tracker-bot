import os
import requests
from dotenv import load_dotenv
from src.tokens import get_main_token_price
load_dotenv()

API_KEY = os.getenv("SNOWTRACE_API_KEY")
ENDPOINT = os.getenv("SNOWTRACE_API_ENDPOINT")

def gas_format(gas_price):
    gas_in_usd = gas_price * 0.001
    
    return '{:.2f}'.format(gas_price) + ' nAVAX (GWei): $' + '{:.6f}'.format(gas_in_usd)

def get_gas_price():
    url = ENDPOINT + '?module=proxy&action=eth_gasPrice&apikey=' + API_KEY
    response = requests.get(url)

    decimal_wei = int(response.json()['result'], 16)
    gas_price = decimal_wei / 1000000000

    return gas_price


def gas_command():
    gas_price = get_gas_price()
    avax_price = get_main_token_price()

    slowest_gas_price = gas_format(gas_price)
    average_gas_price = gas_format(gas_price * 1.01)
    fastest_gas_price = gas_format(gas_price * 1.02)

    return f'AVAX price: ${avax_price}\n\nFast: {fastest_gas_price}\nNormal: {average_gas_price}\nSlow: {slowest_gas_price}\n\nPowered by Avalanche Tracker Bot'