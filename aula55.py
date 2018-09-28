# aula55.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(' EXEMPLO COM OPERADOR IN EM PYTHON '.title().center(50, '='))
print()
a = 10
b = 25
c = 66
x = int(input('Digite um número: '))
# verificação utilizando operadores lógico
# if (x == a) or (x == b) or (x == c):
#     print('Está contido.')
# else:
#     print('Não está contido.')

# verificação com in
if x in [a, b, c]:
    print('Está contido.')
else:
    print('Não está contido.')
print()
print(30 * '-')
print()
cores = ['azul', 'amarelo', 'vermelho', 'branco']
while True:
    cor = input('Digite um nome de uma cor: [0 Sair} ')
    if cor == '0':
        break
    elif cor in cores:
        print(f'A cor {cor} está contida.')
    else:
        print(f'A cor {cor} NÃO está contida.')
