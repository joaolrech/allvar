import os
import random

class Velha():
    def __init__(self):
        self.jogo = [i + 1 for i in range(9)]

    def printjogo(self):
        print(f'{self.jogo[6]} {self.jogo[7]} {self.jogo[8]}')
        print(f'{self.jogo[3]} {self.jogo[4]} {self.jogo[5]}')
        print(f'{self.jogo[0]} {self.jogo[1]} {self.jogo[2]}\n')

    def verificavencedor(self):
        if (self.jogo[0] == self.jogo[1] == self.jogo[2] or
        self.jogo[3] == self.jogo[4] == self.jogo[5] or
        self.jogo[6] == self.jogo[7] == self.jogo[8] or
        self.jogo[0] == self.jogo[3] == self.jogo[6] or
        self.jogo[1] == self.jogo[4] == self.jogo[7] or
        self.jogo[2] == self.jogo[5] == self.jogo[8] or
        self.jogo[2] == self.jogo[4] == self.jogo[6] or
        self.jogo[0] == self.jogo[4] == self.jogo[8]):
            return True
        else:
            return False

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
                os.system("clear")
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
                os.system("clear")
                return inpt - 1
            except ValueError:
                os.system("clear")
                print('Entrada inválida. Tente novamente.\n')

    def inptcaracter(self, desc):
        while True:
            inpt = input(desc).upper()
            if inpt not in ['X', 'O']:
                os.system("clear")
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
                os.system("clear")
                return inpt
            except ValueError:
                os.system("clear")
                print('Entrada inválida. Tente novamente.\n')

    def usjoga(self, usuario):
        jogadaus = self.verificajogada()
        self.jogo[jogadaus] = usuario
        ganhou = self.verificavencedor()
        if ganhou:
            self.printjogo()
            print('Você ganhou.\n')
            return True
        if all(type(pos) != int for pos in self.jogo):
            self.printjogo()
            print('Empate.\n')
            return True
        return False

    def pcjoga(self, computador):
        jogadapc = self.geradordejogada()
        self.jogo[jogadapc] = computador
        ganhou = self.verificavencedor()
        if ganhou:
            self.printjogo()
            print('Computador ganhou.\n')
            return True
        if all(type(pos) != int for pos in self.jogo):
            self.printjogo()
            print('Empate.\n')
            return True
        return False

    def jogar(self):
        os.system('clear')
        print('Bem vindo ao jogo da velha!\n')

        usuario = self.inptcaracter('Deseja ser X ou O?\n\n')
        computador = 'O' if usuario == 'X' else 'X'

        comeca = self.inptcomeca()
        if comeca == 1:
            while True:
                if self.usjoga(usuario):
                    break
                if self.pcjoga(computador):
                    break
        else:
            while True:
                if self.pcjoga(computador):
                    break
                if self.usjoga(usuario):
                    break

velha = Velha()
velha.jogar()
print('Programa finalizado.')