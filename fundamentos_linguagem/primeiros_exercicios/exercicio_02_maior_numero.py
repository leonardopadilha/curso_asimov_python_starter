'''
### Exercício 2
Escreva um script que leia três números e mostre o maior e o menor deles.
'''

def maior_numero(numeros):
  maior_numero = 0
  for i in range(len(numeros)):
    if numeros[i] > maior_numero:
      maior_numero = numeros[i]
    
  return maior_numero

maior_numero = maior_numero([9,4,7,11,10])
print(f'O maior número informado é {maior_numero}')