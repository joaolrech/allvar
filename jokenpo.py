import os
import random

def inptJogada():
    while True:
        try:
            print('          PLACAR')
            print(f'COMPUTADOR: {placarComputador} | USUÁRIO: {placarUsuario}')

            print('\n1 - Pedra')
            print('2 - Papel')
            print('3 - Tesoura\n')
            print('0 - SAIR\n')
            inpt = int(input())
            if inpt not in range(4):
                raise ValueError
            return inpt
        except ValueError:
            os.system('clear')
            print('Entrada inválida. Tente novamente.\n')

def verificar(usuario, computador):
    global placarUsuario, placarComputador
    
    if regras[usuario] == computador:
        placarUsuario += 1
        print('Você ganhou!\n')
    elif regras[computador] == usuario:
        placarComputador += 1
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
placarComputador = 0
placarUsuario = 0

os.system('clear')
print('Bem vindo ao jokenpô!\n')

while True:
    computador = random.choice(jogadas)
    usuario = inptJogada()
    if usuario == 0:
        break
    usuario = jogadas[usuario - 1]

    os.system('clear')
    print('Sua jogada:', usuario)
    print('Jogada do computador:', computador)

    verificar(usuario, computador)

os.system('clear')
