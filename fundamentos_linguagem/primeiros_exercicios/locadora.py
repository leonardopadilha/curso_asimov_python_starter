import os

carros = [
  ("Chevrolet Tracker", 120),
  ("Chevrolet Onix", 90),
  ("Chevrolet Spin", 150),
  ("Chevrolet HB20", 85),
  ("Hyunday Tucson", 120),
  ("Fiat Uno", 60),
  ("Fiat Mobi", 70),
  ("Fiat Pulse", 130)
]

alugados = []


print("""======
Bem Vindo à locadora de carros!
======""")

def mostrar_lista_de_carros(lista_de_carros):
  for i, car in enumerate(lista_de_carros):
    print(f"{[i]} {car[0]} - R$ {car[1]} / dia")


while True:
  os.system('cls')
  print("=======")
  print("Bem vindo à locadora de carros!")
  print("=======")
  print("0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro")
  op = int(input())

  os.system('cls')
  if op == 0:
    mostrar_lista_de_carros(carros)
  elif op == 1:
    mostrar_lista_de_carros(carros)
    print("=======")
    codigo_carro = int(input("Escolha o código do carro: "))
    aluguel_em_dias = int(input("Por quantos dias você deseja alugar este carro? "))
    os.system('cls')

    print(f"Você escolheu o {carros[codigo_carro][0]} por {aluguel_em_dias} dias")
    print(f"O aluguel totalizará R$ {aluguel_em_dias * carros[codigo_carro][1]}. Deseja alugar? ")

    conf = int(input("0 - SIM | 1 - NÃO "))
    if conf == 0:
      print(f"Parabéns você alugou o {carros[codigo_carro][0]} por {aluguel_em_dias} dias.")
      alugados.append(carros.pop(codigo_carro))
  elif op == 2:
    if len(alugados) == 0:
      print("Não há carros para devolver")
    else:
      print("Segue a lista de carros alugados. Qual você deseja devolver? ")
      mostrar_lista_de_carros(alugados)
      print("")
      cod_carro_devolvido = int(input("Escolha o código do carro que deseja devolver: "))
      if cod_carro_devolvido == 0:
        print(f"Obrigado por devolver o carro {alugados[cod_carro_devolvido][0]}")
        carros.append(alugados.pop(cod_carro_devolvido))

  print("")
  print("=======")
  print("Digite 0 para continuar ou 1 para sair")
  if int(input()) == 1:
    break
