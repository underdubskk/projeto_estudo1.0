# predefinições
nomes_de_gato = ['seu jorge','negão','chocolate branco','ednaldo pereira','jubileu']
idade = [1,2,4,6,9]
total = 0

# execuções
print('hello world')
nomes = input('qual é o seu nome?')

print('que nome bonito!')
idade_pessoa = input('quantos anos você tem?')
idade_gato = input('quantos anos seu gato tem?')


if int(idade_pessoa) > int(idade_gato):
    print('então sua idade é maior que a de seu gato? que legal!')
else:
    print('que surpresa! sua idade é menor que a de seu gato!')

input('deixe-me adivinhar, o nome de seus gatos são!:')
for nomes_de_gato in nomes_de_gato:
    print(nomes_de_gato)


input('e a idade de todos respectivamente, são!:')
print(idade)

input('e a soma dessas idades seriam:')
for idade in idade:
    total = total + idade
print(idade)

afirmacao = input('estou correto em minha afirmação?')
if (afirmacao) == "sim" or "yes":
    print('ha, sou realmente incrível em meu trabalho.')
else:
    print('então vá se ferrar.')


