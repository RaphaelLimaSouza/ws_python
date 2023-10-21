# Inicializa uma lista vazia para armazenar as notas
notas = []

# Loop infinito para leitura das notas
while True:
    nota = float(input("Insira uma nota (-1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

# Mostra a quantidade de valores que foram lidos
print("Quantidade de valores lidos: ", len(notas))

# Exibe todos os valores na ordem em que foram informados
print("Valores na ordem informada: ", end="")
for nota in notas:
    print(nota, end=" ")
print()

# Exibe todos os valores na ordem inversa à que foram informados
print("Valores na ordem inversa:")
for nota in reversed(notas):
    print(nota)

# Calcula e mostra a soma dos valores
soma = sum(notas)
print("Soma dos valores: ", soma)

# Calcula e mostra a média dos valores
media = soma / len(notas)
print("Média dos valores: ", media)

# Calcula e mostra a quantidade de valores acima da média calculada
acima_media = len([nota for nota in notas if nota > media])
print("Quantidade de valores acima da média: ", acima_media)

# Calcula e mostra a quantidade de valores abaixo de sete
abaixo_sete = len([nota for nota in notas if nota < 7])
print("Quantidade de valores abaixo de sete: ", abaixo_sete)

# Encerra o programa com uma mensagem
print("Programa encerrado. Obrigado!")
