import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("SNOWTRACE_API_KEY")
ENDPOINT = os.getenv("SNOWTRACE_API_ENDPOINT")

def get_main_token_price():
    url = ENDPOINT + '?module=stats&action=ethprice&apikey=' + API_KEY
    response = requests.get(url)
    
    main_token_price = response.json()['result']['ethusd']
    
    return main_token_price