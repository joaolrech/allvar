import os
import random

def printplacar():
    print('          PLACAR')
    print(f'COMPUTADOR: {placarpc} | USUÁRIO: {placarus}')

def printopcoes():
    print('\n1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura\n')
    print('0 - SAIR\n')

def inptjogada():
    while True:
        try:
            inpt = int(input())
            if inpt not in range(4):
                raise ValueError
            return inpt
        except ValueError:
            os.system('clear')
            print('Entrada inválida. Tente novamente.\n')
            printplacar()
            printopcoes()

def verificar(usuario, computador):
    global placarus, placarpc
    
    if regras[usuario] == computador:
        placarus += 1
        print('Você ganhou!\n')
    elif regras[computador] == usuario:
        placarpc += 1
        print('Computador ganhou!\n')
    else:
        print('Empate!\n')

jogadas = [
    'Pedra',
    'Papel',
    'Tesoura'
]
regras = {
'Pedra': 'Tesoura',
'Papel': 'Pedra',
'Tesoura': 'Papel'
}
placarpc = 0
placarus = 0

os.system('clear')
print('Bem vindo ao jokenpô!\n')

while True:
    printplacar()
    printopcoes()

    computador = random.choice(jogadas)
    usuario = inptjogada()
    if usuario == 0:
        break
    usuario = jogadas[usuario - 1]

    os.system('clear')
    print('Sua jogada:', usuario)
    print('Jogada do computador:', computador)

    verificar(usuario, computador)

os.system('clear')
print('Obrigado por jogar!')