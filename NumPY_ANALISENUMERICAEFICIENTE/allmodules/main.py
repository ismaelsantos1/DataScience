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

#print(moscow.shape)
#print(moscow[0:12])

moscow_ano1 = moscow[0:12]
moscow_ano2 = moscow[12:24]
moscow_ano3 = moscow[24:36]
moscow_ano4 = moscow[36:48]

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

#print(kaliningrad) #nan surge quando tenta dividir um número por 0 ou quando a tentativa ocorre com um número muito pequeno

#print(sum(np.isnan(kaliningrad))) #irá mostrar os locais onde tem nan

#print((kaliningrad[3]+kaliningrad[5])/2) #calcula a média dos valores dos respectivos indíces

#outra forma de calcular a média 
#print(np.mean([kaliningrad[3], kaliningrad[5]]))

kaliningrad[4] = np.mean([kaliningrad[3], kaliningrad[5]]) #substituio resultado na posicao 4

#plt.plot(datas, kaliningrad)
#plt.show()


#gerar um gráfico que compara o preço médio de moscow e kaliningrad

#print(np.mean(moscow))
#print(np.mean(kaliningrad))


#Operações com Arrays

#Ajustar uma reta para entender a taxa de crescimento do preço das maças

#y = mx + b y= preço das maças x = mes a= coe. angular b = coe. lineaar

#x = datas
#y = 2 * x + 80

#plt.plot(datas, moscow)
#plt.plot(x,y)
#plt.show()

#print(moscow-y) #y representa o valor da reta que foi calculado. O valor obtido a partir dessa subtração vai mostrar como a  reta se ajustou aos valores.
#O resultado gerado é negativo, pois a reta está acima dos valores de moscow, se ela estivesse abaixo dos valores, haveria valores +

#para lidar com o problema de valores positivos e negativos, todos podem ser elevados ao quadrado:
#print(np.power(moscow-y, 2)) #números muito grandes foram gerados. o ideal seria resumir a informação num único valor, isso pode ser feito somando todos os números para obter um único valor.

#print(np.sum(np.power(moscow-y, 2))) #pode ser retirado a raiz desse valor para poder deixaar o resultado dentro de um intervalo parecido com o preço das maças

#print(np.sqrt(np.sum(np.power(moscow-y, 2)))) #define a qualidade do ajuste

#para achar um ajuste melhor:

#Y=0.52 * x + 80

#plt.plot(datas, moscow)
#plt.plot(x,y)
#plt.show()
#print(np.sqrt(np.sum(np.power(moscow-y, 2)))) #o valor nunca vai ser muito próximo de 0

#np.linalg.norm resume todo o trabalho que tive para construir o gráfico
#print(np.linalg.norm(moscow-Y))

"""
a= coeficiente angular
n= nº de elementos
y = moscow
x = datas
"""

#regressão linear

#calculando a
y= moscow
x = datas
n = np.size(moscow) ; #print(n)

xQuadrado = np.power(x, 2).shape

a = (n*np.sum(x*y) - np.sum(x) * np.sum(y)) / (n*np.sum(x**2) - np.sum(x)**2)
#print(a)

#calculando b
b = np.mean(y) - a*np.mean(x)
#print(b)

y = a*x+b
#print(y)
#print(np.linalg.norm(moscow-y))


#Motivo da regressão

#plt.plot(datas, moscow)
#plt.plot(x,y)

#se utilizar a equação da reta com os valores calculado, é possível calular valores intermidiários para poder uma estimativa. Esses valores não foram carregados dentro do array de informações, veja:

#plt.plot(41.5, 41.5*a+b, '*r')#; plt.show() #41.5 é o que você quer; cáculo do Y = 41.5* a (já calculado) + b (já calculado); *r plota uma estrela vermelha

"""
O ponto vermelho foi encontrado dentro da fórmula da reta. Com os valores calculados, coefi. a e b é possível ter estimativas de valores para os próximos meses
"""
#plt.plot(100, 100*a+b, '*r'); plt.show()



# Utilizando valores aleatórios

#Valores em um intervalo

#print(np.random.randint(low=40, high=100, size= 100))
coef_angulares = np.random.uniform(low=0.10, high=0.90, size= 100)

#calculando o valor da norma. Testando os valores estimados
#norma= np.array([])
#for i in range(100):
    #vai calcular o valor de y para cada iteração para o loop
#    norma = np.append(norma, np.linalg.norm(moscow-(coef_angulares[i]*x + b)))
#print(norma)
    #np.append(norma, ...) vai armazenar dentro do array
#print(coef_angulares[1]) #0.811 


#Reprodutibilidade

#random.seed -> seleciona um número semente fixo para iniciar o gerador aleatório
np.random.seed(84)
coef_angulares = np.random.uniform(low=0.10, high=0.90, size= 100)
norma= np.array([])
for i in range(100):
    #vai calcular o valor de y para cada iteração para o loop
    norma = np.append(norma, np.linalg.norm(moscow-(coef_angulares[i]*x + b)))
print(norma)

#salvando os resultados
# função np.column_stack    une dois ou mais arrays, lado a lado, como colunas, numa matriz
dados = np.column_stack([norma, coef_angulares])
print(dados.shape)

#função savetxt -> salva um array em arquivo .txt
np.savetxt('dados.csv', dados, delimiter= ',')