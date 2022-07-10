from models.jogador import Jogador


class Exigente(Jogador):
    def comprar_propriedade(self, propriedade):
        if propriedade.preco_aluguel > 50 and self.consultar_saldo_suficiente(propriedade.preco_compra):
            return propriedade.comprar(self)
        return False
