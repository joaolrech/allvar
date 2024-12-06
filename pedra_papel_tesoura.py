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
            if inpt not in range(len(jogadas) + 1):
                raise
            return inpt
        except:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')
            printplacar()
            printopcoes()

def verificar(us, comp):
    global placarus, placarpc
    
    regras = {
    'Pedra': 'Tesoura',
    'Papel': 'Pedra',
    'Tesoura': 'Papel'
    }

    if regras[us] == comp:
        placarus += 1
        print('Você ganhou.\n')
    elif regras[comp] == us:
        placarpc += 1
        print('Computador ganhou.\n')
    else:
        print('Empate.\n')
    
jogadas = [
    'Pedra',
    'Papel',
    'Tesoura'
]
placarpc = 0
placarus = 0

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
    
    verificar(usuario, computador)

os.system("clear")
print('Programa finalizado.')