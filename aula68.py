# aula68.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(' RETORNANDO VALORES PELAS FUNÇÕES EM PYTHON '.title().center(50, '='))
print()


# O objetivo de toda função é o processamento de alguma informação e o retorno do dado processado. Desta forma,
# temos que toda função pode, por definição, retornar valores.
#
# Como estudado, uma função é um bloco de código que possui um nome, pode ser invocado, pode receber argumentos e
# pode retornar valores. Para retornarmos valores por funções, temos que utilizar uma notação especifica para este fim
# que é, a instrução return.
#
# A palavra-chave return é utilizada para declarar a informação a ser retornada pela função.
# A mesma funciona também para finalizar a execução do bloco de instrução da função, retornado assim,
# o valor que estiver a sua frente. Então, a instrução return é utilizada tanto para o retorno de valores pelas funções,
# como também, para finalizar a execução da função.
#
# É importante entender que o uso da palavra-chave return não está só e somente só relacionado com o retorno de valores,
# a mesma é frequentemente utilizada para finalizar a execução das instruções contidas no bloco de instrução da função,
# funcionado de maneira semelhante a palavra-chave break e continue que,
# são utilizadas para finalizar a execução do laço de repetição ou de um único ciclo.

def soma(x: int, y: int) -> int:
    """Soma duas parcelas

    :param x: primeira parcela
    :type x: int
    :param y: segunda parcela
    :type y: int
    :return: a soma das duas parcelas
    :rtype: int
    """
    return x + y


print(soma(10, 20))
