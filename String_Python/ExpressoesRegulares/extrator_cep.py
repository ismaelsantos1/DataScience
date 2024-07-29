"""
Expressões Regulares
"""

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras. Rio De Janeiro, RJ, 23440-120"

import re #Regular Expression -- RegEx
 
 # cep no brasil tem 5 dígitos + hífen (opcional) + 3 dígitos

#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]")#passa um padrão

#busca = padrao.search(endereco) #match, encontrou um padrão ou None

#if busca:
#    cep = busca.group()#retorna a substring que está de acordo com o padrão
#    print(cep)


"""
Vai sempre seguir esse padrão
"""

"""
Pode ser usado quantificadores para repetir esse padrao sem a necessidade de ficar duplicando esses grupos
"""

padrao = re.compile("[0-9]{5}[-][0-9]{3}")
#pode ser nos quantificadores {0,1}, assim ele delimita que pode aparecer de até uma vez



busca = padrao.search(endereco) #match, encontrou um padrão ou None

if busca:
    cep = busca.group()#retorna a substring que está de acordo com o padrão
    print(cep)
