import os

os.system('cls')

print(os.getcwd())

# concatenando caminho de pastas
print(os.path.join(os.getcwd(), 'pasta_1'))
print(os.getcwd() + '/pasta_1')


# retorna apenas a última pasta contida no caminho informado
print(os.path.basename(os.getcwd()))
print(os.getcwd().split('\\'))
print(os.getcwd().split('\\')[-1])

print(os.path.split(os.getcwd()))
print(os.path.dirname(os.getcwd()))

# última alteração
curr_dir = os.getcwd()
lt = os.path.getmtime(curr_dir) # segundos

from datetime import datetime
print(datetime.utcfromtimestamp(lt)) # data

# perguntando se o dado passado é um arquivo ou diretório
print(os.path.isfile(curr_dir))
print(os.path.isdir(curr_dir))