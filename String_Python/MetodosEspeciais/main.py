#desafio do curso

import locale
class ExtratorURL:
    
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        """
        Vai receber uma url como paramêtro e sanitizar (tratar) ela, ou seja, tirar os espaços em branco
        """
        
        self.valida_url() #assim, toda vez que a classe for instanciada já vai acontecer alguma coisa. Isso serve para que o cliente (exemplo) usando o programa não precise chamar o valida_url diretamente, por essa razão ele está incluído no construtor 
    
    
    def sanitiza_url(self, url):
        return url.strip()
    """
    Trata a url e retorna ela sem os espaços em branco
    """
    
    def valida_url(self): #não recebe a url como parâmetro pois ele acessa o atributo da própria instância pra poder validar
        if self.url == "":
            raise ValueError("A URL não pode ser vazia")
        

    def get_url_base(self):
        indiceInterrogacao = self.url.find('?')
        urlBase = self.url[:indiceInterrogacao]
        return urlBase
        
    def get_url_parametros(self):
        indiceInterrogacao = self.url.find('?')
        urlParametros = self.url[indiceInterrogacao+1:] #self é um atributo da instância
        return urlParametros
        
    def get_valor_parametro(self, parametroBusca):
        
        indiceParametro = self.get_url_parametros().find(parametroBusca)
        indiceValor = indiceParametro + len(parametroBusca) + 1
        indiceEComercial = self.get_url_parametros().find('&', indiceValor)
        if indiceEComercial == -1: 
            valor = self.get_url_parametros()[indiceValor:]
        else:
            valor = self.get_url_parametros()[indiceValor:indiceEComercial]
        return valor
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: "+ self.get_url_base()
    
    def __eq__(self, other):
        return self.url == other.url
    
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)
VALOR_DOLAR = 5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "dolar" and moeda_destino == "real":
    conversao = int(quantidade) * VALOR_DOLAR
    print(f"O valor de U${quantidade}, em {moeda_destino} é R${conversao}")
elif moeda_origem == "real" and moeda_destino == "dolar":
    conversao = int(quantidade) / VALOR_DOLAR
    print(f"O valor de R${quantidade}, em {moeda_destino} é R${conversao}")
else:
    print("Não é possível realizar a conversão")