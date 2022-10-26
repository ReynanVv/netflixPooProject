from plano import Plano
from filme import Filme
import datetime


class Assinante(Filme, Plano):
    def __init__(self):
        super().__init__()
        self.__plano = ""
        self.__nome = ""
        self.__dataNascimento = datetime.date(year=1,month=1,day=1)
        self.listAssistindo = []

    def getPlano(self):
        return self.__plano

    def setPlano(self, plano_assinante):
        self.__plano = plano_assinante

    def getNome(self):
        return self.__nome

    def setNome(self, nome_assinante):
        self.__nome = nome_assinante

    def getDataNascimento(self):
        return self.__dataNascimento

    def setDataNascimento(self, ano, mes, dia):
        new_DataNascimento = datetime.date(year=ano,month=mes,day=dia)
        self.__dataNascimento = new_DataNascimento

    def assistir(self, add_filme):
        self.listAssistindo.append(add_filme.__str__())

    def terminar(self, remove_filme):
        self.listAssistindo.remove(remove_filme.__str__())

    def __str__(self):

        return f'Nome do Assinante: {self.__nome} || {self.__plano} || Data de Nascimento: {self.__dataNascimento} || Filmes Assistidos:{self.listAssistindo.__str__()}'
