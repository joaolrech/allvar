import os

def adicao(x, y):
    return x + y
def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x * y
def divisao(x, y):
    return x / y
def exponenciacao(x, y):
    return x ** y
def radiciacao(x, y):
    return x ** (1 / y)

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

operacao = int(input())
while operacao < 0 or operacao > 6:
    operacao = int(input('Operação inválida. Tente novamente: '))

os.system("clear")

match operacao:
    case 0:
        print('Programa finalizado.')
        exit()
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
