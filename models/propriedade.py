class Propriedade():
    def __init__(self, nome, preco_compra, preco_aluguel, proprietario=None):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_aluguel = preco_aluguel
        self.proprietario = proprietario
        
    def esta_disponivel_compra(self):
        return self.proprietario is None
    
    def devolver_propriedade(self):
        if self.proprietario is not None:
            self.proprietario = None