import requests
import json
from src.variables.variables import variables

bearer_token = variables.tweeter_bearer_token

def bearer_oauth(r):

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    try:
        response = requests.get(url, auth=bearer_oauth, params=params)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()
    except Exception as err:
        print(err)
def search(nome_empresa):
    search_url = f"https://api.twitter.com/1.1/search/tweets.json?q={nome_empresa}&result_type=popular&-filter:retweets&-filter:link&-filter:media&lang:en&count:100"
    query_params = {'query': f'({nome_empresa})'}
    json_response = connect_to_endpoint(search_url, query_params)
    comentarios = []
    for comment in json_response['statuses']:
        comentarios.append({'texto':comment['text']})
    return comentarios

