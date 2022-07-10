from models.jogador import Jogador


class Cauteloso(Jogador):
    def comprar_propriedade(self, propriedade):
        if (self.saldo - propriedade.preco_compra) >= 80 and self.consultar_saldo_suficiente(propriedade.preco_compra):
            return propriedade.comprar(self)
        return False
