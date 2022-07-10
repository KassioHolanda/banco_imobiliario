import random


class Tabuleiro:
    def __init__(self):
        self.propriedades = []
        self.jogadores = []
        self.rodada_atual = 0

    def sortear_jogadores(self):
        random.shuffle(self.jogadores)

    def devolver_propriedades_jogador(self, jogador):
        for propriedade in self.propriedades:
            if propriedade.proprietario is not None and propriedade.proprietario.nome == jogador.nome:
                propriedade.proprietario = None
