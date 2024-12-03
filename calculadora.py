import os

def inpfloat():
    while True:
        try:
            return float(input())
        except ValueError:
            print('Entrada inválida. Tente novamente: ', end='')

def inpstr():
    while True:
        try:
            inp = input().upper().strip()
            if inp not in ['+', '-', '*', '/', 'X']:
                raise ValueError
            return inp
        except ValueError:
            os.system("clear")
            print('Entrada inválida. Tente novamente. \n')
            menu()

def menu():
    print('Selecione a operação desejada: ')
    print('+ Adição')
    print('- Subtração')
    print('* Multiplicação')
    print('/ Divisão \n')
    print('X SAIR')

def entrada(titulo):
    print(f'{titulo} \n')
    print(f'Digite o 1º termo da operação: ', end='')
    x = inpfloat()
    print(f'Digite o 2º termo da operação: ', end='')
    y = inpfloat()
    os.system("clear")
    return x, y

def adicao(x, y):
    print(f'{x:g} + {y:g} = {x + y:g} \n')

def subtracao(x, y):
    print(f'{x:g} - {y:g} = {x - y:g} \n')

def multiplicacao(x, y):
    print(f'{x:g} * {y:g} = {x * y:g} \n')

def divisao(x, y):
    if y == 0:
        print('Impossível dividir por 0. \n')
    else:
        print(f'{x:g} / {y:g} = {x / y:g} \n')

os.system("clear")
print('Bem vindo à calculadora.py! \n')

while True:

    menu()

    operacao = inpstr()

    if operacao == 'X':
        break

    os.system("clear")

    match operacao:
        case '+':
            x, y = entrada('SOMA')
            adicao(x, y)
        case '-':
            x, y = entrada('SUBTRAÇÃO')
            subtracao(x ,y)
        case '*':
            x, y = entrada('MULTIPLICAÇÃO')
            multiplicacao(x, y)
        case '/':
            x, y = entrada('DIVISÃO')
            divisao(x, y)

os.system("clear")
print('Programa finalizado.')