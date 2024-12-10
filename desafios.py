# Nesse programa, nas linhas 73, 77 e 86, o criador do código deixou anotado os possíveis problemas e as futuras melhorias.
# Implemente as melhorias para solucionar os problemas apontados, utilizando seu conhecimento em funções.
# Resolva primeiro o desafio 1, e depois o desafio 2.

import os

def inptmenu():
    while True:
        try:
            inpt = int(input())
            if inpt < 0 or inpt > 2:
                raise ValueError
            return inpt
        except ValueError:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')
            printmenu()

def inptdias(desc):
    while True:
        try:
            inpt = int(input(desc))
            if inpt < 1:
                raise ValueError
            return inpt
        except ValueError:
            print('Entrada inválida. Tente novamente.')

def printmenu():
    print('Selecione a opção desejada: ')
    print('1 - Locar veículo')
    print('2 - Devolver veículo \n')
    print('0 - SAIR \n')

def listar(lista):
    if lista == disponiveis:
        if disponiveis:
            print('Veículos disponíveis:')
            for i, (veiculo, preco) in enumerate(disponiveis, start = 1):
                print(f'{i} - {veiculo} - R${preco:.2f}/dia')
        else:
            print('Nenhum veículo está disponível.')
    if lista == locados:
        if locados:
            print('Veículos locados:')
            for i, (veiculo, preco) in enumerate(locados, start = 1):
                print(f'{i} - {veiculo}')
        else:
            print('Nenhum veículo está locado.')
    print('\n0 - VOLTAR \n')

disponiveis = [
    ['Dolphin', 87.06],
    ['Han', 405.83],
    ['King', 124.05],
    ['Seal', 197.92],
    ['Shark', 306.42],
    ['Song', 133.06],
    ['Tan', 374.14],
    ['Yuan', 132.2],
]
locados = []

os.system("clear")
print('Bem vindo à locadora.py! \n')

while True:
    printmenu()
    opcao = inptmenu()
    os.system('clear')
    
    # Desafio 2 - A estrutura do case 1 e 2 é muito parecida e poderia ser simplificada
    match opcao:
        case 1:
            listar(disponiveis)
            escolha = int(input()) # Desafio 1 - A entrada está suscetível a erros
            os.system("clear")
            if escolha == 0:
                continue
            veiculolocado = disponiveis[escolha - 1][0]
            print(f'{veiculolocado} locado. \n')
            locados.append(disponiveis.pop(escolha - 1))
        case 2:
            listar(locados)
            escolha = int(input()) # Desafio 1 - A entrada está suscetível a erros
            os.system("clear")
            if escolha == 0:
                continue
            veiculodevolvido = locados[escolha - 1][0]
            dias = inptdias(f'Digite quantos dias você ficou com o {veiculodevolvido}: ')
            os.system("clear")
            print(f'{veiculodevolvido} devolvido.')
            print(f'Valor em haver: R${locados[escolha - 1][1] * dias:.2f} \n')
            disponiveis.append(locados.pop(escolha - 1))
        case 0:
            break

os.system("clear")
print('Programa finalizado.')