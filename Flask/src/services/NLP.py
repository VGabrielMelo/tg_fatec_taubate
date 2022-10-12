from matplotlib.font_manager import json_load
from src.variables.variables import variables
import pandas as pd
import numpy as np
import nltk
nltk.download('stopwords')
nltk.download('rslp')
stopwords=nltk.corpus.stopwords.words('portuguese')
#import utils.Trata_Dados as TD

class NlpService():

    def TreinoBase():
        return nltk.NaiveBayesClassifier.train(NlpService.Base()) 

    def __init__(self):
        self.frasescomstemming = NlpService.fazstemmer(NlpService.base_tupla())
        self.todaspalavras = NlpService.buscapalavras(self.frasescomstemming)
        self.frequencia =  NlpService.buscafrequencia(self.todaspalavras)
        self.palavrasunicas = NlpService.busca_palavrasunicas(self.frequencia)
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


    def base_tupla():
        df = pd.read_json(variables.caminhoNlp)
        df = df[['title','avaliacao']]
        df['avaliacao'] = df['avaliacao'].map({0:'Negativo',1:'Neutro',2:'Positivo', np.nan:'Indefinido'}, na_action=None)
        base = [tuple(x) for x in df.to_numpy()]
        return base

    def Base():
        base = NlpService.base_tupla()

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
        if (type(ListaComentários) is not list):
            print(type(ListaComentários))
            ListaComentários_json = json_load(ListaComentários)
            df = pd.read_json(ListaComentários_json)
        else:
            df = pd.DataFrame(ListaComentários)
        
        def extrai_palavras(documento):
            doc = set(documento)
            caracteristicas = {}
            for palavras in self.palavrasunicas:
                caracteristicas['%s' % palavras] = (palavras in doc)
            return caracteristicas

        df = df[['title']]
        frases_Novas = df.values.tolist()
        stemmer = nltk.stem.RSLPStemmer()
        frase_resultado =[]
        cont = 0
        for i in frases_Novas:
            frase = frases_Novas[cont][0]
            frase_i = []
            for (palavras) in frase.split():
                comstem = [p for p in palavras.split()]
                frase_i.append(str(stemmer.stem(comstem[0])))
            frase_resultado.append(frase_i)
            cont = cont + 1

        resultado =[]
        id = 0
        for i in frase_resultado:
            nova_frase = extrai_palavras(i)
            distribuicao = self.classificador.prob_classify(nova_frase).max()
            resultado.append(distribuicao)
            response = {
                'total':len(resultado),
                'positivo': resultado.count('Positivo'),
                'negativo': resultado.count('Negativo'),
                'neutro': resultado.count('Neutro')
            }
            #for classe in distribuicao.samples():
                #if float(distribuicao.prob(classe)) > 0.50000:
                    #resultado.append([classe, distribuicao.prob(classe), id])
            id = id + 1


        return response

    def ResumoBusca(self, NomeProcura):
        #Aqui vamos utilizar os Transformes para a criação de um resumo
        NomeProcura

nlp = NlpService()