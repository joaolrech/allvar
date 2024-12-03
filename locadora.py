import os

def inpintfix():
    while True:
        try:
            inp = int(input())
            if inp < 0 or inp > 2:
                raise ValueError
            return inp
        except ValueError:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')
            menu()

def inpintvar(quant, state):
    while True:
        try:
            inp = int(input())
            if inp < 0 or inp > quant:
                raise ValueError
            return inp
        except ValueError:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')
            listar(state)

def inpint(desc):
    while True:
        try:
            inp = int(input(desc))
            if inp < 1:
                raise ValueError
            return inp
        except ValueError:
            print('Entrada inválida. Tente novamente.')

def menu():
    print('Selecione a opção desejada: ')
    print('1 - Locar veículo')
    print('2 - Devolver veículo \n')
    print('0 - SAIR')

def listar(var):
    if var == 'disp':
        print('Veículos disponíveis: \n')
        for i, (veiculo, preco) in enumerate(disponiveis.items(), start = 1):
            print(f'{i} - {veiculo} - R${preco}.00/dia')
    if var == 'loc':
        if locados:
            print('Veículos locados: \n')
            for i, veiculo in enumerate(locados, start = 1):
                print(f'{i} - {veiculo}')
        else:
            print('Nenhum veículo está locado.')
    print('\n0 - VOLTAR')

def catdisponiveis():
    state = 'disp'
    listar(state)
    escolha = inpintvar(len(disponiveis), state)
    os.system("clear")
    if escolha == 0:
        return
    veiculolocado = list(disponiveis.keys())[escolha - 1]
    print(f'{veiculolocado} locado. \n')
    locados[veiculolocado] = disponiveis.pop(veiculolocado)

def catlocados():
    state = 'loc'
    listar(state)
    escolha = inpintvar(len(locados), state)
    os.system("clear")
    if escolha == 0:
        return
    veiculodevolvido = list(locados.keys())[escolha - 1]
    dias = inpint(f'Digite quantos dias você ficou com o {veiculodevolvido}: ')
    os.system("clear")
    print(f'{veiculodevolvido} devolvido.')
    print(f'Valor em haver: R${locados[veiculodevolvido] * dias}.00 \n')
    disponiveis[veiculodevolvido] = locados.pop(veiculodevolvido)

disponiveis = {'Model 3':90, 'Model S':150, 'Model Y':125, 'Model X':110}
locados = {}

os.system("clear")
print('Bem vindo à locadora.py! \n')

while True:
    menu()
    opcao = inpintfix()
    os.system('clear')

    match opcao:
        case 1:
            catdisponiveis()
        case 2:
            catlocados()
        case 0:
            break

os.system("clear")
print('Programa finalizado.')