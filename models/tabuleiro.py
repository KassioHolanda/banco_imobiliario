import random

class Tabuleiro:
    def __init__(self):
        self.propriedades = []
        self.jogadores = []
        self.rodada_inicial = 1
        
    def add_propriedade(self, propriedade):
        self.propriedades.append(propriedade)
    
    def add_jogador(self, jogador):
        self.jogadores.append(jogador)
        
    def sortear_jogadores(self):
        random.shufle(self.jogadores)
        
    def remover_jogador(self, jogador):
        self.jogadores.remove(jogador)