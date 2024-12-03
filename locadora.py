import os

def inpint:
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

def menu():
    print('Selecione a opção desejada: ')
    print('1 - Locar veículo')
    print('2 - Devolver veículo \n')
    print('0 - SAIR')

devolvidos = ['Model 3', 'Model S', 'Model Y', 'Model X', 'Cybertruck']
locados = []

while True:

    menu()

    opcao = inpint()

    if opcao == 0:
        break

    os.system('clear')

    match opcao:
        case 1:
            catdevolvidos()
        case 2:
            catlocados()

os.system("clear")
print('Programa finalizado.')