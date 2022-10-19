from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
import sys
from src.variables.variables import variables

def getReviewsIndeed(nome_empresa):
    url = f"https://br.indeed.com/cmp/{nome_empresa}/reviews?fcountry=ALL&lang=pt"
    div_review = "div[data-tn-entitytype=reviewId]"
    titulo="div h2[data-testid=title] >> text"
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
                "title": titulo
              }
            ]
          }
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(api_url, data=json.dumps(payload), headers=headers)
    result = json.loads(response.text)
    f = open("test.out", 'w')
    sys.stdout = f
    print(str(result))
    f.close()
    return result['result']

