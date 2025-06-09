from academia import Academia
from usuario import Usuario
import seaborn as sns
import random

academia = Academia()
usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia) for i in range(1)]
random.shuffle(usuarios)

list_chaos = []

for k in range(50):
  academia.reiniciar_o_dia()
  for i in range(10):
    random.shuffle(usuarios)

    for user in usuarios:
      user.iniciar_treino()
    for user in usuarios:
      user.finalizar_treino()
  list_chaos += [academia.calcular_caos()]
print(list_chaos)

sns.displot(list_chaos)

#print(academia.porta_halteres)
#print(academia.calcular_caos())