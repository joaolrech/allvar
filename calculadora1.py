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
        break

    os.system("clear")

    match operacao:
        case 1:
            print('SOMA')
            print('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            os.system("clear")
            print(f'Somando {x:g} com {y:g}: {x + y:g}')
            print('\n')
        case 2:
            print('SUBTRAÇÃO')
            ('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            os.system("clear")
            print(f'Subtraindo {y:g} de {x:g}: {x - y:g}')
            print('\n')
        case 3:
            print('MULTIPLICAÇÃO')
            print('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            os.system("clear")
            print(f'Multiplicando {x:g} por {y:g}: {x * y:g}')
            print('\n')
        case 4:
            print('DIVISÃO')
            print('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            os.system("clear")
            if y == 0:
                print('Impossível dividir por 0.')
            else:
                print(f'Dividindo {x:g} por {y:g}: {x / y:g}')
            print('\n')
        case 5:
            print('EXPONENCIAÇÃO')
            print('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            os.system("clear")
            print(f'Elevando {x:g} a {y:g}: {x ** y:g}')
            print('\n')
        case 6:
            print('RADICIAÇÃO')
            print('\n')
            x = float(input('Digite o 1º termo da operação: '))
            y = float(input('Digite o 2º termo da operação: '))
            os.system("clear")
            print(f'Radiciando {x:g} de {y:g}: {x / (1 / y):g}')
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
        break

os.system("clear")
print('Programa finalizado.')