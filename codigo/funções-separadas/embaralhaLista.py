from random import randint
def sorteia(num): #essa função recebe um numero e sorteia, sem repetir, a qntd de vezes digitada
    listaSort = []
    while len(listaSort) < num+1:
        for i in range (num):
            sorteio = randint(0,num)
            if sorteio not in listaSort:
                listaSort.append(sorteio)
    return listaSort

def embaralhalista(lista):
    listaEmbaralhada = []
    cartasAleatorias = sorteia(len(lista)-1)
    for j in cartasAleatorias:
        listaEmbaralhada.append(lista[j])
    return listaEmbaralhada
lista = ['k','r','t','u']
print(embaralhalista(lista))
