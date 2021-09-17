from random import randint
def sorteiaCarta(cartasDoJogador): # essa função sorteia um número no intervalo da quantidade de cartas que o jogador tem. Esse numero sera utilizado para estabelecer a posição da carta que jogador jogará
    posicao = randint(0,len(cartasDoJogador)-1)
    return posicao

lista = [1,2,34,5,7,8]
numero = sorteiaCarta(lista)
print(lista)
print(" ")
print(numero)
print(lista[numero])
lista.pop(numero)
print('')
print(lista)
