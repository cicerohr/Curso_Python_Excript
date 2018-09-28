# depuracao.py criado por Cicero em 2018-09-27. Projeto Curso_Python_Excript.
# 
# Como depurar códigos Python com o uso da IDE PyCharm
#
# clicando em Run > Debug... ou pressionando as teclas ALT + SHIFT +F9 aparecerá o console do Debug.
# você deve criar um breakpoint clicando no lado esquerdo da linha do código que você quer depurar.
# no lado direito do painel debug (Watches) você deve acrescentar as variáveis que você quer monitorar clicando em +.
# com a tecla F8 ou clicando em Step Over você poderá rodar o programa passo-a-passo
print()
print(' Início '.center(20, '='))
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    if i > 5:
        break
    print(i)
else:
    print('else')
print(' Fim '.center(20, '='))
print()
