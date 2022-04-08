import requests
import json
from src.variables.variables import variables

def getReviews(nome_empresa):
       
    procura = requests.get(f"https://www.glassdoor.com.br/searchsuggest/typeahead?source=Review&version=New&rf=full&input={nome_empresa}").json()
    employer_id=procura[0]['employerId']
    api_url = 'https://www.page2api.com/api/v1/scrape'
    page2api_api_key=variables.page2api_api_key
    payload = {
      "api_key": page2api_api_key,
      "url": f"https://www.glassdoor.com/Reviews/{nome_empresa}-Reviews-E{employer_id}.htm",
      "real_browser": True,
      "merge_loops": True,
      "premium_proxy": "us",
      "scenario": [
        {
          "loop": [
            { "wait_for": "div.gdReview" },
            { "execute": "parse" },
            { "execute_js": "document.querySelector(\".nextButton\").click()" }
          ],
          "iterations": 2
        }
      ],
      "parse": {
        "reviews": [
          {
            "_parent": "div.gdReview",
            "title": "a.reviewLink >> text",
            "author_info": ".authorInfo >> text",
            "rating": "span.ratingNumber >> text",
            "pros": "span[data-test=pros] >> text",
            "cons": "span[data-test=cons] >> text",
            "helpful": "div.common__EiReviewDetailsStyle__socialHelpfulcontainer >> text"
          }
        ]
      }
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(api_url, data=json.dumps(payload), headers=headers)
    result = json.loads(response.text)
    return result['result']