# local onde às variáveis serão predefinidas e armazenadas
notas = []

# local onde serão mostradas às variáveis respectivamente

# através de for
for x in range(5):
    codigo_aluno = input('RM: ')
    nota = float(input("nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print('quantidades de notas', len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print('O RM', codigo_aluno, 'tirou a nota:', nota)
    

# através de while
notas = []
contador = 1

while contador <= 5:
    codigo_aluno = input("RM: ")
    nota = float(input("nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

# alternativa: contador += 1
    contador = contador + 1

print('quantidade de notas', len(notas))

'''
# while se repete enquanto se for "True"
-
while True:
    print("se eu rodar o script meu pc morre!")
-
-
# for se repete por sequências
-
for x in range(10):
    print(x) 
-
'''