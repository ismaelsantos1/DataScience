'''import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()
'''
print("Aberta a eleição para a gerência")
print('Os números dos candidatos são\nCandidato 1: 1\nCandidato 2: 2\nCandidato 3: 3\n Candidato 4: 4\n Voto Nulo: 5\n')

c = int(input('Insira o número do seu candidato: '))
cand1=0
cand2=0
cand3=0
cand4=0
nulo=0
while c !=5:
    if (c>0) and (c<=5):
        
        if c == 1:
            cand1+=1
        
        elif c==2:
            cand2+=1
        
        elif c==3:
            cand3+=1
            
        elif c==4:
            cand4+=1
        
        elif c == 5:
            nulo+=1
        else:
            print("Valor inválido. Candidato não encontrado no sistema")
    else:
        print('Digite um valor válido')
        
for c in range (20):
    if (cand1 > cand2) and (cand1>cand3) and (cand1>cand4) :
        print("Candidato nº1 venceu")
    
    elif (cand2 > cand1) and (cand2>cand3) and (cand2>cand4) :
        print("Candidato nº2 venceu")

    elif (cand3 > cand1) and (cand3>cand2) and (cand3>cand4) :
        print("Candidato nº3 venceu")
    
    elif (cand4 > cand1) and (cand4>cand2) and (cand4>cand3) :
        print("Candidato nº4 venceu")
    else:
        print("Não houve vencedor, ou todos os votos foram nulos.")
