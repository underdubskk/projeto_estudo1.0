# projeto de medidor de velocidade
velocidade_maxima = 80
acertou = False


while acertou == False:
    velocidade = int(input('digite sua velocidade!'))
    
    if velocidade <= velocidade_maxima:
        print('você não levou nenhuma multa<3')
        acertou = True

    elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
        print('você levou uma multa leve')
    elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
        print('você levou uma multa grave')
    elif velocidade > velocidade_maxima + 20:
        print('você é a vergonha da profission, tome uma multa gravíssima!')
