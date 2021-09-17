def PPT (jogador1, jogador2, carta1,carta2): #essa função estabelece as possibilidades de combinações de Pedra, Papel e Tesoura e os vencedores dessa disputa
    if carta1.jokenpo == 'Pedra' and carta2.jokenpo == 'Papel' or carta1.jokenpo == 'Tesoura' and carta2.jokenpo == 'Pedra' or carta1.jokenpo == 'Papel' and carta2.jokenpo == 'Tesoura':
        return jogador2
    elif carta2.jokenpo == 'Pedra' and carta1.jokenpo == 'Papel' or carta1.jokenpo == 'Pedra' and carta2.jokenpo == 'Tesoura' or carta1.jokenpo == 'Tesoura' and carta2.jokenpo == 'Papel':
        return jogador1 

def destribui2(lista,x, player): #essa função recebe uma lista embaralhada e destribui, x cartas desta um jogador player
    for i in range (x):
        player.append(lista[len(lista)-1])
        lista.pop(len(lista)-1)
    return player

def compara(jogador1, jogador2, opcao): #essa função recebe duas listas de cartas (de cada usuario) e um atributo. A função irá comparar os valores desse atributo, e retorna o maior

    maiorJogador1 = 0
    maiorJogador2 = 0
    for i in jogador1:
        if int(i.opcao) >= maiorJogador1:
            maiorJogador1 = int(i.opcao)
            carta1 = i
    for j in jogador2:
        if int(j.opcao) >= maiorJogador2:
            maiorJogador2 = int(j.opcao)
            carta2 = j
    if maiorJogador1 > maiorJogador2:
        jogador1.remove(carta1)
        jogador2.remove(carta2)
        print('Jogador 1 venceu')
        destribui(cava,1,jogador1)
        return jogador1
    elif maiorJogador2 > maiorJogador1:
        jogador2.remove(carta2)
        jogador1.remove(carta1)
        print('Jogador 2 venceu')
        destribui(cava,1,jogador2)
        return jogador2
    else:
        jogador1.remove(carta1)
        jogador2.remove(carta2)
        destribui(cava,1,jogador1)
        destribui(cava,1,jogador2)
        return jogador1, jogador2
        

    
