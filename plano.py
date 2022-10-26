class Plano:
    def __init__(self):
        self.__nome = ""
        self.__preco = 0.0

    def getNome(self):
        return self.__nome

    def setNome(self, nomeplano):
        self.__nome = nomeplano

    def getPreco(self):
        return self.__preco

    def setPreco(self, precoplano):
        self.__preco = precoplano

    def __str__(self):
        return f'Plano:{self.__nome} || Preço: R${self.__preco}'
