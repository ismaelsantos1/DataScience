import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'
#Há uma forma mais fácil que é apenas pegar um link do arquivo, um raw, e inserir numa variável string, veja

dado = np.loadtxt(url, delimiter= ',', usecols= np.arange(1,88))#o resultado gerado é o mesmo
#np.loadtxt('apples_ts.csv', delimiter= ',', usecols= np.arange(1,88))#foram 7 anos =>  7*12+3

#print(dado)


#print(dado.ndim) #ndim -> verifica a quantidade de dimensões na array
#print(dado.size)#verifica o tamanho
#print(dado.shape) #verifica o número de elementos em cada dimensão
#6 linhas e 87 colunas

"""
Para transformar linha em coluna você utiliza a transposição
"""
dado_transposto= dado.T
#print(dado_transposto)


#visuliazão e seleção 
#print(dado[0:10, 0:10]) #pega os 10 primeiros
datas = dado_transposto[:,0] #  : pega todo o intervalo de linhas no dataset, vai pegar as colunas do índice 0
precos = dado_transposto[:, 1:6] 

datas = np.arange(1,88,1)

#plt.plot(datas, precos[:, 0]) #x , y #primeira coluna está na coluna 0
#plt.show()

moscow = precos[:, 0]
kaliningrad = precos[:, 1]
peterbusg = precos[:,2]
krasnodar = precos[:,3]
ekaterinburg = precos[:,4]

print(moscow.shape)
print(moscow[0:12])

moscow_ano1 = moscow[0:12]
moscow_ano2 = moscow[13:25]
moscow_ano3 = moscow[25:37]
moscow_ano4 = moscow[37:49]

#plt.plot(np.arange(1,13,1), moscow_ano1)
#plt.plot(np.arange(1,13,1), moscow_ano2)
#plt.plot(np.arange(1,13,1), moscow_ano3)
#plt.plot(np.arange(1,13,1), moscow_ano4)
#plt.legend(['ano1', 'ano2', 'ano3', 'ano4'])#
#plt.show() #mostra a imagem gerada


#comparando precos das maças de anos diferentes

compara = np.array_equal(moscow_ano1, moscow_ano3)
#print(compara) #false


#funcao allclose verifica se arrays são próximos (dentro de um intervalo)
#print(np.allclose(moscow_ano1, moscow_ano3, 10)) #terceiro argumento é a distância entre eles, para verificar a distância se é verdadeira ou não

#plt.plot(datas, kaliningrad)
#plt.show()

print(kaliningrad) #nan surge quando tenta dividir um número por 0 ou quando a tentativa ocorre com um número muito pequeno

print(sum(np.isnan(kaliningrad))) #irá mostrar os locais onde tem nan

print((kaliningrad[3]+kaliningrad[5])/2) #calcula a média dos valores dos respectivos indíces

#outra forma de calcular a média 
print(np.mean([kaliningrad[3], kaliningrad[5]]))

kaliningrad[4] = np.mean([kaliningrad[3], kaliningrad[5]]) #substituio resultado na posicao 4

plt.plot(datas, kaliningrad)
plt.show()


#gerar um gráfico que compara o preço médio de moscow e kaliningrad

print(np.mean(moscow))
print(np.mean(kaliningrad))
