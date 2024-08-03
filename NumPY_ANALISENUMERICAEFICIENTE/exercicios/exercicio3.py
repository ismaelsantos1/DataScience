"""
Chegou a hora de você testar os conhecimentos desenvolvidos durante a aula. Continuando com o projeto das laranjas/toranjas, agora
você deve calcular o coeficiente angular utilizando a geração de números aleatórios. Assuma que já conhece b e que este é igual a 17.
"""
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'
dado = np.loadtxt(url, delimiter= ',', usecols=np.arange(1,6,1),skiprows=1)

#pegando os dados das linhas
diametro_laranja = dado[:5000,0]
diametro_toranja = dado[5000:,0]
peso_laranja = dado[:5000,1]
peso_toranja = dado[5000:,1]

#Laranja
sl = np.size(diametro_laranja)
xl = diametro_laranja
yl = peso_laranja

#Toranja
st = np.size(diametro_toranja)
xt = diametro_toranja
yt = peso_toranja

#coeficiente angular
np.random.seed(16)
coef_angulares = np.random.uniform(low=1.00, high=5.00, size= 100)
laranja= np.array([])
toranja = np.array([])

b= 17

for i in range(100):

    laranja = np.append(laranja, np.linalg.norm(yl-(coef_angulares[i]*xl + b)))
    toranja = np.append(toranja, np.linalg.norm(yt-(coef_angulares[i]*xt + b)))

coef_angulares[laranja == np.min(laranja)]
coef_angulares[toranja == np.min(toranja)]

valorMinimoLaranja = np.min(laranja)
valorMinimoToranja = np.min(toranja)

print(laranja)
print(toranja)
print(valorMinimoToranja)
print(valorMinimoLaranja)
