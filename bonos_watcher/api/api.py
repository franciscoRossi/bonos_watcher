import json
import requests


class Api:

    def __init__(self):
        pass

    @staticmethod
    def get_prices():
        authorized_client = ''
        client_key = ''
        api_url = "https://api.portfoliopersonal.com/api/Cotizaciones/WatchList/12967?plazoId=3"

        headers = {'Content-Type': 'application/json',
                   'authorizedclient': authorized_client, 'clientkey': client_key}

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None