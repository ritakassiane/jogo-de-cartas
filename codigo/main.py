import os 
from random import randint

###############################################################################################################################################################
# Autor: Rita Kassiane Santos dos Santos                                                                                                                                      #
# Componente Curricular: Algoritmos I                                                                                                                         #
# Concluido em: 15/08/2019                                                                                                                                    #
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de outro colega ou de outro autor,                   #
# tais como provindos de livros e apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código de outra autoria que                  #
# não a minha está destacado com uma citação para o autor e a fonte do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.#
###############################################################################################################################################################


# CLASSES

class Cartas:

    def __init__(self):
        self.nomeDaCarta = ''
        self.valor = 0
        self.forca = 0.0
        self.energia = 0.0
        self.jokenpo = ''
        
class Cadastro:
    def __init__(self):
        self.nick = ''
        self.partJogadas = 0
        self.partVencidas = 0
    def taxaSucesso(self):
        taxa = (self.partVencidas*100)/self.partJogadas
        return taxa


        
# FUNÇÕES DE ESTÉTICA E EXIBIÇÃO DO JOGO


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
    return ''


def exibição_estatisticas(nick, x, y): # Essa função mostra de maneira organizada a estatistica do usuário # x =  patidas jogadas, y = patidas ganhas 
    print('-----------------------------------------------')
    print(f'                {nick}                        ')
    print('-----------------------------------------------')
    print(f' Partidas Jogadas: {x}   Partidas Ganhas: {y} ')
    print(f'             Taxa de Sucesso                  ')
    try:
        print(f'               {y*100//x}                     ')
    except (ZeroDivisionError):
        print('         Ainda não há dados!')
    return ('')

    
def menuIniciar():
    print('-------------------------------------------------------------------------------------------------------------------------------------------------')
    print('                                                  J O G O   D A   D I S P U T A                                                                  ')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' 1. Jogar                                         ')
    print(' 2. Sair                                          ')
    

def setup_disputa(): 
    print('QUAL DISPUTA VOCÊ DESEJA PROPOR?')
    print('-------------------------------------------------')
    print('          1. Valor')
    print('          2. Força')
    print('          3. Energia')
    print('          4. Jokenpô(Pedra, Papel ou tesoura')
    print('-------------------------------------------------')    

def modoDeJogo():
    print('-------------------------------------------------')
    print('                 MODOS DE JOGO                   ')
    print('-------------------------------------------------')
    print('               1. MODO ALEATORIO                 ')
    print('               2. MODO MANUAL                    ')
    print('-------------------------------------------------')
    

# FUNÇÕES DE ORGANIZAÇÃO E ORDENAÇÃO DE CARTAS


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

def escreveTXT(dicionario, file): # Essa função recebe um dicionario, e um arquivo txt. Ela irá apagar tudo que tem no arquivo txt e escrever o que tem em cada posição do dicionario, em uma linha
    arquivo = open(file, 'r')
    lista = arquivo.readlines()
    lista.append('\n')
    for i in dicionario.keys():
        lista.append(i+';')
        for j in dicionario[i]:
            lista.append(str(j)+';')
        lista.append('\n')
    arquivo = open(file, 'w')
    arquivo.writelines(lista)


# FUNÇÕES DIRETAMENTE ATRELADAS À JOGABILIDADE

def modo_manual(player1, player2): #Essa função define as características principais do modo aleatorio (jogador escolhe a carta jogada, as quais estão ordenadas em ordem alfabetica)
   
    print(f' Jogador 1, digite um valor de 0 a {len(player1)-1}')
    y1 = int(input(':'))
    print(f' Jogador 2, digite um valor de 0 a {len(player2)-1}')
    y2 = int(input(':'))
    carta1 = player1[y1]
    carta2 = player2[y2]
    return carta1, carta2

def modo_aleatorio(player1, player2): #Essa função define as características princiapis do modo manual (a cada rodada, ocorre o sorteio de um número no intervalo entre a quantidade de cartas do jogador, o qual definirá automaticamente qual carta sera jogada)
    carta1 = player1[randint(0, len(player1)-1)]
    carta2 = player2[randint(0, len(player2)-1)]
    return carta1, carta2

def verificaExistencia(nick, dicionario):# Essa função recebe o nick do usuário e verifica se ele existe no dicionario de cadastro
    if dicionario.get(nick) == None:
        dicionario[nick] = [0,0,0]
    else:
        for i in dicionario.keys():
            if i == nick:
                dados = dicionario[i]
                print(exibição_estatisticas(nick, dados[0], dados[1]))


    
def final (player1, player2): #essa função sera chamada caso, ao final das 10 partidas, os jogadores ainda possuam cartas.
    somaP1 = [0,0,0] #respectivamente, valor, força e energia
    somaP2 = [0,0,0] # respectivamente, valor, força e energia
    for cartasP1 in player1:
        for carta in cartasP1:
            somaP1[0] += int(carta.valor)
    for cartasP2 in player2:
        for carta in cartasP2:
            somaP2[0] += int(carta.valor)
    for cartasP1 in player1:
        for carta in cartasP1:
            somaP1[1] += int(carta.forca)
    for cartasP2 in player2:
        for carta in cartasP2:
            somaP2[1] += int(carta.forca)
    for cartasP1 in player1:
        for carta in cartasP1:
            somaP1[2] += int(carta.energia)
    for cartasP2 in player2:
        for carta in cartasP2:
            somaP2[2] += int(carta.energia)
    if somaP1[0] == somaP2[0] and somaP1[1] == somaP2[1] and somaP1[2] == somaP1[2]:
        print('Não há vencedores')
    elif somaP1[0] == somaP2[0] or somaP1[1] == somaP2[1] or somaP1[2] == somaP1[2]:
        if somaP1[0] > somaP2[0] or somaP1[1] > somaP2[1] or somaP1[2] > somaP2[2]:
            print('Player 1 venceu!')
        elif somaP2[0] > somaP1[0] or somaP2[1] > somaP1[1] or somaP2[2] > somaP1[2]:
            print('Player 2 venceu')


def PPT (jogador1, jogador2, carta1,carta2, cava): #essa função estabelece as possibilidades de combinações de Pedra, Papel e Tesoura e os vencedores dessa disputa
    if carta1.jokenpo == 'Pedra' and carta2.jokenpo == 'Papel' or carta1.jokenpo == 'Tesoura' and carta2.jokenpo == 'Pedra' or carta1.jokenpo == 'Papel' and carta2.jokenpo == 'Tesoura':
        print(f'Jokenpo Jogador 1: {carta1.jokenpo}')
        print(f'Jokenpo Jogador 2: {carta2.jokenpo}')
        print("")
        print('Jogador 2 venceu')
        jogador1.remove(carta1)
        jogador2.remove(carta2)
        destribui2(cava,1,jogador1)
        
    elif carta2.jokenpo == 'Pedra' and carta1.jokenpo == 'Papel' or carta1.jokenpo == 'Pedra' and carta2.jokenpo == 'Tesoura' or carta1.jokenpo == 'Tesoura' and carta2.jokenpo == 'Papel':
        print(f'Jokenpo Jogador1: {carta1.jokenpo}')
        print(f'Jokenpo Jogador2: {carta2.jokenpo}')
        print("")
        print('Jogador 1 venceu')
        jogador1.remove(carta1)
        jogador2.remove(carta2)
        destribui2(cava,1,jogador2)
        
    elif carta1.jokenpo == carta2.jokenpo:
        jogador1.remove(carta1)
        jogador2.remove(carta2)
        destribui2(cava,1,jogador2)

def escolhe_disputa(jogador1, jogador2, cava, modo): #essa é a função que sera chamada a cada rodada, a qual da as possibilidades de jogada dos jogadores e onde se concentra maior parte da jogabilidade
    jogador1dispTemporario = 0 #essa variavel guardará a quantidade de vezes que o jogador 1 ganha nas disputas de 1 a 3
    jogador2dispTemporario = 0 #essa variavel guardará a quantidade de vezes que o jogador 2 ganha nas disputas de 1 a 3
    setup_disputa()
    try:
        x = int(input(':'))
    except (ValueError, TypeError):
        print('Ação invalida, tente novamente!')
       
    try:
        cartas = modo(jogador1, jogador2)
        carta1 = cartas[0]
        carta2 = cartas[1] 
    except:
        print('Fim de jogo!')
        partidas == 10
    else:
        for i in jogador1:
            print(exibicaoCartas(1,i.nome,i.valor,i.forca,i.energia,i.jokenpo))
        for j in jogador2:
            print(exibicaoCartas(2,j.nome,j.valor,j.forca,j.energia,j.jokenpo))
            
        if x == 1:
            if int(carta1.valor) > int(carta2.valor):
                print(f'Jogador 1 {carta1.valor}')
                print(f'Jogador 2 {carta2.valor}')
                print("")
                print('Jogador 1 venceu')
                destribui2(cava,1,jogador2)
                jogador1dispTemporario += 1
                jogador1.remove(carta1)
                jogador2.remove(carta2)                            
            elif int(carta1.valor) < int(carta2.valor):
                print(f'Jogador 1 {carta1.valor}')
                print(f'Jogador 2 {carta2.valor}')
                print("")
                print('Jogador 2 venceu')
                destribui2(cava,1,jogador1)
                jogador2dispTemporario += 1
                jogador1.remove(carta1)
                jogador2.remove(carta2)
                            
            elif int(carta1.valor) == int(carta2.valor):
                print(f'Jogador 1 {carta1.valor}')
                print(f'Jogador 2 {carta2.valor}')
                print("")
                print('SEM VITORIAS')
                destribui2(cava,1,jogador2)
                destribui2(cava,1,jogador1)
                jogador1.remove(carta1)
                jogador2.remove(carta2)
                            
        elif x == 2:
            print('FORÇA vs FORÇA')
            if float(carta1.forca) > float(carta2.forca):
                print(f'Jogador1 {carta1.forca}')
                print(f'Jokenpo Jogador2 {carta2.forca}')
                print("")
                print('Jogador 1 venceu')
                destribui2(cava,1,jogador2)
                jogador1dispTemporario += 1
                jogador1.remove(carta1)
                jogador2.remove(carta2)
                                                  
            elif float(carta1.forca) < float(carta2.forca):
                print(f' Força Jogador 1: {carta1.forca}')
                print(f'Força Jogador 2: {carta2.forca}')
                print("")
                print('Jogador 2 venceu')
                destribui2(cava,1,jogador1)
                jogador2dispTemporario += 1
                jogador1.remove(carta1)
                jogador2.remove(carta2)
                                                
            elif float(carta1.forca) == float(carta2.forca):
                print(f'Força Jogador 1: {carta1.forca}')
                print(f'Força Jogador 2: {carta2.forca}')
                print("")
                print('SEM VITORIAS')
                destribui2(cava,1,jogador2)
                destribui2(cava,1,jogador1)
                jogador1.remove(carta1)
                jogador2.remove(carta2)
                                                 
        elif x == 3:
            print('ENERGIA vs ENERGIA')
            if float(carta1.energia) > float(carta2.energia):
                print(f'Energia Jogador1: {carta1.energia}')
                print(f'Energia Jogador2 {carta2.energia}')
                print("")
                print('Jogador 1 venceu')
                destribui2(cava,1,jogador2)
                jogador1dispTemporario += 1
                jogador1.remove(carta1)
                jogador2.remove(carta2)
                           
            elif float(carta1.energia) < float(carta2.energia):
                print(f' Energia Jogador 1: {carta1.energia}')
                print(f'Energia Jogador 2: {carta2.energia}')
                print("")
                print('Jogador 2 venceu')
                destribui2(cava,1,jogador1)
                jogador2dispTemporario += 1
                jogador1.remove(carta1)
                jogador2.remove(carta2)                            
                                                
            elif float(carta1.energia) == float(carta2.energia):
                print(f'Energia Jogador 1: {carta1.energia}')
                print(f'Energia Jogador 2: {carta2.energia}')
                print("")
                print('SEM VITORIAS')
                destribui2(cava,1,jogador2)
                destribui2(cava,1,jogador1)
                jogador1.remove(carta1)
                jogador2.remove(carta2)
 
        elif x == 4:
            print('JOKENPO')
            print(PPT(player1,player2,carta1,carta2,cartas_embaralhadas))
    print("")
    print(f'jogador1: {jogador1dispTemporario}')
    print("")
    print(f'jogador2: {jogador2dispTemporario}')
    return jogador1dispTemporario, jogador2dispTemporario

def main (nick1, nick2): #função executora do jogo
    modoDeJogo()

    try:
        mode = int(input('Digite o modo de jogo:'))
    except (ValueError, TypeError):
        print('Resposta inválida. Tente novamente!')

    if mode == 1:
        result = escolhe_disputa(player1, player2,cartas_embaralhadas, modo_aleatorio)
    elif mode == 2:
        result = escolhe_disputa(player1, player2, cartas_embaralhadas, modo_manual)
    else:
        print('Modo inexistente!')
        os.system('pause')
    
    partidas = 0
    while partidas != 10:
        if mode == 1:
            result = escolhe_disputa(player1, player2,cartas_embaralhadas, modo_aleatorio)
        elif mode == 2:
            result = escolhe_disputa(player1, player2, cartas_embaralhadas, modo_manual)
        else:
            print('Modo inexistente!')
            os.system('pause')
        partidas -= 1
        jogador1pontos = 0
        jogador2pontos = 0      
        if result[0] > result[1]:
            jogador1pontos += 1
        else:
            jogador2pontos += 1
    if jogador1pontos > jogador2pontos:
        print('Jogador 1 venceu!!')
        return nick1
    elif jogador1pontos < jogador2pontos:
        print('Jogador 2 venceu!!')
        return nick2
    else:
        print(final(player1, player2))
        

def Iniciar(dicionario): # Essa função pega o nick do usuário e vê se ja existe, em caso afirmativo mostra. O parametro "dicionario" é o dicionario com todos os cadastrados
    menuIniciar()
    y = input('Digite 0 para iniciar:')
    if y == '0':
        menuIniciar()
        try:
            iniciar = int(input(':'))
        except (ValueError, TypeError):
            print('Ação inválida, tente novamente!')
            
        else:
            
            if iniciar == 1:
                nick1 = input('[JOGADOR 1]   nickname:')
                nick2 = input('[JOGADOR 2]   nickname:')
                verificaExistencia(nick1, dicionario)
                verificaExistencia(nick2, dicionario)
                ((dicionario[nick1])[0] + 1)
                ((dicionario[nick2])[0] + 1)
                jogo = main(nick1, nick2)
                if jogo == nick1:
                    ((dicionario[jogo])[1] + 1)
                elif jogo == nick2:
                    ((dicionario[jogo])[1] + 1)
                else:
                    print('Sem vencedores!')
                

                
            elif iniciar == 2:
                os.system('Pause')
                
                
        return dicionario               
                    
                    
                    
                        
                    
            
        
# CRIANDO LISTA COM TODAS AS CARTAS

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

# EMBARALHANDO LISTA DE CARTAS

cartas_embaralhadas = embaralhaLista(listaCartas)

# DESTRIBUINDO CARTA AOS JOGADORES E MOSTRANDO-AS:

player1 = destribui(cartas_embaralhadas,5)
player2 = destribui(cartas_embaralhadas,5)

for i in player1:
    print(exibicaoCartas(1,i.nome,i.valor,i.forca,i.energia,i.jokenpo))
for j in player2:
    print(exibicaoCartas(2,j.nome,j.valor,j.forca,j.energia,j.jokenpo))

cadastro_Geral = {} #Esse dicionario armazena como chave o nome do nick de cada usuário e como valor, uma lista com patidas jogadas, partidas vencidas e taxa de sucesso do jogador
inicio = Iniciar(cadastro_Geral)
escreveTXT(inicio,'Cadastro.txt')

os.system('pause')






    
