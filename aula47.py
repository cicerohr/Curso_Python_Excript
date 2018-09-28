# aula47.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
# Interando lista

# neste laço esta buscando os indices em uma lista para imprimir outra lista
lista_num = [100, 200, 300, 400]
lista_indice = [0, 1, 2, 3]
for item in lista_indice:
    lista_num[item] += 1000
print(f'Lista com os índices -> {lista_num}')
print('-' * 30)

# alternativamente poderia colocar os índices diretamente no laço
lista_num = [100, 200, 300, 400]
for item in [0, 1, 2, 3]:
    lista_num[item] += 1000
print(f'Lista de índice no próprio lopping -> {lista_num}')
print('-' * 30)

# ou ainda poderia se utilizar a função range para gerar a lista de índice
lista_num = [100, 200, 300, 400]
for item in range(4):
    lista_num[item] += 1000
print(f'Função range(4) gera uma lista de índice -> {lista_num}')
print('-' * 30)

# ou ainda poderia se utilizar a função range para ler o total de elementos da lista usando a função len()
lista_num = [100, 200, 300, 400]
for item in range(len(lista_num)):
    lista_num[item] += 1000
print(f'Função range() + função len(lista_num) gera uma lista de índice -> {lista_num}')
print('-' * 30)

# a função enumerate gerará tuplas com índice e item
# list(enumerate([100, 200, 300, 400])) ==> [(0, 100), (1, 200), (2, 300), (3, 400)]
lista_num = [100, 200, 300, 400]
for indice, item in enumerate(lista_num):
    lista_num[indice] += 1000
print(f'Função enumerate() gera tuplas com índice e itens -> {lista_num}')
print('-' * 30)
