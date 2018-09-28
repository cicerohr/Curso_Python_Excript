# aula67.py criado por Cicero em 2018-09-28. Projeto Curso_Python_Excript.
# 
print()
print(' ARGUMENTO DE FUNÇÃO NOMEADO VS POSICIONAL EM PYTHON '.title().center(70, '='))
print()


# Argumento posicional é o nome utilizado para a passagem de valores onde
# cada valor estara na ordem conforme implementado na função.
#
# Argumento nomeado é a passagem de valores fazendo associação com o nome do parâmetro e o valor que está sendo enviado.
#
# Lembre-se que argumento e parâmetro são nomes diferentes para conceitos iguais.
# O termo argumento é utilizado quando determinada função está sendo invocada, logo,
# dizemos que a função tem definido x argumentos. Parâmetro é o nome utilizado quando
# estamos manipulando a função propriamente dita, logo, dizemos que a função declarou x parâmetros.

def dados_pessoais(nome: str, sobrenome: str, idade: int, sexo: bool) -> print():
    """Recebe dados pessoais do usuário

    :type nome: str
    :type sobrenome: str
    :type idade: int
    :type sexo: bool
    :rtype : print
    """
    print(f'Nome: {nome}\nSobrenome: {sobrenome}\nIdade: {idade}\nSexo: {sexo}')


print(' Argumento posicional '.center(30, '-'))
dados_pessoais('Cícero', 'Rodrigues', 52, True)

print(' Argumento nomeado '.center(30, '-'))
dados_pessoais(nome='Cícero',
               sobrenome='Rodrigues',
               idade=52,
               sexo=True)
