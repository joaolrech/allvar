import os
import random

def inptcaracter(desc):
    while True:
        inpt = input(desc).upper()
        if inpt not in ['X', 'O']:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')
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
                raise ValueError
            os.system("clear")
            return inpt - 1
        except ValueError:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')

def geradordejogada(situacao):
    while True:
        jogada = random.randint(0, 8)
        if type(situacao[jogada]) != int:
            continue
        return jogada

def verificajogada(situacao):
    while True:
        jogada = inptjogada()
        if type(situacao[jogada]) != int:
            os.system("clear")
            print('Posição inválida. Tente novamente.\n')
            continue
        return jogada
            
def verificavencedor(x):
    if x[0] == x[1] == x[2]:
        return True
    elif x[3] == x[4] == x[5]:
        return True
    elif x[6] == x[7] == x[8]:
        return True
    elif x[0] == x[3] == x[6]:
        return True
    elif x[1] == x[4] == x[7]:
        return True
    elif x[2] == x[5] == x[8]:
        return True
    elif x[2] == x[4] == x[6]:
        return True
    elif x[0] == x[4] == x[8]:
        return True
    else:
        return False

situacao = [i + 1 for i in range(9)]

os.system('clear')
print('Bem vindo ao jogo da velha!\n')

usuario = inptcaracter('Deseja ser X ou O?\n\n')
computador = 'O' if usuario == 'X' else 'X'

while True:
    jogadaus = verificajogada(situacao)
    if jogadaus == -1:
        break
    situacao[jogadaus] = usuario
    ganhou = verificavencedor(situacao)
    if ganhou:
        printjogo(situacao)
        print('\nVocê ganhou.\n')
        break
    if all(type(pos) != int for pos in situacao):
        printjogo(situacao)
        print('\nEmpate.\n')
        break

    jogadapc = geradordejogada(situacao)
    situacao[jogadapc] = computador
    ganhou = verificavencedor(situacao)
    if ganhou:
        printjogo(situacao)
        print('\nComputador ganhou.\n')
        break
    if all(type(pos) != int for pos in situacao):
        printjogo(situacao)
        print('\nEmpate.\n')
        break

print('Programa finalizado.')