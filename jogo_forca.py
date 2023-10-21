# Importa a biblioteca random para escolher uma palavra aleatória
import random

# Define uma lista de palavras possíveis
palavras = ["casa", "carro", "livro", "python", "jogo", "forca"]

# Escolhe uma palavra da lista
palavra = random.choice(palavras).upper()

# Cria uma lista com um traço para cada letra da palavra
letras = ["_"] * len(palavra)

# Define o número de vidas
vidas = 6

# Define uma variável para indicar se o jogo acabou
fim = False

# Imprime uma mensagem de boas-vindas
print("Bem-vindo ao jogo da forca!")
print("Adivinhe a palavra secreta:")

# Enquanto o jogo não acabar, repete o seguinte
while not fim:

    # Imprime as letras já descobertas e as vidas restantes
    print(" ".join(letras))
    print(f"Vidas: {vidas}")

    # Pede ao usuário para digitar uma letra
    letra = input("Digite uma letra: ").upper()
a
    # Verifica se a letra está na palavra
    if letra in palavra:

        # Substitui os traços pelas letras acertadas
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras[i] = letra

        # Imprime uma mensagem de acerto
        print("Você acertou uma letra!")

    else:

        # Diminui uma vida
        vidas -= 1

        # Imprime uma mensagem de erro
        print("Você errou uma letra!")

    # Verifica se o usuário acertou a palavra inteira
    if "_" not in letras:

        # Imprime uma mensagem de vitória
        print("Parabéns, você ganhou!")
        print(f"A palavra era: {palavra}")

        # Encerra o jogo
        fim = True

    # Verifica se o usuário perdeu todas as vidas
    if vidas == 0:

        # Imprime uma mensagem de derrota
        print("Que pena, você perdeu!")
        print(f"A palavra era: {palavra}")

        # Encerra o jogo
        fim = True

