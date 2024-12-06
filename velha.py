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

def printjogo(x):
    print(f'{x[6]} {x[7]} {x[8]}')
    print(f'{x[3]} {x[4]} {x[5]}')
    print(f'{x[0]} {x[1]} {x[2]}')

def inptjogada():
    while True:
        try:
            print('Selecione a posição em que deseja jogar.\n')
            printjogo(situacao)
            print('\n0 - FINALIZAR\n')
            inpt = int(input())
            if inpt < 0 or inpt > 9:
                raise
            os.system('clear')
            return inpt - 1
        except:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')

def geradordejogada(situacao):
    while True:
        jogada = random.randint(0, 8)
        if type(situacao[jogada]) == int:
            return jogada

def verificajogada(situacao):
    while True:
        jogada = inptjogada()
        if type(situacao[jogada]) == int:
            return jogada

situacao = [i + 1 for i in range(9)]

os.system('clear')
print('Bem vindo ao jogo da velha!\n')

usuario = 'X'
computador = 'O'

while True:
    jogadaus = verificajogada(situacao)
    if jogadaus == -1:
        break
    jogadapc = geradordejogada(situacao)
    situacao[jogadaus] = usuario
    situacao[jogadapc] = computador

os.system("clear")
print('Programa finalizado.')