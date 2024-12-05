import os
import random

def inptjogada(desc):
    while True:
        inpt = input(desc).upper()
        if inpt not in ['X', 'O']:
            os.system("clear")
            print('Entrada inválida. Tente novamente\n')
        else:
            return inpt
    os.system('clear')
    if inpt == 'O':
        pc = 'X'
    else:
        inpt = 'O'

def printjogo(s):
    print(f'{s[0]} {s[1]} {s[2]}')
    print(f'{s[3]} {s[4]} {s[5]}')
    print(f'{s[6]} {s[7]} {s[8]}')

def printopcoes():
    print('Selecione a posição em que deseja jogar.\n')
    print('0 - FINALIZAR')



situacao = [i + 1 for i in range(9)]

os.system('clear')
print('Bem vindo ao jogo da velha! \n')
us = inptjogada('Deseja ser X ou O?\n\n')




while True:
    printjogo(situacao)
    break







