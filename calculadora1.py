import os

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
        os.system("clear")
        print('Programa finalizado.')
        exit()

    os.system("clear")

    match operacao:
        case 1:
            print('SOMA')
            print('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            print('\n')
            print('Somando {:.2f} com {:.2f}: {:.2f}'.format(x, y, x + y))
            print('\n')
        case 2:
            print('SUBTRAÇÃO')
            print('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            print('\n')
            print('Subtraindo {:.2f} de {:.2f}: {:.2f}'.format(y, x, x - y))
            print('\n')
        case 3:
            print('MULTIPLICAÇÃO')
            print('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            print('\n')
            print('Multiplicando {:.2f} por {:.2f}: {:.2f}'.format(x, y, x * y))
            print('\n')
        case 4:
            print('DIVISÃO')
            print('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            print('\n')
            if y == 0:
                print('Impossível dividir por 0.')
            else:
                print('Dividindo {:.2f} por {:.2f}: {:.2f}'.format(x, y, x / y))
            print('\n')
        case 5:
            print('EXPONENCIAÇÃO')
            print('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            print('\n')
            print('Elevando {:.2f} a {:.2f}: {:.2f}'.format(x, y, x ** y))
            print('\n')
        case 6:
            print('RADICIAÇÃO')
            print('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            print('\n')
            print('Radiciando {:.2f} de {:.2f}: {:.2f}'.format(x, y, x ** (1 / y)))
            print('\n')

    print('Deseja realizar outra operação?')
    print('\n')    
    print('1 - SIM')
    print('0 - NÃO')
    print('\n') 
    operacao = int(input())
    while operacao < 0 or operacao > 1:
        operacao = int(input('Opção inválida. Tente novamente: '))

    if operacao == 0:
        os.system("clear")
        print('Programa finalizado.')
        exit()