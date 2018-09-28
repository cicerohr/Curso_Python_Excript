# aula65.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(' PARÂMETROS DE FUNÇÃO EM PYTHON '.title().center(50, '='))
print()


# Parâmetro é o nome utilizado quando estamos dentro do código da função propriamente dita e,
# argumento, é o nome dado aos valores referentes a cada parâmetro.

def soma(x: int, y: int) -> print():
    """Soma duas parcelas de inteiros

    :param x: valor da primeira parcela
    :type x: int
    :param y: valor da segunda parcela
    :type y: int
    :return: mostra o resultado da soma das duas parcelas
    :rtype: print
    """
    total = x + y
    return print(f'A soma de {x} + {y} é {total}')


soma(10, 50)
