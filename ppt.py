import os
import random

def printplacar():
    print('          PLACAR')
    print(f'COMPUTADOR: {pointscomp} | USUÁRIO: {pointsus}')

def printmenu():
    print('\n1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura\n')
    print('0 - SAIR\n')

def inptjogada():
    while True:
        try:
            inpt = int(input())
            if inpt not in range(len(jogadas) + 1):
                raise
            return inpt
        except:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')
            printplacar()
            printmenu()

def verificar(us, comp):
    global pointsus, pointscomp

    rules = {
    'Pedra': 'Tesoura',
    'Papel': 'Pedra',
    'Tesoura': 'Papel'
    }

    if rules[us] == comp:
        pointsus += 1
        return 'uswon'
    elif rules[comp] == us:
        pointscomp += 1
        return 'compwon'
    
jogadas = [
    'Pedra',
    'Papel',
    'Tesoura'
]
pointscomp = 0
pointsus = 0

os.system("clear")

while True:
    printplacar()
    printmenu()

    usuario = inptjogada()
    if usuario == 0:
        break
    usuario = jogadas[usuario - 1]

    computador = random.choice(jogadas)

    os.system("clear")
    print('Sua jogada:', usuario)
    print('Jogada do computador:', computador)
    
    winner = verificar(usuario, computador)

    if winner == 'uswon':
        print('Você ganhou.\n')
    elif winner == 'compwon':
        print('Computador ganhou.\n')
    else:
        print('Empate.\n')

os.system("clear")
print('Programa finalizado.')