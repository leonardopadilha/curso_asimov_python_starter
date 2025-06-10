import os

while True: 
  print(''' Calculadora
  Escolha uma das opções abaixo:
        1 para somar;
        2 para subtrair;
        3 para multiplicar
        4 para dividir
        5 para sair
  ''')

  opcao_desejada = input()

  soma = []
  divisao = []
  subtracao = []
  multiplicacao = []

  if opcao_desejada == '1':
    for i in range(1,3):
      soma.append(int(input(f"Informe o {i}º numero: ")))
    print(f"O resultado da soma é {soma[0] + soma[1]}")

  if opcao_desejada == '2':
    for i in range(1,3):
      subtracao.append(int(input(f"Informe o {i}º numero: ")))
    print(f"O resultado da subtração é {subtracao[0] - subtracao[1]}")

  if opcao_desejada == '3':
    for i in range(1,3):
      multiplicacao.append(int(input(f"Informe o {i}º numero: ")))
    print(f"O resultado da multiplicação é {multiplicacao[0] * multiplicacao[1]}")

  if opcao_desejada == '4':
    for i in range(1,3):
      divisao.append(int(input(f"Informe o {i}º numero: ")))
    print(f"O resultado da divisão é {int(divisao[0] / divisao[1])}")

  if opcao_desejada == '5':
    print('Até logo!!')
    break

  opcao_desejada = input("Deseja realizar um novo cálculo? sim ou nao: ")
  if opcao_desejada == 'nao':
    print("Fim!!")
    break
  else:
    os.system('cls')
    continue
  
      





