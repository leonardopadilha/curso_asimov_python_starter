'''
### Exercício 3 
Nome na vertical em escada. 
F
FU
FUL
FULA
FULAN
FULANO
'''

def palavra_desejada(palavra):
  for i in range(len(palavra) + 1):
    print(palavra[:i])

palavra_desejada('fulano')