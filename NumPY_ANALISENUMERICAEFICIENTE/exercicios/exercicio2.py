"""
Chegou a hora de você testar os conhecimentos desenvolvidos durante a aula. Continuando com o projeto das laranjas/toranjas agora
você deve calcular o coeficiente ângular e o linear para a reta da laranja e para a reta da toranja. Use a fórmula de mínimos 
quadrados para encontrar cada um.
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
coef_Angular_Laranja = (sl*np.sum(xl*yl) - np.sum(xl) * np.sum(yl)) / (sl*np.sum(xl**2) - np.sum(xl)**2)
coef_Angular_Toranja = (st*np.sum(xt*yt) - np.sum(xt) * np.sum(yt)) / (st*np.sum(xt**2) - np.sum(xt)**2)


#coeficiente linear
coef_Lin_Laranja = np.mean(yl) - coef_Angular_Laranja * np.mean(xl)
coef_Lin_Toranja = np.mean(yt) - coef_Angular_Toranja * np.mean(xt)

#calculando a norma
yLaranja = np.linalg.norm(yl-(coef_Angular_Laranja*xl + coef_Lin_Laranja))
yToranja = np.linalg.norm(yt-(coef_Angular_Toranja*xt + coef_Lin_Toranja))
print(yLaranja)
print(yToranja)

#plotando as retas:
y_laranja = coef_Angular_Laranja * xl + coef_Lin_Laranja
plt.plot(xl, y_laranja, label='Regressão Laranja', color='orange')
y_toranja = coef_Angular_Toranja * xt + coef_Lin_Toranja
plt.plot(xt, y_toranja, label='Regressão Toranja', color='green')


plt.scatter(xt, yt, label='Toranja')
plt.scatter(xl, yl, label='Laranja') #cria um gráfico de dispersão
plt.legend()
plt.show()