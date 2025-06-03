'''
### Exercício 4
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
(o próximo termo, a partir do terceiro, é sempre gerado a partir do somatório dos últimos dois). 
Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo 
usuário).
'''

def fibonacci(numero_maximo):
  primeiro_numero = 0
  proximo_numero = 1

  for i in range(numero_maximo):
    print(f"{proximo_numero} ", end="")
    proximo_numero, primeiro_numero = primeiro_numero + proximo_numero, proximo_numero

fibonacci(10)