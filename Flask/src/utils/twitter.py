from src.variables.variables import variables
import requests
import json

bearer_token = variables.twitter_bearer_token

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def searchReviewsTwitter(nome_empresa: str):
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {'query': f'({nome_empresa} -is:retweet lang:pt) ','tweet.fields': 'author_id','tweet.fields':'text','tweet.fields':'referenced_tweets','max_results':100,'sort_order':'relevancy'}
    json_response = connect_to_endpoint(search_url, query_params)
    response = []
    for t in json_response['data']:
        response.append({"review":t['text'],"autor":t['id']})
    return response


