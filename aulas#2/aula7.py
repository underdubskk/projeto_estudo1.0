# local onde às variáveis serão predefinidas e armazenadas 
acertou = False

# local onde serão mostradas às variáveis respectivamente
while acertou == False:
    idade = int(input('com licença, poderia nos informar qual seria sua idade?'))

    if idade >= 18:
        print('desculpe o mal entendido!, pode prosseguir')
        acertou = True
    else:
        print('eita, desculpe-me mas você terá que se retirar.')

if acertou == True:
    salário = int(input('boa tarde, informe a nós seu salário:'))

    if salário <= 3000:
        print('progamador junior')
    elif salário > 3000 and salário <= 6000:
        print('progamador pleno')
    elif salário > 6000 and salário <= 15000:
        print('progamador senior')
    
    else:
        print('gerente de projetos')