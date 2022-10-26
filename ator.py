import datetime
from ator import Ator


class Filme(Ator):
    #construtor
    def __init__(self):
        super().__init__()
        self.__nome = ""
        self.__categoria = ""
        self.__duracao = datetime.time(hour=0, minute=0, second=0)
        self.listAtores = []

    #metodos acessores
    def getNome(self):
        return self.__nome

    def setNome(self, nome_filme):
        self.__nome = nome_filme

    def getCategoria(self):
        return self.__categoria

    def setCategoria(self, categoria_filme):
        self.__categoria = categoria_filme

    def getDuracao(self):
        return self.__duracao

    def setDuracao(self, hora, minuto, segundo):
        new_duracao = datetime.time(hour=hora, minute=minuto, second=segundo)
        self.__duracao = new_duracao

    def adicionar(self, add_ator):
        # sobrescrita
        self.listAtores.append(add_ator.__str__())



    def __str__(self):
        return f"Nome do Filme: {self.__nome} || Categoria do Filme: {self.__categoria} || Duração do Filme: {self.__duracao} || Atores do Filme: {self.listAtores.__str__()}"
