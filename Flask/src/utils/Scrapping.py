from pickle import UNICODE
import bs4 as bs
import urllib.request
import re
def scrapped(self,Empresa):
    Empresa = str('Cartão_private_label')
    scraped_data = urllib.request.urlopen(f'https://pt.wikipedia.org/wiki/{Empresa}')
    article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')
paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text

# Removendo sujeiras
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)