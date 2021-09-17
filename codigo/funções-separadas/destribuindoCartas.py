"""def destribui(lista,x): #essa função recebe uma lista embaralhada e destribui, x cartas desta a dois jogadores
    player1 = []
    player2 = []
    for i in range (x):
        player1.append(lista[len(lista)-1])
        lista.pop(len(lista)-1)
        player2.append(lista[len(lista)-2])
        lista.pop(len(lista)-2)
        
    return player1, player2"""

def destribui(lista,x): #essa função recebe uma lista embaralhada e destribui, x cartas desta um jogador
    player = []
    for i in range (x):
        player.append(lista[len(lista)-1])
        lista.pop(len(lista)-1)
    return player

teste = [2,3,1,5,6,7,8,9,0,4]
player1 = destribui(teste,5)
print(player1)
print(teste)
player2 = destribui(teste,5)
print(player2)
print(teste)
    
