import json
import requests
BASE_PATH = 'https://api.apilayer.com/fixer/latest'


def get_rates(api_key):
    # send a requests for get crypto price
    response = requests.get(BASE_PATH, headers=api_key)
    if response.status_code == 200:
        return json.loads(response.text)
