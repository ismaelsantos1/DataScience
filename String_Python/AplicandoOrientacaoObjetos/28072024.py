#Validando URL


#url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

url = "      "

#Sanitizando a URL

# antes de validar

#url = url.replace(" ", "") #substitui o espaço em branco por vazio

url = url.strip() #retira todos os espaços em brancos dentro de uma string, tira também caracteres especiais

#Validando URL

if url == "": #url vazia retorna 0
    
    raise ValueError ('URL vazia')

elif url == " ": #url com espaço em branco retorna 1
    
    raise ValueError ('URL vazia')



#Separa base e parâmetros

indiceInterrogacao = url.find("?")
urlBase = url[:indiceInterrogacao]
urlParametros = url[indiceInterrogacao+1:]
print(urlParametros)

#Busca o valor de um parâmetro

parametroBusca = 'quantidade'
indiceParametro = urlParametros.find(parametroBusca)
indiceValor = indiceParametro + len(parametroBusca) + 1
indiceEComercial = urlParametros.find('&', indiceValor)
if indiceEComercial == -1: 
    valor = urlParametros[indiceValor:]
else:
    valor = urlParametros[indiceValor:indiceEComercial]
print(valor)