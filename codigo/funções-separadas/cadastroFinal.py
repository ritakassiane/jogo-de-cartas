class Cadastro:
    def __init__(self):
        self.nick = ''
        self.partJogadas = 0
        self.partVencidas = 0
    def taxaSucesso(self):
        taxa = (self.partVencidas*100)/self.partJogadas
        return taxa



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
    

    
cadastro_Geral = {} #Esse dicionario armazena como chave o nome do nick de cada usuário e como valor, uma lista com patidas jogadas, partidas vencidas e taxa de sucesso do jogador
def verificaExistencia(nick, dicionario):# Essa função recebe o nick do usuário e verifica se ele existe no dicionario de cadastro
    if dicionario.get(nick) == None:
        dicionario[nick] = [0,0,0]
    else:
        for i in dicionario.keys():
            if i == nick:
                dados = dicionario[i]
                print(exibição_estatisticas(nick, dados[0], dados[1]))
                
def menuIniciar():
    print('-------------------------------------------------------------------------------------------------------------------------------------------------')
    print('                                                  J O G O   D A   D I S P U T A                                                                  ')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' 1. Jogar                                         ')
    print(' 2. Sair                                          ')


def Iniciar(dicionario): # Essa função pega o nick do usuário e vê se ja existe, em caso afirmativo mostra. O parametro "dicionario" é o dicionario com todos os cadastrados
    menuIniciar()
    while True:
        try:
            iniciar = int(input(':'))
        except (ValueError, TypeError):
            print('Ação inválida, tente novamente!')
            continue
        else:
            if iniciar == 1:
                for i in range(2):
                    nick = input(f'[JOGADOR {i+1}]   nickname:')
                    verificaExistencia(nick, dicionario)                
            elif iniciar == 2:
                os.system('Pause')




    
