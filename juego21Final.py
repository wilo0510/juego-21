#!/usr/bin/python3
from random import sample

def juego(lJugador, lCasa, lista):
    print(lJugador)
    if(len(lJugador)==0 and len(lCasa)==0):
        repartirIni(lJugador, lCasa, lista)
        return "primera"
    else:
        if(contador(lJugador) <= 21):
            if(input("Desa continuar? (Y/N)").upper() != "N"):
                repartir(lJugador,lCasa,lista)
            elif(contador(lCasa) > 21):
                print("La casa empato: " + str(contador(lCasa)) + " a " + str(contador(lJugador)))
                return "final"
            elif(contador(lCasa) >= contador(lJugador)):
                print("La casa gano: " + str(contador(lCasa)) + " a " + str(contador(lJugador)))
                return "final"
            else:
                print("Usted gano: " + str(contador(lJugador)) + " a " + str(contador(lCasa)))
                return "final"
        else:
            return print("Perdio tiene: " + str(contador(lJugador)))

def creadorbaraja():
    return sample([(x,y)for x in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']for y in ['DIAMANTES','TREBOLES','PICAS','CORAZONES']], 52)

def valor(carta):
    if carta[0] == 'J' or  carta[0] == 'K' or  carta[0] == 'Q':
        return 10
    elif carta[0] == 'A':
        return 10
    else:
        return carta[0]

def contador(lista):
    if(len(lista)==0):
        return 0
    else:
        for i in range(0,len(lista)):
            return contador(lista[1:])+valor(lista[0])


def repartirIni(lJugador, lCasa, lista):
    lJugador.append(lista[0])
    lJugador.append(lista[2])
    lCasa.append(lista[1])
    lCasa.append(lista[3])
    print("Cartas jugador: " + str(lJugador))
    print("Cartas casa: " + str(lCasa))
    juego(lJugador, lCasa, lista[4:])

def repartir(lJugador, lCasa, lista):
    lJugador.append(lista[0])
    lCasa.append(lista[1])
    print("Cartas jugador: " + str(lJugador))
    print("Cartas casa: " + str(lCasa))
    juego(lJugador, lCasa, lista[2:])

juego([],[],creadorbaraja())
