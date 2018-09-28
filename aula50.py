# aula50.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(' ORDENAMENTO DE LISTAS EM PYTHON '.title().center(113, '='))
print()
lista = ['Cláudio', 'José', 'Maria', 'Beltrano', 'João', 'Fulano', 'Ciclano']
print(f'Lista -> \t\t\t\t\t\t\t\t\t{lista}')

# método reverse() inverte a lista
lista.reverse()
print(f'Lista invertida com o método reverse() -> \t{lista}')

# método sort() ordena a lista de forma ascendente
lista.sort()
print(f'Lista ordenada (asc) com o método sort() -> {lista}')

# método sort() ordena a lista de forma descendente com o parâmetro reverse=True
lista.sort(reverse=True)
print(f'Lista ordenada (dsc) com o método sort() -> {lista}')
