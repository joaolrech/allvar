import os
import random

def printplacar():
    print('COMPUTADOR: ', pointscomp, end='')
    print('        ', end='')
    print('USUÁRIO: ', pointsus)

def printmenu():
    print('\n1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura\n')
    print('0 - SAIR\n')

def inptmenu():
    while True:
        try:
            inpt = int(input())
            if inpt < 0 or inpt > 3:
                raise ValueError
            return inpt
        except ValueError:
            os.system("clear")
            print('Entrada inválida. Tente novamente.')
            printmenu()

def won(points):
    points += 1
    print("Sua jogada")

pointscomp = 0
pointsus = 0

while True:
    printplacar()
    printmenu()
    usuario = inptmenu()
    computador = random.randint(1, 3)

    if usuario == 1:
        if computador == 2:
            pointscomp += 1
            jogadaus = 
            jogadacomp = 
        else:
            won(pointscomp)
    if usuario == 2:
        if computador == 1:
            pointsus += 1
        else:
            pointscomp += 1
    if usuario == 3:
        if computador == 1:
            pointscomp += 1
        else:
            pointsus += 1
    if usuario == 0:
        break

os.system("clear")
print('Programa finalizado.')