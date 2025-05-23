'''
### Exercício 1
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
- A mensagem "Reprovado", se a média for menor do que 7;
- A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

nota = 0
resultado = ''
for i in range(2):
  nota += int(input(f'Informe a {i + 1}ª nota: '))

media = nota / 2

if media >= 10 : 
  resultado = "Aprovado com Distinção" 
elif media >= 7:
  resultado = "Aprovado"
else:
  resultado = "Reprovado"

print(resultado)