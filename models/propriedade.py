class Propriedade():
    def __init__(self, nome, preco_compra, preco_aluguel, proprietario=None):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_aluguel = preco_aluguel
        self.proprietario = proprietario
    
    def devolver(self):
        if self.proprietario is not None:
            self.proprietario = None
            
    def comprar(self, jogador):
        if self.proprietario is None:
            self.proprietario = jogador
            jogador.saldo -= self.preco_compra
            return True
        return False
    
    def receber_aluguel(self, jogador):
        jogador.saldo -= self.preco_aluguel
        self.proprietario.saldo += self.preco_aluguel
    
    def __repr__(self):
        return self.nome
            