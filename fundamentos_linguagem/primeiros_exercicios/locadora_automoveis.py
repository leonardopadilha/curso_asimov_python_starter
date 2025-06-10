import os

opcao_escolhida = int(input("""O que deseja fazer?
0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro
"""))

carros = [
    {"Nome": "Chevrolet Tracker", "Valor": 120},
    {"Nome": "Chevrolet Onix", "Valor": 90},
    {"Nome": "Chevrolet Spin", "Valor": 150},
    {"Nome": "Hyunday HB20", "Valor": 85},
    {"Nome": "Hyunday Tucson", "Valor": 120},
    {"Nome": "Fiat Uno", "Valor": 60},
    {"Nome": "Fiat Mobi", "Valor": 70},
    {"Nome": "Fiat Pulse", "Valor": 130},
]

if opcao_escolhida == 0:
  for indice, carro in enumerate(carros):
    print(f"{[indice]} {carro['Nome']} - R$ {carro['Valor']} /dia")

  opcao_escolhida = int(input("""\n 0 - Continuar | 1 - Sair """))
  if opcao_escolhida == 0:
    os.system('cls')

  print ("""==========
  Bem vindo à locadora de carros!
==========""")

  opcao_escolhida = int(input("""O que deseja fazer?
  0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro
  """))

  if opcao_escolhida == 1:
    print(f"[ ALUGAR ] Dê uma olhada em nosso portifólio. \n")
    for indice, carro in enumerate(carros):
      print(f"{[indice]} {carro['Nome']} - R$ {carro['Valor']} /dia")

  carro_escolhido = int(input("""\nEscolha o código do carro: """))
  dias_viagens = int(input("Escolha por quantos dias deseja alugar o carro: "))

os.system('cls')

confirma_aluguel_carro = int(input(f"""Você escolheu {carros[carro_escolhido]['Nome']} por {dias_viagens} dias 
O aluguel totalizará R$ {dias_viagens * carros[carro_escolhido]['Valor']}. Deseja alugar?
0 - SIM | 1 - Não \n"""))

if confirma_aluguel_carro == 0:
  print(f"Parabéns você alugou o {carros[carro_escolhido]['Nome']} por {dias_viagens} dias. \n")

menu_escolhido = int(input("""==========
0 - CONTINUAR | 1 - SAIR \n"""))

if menu_escolhido == 0:
  opcao_escolhida = int(input("""O que deseja fazer?
  0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro
  """))

  if opcao_escolhida == 0:
    for indice, carro in enumerate(carros):
      if indice == carro_escolhido:
        carros.pop(indice)
      print(f"{[indice]} {carro['Nome']} - R$ {carro['Valor']} /dia")


