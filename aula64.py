# aula64.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(' INTRODUÇÃO ÀS FUNÇÕES EM PYTHON '.title().center(50, '='))
print()


# FUNÇÃO vs MÉTODO
# O conceito de função e método se diferenciam só e somente só pelo retorno de valores.
#
# Toda função é um bloco de instrução que, possui um nome único que a identifica em seu escopo,
# pode receber parâmetros e SEMPRE retorna um valor.
#
# Um método é um bloco de instrução, possui um nome único que o identifica em seu escopo, pode receber parâmetros e
# NUNCA retorna valores.
#
# Na prática utilizamos diversas vezes ambos conceitos, até porque,
# é normal precisarmos agrupar um conjunto de instruções para que sejam executadas sequencialmente e
# após a execução da última instrução, o cursor volta e o programa continua de onde parou.
#
# Outras vezes, implementaremos blocos de instruções que processarão uma informação e
# retornaram informações processadas, logo, estamos utilizando o conceito de funções.
#
# No nosso caso, temos que o Python não faz distinção explicita entre ambos conceitos.
# Então, o importante é somente conhecer os conceitos, até porque, na prática a implementação se tornará transparente.
def minha_func():
    print('Olá mundo!')


minha_func()