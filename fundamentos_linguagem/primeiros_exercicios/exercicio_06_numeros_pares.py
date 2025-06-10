'''
### Exercício 6
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. 
Dica: Utilize o operador aritmético `%`, que retorna o resto da divisão de dois números.
'''

def numeros_primos(numero):
  numero_primo = 0
  if numero > 0:
    
    if numero != 2 and numero % 2 == 0:
      return f'O número {numero} não é primo pois é um número par'
    else:
      for i in range(1, numero + 1):
        if numero % i == 0:
          numero_primo += 1

    if numero_primo == 2:
      return f'O número {numero} é primo'
  return f'O número {numero} não é primo'


print(numeros_primos(9))
  