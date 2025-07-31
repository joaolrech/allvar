import os

def inptEscolha(quant, lista):
    while True:
        try:
            inpt = int(input())
            if inpt < 0 or inpt > quant:
                raise ValueError
            return inpt
        except ValueError:
            os.system('clear')
            print('Entrada inválida. Tente novamente.\n')
            listar(lista)

def inptMenu():
    while True:
        try:
            print('Selecione a opção desejada: ')
            print('1 - Locar veículo')
            print('2 - Devolver veículo \n')
            print('0 - SAIR \n')
            inpt = int(input())
            if inpt < 0 or inpt > 2:
                raise ValueError
            return inpt
        except ValueError:
            os.system('clear')
            print('Entrada inválida. Tente novamente.\n')

def inptDias(desc):
    while True:
        try:
            inpt = int(input(desc))
            if inpt < 1:
                raise ValueError
            return inpt
        except ValueError:
            print('Entrada inválida. Tente novamente.')

def listar(lista):
    if lista:
        print('Veículos ', end='')
        print('disponíveis:' if lista is disponiveis else 'locados:')

        for i, (veiculo, preco) in enumerate(lista, start = 1):
            if lista is disponiveis:
                print(f'{i} - {veiculo} - R${preco:.2f}/dia')
            else:
                print(f'{i} - {veiculo}')
    else:
        print('Nenhum veículo está ', end='')
        print('disponível.' if lista is disponiveis else ' locado.')

    print('\n0 - VOLTAR\n')

def tramit(lista):
    listar(lista)
    escolha = inptEscolha(len(lista), lista)
    os.system('clear')

    if escolha == 0:
        return

    escolhido = lista[escolha - 1][0]

    if lista is disponiveis:
        print(f'{escolhido} locado.\n')
        locados.append(disponiveis.pop(escolha - 1))
    else:
        dias = inptDias(f'Digite quantos dias você ficou com o {escolhido}: ')
        os.system('clear')
        print(f'{escolhido} devolvido.')
        print(f'Valor em haver: R${locados[escolha - 1][1] * dias:.2f}\n')
        disponiveis.append(locados.pop(escolha - 1))

disponiveis = [
    ('Dolphin', 87.06),
    ('Han', 405.83),
    ('King', 124.05),
    ('Seal', 197.92),
    ('Shark', 306.42),
    ('Song', 133.06),
    ('Tan', 374.14),
    ('Yuan', 132.2),
]
locados = []

os.system('clear')
print('Bem vindo à locadora de veículos!\n')

while True:
    opcao = inptMenu()
    os.system('clear')

    if opcao == 0:
        break

    tramit(disponiveis if opcao == 1 else locados)
