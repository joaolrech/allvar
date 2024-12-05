import os
import random

def printplacar():
    print('          PLACAR')
    print(f'COMPUTADOR: {poinspc} | USUÁRIO: {pointsus}')

def printopcoes():
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
            printopcoes()

def verificar(us, comp):
    global pointsus, poinspc

    rules = {
    'Pedra': 'Tesoura',
    'Papel': 'Pedra',
    'Tesoura': 'Papel'
    }

    if rules[us] == comp:
        pointsus += 1
        return 'uswon'
    elif rules[comp] == us:
        poinspc += 1
        return 'pcwon'
    
jogadas = [
    'Pedra',
    'Papel',
    'Tesoura'
]
poinspc = 0
pointsus = 0

os.system("clear")

while True:
    printplacar()
    printopcoes()

    computador = random.choice(jogadas)
    usuario = inptjogada()
    if usuario == 0:
        break
    usuario = jogadas[usuario - 1]

    os.system("clear")
    print('Sua jogada:', usuario)
    print('Jogada do computador:', computador)
    
    winner = verificar(usuario, computador)

    if winner == 'uswon':
        print('Você ganhou.\n')
    elif winner == 'pcwon':
        print('Computador ganhou.\n')
    else:
        print('Empate.\n')

os.system("clear")
print('Programa finalizado.')