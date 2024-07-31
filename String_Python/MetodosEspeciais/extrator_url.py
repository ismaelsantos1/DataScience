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
    
    #adicionado agora
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: "+ self.get_url_base() #cocatenando str
    
    def __eq__(self, other):#other seria o objeto a direita da comparação
        return self.url == other.url
    
url = ("bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url); print(extrator_url == extrator_url_2); print(id(extrator_url)); print(id(extrator_url_2))#adicionado no módulo 5 
#dois objetos podem ser iguais mas possuem identidades diferentes, logo, ainda que sobrescreva o eq dos objetos a id não é mesma, eles só são iguais por terem os mesmos atributos

#extrator_url is extrator_url funciona para saber se é do mesmo endereço de memória

print(extrator_url)
print('O tamanho da url: ', len(extrator_url))

valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

"""
__str__ (método)
esse método é chamado sempre que é usado o print() num objeto, ele imprime a classe do obj e o endereço de memória

__eq__

extrator_url.__eq__(extrator_url_2)
Ele compara os endereços de memória desses objetos

"""