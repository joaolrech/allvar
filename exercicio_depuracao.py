import os
import random

jogadas = [
    'Pedra',
    'Papel',
    'Tesoura'
]
placarpc = 0
placarus = 0

os.system("clear")
print('Bem vindo ao jokenpô!\n')

while True:
    print('          PLACAR')
    print(f'COMPUTADOR: {placarpc} | USUÁRIO: {placarus}')
    print('\n1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura\n')
    print('0 - SAIR\n')

    computador = random.choice(jogadas)
    usuario = int(input())
    if usuario == 0:
        break
    usuario = jogadas[usuario - 1]

    os.system("clear")
    print('Sua jogada:', usuario)
    print('Jogada do computador:', computador)
    
    if usuario == jogadas[0]:
        if computador == jogadas[0]:
            print('Empate.\n')
        if computador == jogadas[1]:
            placarpc += 1
            print('Computador ganhou.\n')
        if computador == jogadas[2]:
            placarus += 1
            print('Você ganhou.\n')
    if usuario == jogadas[1]:
        if computador == jogadas[0]:
            placarus += 1
            print('Você ganhou.\n')
        if computador == jogadas[1]:
            print('Empate.\n')
        if computador == jogadas[2]:
            placarpc += 1
            print('Computador ganhou.\n')
    if usuario == jogadas[2]:
        if computador == jogadas[0]:
            placarpc += 1
            print('Computador ganhou.\n')
        if computador == jogadas[1]:
            placarus += 1
            print('Você ganhou.\n')
        if computador == jogadas[2]:
            print('Empate.\n')

os.system("clear")
print('Programa finalizado.')