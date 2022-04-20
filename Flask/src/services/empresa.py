from src.exceptions.request_error import RequestError
from src.utils.jwt_util import jwt_util
from src.utils.twitter import searchReviewsTwitter
from src.utils.glassdoor import getReviewsGlassdoor
import asyncio

class EmpresaService:
    def getEmpresaByName(self, nome_empresa):
        #reviews_glassdoor = getReviewsGlassdoor(nome_empresa)
        reviews_twitter = searchReviewsTwitter(nome_empresa)
        reviews_glassdoor = {
"reviews": [
{
"author_info": "2 de mar. de 2022 - Engenheiro",
"cons": "Precisa melhorar a questão de desenvolvimento de carreira.",
"helpful": "Seja a primeira pessoa a indicar esta avaliação como útil",
"pros": "A Embraer é uma empresa que te ensina muita coisa e possui pessoas muito capacitadas.",
"rating": "5,0",
"title": "Ótima empresa"
},
{
"author_info": "18 de abr. de 2022 - Projetista Sênior em Araraquara",
"cons": "Bairrista, não dá feedback, valoriza discurso, direcionada para jovens, lideres sem experiência.",
"helpful": "Seja a primeira pessoa a indicar esta avaliação como útil",
"pros": "Alta tecnologia, desafiadora, vc pode ver o resultado, conhece outros países, pode acessar superiores",
"rating": "5,0",
"title": "Trabalho gratificante"
},
{
"author_info": "18 de abr. de 2022 - Engenheiro De Vendas em São José dos Campos, São Paulo",
"cons": "Salário defasado, muitas horas semanais, modelo híbrido.",
"helpful": "Seja a primeira pessoa a indicar esta avaliação como útil",
"pros": "Clima de cooperação, benefícios, trabalhar com pessoas fantásticas.",
"rating": "5,0",
"title": "-"
},
{
"author_info": "18 de abr. de 2022 - Engenheiro De Suporte Ao Cliente em São José dos Campos, São Paulo",
"cons": "Grande inercia pra mudanças, progressão de carreira não tão rápida",
"helpful": "Seja a primeira pessoa a indicar esta avaliação como útil",
"pros": "Ambiente de trabalho, flexibilidade, benefícios, crescimento pessoal",
"rating": "5,0",
"title": "Ótima empresa"
},
{
"author_info": "17 de abr. de 2022 - Engenheiro De Desenvolvimento Do Produto em São José dos Campos, São Paulo",
"cons": "Plano de careira não é satisfatório.",
"helpful": "Seja a primeira pessoa a indicar esta avaliação como útil",
"pros": "Ambiente criativo, amigável. Acesso ao estado da arte em tecnologia. Aprendizado contínuo.",
"rating": "4,0",
"title": "Avaliação Embraer"
},
{
"author_info": "13 de abr. de 2022 - ESTÁGIO",
"cons": "nada, nenhum, poucos ,leves, contras",
"helpful": "Seja a primeira pessoa a indicar esta avaliação como útil",
"pros": "bom, legal, interessante, brabo, lindo",
"rating": "5,0",
"title": "Bom"
},
{
"author_info": "13 de abr. de 2022 - Product Development Engineer",
"cons": "Muita burocracia, demora em mudar de módulo e muitas normas",
"helpful": "Seja a primeira pessoa a indicar esta avaliação como útil",
"pros": "Empresa com treinamentos, home office e boas oportunidades em projetos",
"rating": "4,0",
"title": "Boa empresa com boas oportunidades"
},
{
"author_info": "12 de abr. de 2022 - Recursos Humanos",
"cons": "Pontos de melhoria, empresa muito burocrática",
"helpful": "Seja a primeira pessoa a indicar esta avaliação como útil",
"pros": "Muito ponto, ambiente inspira criatividade",
"rating": "5,0",
"title": "Ambie ten Embraer"
},
{
"author_info": "12 de abr. de 2022 - Capitão em São Paulo, São Paulo",
"cons": "Nada a dizer muito bom",
"helpful": "Seja a primeira pessoa a indicar esta avaliação como útil",
"pros": "Lugar ótimo demais, você não vai se arrepender",
"rating": "5,0",
"title": "Muito bom"
},
{
"author_info": "11 de abr. de 2022 - Engenheiro De Desenvolvimento De Produto",
"cons": "O perfil de liderança varia muito.",
"helpful": "Seja a primeira pessoa a indicar esta avaliação como útil",
"pros": "Oportunidades para o crescimento profissional.",
"rating": "5,0",
"title": "Bom lugar para trabalhar!"
}
]
}
        """ IGNORAR, APENAS TESTANDO FUNÇÃO ASSINCRONA 
        reviews_twitter,reviews_glassdoor = await asyncio.gather(
            getReviewsGlassdoor(nome_empresa),
            getReviewsTwitter(nome_empresa)
        ) """
        #função_de_analise(reviews_twitter,reviews_glassdoor)
        pass

empresaService = EmpresaService()