# projeto de chute de um número
import random
acertou = False

valor_aleatorio = random.randint(1,10)


while acertou == False:
    chute = int(input('chute um valor de 1 a 10: '))

    if chute > valor_aleatorio:
        print('chute foi maior que o valor gerado')
    elif chute < valor_aleatorio:
        print('chute foi menor que o valor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print('você acertou!')  