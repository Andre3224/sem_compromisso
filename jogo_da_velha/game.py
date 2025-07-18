def mostrar_tabuleiro(tab):
    for linha in tab:
        print(" | ".join(linha))

def Verificacao(tab, jogador):
    for i in range(3):
        if tab[i][0] == jogador and tab[i][1] == jogador and tab[i][2] == jogador:
            return True
    #verificar colunas
    for j in range(3):
        if tab[0][j] == jogador and tab[1][j] == jogador and tab[2][j] == jogador:
            return True
    if tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2]== jogador:
        return True
    if tab[0][2] == jogador and tab[1][1] == jogador and tab[2][0]== jogador:
        return True
    
    return False


tabuleiro = [['1','2','3'],['4', '5', '6'], ['7','8','9']]


jogador = 'X'
for rodada in range(9):
    mostrar_tabuleiro(tabuleiro)
    entrada = int(input(f"Jogador {jogador}, digite um valor entre [1 - 9] que não esteja marcado o X ou O: "))
    posicao = entrada - 1

    i, j = posicao // 3, posicao % 3

    #Atualização do Tabuleiro
    if tabuleiro[i][j] != 'X' and 'O':
        if jogador == 'X':
            tabuleiro[i][j] = 'X'
        else:
            tabuleiro[i][j] = 'O'
    else:
        print('Movimento Inválido')
    #Verificacao de Vitória
    if Verificacao(tabuleiro, jogador) == True:
        mostrar_tabuleiro(tabuleiro)
        print(f'Fim de Jogo, vitoria de {jogador}')
        break

    #Mudanca de Jogador
    if jogador == 'X':
        print('Jogador O irá jogar')
        jogador ='O'
    else:
        print('Jogador X irá jogar')
        jogador = 'X'

    