# aula51.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(f' QUANTIDADE DE ITENS EM PYTHON '.title().center(130, '='))
print()
lista = ['Cláudio', 'José', 'Maria', 'Beltrano', 'João', 'Fulano', 'Ciclano']
print(f'Lista -> \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{lista}')

# função len() obtem a quantidade de itens no objeto
print(f'Quantidade de itens no objeto lista com a função len() -> \t\t\t{len(lista)}')

# obtendo o último elemento do objeto lista com a função len() - 1
print(f'Obtendo o último elemento do objeto lista com a função (len()-1) -> {lista[len(lista)-1]}')

# descobrindo elementos repetidos no objeto lista com a função count()
lista.insert(5, 'José')
lista.append('José')
print(f'Lista -> \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{lista}')
print(f'Quantas vezes existe o nome "José" (count())? -> \t\t\t\t\t{lista.count("José")}')
print(f'Obtendo o índice do elemento "Maria" -> \t\t\t\t\t\t\t{lista.index("Maria")}')
print(f'Obtendo o índice do elemento "José" -> \t\t\t\t\t\t\t\t{lista.index("José")}')
