from models.jogador import Jogador


class Impulsivo(Jogador):
    def posso_comprar_propriedade(self, propriedade):
        if self.consultar_saldo_suficiente(propriedade.preco_compra):
            return self.comprar_propriedade(propriedade)
        return False
