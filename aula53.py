# aula53.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(' OPERADORES "IN" E "NOT IN" DO PYTHON '.title().center(55, '='))
print()
# verifica se um objeto esta ou não contido em um lista, tupla, dicionário etc.
print(f'O número 2 esta contido na tupla (1, 2, 3, 4, 5)? {2 in (1, 2, 3, 4, 5)}')
print(f'O número 6 não esta contido na tupla (1, 2, 3, 4, 5)? {6 not in (1, 2, 3, 4, 5)}')
print()

#
x = range(1, 6)
print(f'O número 1 esta contido na lista {list(x)}?', end=' ')
if 1 in x:
    print('está contido')
else:
    print('Não está contido')

print(f'O número 6 esta contido na lista {list(x)}?', end=' ')
if 6 in x:
    print('está contido')
else:
    print('Não está contido')
