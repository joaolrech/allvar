import os

def inptFloat(desc):
    while True:
        try:
            return float(input(desc))
        except ValueError:
            print('Entrada inválida. Tente novamente.')

def inptMenu():
    while True:
        print('Selecione a operação desejada:')
        print('+ Adição')
        print('- Subtração')
        print('* Multiplicação')
        print('/ Divisão')
        print('^ Exponenciação\n')
        print('X SAIR\n')
        inpt = input().upper()
        if inpt not in ['+', '-', '*', '/', '^', 'X']:
            os.system('clear')
            print('Entrada inválida. Tente novamente\n')
        else:
            return inpt

def entrada(titulo):
    print(f'{titulo}\n')
    x = inptFloat('Digite o 1º termo da operação: ')
    y = inptFloat('Digite o 2º termo da operação: ')
    os.system('clear')
    return x, y

def calcular(operacao):
    match operacao:
        case '+':
            x, y = entrada('SOMA')
            z = x + y
        case '-':
            x, y = entrada('SUBTRAÇÃO')
            z = x - y
        case '*':
            x, y = entrada('MULTIPLICAÇÃO')
            z = x * y
        case '/':
            x, y = entrada('DIVISÃO')
            if y == 0:
                print('Impossível dividir por 0.\n')
                return
            else:
                z = x / y
        case '^':
            x, y = entrada('EXPONENCIAÇÃO')
            z = x ** y

    print(f'{x:g} {op} {y:g} = {z:g}\n')

os.system('clear')
print('Bem vindo à calculadora!\n')

while True:
    op = inptMenu()
    os.system('clear')

    if op == 'X':
        break
        
    calcular(op)
