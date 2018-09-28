# aula57.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
#
print()
print(' FATIANDO STRINGS COM PYTHON '.title().center(40, '='))
print()
s = 'Para o Python, toda string é uma lista imutável.'
print(s)
# retornando um caracter através do índice
print()
print(f'Caracter no índice 0 é "{s[0]}".')
print(f'O último caracter é "{s[-1]}".')
print(f'Caracteres entre o índice 5 e 9 são "{s[5:10]}".')
print(f'Inverter a frase "{s[::-1]}".')
print(f'Definindo passo "{s[::5]}".')
