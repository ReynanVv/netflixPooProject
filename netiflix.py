from assinante import Assinante
from filme import Filme
from plano import Plano


class Netflix(Assinante, Filme, Plano):

    listFilmes = []
    listAssinantes = []
    listPlanos = []


    @classmethod
    def pagar(cls, assinante, valor, vouche=0):
        if vouche == 0:
            if valor >= assinante.getPlano().getPreco():
                print(f"{assinante.getNome()} pagou o plano normal")
                return True
            else:
                return False
        else:
            disc = vouche / 100
            newValor = valor - (valor * disc)
            if newValor <= assinante.getPlano().getPreco():
                print(f"{assinante.getNome()} pagou com desconto")
                return True
            else:
                return False

    @classmethod
    def assinar(cls, add_assinante):
        cls.listAssinantes.append(add_assinante.__str__())

    @classmethod
    def comprar(cls, add_filme):
        cls.listFilmes.append(add_filme.__str__())

    @classmethod
    def planos(cls, add_planos):
        cls.listPlanos.append(add_planos.__str__())

