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
                raise
            return inpt
        except:
            os.system("clear")
            print('Entrada inválida. Tente novamente.')
            printmenu()

pointscomp = 0
pointsus = 0

os.system("clear")

while True:
    printplacar()
    printmenu()
    usuario = inptmenu()
    computador = random.randint(1, 3)

    if usuario == 1:
        if computador == 1:
            os.system("clear")
            print('Sua jogada: Pedra')
            print('Jogada do computador: Pedra')
            print('Empate.\n')
        if computador == 2:
            os.system("clear")
            print('Sua jogada: Pedra')
            print('Jogada do computador: Papel')
            print('Computador ganhou.\n')
            pointscomp += 1
        if computador == 3:
            os.system("clear")
            print('Sua jogada: Pedra')
            print('Jogada do computador: Tesoura')
            print('Você ganhou.\n')
            pointsus += 1
    if usuario == 2:
        if computador == 1:
            os.system("clear")
            print('Sua jogada: Papel')
            print('Jogada do computador: Pedra')
            print('Você ganhou.\n')
            pointsus += 1
        if computador == 2:
            os.system("clear")
            print('Sua jogada: Papel')
            print('Jogada do computador: Papel')
            print('Empate.\n')
        if computador == 3:
            os.system("clear")
            print('Sua jogada: Papel')
            print('Jogada do computador: Tesoura')
            print('Computador ganhou.\n')
            pointscomp += 1
    if usuario == 3:
        if computador == 1:
            os.system("clear")
            print('Sua jogada: Tesoura')
            print('Jogada do computador: Pedra')
            print('Computador ganhou.\n')
            pointscomp += 1
        if computador == 2:
            os.system("clear")
            print('Sua jogada: Tesoura')
            print('Jogada do computador: Papel')
            print('Você ganhou.\n')
            pointsus += 1
        if computador == 3:
            os.system("clear")
            print('Sua jogada: Tesoura')
            print('Jogada do computador: Tesoura')
            print('Empate.\n')
    if usuario == 0:
        break

os.system("clear")
print('Programa finalizado.')