from abc import abstractmethod


class Jogador:
    def __init__(self, nome, saldo_inicial=300.00):
        self.nome = nome
        self.saldo = saldo_inicial
        self.jogando = True
        self.saldo_inicial = saldo_inicial
        self.posicao_tabuleiro = 0
        self.numero_jogadas = 0

    def consultar_saldo_suficiente(self, valor):
        if self.saldo >= valor:
            return True
        return False

    def validar_saldo(self):
        if self.saldo < 0:
            self.jogando = False
        return self.jogando

    @abstractmethod
    def comprar_propriedade(self, propriedade):
        pass

    def pagar_aluguel(self, propriedade):
        self.saldo -= propriedade.preco_aluguel
        propriedade.receber_aluguel()

    def __repr__(self):
        return self.nome
