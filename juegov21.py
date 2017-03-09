#!/usr/bin/python3
from random import sample

def juego(pJugador, pCasa, lista):
    print(pJugador)
    if(pJugador==0 and pCasa==0):
        repartir(pJugador, pCasa, lista)
        return "Primera Ronda"
    if(input("Desa continuar ") != "N"):
        print("Casa "+str(listaC[0])+" ?")
        if(contar(listaJ)<=21):
            return repartir(listaJ,listaC,lista)
        else:
            return print("Perdio tiene: "+str(contar(listaJ)))
    elif(contar(listaJ)>21):
        return print("Perdio tiene: "+str(contar(listaJ)))
    elif(contar(listaJ)<=21):
        print("Tiene: "+str(contar(listaJ)))
        return juegoCasa(listaJ,listaC,lista)

def creadorbaraja():
    return sample([(x,y)for x in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']for y in ['DIAMANTES','TREBOLES','PICAS','CORAZONES']], 52)

def valor(carta):
    if carta[0] == 'J' or  carta[0] == 'K' or  carta[0] == 'Q':
        return 10
    elif carta[0] == 'A':
        return 10
    else:
        return carta[0]
def contarValores(pJugador):

def repartirIni(pJugador, pCasa, lista):
    print("Cartas jugador: " + str(lista[0]) + ", " + lista[2])
    print("Cartas casa: " + str(lista[1]) + ", " + lista[3])
    pJugador += valor(lista[0]) + valor(lista[2])
    pCasa += valor(lista[1]) + valor(lista[3])
    juego(pJugador, pCasa, lista[4:])

def repartir(pJugador, pCasa, lista):
    pJugador += valor(lista[0])
    pCasa += valor(lista[1])
    juego(pJugador, pCasa, lista[2:])

juego(,0,creadorbaraja())
