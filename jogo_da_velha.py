# Criando o tabuleiro com um dicionário
tabuleiro = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

# Lista com as chaves do tabuleiro
chaves = []

# Inserindo as chaves na lista
for chave in tabuleiro:
    chaves.append(chave)

# Função para imprimir o tabuleiro na tela
def imprimir_tabuleiro(tab):
    print(tab['1'] + '|' + tab['2'] + '|' + tab['3'])
    print('-+-+-')
    print(tab['4'] + '|' + tab['5'] + '|' + tab['6'])
    print('-+-+-')
    print(tab['7'] + '|' + tab['8'] + '|' + tab['9'])

# Função para verificar se há vitória ou empate
def verificar_vitoria():
    # Verificando as linhas
    if (tabuleiro['1'] == tabuleiro['2'] == tabuleiro['3'] != ' '):
        return True
    elif (tabuleiro['4'] == tabuleiro['5'] == tabuleiro['6'] != ' '):
        return True
    elif (tabuleiro['7'] == tabuleiro['8'] == tabuleiro['9'] != ' '):
        return True
    # Verificando as colunas
    elif (tabuleiro['1'] == tabuleiro['4'] == tabuleiro['7'] != ' '):
        return True
    elif (tabuleiro['2'] == tabuleiro['5'] == tabuleiro['8'] != ' '):
        return True
    elif (tabuleiro['3'] == tabuleiro['6'] == tabuleiro['9'] != ' '):
        return True
    # Verificando as diagonais
    elif (tabuleiro['1'] == tabuleiro['5'] == tabuleiro['9'] != ' '):
        return True
    elif (tabuleiro['3'] == tabuleiro['5'] == tabuleiro['7'] != ' '):
        return True
    # Verificando se há empate (tabuleiro cheio)
    elif (' ' not in tabuleiro.values()):
        return "Empate"
    # Caso contrário, o jogo continua
    else:
        return False

# Função principal do jogo
def jogo():
    # Definindo as variáveis de controle
    turno = 0 # Contador de turnos
    fim = False # Indicador de fim de jogo

    # Imprimindo o tabuleiro inicial vazio
    imprimir_tabuleiro(tabuleiro)

    # Loop principal do jogo
    while not fim:
        # Alternando os jogadores a cada turno
        if turno % 2 == 0:
            jogador = "X"
        else:
            jogador = "O"

        # Pedindo a jogada do jogador atual
        print(f"Vez do jogador {jogador}. Escolha uma posição entre 1 e 9:")
        jogada = input()

        # Verificando se a jogada é válida (está entre 1 e 9 e é um espaço vazio)
        if jogada in chaves and tabuleiro[jogada] == " ":
            # Atualizando o tabuleiro com a jogada do jogador atual
            tabuleiro[jogada] = jogador

            # Imprimindo o tabuleiro atualizado na tela
            imprimir_tabuleiro(tabuleiro)

            # Incrementando o contador de turnos
            turno += 1

            # Verificando se há vitória ou empate após a jogada atual
            fim = verificar_vitoria()

            # Se houver vitória, parabenizar o jogador vencedor e encerrar o jogo
            if fim == True:
                print(f"Parabéns, jogador {jogador}! Você venceu o jogo!")
                break

            # Se houver empate, avisar que o jogo terminou em velha e encerrar o jogo
            elif fim == "Empate":
                print("O jogo terminou em velha!")
                break

        # Se a jogada não for válida, pedir outra jogada ao mesmo jogador
        else:
            print("Jogada inválida! Tente novamente.")

# Chamando a função principal do jogo
jogo()