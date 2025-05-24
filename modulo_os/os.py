import os

#Alguns exemplos
# https://didatica.tech/explorando-a-biblioteca-os-em-python-com-exemplos/

# exibe o caminho do arquivo
print(os.getcwd())

# exibe uma lista com os arquivos e pastas no diretório onde estou
print(os.listdir())

# é possível passar um caminho para que seja exibido o que tem na pasta
caminho = 'C:\\Users\\user\\Desktop\OpenAI\\asimov\\automacao_python\\python_starter'
print(os.listdir(caminho))

# permite alterar o diretório
# os.chdir('informe_um_caminho')

# remove uma pasta
os.rmdir('pasta_2')

# permite criar uma nova pasta
os.mkdir('pasta_2')

# renomear um arquivo (nome_atual, novo_nome) -> também pode mudar o caminho dos arquivos
os.rename('teste.txt', 'teste_2.txt')

# remove um arquivo
os.remove('teste_2.txt')

# recriando o arquivo teste.txt
with open('teste.txt', 'x') as f:
  f.write('teste')

# simula comandos no terminal
cmd = 'date'
os.system(cmd)

