# aula49.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(f' INCLUINDO, ALTERANDO E EXCLUINDO ELEMENTOS NO PYTHON '.title().center(95, '='))
print()
lista = ['bbb', 'ccc', 'ddd']
print(f'lista -> \t\t\t\t\t\t\t\t\t\t\t\t\t{lista}')

# inserindo item no final da lista
lista.append('eee')
print(f'Inserindo item com a função append() -> \t\t\t\t\t{lista}')

# inserindo item na posição desejada
lista.insert(0, 'aaa')
print(f'Inserindo item com a função insert() -> \t\t\t\t\t{lista}')

# alterando valor da lista
lista[1] = 'bbbb'
print(f'Alterando um item da lista através do índice da lista -> \t{lista}')

# Excluir elementos da lista
# função pop() apaga um item específico da lista com
lista.pop()  # sem argumento apaga o último elemento
print(f'Apagando o último item da lista com a função pop() -> \t\t{lista}')
#
lista.pop(0)
print(f'Apagando um item específico da lista com a função pop() -> \t{lista}')
# função del() apaga vários itens
del (lista[1:])
print(f'Apagando vários itens da lista com a função del() -> \t\t{lista}')
# função clear() limpa todos os itens da lista
lista.clear()
print(f'Apagando todos os itens com a função clear() -> \t\t\t{lista}')
