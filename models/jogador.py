from abc import abstractmethod


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.jogando = True
        self.saldo_inicial = 300
        self.saldo = 300
        self.posicao_tabuleiro = 0
        self.numero_rodadas = 0

    def consultar_saldo_suficiente(self, valor):
        if self.saldo >= valor:
            return True
        return False

    def validar_saldo(self):
        if self.saldo < 0:
            self.jogando = False

        return self.jogando

    @abstractmethod
    def posso_comprar_propriedade(self, propriedade):
        pass

    def pagar_aluguel(self, propriedade):
        self.saldo -= propriedade.preco_aluguel
        propriedade.receber_aluguel()

    def completar_volta_tabuleiro(self, posicao=1):
        self.posicao_tabuleiro = posicao
        self.saldo += 100

    def comprar_propriedade(self, propriedade):
        if propriedade.proprietario is None:
            propriedade.proprietario = self
            self.saldo -= propriedade.preco_compra

    def __repr__(self):
        return self.nome
