import random

from distlib.compat import raw_input

from models.aleatorio import Aleatorio
from models.cauteloso import Cauteloso
from models.exigente import Exigente
from models.impulsivo import Impulsivo
from models.jogador import Jogador
from models.propriedade import Propriedade
from models.tabuleiro import Tabuleiro


class BancoImobiliario:

    def __init__(self):
        self.total_rodadas = 1000
        self.total_partidas = 0
        self.total_rodadas_partida = 0
        self.total_partidas_timeout = 0

        self.quantidade_vitorias_por_jogador = {}
        self.set_quantidade_vitorias()

    def set_quantidade_vitorias(self):
        for jogador in self.criar_jogadores():
            self.quantidade_vitorias_por_jogador[jogador.nome] = 0

    def criar_jogadores(self):
        jogadores = []
        jogadores.append(Aleatorio('Aleatorio'))
        jogadores.append(Cauteloso('Cauteloso'))
        jogadores.append(Exigente('Exigente'))
        jogadores.append(Impulsivo('Impulsivo'))
        return jogadores

    def criar_propriedades(self):
        propriedades = []
        for numero in range(20):
            nome_propriedade = 'PropriedadeNumero: {}'.format(numero)
            propriedade = Propriedade(nome_propriedade, random.randint(10, 300), random.randint(10, 100))
            propriedades.append(propriedade)
        return propriedades

    def criar_tabuleiro(self):
        self.tabuleiro = Tabuleiro()
        self.tabuleiro.jogadores = self.criar_jogadores()
        self.tabuleiro.propriedades = self.criar_propriedades()
        self.tabuleiro.sortear_jogadores()

    def iniciar_jogo(self):
        print('\n### BANCO IMOBILIARIO ###')
        print('## EXECUTANDO JOGO ##')
        while self.total_partidas < 300:
            self.criar_tabuleiro()
            self.jogar()
            self.total_partidas += 1
        self.resultado()

    def jogar(self):
        while self.tabuleiro.rodada_atual < self.total_rodadas:
            for jogador in self.tabuleiro.jogadores:
                if not jogador.jogando:
                    continue
                posicao_jogador = self._jogar_dado(jogador)
                propriedade: Propriedade = self.tabuleiro.propriedades[posicao_jogador]
                if propriedade.proprietario is None:
                    jogador.posso_comprar_propriedade(propriedade)
                if propriedade.proprietario is not None and propriedade.proprietario.nome != jogador.nome:
                    propriedade.proprietario.saldo += propriedade.preco_aluguel
                    jogador.saldo -= propriedade.preco_aluguel
                if not jogador.validar_saldo():
                    self.tabuleiro.devolver_propriedades_jogador(jogador)
                lista_jogadores_jogando = self.continuar_jogo()
                if len(lista_jogadores_jogando) == 1:
                    self.quantidade_vitorias_por_jogador[lista_jogadores_jogando[0].nome] += 1
                    self.tabuleiro.rodada_atual = 1000
                    break
            self.tabuleiro.rodada_atual += 1
            self.total_rodadas_partida += 1
        if self.tabuleiro.rodada_atual == self.total_rodadas:
            self.total_partidas_timeout += 1
            jogadores_jogando: [Jogador] = []
            for jogador in self.tabuleiro.jogadores:
                if jogador.jogando and jogador.numero_rodadas == self.tabuleiro.rodada_atual:
                    jogadores_jogando.append(jogador)
            jogador_com_maior_saldo: Jogador = max(jogadores_jogando, key=lambda jogador: jogador.saldo)
            self.quantidade_vitorias_por_jogador[jogador_com_maior_saldo.nome] += 1

    def resultado(self):
        print('\n\n### RESULTADO ###\n')
        print('QUANTIDADE DE PARTIDAS TERMINADAS POR TIMEOUT:  {}'.format(self.total_partidas_timeout))
        print('MEDIA DE RODADAS POR PARTIDAS:  {}'.format(self.total_rodadas_partida / 300))
        print('PORCENTAGEM VITORIAS JOGADOR ALEATORIO:  {:.2f}'.format(self._get_porcentagem_jogador('Aleatorio')))
        print('PORCENTAGEM VITORIAS JOGADOR CAUTELOSO:  {:.2f}'.format(self._get_porcentagem_jogador('Cauteloso')))
        print('PORCENTAGEM VITORIAS JOGADOR EXIGENTE:  {:.2f}'.format(self._get_porcentagem_jogador('Exigente')))
        print('PORCENTAGEM VITORIAS JOGADOR IMPULSIVO:  {:.2f}'.format(self._get_porcentagem_jogador('Impulsivo')))
        print('JOGADOR MAIS VITORIOSO:  {}'.format(
            max(self.quantidade_vitorias_por_jogador, key=self.quantidade_vitorias_por_jogador.get)))

    def _get_porcentagem_jogador(self, nome_jogador):
        total_vitorias = self.quantidade_vitorias_por_jogador[nome_jogador]
        porcentagem = (total_vitorias / 300) * 100
        return porcentagem

    def continuar_jogo(self):
        jogadores = []
        for jogador in self.tabuleiro.jogadores:
            if jogador.jogando:
                jogadores.append(jogador)
        return jogadores

    def _jogar_dado(self, jogador):
        dado = random.randint(1, 7)
        jogador.posicao_tabuleiro += dado
        jogador.numero_rodadas += 1

        if jogador.posicao_tabuleiro > 19:
            posicao = jogador.posicao_tabuleiro - 19
            if posicao:
                jogador.completar_volta_tabuleiro(posicao=posicao)
            else:
                jogador.completar_volta_tabuleiro()
        return jogador.posicao_tabuleiro
