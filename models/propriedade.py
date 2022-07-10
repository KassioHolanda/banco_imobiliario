from models.jogador import Jogador


class Propriedade():
    def __init__(self, nome, preco_compra, preco_aluguel, proprietario=None):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_aluguel = preco_aluguel
        self.proprietario: Jogador = proprietario
    
    def __repr__(self):
        return self.nome
            