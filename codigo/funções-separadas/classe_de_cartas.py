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

def embaralhaLista(lista):
    listaEmbaralhada = []
    cartasAleatorias = sorteia(len(lista)-1)
    for j in cartasAleatorias:
        listaEmbaralhada.append(lista[j])
    return listaEmbaralhada

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


