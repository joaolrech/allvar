# 1. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#    • A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
#    • A mensagem "Reprovado", se a média for menor do que 7;
#    • A mensagem "Aprovado com Distinção", se a média for igual a 10.

def q01():

    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))

    media = (nota1 + nota2) / 2

    print(f'Média: {media:.1f}')

    if media == 10:
        print('Aprovado com distinção.')
    elif media >= 7:
        print('Aprovado.')
    else:
        print('Reprovado.')

# 2. Escreva um script que leia três números e mostre o maior e o menor deles.

def q02():

    lista = []
    for i in range(3):
        lista.append(int(input(f'Digite o {i + 1}º número: ')))

    maior = max(lista)
    menor = min(lista)

    print('Maior número: ', maior)
    print('Menor número: ', menor)

# 3. Nome na vertical em escada.
#    F
#    FU
#    FUL
#    FULA
#    FULAN
#    FULANO

def q03():

    nome = input('Digite seu nome: ')

    for i in range(len(nome)):
        print(nome[:i + 1])

# 4. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
#    (o próximo termo, a partir do terceiro, é sempre gerado a partir do somatório dos últimos dois).
#    Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo usuário).

def q04():

    n = int(input('Digite quantos termos deseja: '))

    x, y = 1, 1
    
    if n >= 1:
        print(x)
    if n >= 2:
        print(y)

    for _ in range(2, n):
        z = x + y
        print(z)
        x, y = y, z

# 5. Faça um programa que leia e valide as seguintes informações:
#    • Nome: maior que 3 caracteres;
#    • Idade: entre 0 e 150;
#    • Salário: maior que zero;
#    • Sexo: 'f' ou 'm';
#    • Estado Civil: 's', 'c', 'v', 'd';

def q05():

    nome = input('Digite seu nome: ')
    while len(nome) <= 3:
        nome = input('Nome inválido. Tente novamente: ')
    print('Nome validado.')

    idade = int(input('Digite sua idade: '))
    while idade < 0 or idade > 150:
        idade = int(input('Idade inválida. Tente novamente: '))
    print('Idade validada.')

    salario = float(input('Digite seu salário: '))
    while salario <= 0:
        salario = float(input('Salário inválido. Tente novamente: '))
    print('Salário validado.')

    sexo = input('Digite seu sexo ("f" para feminino e "m" para masculino): ')
    while sexo not in ['f', 'm']:
        sexo = input('Sexo inválido. Tente novamente: ')
    print('Sexo validado.')

    estciv = input('Digite seu estado civil ("s" para solteiro, "c" para casado, "v" para viúvo, "d" para divorciado): ')
    while estciv not in ['s', 'c', 'v', 'd']:
        estciv = input('Estado civil inválido. Tente novamente: ')
    print('Estado civil validado.')

# 6. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#    Um número primo é aquele que é divisível somente por ele mesmo e por 1. Dica: Utilize o operador aritmético %,
#    que retorna o resto da divisão de dois números.

def q06():

    num = int(input('Digite um número inteiro: '))

    primo = True

    if num <= 1:
        primo = False

    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print('O número digitado é primo.')
    else:
        print('O número digitado não é primo.')

questao = int(input('Digite a questão a ser executada: '))

match questao:
    case 1:
        q01()
    case 2:
        q02()
    case 3:
        q03()
    case 4:
        q04()
    case 5:
        q05()
    case 6:
        q06()