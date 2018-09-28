# aula48.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
# Fatiando lista no Python
#
# lista[start :   stop   :   step]
#        0     len(lista)      1    Padrão
#
#  0  1  2  3  4  5     Índice positivo
#  P  Y  T  H  O  N     Lista ou string
# -6 -5 -4 -3 -2 -1     Índice negativo
#
print()
print(' Fatiando lista no Python '.center(40,'='))
print()
print(' lista[start  [:   stop   :   step]]\n'
      '         0      len(lista)      1    Padrão\n')
lista = list('PYTHON')
print('Índices (+):   0    1    2    3    4    5')
print(f'lista   ->   {lista}')
print('Índices (-):  -6   -5   -4   -3   -2   -1\n')
print(f'lista[0] -> {lista[0]}')
print(f'lista[:2] -> {lista[:2]}')
print(f'lista[2:] -> {lista[2:]}')
print(f'lista[::2] -> {lista[::2]}')
print(f'lista[2::2] -> {lista[2::2]}')
print(f'lista[-1] -> {lista[-1]}')
print(f'lista[::-1] -> {lista[::-1]}')
print(f'lista[:-1] -> {lista[:-1]}')
