# aula58.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(' FUNÇÕES DAS STRINGS NO PYTHON '.title().center(50, '='))
# para o Python as strings são imutáveis
# então como podemos altera-la?
s = 'Lista de caracteres'
print(s)
# a técnica é desmontá-la e mota-la novamente com as alterações
# split()
lista = s.split(' ')
print(lista)
print(f'{lista[0]} {lista[2]}')
print('-' * 30)
# replace()
print(s.replace('de', ''))
print('Observe que a string "s" não foi modificada')
print(s)
