from models.jogador import Jogador


class Cauteloso(Jogador):
    def posso_comprar_propriedade(self, propriedade):
        if (self.saldo - propriedade.preco_compra) >= 80 and self.consultar_saldo_suficiente(propriedade.preco_compra):
            return self.comprar_propriedade(propriedade)
        return False
