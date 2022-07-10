from models.jogador import Jogador


class Impulsivo(Jogador):
    def comprar_propriedade(self, propriedade):
        if self.consultar_saldo_suficiente(propriedade.preco_compra):
            return propriedade.comprar(self)
        return False
