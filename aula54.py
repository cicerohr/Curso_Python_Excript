# aula54.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(' OPERADORES AND, OR E IN DO PYTHON '.title().center(50, '='))
print()
# Verificar se dois elementos estão contidos em uma lista, tupla, dicionário etc.
x = range(1, 6)
print(f'Os números 1 e 4 estão contidos na lista {list(x)}? {(1 and 4) in list(x)}')
print(f'Os números 1 e 6 estão contidos na lista {list(x)}? {(1 and 6) in list(x)}')
print(f'O número 1 e 6 ou o número 5 e 6 estão contidos na lista {list(x)}? {((1 and 6) or (5 and 6)) in list(x)}')
print(f'O número 1 e 3 ou o número 5 e 6 estão contidos na lista {list(x)}? {((1 and 3) or (5 and 6)) in list(x)}')
# bug do Python
print(f'O números 10 ou 2 estão contidos na lista {list(x)}? {(10 or 2) in list(x)}')
print(f'O números 2 ou 10 estão contidos na lista {list(x)}? {(2 or 10) in list(x)}')
