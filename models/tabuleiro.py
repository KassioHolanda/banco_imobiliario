import random

class Tabuleiro:
    def __init__(self):
        self.propriedades = []
        self.jogadores = []
        self.rodada_inicial = 1
        
    def add_propriedade(self, propriedade):
        self.propriedades.append(propriedade)
    
    def add_jogadores(self, jogadores):
        for jogador in jogadores:
            self.jogadores.append(jogador)
        
    def sortear_jogadores(self):
        random.shuffle(self.jogadores)
        
    def remover_jogador(self, jogador):
        self.jogadores.remove(jogador)

    def devolver_propriedades_jogador(self, jogador):
        for propriedade in self.propriedades:
            if propriedade.proprietario.nome == jogador.nome:
                propriedade.devolver()
