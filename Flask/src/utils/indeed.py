from bs4 import BeautifulSoup
import pandas as pd
import requests
import json

from src.variables.variables import variables

def getReviewsIndeed(nome_empresa):
    url = f"https://br.indeed.com/cmp/{nome_empresa}/reviews?fcountry=ALL&lang=pt"
    #url = f"https://br.indeed.com/cmp/{nome_empresa}/reviews?fcountry=ALL&sort=rating_asc&lang=pt"

    div_review = "div.css-5cqmw8"
    titulo="a[data-testid=titleLink] >> text"
    rating="button.css-1c33izo >> text"
    autor = "span[itemprop=author] >> text"
    review = "span[itemprop=reviewBody] >> text "
    api_url = 'https://www.page2api.com/api/v1/scrape'
    page2api_api_key=variables.page2api_api_key
    payload = {
          "api_key": page2api_api_key,
          "url": url,
          "merge_loops": True,
          "real_browser": True,
          "scenario": [
            {
              "loop": [
                { "wait_for": div_review },
                { "execute": "parse" },
                { "execute_js": "var next = document.querySelector(\"a[data-tn-element=next-page]\"); if(next) { next.click() }" }
              ],
              "stop_condition": "document.querySelector(\"a[data-tn-element=next-page]\") == null"
            }
          ],
          "parse": {
            "reviews": [
              {
                "_parent": div_review,
                "title": titulo,
                "rating": rating,
                "autor":autor,
                "review":review
              }
            ]
          }
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(api_url, data=json.dumps(payload), headers=headers)
    result = json.loads(response.text)
    return result['result']

