# aula66.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(' PARÂMETROS DEFAULT EM PYTHON '.title().center(50, '='))
print()


# Parâmetro default é uma parâmetro que tem um valor associado na declaração da função, ou seja,
# o valor é atribuído ao parâmetro dentro do parêntesis. O parâmetros default funciona da mesma forma
# que a inicialização e declaração de variáveis, isto é, a mesma recebe um valor no momento da sua declaração.
#
# Podemos pensar em parâmetros default como se fossem variáveis que são inicializadas no momento da declaração.

def login(usuario='root', senha='123'):  # TODO retirar usuário e senha default. (Este é um teste TODO do PyCharm)
    """Recebe usuário e senha ou utiliza os parametros default

    :param usuario: nome do usuário
    :type usuario: str
    :param senha: senha do usuário
    :type senha: str
    """
    print(f'Usuário: {usuario}')
    print(f'Senha: {senha}')


login()
