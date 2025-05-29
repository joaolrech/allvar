import os
import random

class Velha():
    def __init__(self):
        os.system('clear')
        print('Bem vindo ao jogo da velha!\n')
        
        self.usuario = self.inptcaracter('Deseja ser X ou O?\n\n')
        self.computador = 'O' if self.usuario == 'X' else 'X'
        
        while True:
            self.jogo = [i + 1 for i in range(9)]
            
            comeca = self.inptcomeca()
            if comeca == 1:
                while True:
                    if self.jogar(self.usuario):
                        break
                    if self.jogar(self.computador):
                        break
            if comeca == 2:
                while True:
                    if self.jogar(self.computador):
                        break
                    if self.jogar(self.usuario):
                        break
                    
            novamente = self.inptnovamente()
            if novamente == 2:
                break
     
        print('Obrigado por jogar!')

    def printjogo(self):
        print(f'{self.jogo[6]} {self.jogo[7]} {self.jogo[8]}')
        print(f'{self.jogo[3]} {self.jogo[4]} {self.jogo[5]}')
        print(f'{self.jogo[0]} {self.jogo[1]} {self.jogo[2]}\n')
       
    def verificavencedor(self):
        regras = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(self.jogo[x] == self.jogo[y] == self.jogo[z] for x, y, z in regras)

    def geradordejogada(self):
        while True:
            jogada = random.randint(0, 8)
            
            if type(self.jogo[jogada]) != int:
                continue
            
            return jogada

    def verificajogada(self):
        while True:
            jogada = self.inptjogada()
            
            if type(self.jogo[jogada]) != int:
                os.system('clear')
                print('Posição inválida. Tente novamente.\n')
                continue
            
            return jogada

    def inptjogada(self):
        while True:
            try:
                print('Selecione a posição em que deseja jogar.\n')
                self.printjogo()
                
                inpt = int(input())
                
                if inpt < 1 or inpt > 9:
                    raise ValueError
                    
                os.system('clear')
                return inpt - 1
                
            except ValueError:
                os.system('clear')
                print('Entrada inválida. Tente novamente.\n')

    def inptcaracter(self, desc):
        while True:
            inpt = input(desc).upper()
            
            if inpt not in ['X', 'O']:
                os.system('clear')
                print('Entrada inválida. Tente novamente.\n')
            else:
                os.system('clear')
                return inpt

    def inptcomeca(self):
        while True:
            try:
                print('Digite quem começa.\n')
                print('1 - Você')
                print('2 - Computador\n')
                
                inpt = int(input())
                
                if inpt < 1 or inpt > 2:
                    raise ValueError
                    
                os.system('clear')
                return inpt
                
            except ValueError:
                os.system('clear')
                print('Entrada inválida. Tente novamente.\n')
 
    def inptnovamente(self):
        while True:
            try:
                print('Deseja jogar novamente?\n')
                print('1 - Sim')
                print('2 - Não\n')
                
                inpt = int(input())
                
                if inpt < 1 or inpt > 2:
                    raise ValueError
                    
                os.system('clear')
                return inpt
                
            except ValueError:
                os.system('clear')
                print('Entrada inválida. Tente novamente.\n')

    def jogar(self, jogador):
        if jogador is self.usuario:
            jogada = self.verificajogada()
        if jogador is self.computador:
            jogada = self.geradordejogada()
            
        self.jogo[jogada] = jogador
        
        ganhou = self.verificavencedor()
        if ganhou:
            self.printjogo()
            if jogador is self.usuario:
                print('Você ganhou!\n')
            if jogador is self.computador:
                print('Computador ganhou!\n') 
            return True
        
        if all(type(pos) != int for pos in self.jogo):
            self.printjogo()
            print('Empate!\n')
            return True
        return False

Velha()