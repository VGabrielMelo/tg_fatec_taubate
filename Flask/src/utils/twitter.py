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
    return json_response
""" 
def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
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

def searchReviewsTwitter(nome_empresa: str):
    search_url = f"https://api.twitter.com/1.1/search/tweets.json?q={nome_empresa}&result_type=popular&-filter:link&count:100&include_entities=true"
    query_params = {'query': f'({nome_empresa})'}
    json_response = connect_to_endpoint(search_url, query_params)
    comentarios = []
    for comment in json_response['statuses']:
        comentario = getTweet(comment['id'])
        comentarios.append(comentario)
    return comentarios

def getTweet(id: int):
    search_url = f"https://api.twitter.com/1.1/statuses/show.json?id={id}"
    query_params = {'query': f'({id})'}
    return connect_to_endpoint(search_url, query_params) """
    

