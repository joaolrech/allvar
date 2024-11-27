#1. Utilizando o built-in method input(), crie um programa que receba a altura e opesode uma pessoa eimprima natelao IMC da mesma.

def q01():

    altura = float(input("Digite sua altura (m): "))
    peso = float(input("Digite seu peso (kg): "))

    imc = peso / altura ** 2

    print("Seu IMC é: {:.2f}".format(imc))

#2. Escreva um programa que pergunte o nome completo do usuário e cumprimente o mesmo pelo primeiro nome.

def q02():

    nome = input("Digite seu nome completo: ")

    nome1 = nome.split()

    print("Seja bem vindo, {}!".format(nome1[0]))

#3. Escreva um código que extraia o domínio de um e-mail informado.

def q03():

    email = input("Digite seu e-mail: ")

    emaildompol = email.split("@")
    emaildom = emaildompol[1].split(".")

    print("O domínio do e-mail informado é: ", emaildom[0])

#4. Faça um programa para uma loja de tintas. A pessoa informa a área em m2 que deseja pintar,
#   e o script calculará a quantidade de latas de tinta que a pessoa deve comprar e o valor.
#   Considere que cada litro de tinta pinta 3m2, que cada lata contém 18L e que custa R$ 80.

def q04():

    area = float(input("Digite a área que deseja pintar (m²): "))

    litros = area / 3
    latas = int(litros / 18)

    if litros % 18 != 0:
        latas += 1
    
    preco = latas * 80

    print("Você precisará de {} latas de tinta, e isso irá custar R${:.2f}".format(latas, preco))

#5. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#   Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#   8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#   • Salário bruto.
#   • Quanto pagou ao INSS.
#   • Quanto pagou ao sindicato.
#   • O salário líquido.

def q05():

    salphora = float(input("Digite quantos reais você ganha por hora: "))
    numhoras = float(input("Digite quantas horas você trabalha por mês: "))

    bruto = salphora * numhoras
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05
    liquido = bruto - ir - inss - sindicato

    print("Salário bruto: R${:.2f}".format(bruto))
    print("Pagou ao INSS: R${:.2f}".format(inss))
    print("Pagou ao sindicato: R${:.2f}".format(sindicato))
    print("Salário líquido: R${:.2f}".format(liquido))

questao = int(input("Digite a questão a ser executada: "))

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
    case _:
    	print("Opção inválida. \n")