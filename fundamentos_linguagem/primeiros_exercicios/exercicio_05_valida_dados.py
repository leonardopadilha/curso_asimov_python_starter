'''
### Exercício 5
Faça um programa que leia e valide as seguintes informações:
- Nome: maior que 3 caracteres;
- Idade: entre 0 e 150;
- Salário: maior que zero;
- Sexo: 'f' ou 'm';
- Estado Civil: 's', 'c', 'v', 'd';
'''


def valida_dados_pessoais(nome, idade, salario, sexo, estado_civil):
  if ((len(nome) > 3) and (idade > 0 and idade <= 150) and (salario > 0) and (sexo == 'f' or sexo == 'm') and (estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd')):
    return 'dados validados com sucesso'
  return 'dados inválidos, favor verificar as informações'

nome = input('Informe o nome do usuário: ')
idade = int(input("Informe uma idade 0 e 150 anos: "))
salario = float(input("Informe um salário maior do que 0: "))
sexo = input("Informe o sexo (m) para masculino e (f) para feminino: ")
estado_civil = input('''Informe o estado civil: (s) solteiro
(c) solteiro, (v) viúvo, (d) divorciado: ''')

print(valida_dados_pessoais(nome, idade, salario, sexo, estado_civil))