# local onde às variáveis serão predefinidas e armazenadas
def minha_funcao(valor1, valor2):
    return valor1 + valor2

resposta = minha_funcao(10,10)

# local onde serão mostradas às variáveis respectivamente
while True:
    valor1 = int(input('valor1: '))
    valor2 = int(input('valor2: '))

    resposta = minha_funcao(valor1, valor2)
    print(valor1, '+', valor2, '=', resposta)
