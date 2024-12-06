import os
import random

def inptcaracter(desc):
    while True:
        inpt = input(desc).upper()
        if inpt not in ['X', 'O']:
            os.system("clear")
            print('Entrada inválida. Tente novamente\n')
        else:
            os.system('clear')
            return inpt

def printjogo(s):
    print(f'{s[0]} {s[1]} {s[2]}')
    print(f'{s[3]} {s[4]} {s[5]}')
    print(f'{s[6]} {s[7]} {s[8]}')

def inptjogada():
    while True:
        try:
            print('Selecione a posição em que deseja jogar.\n')
            printjogo(situacao)
            print('\n0 - FINALIZAR\n')
            inpt = int(input())
            if inpt < 0 or inpt > 10:
                raise
            return inpt
        except:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')

situacao = [i + 1 for i in range(9)]

os.system('clear')
print('Bem vindo ao jogo da velha!\n')

while True:
    jogada = inptjogada()
    break