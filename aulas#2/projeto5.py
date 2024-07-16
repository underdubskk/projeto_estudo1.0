# local onde às variáveis serão predefinidas e armazenadas 
import os

mensagens = []
nome = input('nome: ')

# local onde serão mostradas às variáveis respectivamente
while True:

    # limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['texto'])


    print('__________________')


    # obtendo o texto
    texto = input('mensagens: ')

    if texto == 'fim':
        break
    
    # adicionando mensagens na lista
    mensagens.append({
        'nome': nome,
        'texto': texto
    })