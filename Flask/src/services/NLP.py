import pandas as pd
import numpy as np
import sys
import csv
import re
import nltk
stopwords=nltk.corpus.stopwords.words('portuguese')
#import utils.Trata_Dados as TD
from src.variables.variables import variables


class NlpService():

    def TreinoBase():
        #classificador = nltk.NaiveBayesClassifier.train(NlpService.Base())
        #return classificador
        print("Não deu ruim")
        return nltk.NaiveBayesClassifier.train(NlpService.Base()) 

    def __init__(self):
        self.classificador = NlpService.TreinoBase()

    def fazstemmer(frases):
            stemmer = nltk.stem.RSLPStemmer()
            frasessstemming = []
            for (palavras, emocao) in frases:
                comstemming = [str(stemmer.stem(p))
                                for p in palavras.split() if p not in stopwords]
                frasessstemming.append((comstemming, emocao))
            return frasessstemming

    def buscapalavras(frases):
            todaspalavras = []
            for (palavras, emocao) in frases:
                todaspalavras.extend(palavras)
            return todaspalavras

    def buscafrequencia(palavras):
            palavras = nltk.FreqDist(palavras)
            return palavras
    
    def busca_palavrasunicas(frequencia):
            freq = frequencia.keys()
            return freq

    def Base():
        df = pd.read_json(variables.caminhoNlp)
        df = df[['title','avaliacao']]
        df['avaliacao'] = df['avaliacao'].map({0:'Negativo',1:'Neutro',2:'Positivo', np.nan:'Indefinido'}, na_action=None)
        base = [tuple(x) for x in df.to_numpy()]

        frasescomstemming = NlpService.fazstemmer(base)

        todaspalavras = NlpService.buscapalavras(frasescomstemming)

        frequencia = NlpService.buscafrequencia(todaspalavras)

        palavrasunicas = NlpService.busca_palavrasunicas(frequencia)

        def extrai_palavras(documento):
            doc = set(documento)
            caracteristicas = {}
            for palavras in palavrasunicas:
                caracteristicas['%s' % palavras] = (palavras in doc)
            return caracteristicas

        basecompleta = nltk.classify.apply_features(extrai_palavras,frasescomstemming)
        return basecompleta

 


    def AnaliseSentimento(self, ListaComentários):
        print(type(ListaComentários))
        df = pd.read_json(ListaComentários)
        df = df[['title']]
        comentarios = [tuple(x) for x in df.to_numpy()]
        frasescomstemming = NlpService.fazstemmer(comentarios)
        todaspalavras = NlpService.buscapalavras(frasescomstemming)
        frequencia = NlpService.buscafrequencia(todaspalavras)
        palavrasunicas = NlpService.busca_palavrasunicas(frequencia)

        def extrai_palavras(documento):
            doc = set(documento)
            caracteristicas = {}
            for palavras in palavrasunicas:
                caracteristicas['%s' % palavras] = (palavras in doc)
            return caracteristicas
        
        #classificador = NlpService.TreinoBase()
        frases_Novas = df.values.tolist()
        stemmer = nltk.stem.RSLPStemmer()
        frase_resultado =[]
        for i in frases_Novas:
            frase= i
            frase_i = []
            for (palavras) in frase.split():
                comstem = [p for p in palavras.split()]
                frase_i.append(str(stemmer.stem(comstem[0])))
            frase_resultado.append(frase_i)

        resultado =[]
        for i in frase_resultado:
            nova_frase = extrai_palavras(i)
            distribuicao = self.classificador.prob_classify(nova_frase)
            for classe in distribuicao.samples():
                resultado.append([classe, distribuicao.prob(classe)])
        return resultado

    def ResumoBusca(self, NomeProcura):
        #Aqui vamos utilizar os Transformes para a criação de um resumo
        NomeProcura

