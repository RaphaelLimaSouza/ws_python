# Inicializa uma lista para armazenar a contagem de vendedores em cada intervalo de salário
contadores = [0] * 9

# Loop para ler as vendas brutas de cada vendedor
while True:
    vendas_brutas = input("Insira as vendas brutas do vendedor (-1 para encerrar): ")
    if vendas_brutas == "-1":
        break
    vendas_brutas = float(vendas_brutas)

    # Calcula o salário do vendedor
    salario = 200 + 0.09 * vendas_brutas

    # Determina o intervalo de salário
    if salario >= 1000:
        indice = 8
    else:
        indice = int((salario - 200) / 100)

    # Incrementa o contador apropriado
    contadores[indice] += 1

# Imprime a contagem de vendedores em cada intervalo de salário
for i in range(9):
    if i == 8:
        print("$1000 em diante: ", contadores[i])
    else:
        print("${} - ${}: ".format(200 + i*100, 299 + i*100), contadores[i])