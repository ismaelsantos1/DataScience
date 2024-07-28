#url = "https://www.bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"


#url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
url= "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
#print(url)


#print(url[0:31]) #b-1, a ? é excluída do print

#url_parametros = url[32:48]
#print(url_parametros)

#Separa base e os paramêtros

indiceInterrogacao = url.find("?")
urlBase = url[:indiceInterrogacao]
urlParametros = url[indiceInterrogacao+1:]
print(urlParametros)


#Busca valor de um parâmetro

parametroBusca = 'quantidade'
indiceParametro = urlParametros.find(parametroBusca)
indiceValor = indiceParametro + len(parametroBusca) + 1
indiceEcomercial = urlParametros.find('&', indiceValor)
valor = urlParametros[indiceValor:] #vai até o final

if indiceEcomercial == -1:
    valor = urlParametros[indiceValor:]
else:
    valor = urlParametros[indiceValor:indiceEcomercial]

print(valor)


#Múltiplos Parâmetros

"""
O método .find() pode receber string como parâmetro e o console retornará a posição inicial de onde essa string se encontra.
EX: 
url = "https://www.bytebank.com/cambio?moedaOrigem=real&moedaOrigem"
indiceInterrogacao = url.find("bytebank")
print(indiceInterrogacao)

-> 12 (saída no terminal)
"""


"""
Fatiamento => é a divisão de caracteres dentro de uma string. Isso ocorre por meio do índice do conteúdo. Veja:

texto = "abcde"
texto[0] -> 'a'
texto[0:2] -> inicia na posição 0 e termina na posição 1
print(texto[0:2])
"""
