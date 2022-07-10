import random
from models.jogador import Jogador


class Aleatorio(Jogador):
    def comprar_propriedade(self, propriedade):
        if random.choice([True, False]) and self.consultar_saldo_suficiente(propriedade.preco_compra):
            return propriedade.comprar(self)
        return False
