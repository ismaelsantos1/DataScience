"""
Chegou a hora de você testar os conhecimentos desenvolvidos durante a aula. Continuando com o projeto das laranjas/toranjas agora 
você deve selecionar parte dos dados. As colunas que iremos avaliar são as de diâmetro e peso. Crie arrays específicos para guardar 
o diâmetro e peso da laranja e toranja. O diâmetro está na coluna zero e o peso na coluna 1. Os dados referentes a laranja vão até a 
linha 4999 e os referentes à toranja iniciam na linha 5000 do arquivo.


Após fazer a seleção de dados, importe a biblioteca matplotlib e crie um gráfico para a laranja e para a toranja do peso pelo 
diâmetro.

"""

#O diâmetro está na coluna zero e o peso na coluna 1
#laranja e toranja
#Os dados referentes a laranja vão até a linha 4999 e os referentes à toranja iniciam na linha 5000 do arquivo.
#Crie arrays específicos para guardar o diâmetro e peso da laranja e toranja.
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'
dado = np.loadtxt(url, delimiter= ',', usecols=np.arange(1,6,1),skiprows=1)

#pegando os dados das linhas
diametro_laranja = dado[:5000,0]
diametro_toranja = dado[5000:,0]
peso_laranja = dado[:5000,1]
peso_toranja = dado[5000:,1]

#criando arrays para guardar diâmetro e peso de cada um
array_laranja = np.array([diametro_laranja, peso_laranja]).T#linha para coluna
array_toranja = np.array([diametro_toranja, peso_toranja]).T#linha para coluna
#print(array_laranja)
#print(array_toranja)

visu = np.column_stack([array_laranja, array_toranja])
print(visu)

#salvando o array em arquivo .txt
np.savetxt('exercicio.csv', visu, delimiter= ',')

plt.plot(diametro_laranja, peso_laranja)
plt.plot(diametro_toranja, peso_toranja)
plt.legend(['laranja', 'toranja'])
plt.show()
