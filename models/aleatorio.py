import random
from models.jogador import Jogador


class Aleatorio(Jogador):
    def posso_comprar_propriedade(self, propriedade):
        if random.choice([True, False]) and self.consultar_saldo_suficiente(propriedade.preco_compra):
            return self.comprar_propriedade(propriedade)
        return False
