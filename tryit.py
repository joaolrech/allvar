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
            if inpt == 0:
                return -1  # Permite ao jogador finalizar o jogo
            if inpt < 1 or inpt > 9:
                raise ValueError
            os.system("clear")
            return inpt - 1
        except ValueError:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')

def geradordejogada(situacao):
    posicoes_vazias = [i for i, pos in enumerate(situacao) if type(pos) == int]
    if posicoes_vazias:
        return random.choice(posicoes_vazias)
    return -1  # Caso não haja posições vazias, o jogo acabou

def verificajogada(situacao):
    while True:
        jogada = inptjogada()
        if jogada == -1:  # Verifica se o jogador deseja sair
            return jogada
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

def verificar_empate(situacao):
    # Verifica se todas as posições estão preenchidas com caracteres (X ou O)
    return all(isinstance(pos, str) for pos in situacao)

situacao = [i + 1 for i in range(9)]

os.system('clear')
print('Bem-vindo ao jogo da velha!\n')

usuario = inptcaracter('Deseja ser X ou O?\n\n')
if usuario == 'X':
    computador = 'O'
else:
    computador = 'X'

while True:
    jogadaus = verificajogada(situacao)
    if jogadaus == -1:  # Jogador escolheu finalizar
        print('Programa finalizado.')
        break
    situacao[jogadaus] = usuario
    ganhou = verificavencedor(situacao)
    if ganhou:
        printjogo(situacao)
        print('\nVocê ganhou.\n')
        break

    jogadapc = geradordejogada(situacao)
    if jogadapc == -1:  # Caso o computador não tenha jogadas válidas
        printjogo(situacao)
        print('\nO jogo terminou em empate.\n')
        break
    situacao[jogadapc] = computador
    ganhou = verificavencedor(situacao)
    if ganhou:
        printjogo(situacao)
        print('\nComputador ganhou.\n')
        break

    if verificar_empate(situacao):
        printjogo(situacao)
        print('\nO jogo terminou em empate.\n')
        break

print('Programa finalizado.')
