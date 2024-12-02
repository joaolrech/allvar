import os

def adicao():
    print('SOMA')
    print('\n')
    x = float(input('Digite o 1º termo da operação: '))
    y = float(input('Digite o 2º termo da operação: '))
    os.system("clear")
    print('Somando {:.2f} com {:.2f}: {:.2f}'.format(x, y, x + y))
    print('\n')

def subtracao():
    print('SUBTRAÇÃO')
    print('\n')
    x = float(input('Digite o 1º termo da operação: '))
    y = float(input('Digite o 2º termo da operação: '))
    os.system("clear")
    print('Subtraindo {:.2f} de {:.2f}: {:.2f}'.format(y, x, x - y))
    print('\n')

def multiplicacao():
    print('MULTIPLICAÇÃO')
    print('\n')
    x = float(input('Digite o 1º termo da operação: '))
    y = float(input('Digite o 2º termo da operação: '))
    os.system("clear")
    print('Multiplicando {:.2f} por {:.2f}: {:.2f}'.format(x, y, x * y))
    print('\n')

def divisao():
    print('DIVISÃO')
    print('\n')
    x = float(input('Digite o 1º termo da operação: '))
    y = float(input('Digite o 2º termo da operação: '))
    os.system("clear")
    if y == 0:
        print('Impossível dividir por 0.')
    else:
        print('Dividindo {:.2f} por {:.2f}: {:.2f}'.format(x, y, x / y))
    print('\n')

def exponenciacao():
    print('EXPONENCIAÇÃO')
    print('\n')
    x = float(input('Digite o 1º termo da operação: '))
    y = float(input('Digite o 2º termo da operação: '))
    os.system("clear")
    print('Elevando {:.2f} a {:.2f}: {:.2f}'.format(x, y, x ** y))
    print('\n')

def radiciacao():
    print('RADICIAÇÃO')
    print('\n')
    x = float(input('Digite o 1º termo da operação: '))
    y = float(input('Digite o 2º termo da operação: '))
    os.system("clear")
    print('Radiciando {:.2f} de {:.2f}: {:.2f}'.format(x, y, x ** (1 / y)))
    print('\n')

while True:
    os.system("clear")
    print('Bem vindo à calculadora.py!')
    print('\n')
    print('Selecione a operação desejada: ')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Exponenciação')
    print('6 - Radiciação')
    print('\n')
    print('0 - SAIR')
    print('\n') 
    operacao = int(input())
    while operacao < 0 or operacao > 6:
        operacao = int(input('Operação inválida. Tente novamente: '))
    if operacao == 0:
        break

    os.system("clear")

    match operacao:
        case 1:
            adicao()
        case 2:
            subtracao()
        case 3:
            multiplicacao()
        case 4:
            divisao()
        case 5:
            exponenciacao()
        case 6:
            radiciacao()

    print('Deseja realizar outra operação?')
    print('\n')    
    print('1 - SIM')
    print('0 - NÃO')
    print('\n') 
    operacao = int(input())
    while operacao < 0 or operacao > 1:
        operacao = int(input('Opção inválida. Tente novamente: '))
    if operacao == 0:
        break

os.system("clear")
print('Programa finalizado.')