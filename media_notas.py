# Definindo uma função que recebe as notas e retorna a média
def calcular_media(notas):
    # Somando as notas e dividindo pelo número de notas
    media = sum(notas) / len(notas)
    return media

# Pedindo ao usuário o nome e a quantidade de notas do aluno
nome = input("Digite o nome do aluno: ")
quantidade = int(input("Digite a quantidade de notas: "))

# Criando uma lista vazia para armazenar as notas
notas = []

# Usando um loop for para pedir as notas ao usuário e adicionar à lista
for i in range(quantidade):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

# Chamando a função para calcular a média e atribuindo o resultado a uma variável
media = calcular_media(notas)

# Imprimindo o nome e a média do aluno
print(f"O aluno {nome} tem média {media:.2f}")
