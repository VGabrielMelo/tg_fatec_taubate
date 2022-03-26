import pandas as pd
import numpy as np
import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

class Trata_Dados:

    def hashtag(text):
        hash = re.findall(r"#(\w+)", text)
        return hash

    def remove_username(text):
        clean_text = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', text)
        return clean_text

    def remove_links_http(text):
        text = re.sub(r'http\S+','', text)
        text = re.sub(r'bit.ly/\S+','', text)
        text = text.strip('[link]')
        return text

    def remove_html_tag(text):
        clean_text = re.compile('<.*?>')
        return clean_text.sub(r'', text)
    
    def non_ascii(s):
        return "".join(i for i in s if ord(i)<128)

    def lower(text):
        return text.lower()

    def remove_stopwords(text):
        stopptbr = set(stopwords.words("portuguese"))
        clean_text = ' '.join([word for word in text.split() if word not in stopptbr])
        return clean_text

    def remove_email_address(text):
        email = re.compile(r'[\w\.-]+@[\w\.-]+')
        return email.sub(r'',text)
        
    def remove_punct(text):
        token=RegexpTokenizer(r'\w+')#regex
        text = token.tokenize(text)
        text= " ".join(text)
        return text