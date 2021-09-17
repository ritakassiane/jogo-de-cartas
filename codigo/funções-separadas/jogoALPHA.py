from random import randint
class Cartas:

    def __init__(self):
        self.nomeDaCarta = ''
        self.valor = 0
        self.forca = 0.0
        self.energia = 0.0
        self.jokenpo = ''

def sorteia(num): #essa função recebe um numero e sorteia, sem repetir, a qntd de vezes digitada
    listaSort = []
    while len(listaSort) < num+1:
        for i in range (num):
            sorteio = randint(0,num)
            if sorteio not in listaSort:
                listaSort.append(sorteio)
    return listaSort

def sorteiaCarta(cartasDoJogador): # essa função sorteia um número no intervalo da quantidade de cartas que o jogador tem. Esse numero sera utilizado para estabelecer a posição da carta que jogador jogará
    posicao = randint(0,len(cartasDoJogador)-1)
    return posicao


def embaralhaLista(lista):
    listaEmbaralhada = []
    cartasAleatorias = sorteia(len(lista)-1)
    for j in cartasAleatorias:
        listaEmbaralhada.append(lista[j])
    return listaEmbaralhada

def destribui(lista,x): #essa função recebe uma lista embaralhada e destribui, x cartas desta um jogador
    player = []
    for i in range (x):
        player.append(lista[len(lista)-1])
        lista.pop(len(lista)-1)
    return player

def destribui2(lista,x, player): #essa função recebe uma lista embaralhada e destribui, x cartas desta um jogador player
    for i in range (x):
        player.append(lista[len(lista)-1])
        lista.pop(len(lista)-1)
    return player

def linha():
    print('##############################################################################################################')

def exibicaoCartas(x,nome,valor,forca,energia,jokenpo): #essa função é de exibicao das cartas, onde x é o player.
    linha()
    print(f'                   PLAYER {x}                                           ')
    print(f'                    {nome}                  ')
    print(' ')
    print(f"""
 VALOR      FORCA     ENERGIA        JOKENPO
{valor} ## {forca}  ## {energia}   ##      {jokenpo}""")
    linha()
    
def PPT (jogador1, jogador2, carta1,carta2, cava): #essa função estabelece as possibilidades de combinações de Pedra, Papel e Tesoura e os vencedores dessa disputa
    if carta1.jokenpo == 'Pedra' and carta2.jokenpo == 'Papel' or carta1.jokenpo == 'Tesoura' and carta2.jokenpo == 'Pedra' or carta1.jokenpo == 'Papel' and carta2.jokenpo == 'Tesoura':
        print(f'Jokenpo Jogador 1 {carta1.jokenpo}')
        print(f'Jokenpo Jogador 2 {carta2.jokenpo}')
        print("")
        print('Jogador 2 venceu')
        jogador1.remove(carta1)
        jogador2.remove(carta2)
        destribui2(cava,1,jogador1)
        return jogador1, jogador2
    elif carta2.jokenpo == 'Pedra' and carta1.jokenpo == 'Papel' or carta1.jokenpo == 'Pedra' and carta2.jokenpo == 'Tesoura' or carta1.jokenpo == 'Tesoura' and carta2.jokenpo == 'Papel':
        print(f'Jokenpo Jogador1 {carta1.jokenpo}')
        print(f'Jokenpo Jogador2 {carta2.jokenpo}')
        print("")
        print('Jogador 1 venceu')
        jogador1.remove(carta1)
        jogador2.remove(carta2)
        destribui2(cava,1,jogador2)
        return jogador1, jogador2
    elif carta1.jokenpo == carta2.jokenpo:
        jogador1.remove(carta1)
        jogador2.remove(carta2)
        destribui2(cava,1,jogador2)
        return jogador1, jogador2
        
        
        
    

def setup_disputa(): 
    print('QUAL DISPUTA VOCÊ DESEJA PROPOR?')
    print('-------------------------------------------------')
    print('          1. Valor')
    print('          2. Força')
    print('          3. Energia')
    print('          4. Jokenpô(Pedra, Papel ou tesoura')
    print('-------------------------------------------------')    


def escolhe_disputa(jogador1, jogador2, carta1, carta2, cava): #essa é a função que sera chamada a cada rodada, a qual da as possibilidades de jogada dos jogadores
    setup_disputa()
    jogador1pontos = 0
    jogador2pontos = 0
    partidas = 0
    while partidas != 10:
        for disputa in range (3):
            jogador1dispTemporario = 0 #essa variavel guardará a quantidade de vezes que o jogador 1 ganha nas disputas de 1 a 3
            jogador2dispTemporario = 0 #essa variavel guardará a quantidade de vezes que o jogador 2 ganha nas disputas de 1 a 3
            
            while True:
                try:
                    x = int(input(':'))
                except (ValueError, TypeError):
                    print('Ação invalida, tente novamente!')
                    continue
                else:
                
                
                    if x == 1:
                        print('VALOR vs VALOR')
                        if int(carta1.valor) > int(carta2.valor):
                            print(f'Jogador1 {carta1.valor}')
                            print(f'Jokenpo Jogador2 {carta2.valor}')
                            print("")
                            print('Jogador 1 venceu')
                            jogador1.remove(carta1)
                            jogador2.remove(carta2)
                            destribui2(cava,1,jogador2)
                            jogador1dispTemporario += 1
                            return jogador1, jogador2
                            
                        elif int(carta1.valor) < int(carta2.valor):
                            print(f'Jokenpo Jogador 1 {carta1.valor}')
                            print(f'Jokenpo Jogador 2 {carta2.valor}')
                            print("")
                            print('Jogador 2 venceu')
                            jogador1.remove(carta1)
                            jogador2.remove(carta2)
                            destribui2(cava,1,jogador1)
                            jogador2dispTemporario += 1
                            return jogador1, jogador2
                        elif int(carta1.valor) == int(carta2.valor):
                            print(f'Jokenpo Jogador 1 {carta1.valor}')
                            print(f'Jokenpo Jogador 2 {carta2.valor}')
                            print("")
                            print('SEM VITORIAS')
                            jogador1.remove(carta1)
                            jogador2.remove(carta2)
                            destribui2(cava,1,jogador2)
                            destribui2(cava,1,jogador1)
                            return jogador1, jogador2
                            break
                    
                        elif x == 2:
                            print('FORÇA vs FORÇA')
                            if float(carta1.forca) > float(carta2.forca):
                                print(f'Jogador1 {carta1.forca}')
                                print(f'Jokenpo Jogador2 {carta2.forca}')
                                print("")
                                print('Jogador 1 venceu')
                                jogador1.remove(carta1)
                                jogador2.remove(carta2)
                                destribui2(cava,1,jogador2)
                                jogador1dispTemporario += 1
                                return jogador1, jogador2
                                
                            elif float(carta1.forca) < float(carta2.forca):
                                print(f' Força Jogador 1: {carta1.forca}')
                                print(f'Força Jogador 2: {carta2.forca}')
                                print("")
                                print('Jogador 2 venceu')
                                jogador1.remove(carta1)
                                jogador2.remove(carta2)
                                destribui2(cava,1,jogador1)
                                jogador2dispTemporario += 1
                                return jogador1, jogador2
                            elif float(carta1.forca) == float(carta2.forca):
                                print(f'Força Jogador 1: {carta1.forca}')
                                print(f'Força Jogador 2: {carta2.forca}')
                                print("")
                                print('SEM VITORIAS')
                                jogador1.remove(carta1)
                                jogador2.remove(carta2)
                                destribui2(cava,1,jogador2)
                                destribui2(cava,1,jogador1)
                                return jogador1, jogador2
                                break
                           
                        elif x == 3:
                            print('ENERGIA vs ENERGIA')
                            if float(carta1.energia) > float(carta2.energia):
                                print(f'Energia Jogador1: {carta1.energia}')
                                print(f'Energia Jogador2 {carta2.energia}')
                                print("")
                                print('Jogador 1 venceu')
                                jogador1.remove(carta1)
                                jogador2.remove(carta2)
                                destribui2(cava,1,jogador2)
                                jogador1dispTemporario += 1
                                return jogador1, jogador2
                                
                            elif float(carta1.energia) < float(carta2.energia):
                                print(f' Energia Jogador 1: {carta1.energia}')
                                print(f'Energia Jogador 2: {carta2.energia}')
                                print("")
                                print('Jogador 2 venceu')
                                jogador1.remove(carta1)
                                jogador2.remove(carta2)
                                destribui2(cava,1,jogador1)
                                jogador2dispTemporario += 1
                                return jogador1, jogador2
                            elif float(carta1.energia) == float(carta2.energia):
                                print(f'Energia Jogador 1: {carta1.energia}')
                                print(f'Energia Jogador 2: {carta2.energia}')
                                print("")
                                print('SEM VITORIAS')
                                jogador1.remove(carta1)
                                jogador2.remove(carta2)
                                destribui2(cava,1,jogador2)
                                destribui2(cava,1,jogador1)
                                return jogador1, jogador2
                                break
                            
                        elif x == 4:
                            print('JOKENPO')
                            PPT(player1,player2,player1[2],player2[2],cartas_embaralhadas)
                            break
            if jogador1dispTemporario == jogador2dispTemporario:
                

                    



arquivo = open('Cartas.txt', 'r')
listaArquivo = arquivo.readlines()
novoArquivo = []
for i in listaArquivo:
    i = i.strip('\n')
    i = i.split(';')       
    novoArquivo.append(i)
listaCartas = []
for j in novoArquivo[1:]:
    carta = Cartas()
    carta.nome = j[0]
    carta.valor = int(j[1])
    carta.forca = float(j[2])
    carta.energia = float(j[3])
    carta.jokenpo = j[4]
    listaCartas.append(carta)
cartas_embaralhadas = embaralhaLista(listaCartas)
#destribuindo as cartas para os jogadores:
player1 = destribui(cartas_embaralhadas,5)
player2 = destribui(cartas_embaralhadas,5)

for i in player1:
    print(exibicaoCartas(1,i.nome,i.valor,i.forca,i.energia,i.jokenpo))
for j in player2:
    print(exibicaoCartas(2,j.nome,j.valor,j.forca,j.energia,j.jokenpo))

print("")
print("")
print(escolhe_disputa(player1, player2, player1[sorteiaCarta(player1)],player2[sorteiaCarta(player2)],cartas_embaralhadas))
for i in player1:
    print(exibicaoCartas(1,i.nome,i.valor,i.forca,i.energia,i.jokenpo))
for j in player2:
    print(exibicaoCartas(2,j.nome,j.valor,j.forca,j.energia,j.jokenpo))


#print(exibicaoCartas(1,destribui(cartas_embaralhadas,5)[0][0].nome,destribui(cartas_embaralhadas,5)[0][1].valor,destribui(cartas_embaralhadas,5)[0][2].forca,destribui(cartas_embaralhadas,5)[0][3].energia,destribui(cartas_embaralhadas,5)[0][4].jokenpo))



















