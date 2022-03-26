import pandas as pd
import numpy as np
import sys
import csv
import nltk
nltk.download('stopwords')
import utils.Trata_Dados as TD


class NlpService:
    
    #Realiza a coleta de dados via API
    def ColetaDados(self, NomeProcura):
        #Aqui vai as API e junção de dados em um Json.
        NomeProcura

    def TrataDados(Json):
        df = pd.read_json(Json)
        #Tratamento de dados
        df["NOMEDACOLUNA"] = df.NOMEDACOLUNHA.apply(TD.Trata_Dados.hashtag)
        df["NOMEDACOLUNA"] = df.NOMEDACOLUNHA.apply(TD.Trata_Dados.remove_links_http)
        df["NOMEDACOLUNA"] = df.NOMEDACOLUNHA.apply(TD.Trata_Dados.remove_username)
        df["NOMEDACOLUNA"] = df.NOMEDACOLUNHA.apply(TD.Trata_Dados.remove_html_tag)
        df["NOMEDACOLUNA"] = df.NOMEDACOLUNHA.apply(TD.Trata_Dados.non_ascii)
        df["NOMEDACOLUNA"] = df.NOMEDACOLUNHA.apply(TD.Trata_Dados.lower)
        df["NOMEDACOLUNA"] = df.NOMEDACOLUNHA.apply(TD.Trata_Dados.remove_stopwords)
        df["NOMEDACOLUNA"] = df.NOMEDACOLUNHA.apply(TD.Trata_Dados.remove_email_address)
        df["NOMEDACOLUNA"] = df.NOMEDACOLUNHA.apply(TD.Trata_Dados.remove_punct)

        result = df.to_json(orient="split")
        return result


    def AnaliseSentimento(self, ListaComentários):
        #Aqui vamos utilizar o Json retornado do tratamento de dados e analizar os sentimentos 1 por 1
        ListaComentários

    def ResumoBusca(self, NomeProcura):
        #Aqui vamos utilizar os Transformes para a criação de um resumo
        NomeProcura