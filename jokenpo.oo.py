import os
import random

class Jokenpo():
    def __init__(self):
        self.jogadas = [
            'Pedra',
            'Papel',
            'Tesoura'
        ]
        self.regras = {
        'Pedra': 'Tesoura',
        'Papel': 'Pedra',
        'Tesoura': 'Papel'
        }
        self.placarpc = 0
        self.placarus = 0
        
        os.system("clear")
        print('Bem vindo ao jokenpô!\n')
        
        while True:
            self.printplacar()
            self.printopcoes()
            
            self.computador = random.choice(self.jogadas)

            self.usuario = self.inptjogada()
            if self.usuario == 0:
                break
            self.usuario = self.jogadas[self.usuario - 1]
            
            print('Sua jogada:', self.usuario)
            print('Jogada do computador:', self.computador)
            
            self.verificar()
      
        print('Obrigado por jogar!')

    def printplacar(self):
        print('          PLACAR')
        print(f'COMPUTADOR: {self.placarpc} | USUÁRIO: {self.placarus}')
    
    def printopcoes(self):
        print('\n1 - Pedra')
        print('2 - Papel')
        print('3 - Tesoura\n')
        print('0 - SAIR\n')
    
    def inptjogada(self):
        while True:
            try:
                inpt = int(input())

                if inpt not in range(4):
                    raise ValueError

                os.system("clear")
                return inpt

            except ValueError:
                os.system("clear")
                print('Entrada inválida. Tente novamente.\n')
                self.printplacar()
                self.printopcoes()
    
    def verificar(self):
        if self.regras[self.usuario] == self.computador:
            self.placarus += 1
            print('Você ganhou!\n')
        elif self.regras[self.computador] == self.usuario:
            self.placarpc += 1
            print('Computador ganhou!\n')
        else:
            print('Empate!\n')

Jokenpo()