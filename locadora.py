import os

def inptint(desc, rang, minimo):
    while True:
        try:
            inpt = int(input(desc))
            if rang:
                if inpt not in rang:
                    raise ValueError
            if minimo:
                if inpt < minimo:
                    raise ValueError
            return inpt
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def printmenu():
    print('Selecione a opção desejada:')
    print('1 - Locar veículo')
    print('2 - Devolver veículo\n')
    print('0 - SAIR\n')

def listar(lista):
    if lista:
        print('Veículos ', end='')
        print('disponíveis:' if lista is disponiveis else 'locados:')

        for i, (veiculo, preco) in enumerate(lista, start = 1):
            if lista == disponiveis:
                print(f'{i} - {veiculo} - R${preco:.2f}/dia')
            else:
                print(f'{i} - {veiculo}')
    else:
        print('Nenhum veículo está ', end='')
        print('disponível.' if lista is disponiveis else ' locado.')
        
    print('\n0 - VOLTAR\n')

def tramit(lista):
    listar(lista)
    escolha = inptint('', range(len(lista) + 1), None)
    os.system("clear")

    if escolha == 0:
        return

    escolhido = lista[escolha - 1][0]

    if lista == disponiveis:
        print(f'{escolhido} locado.\n')
        locados.append(disponiveis.pop(escolha - 1))
    else:
        dias = inptint(f'Digite quantos dias você ficou com o {escolhido}: ', None, 1)
        os.system("clear")
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

os.system("clear")
print('Bem vindo à locadora de veículos!\n')

while True:
    printmenu()
    opcao = inptint('', range(3), None)
    os.system('clear')

    if opcao == 0:
        break

    tramit(disponiveis if opcao == 1 else locados)

os.system("clear")
print('Programa finalizado.')