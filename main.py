from plano import Plano
from netflix import Netflix
from filme import Filme
from ator import Ator
from assinante import Assinante

#criando atores
a1 = Ator()
a1.setNome('Nicolas')
a1.setSexo('Masculino')
a1.setNacionalidade('americano')
a1.setDataNascimento(ano=1987, mes=6, dia=12)


a2 = Ator()
a2.setNome('Julio')
a2.setSexo('Masculino')
a2.setNacionalidade('uruguaio')
a2.setDataNascimento(ano=1853,mes=2, dia=16)


a3 = Ator()
a3.setNome('Jair')
a3.setSexo('Masculino')
a3.setNacionalidade('brasileiro')
a3.setDataNascimento(ano=1922,mes=12, dia=22)


a4 = Ator()
a4.setNome('Amanda')
a4.setSexo('Feminino')
a4.setNacionalidade('espanhola')
a4.setDataNascimento(ano=2003, mes=8, dia=1)


a5 = Ator()
a5.setNome('Sophia')
a5.setSexo('Feminino')
a5.setNacionalidade('brasileira')
a5.setDataNascimento(ano=2006, mes=9, dia=16)



#criando filmes
f1 = Filme()
f1.setNome('Interstellar')
f1.setCategoria('Ficção')
f1.setDuracao(2, 49, 12)
f1.adicionar(a5)
f1.adicionar(a4)


f2 = Filme()
f2.setNome('Bastardos Inglórios')
f2.setCategoria('Guerra/Ação')
f2.setDuracao(2, 33, 00)
f2.adicionar(a1)
f2.adicionar(a2)


#criando planos
p1 = Plano()
p1.setNome('Simples')
p1.setPreco(24.99)

p2 = Plano()
p2.setNome('Master')
p2.setPreco(44.99)

#criando assinante
as1 = Assinante()
as1.setNome('Rey')
as1.setPlano(plano_assinante=p2)
as1.setDataNascimento(2002, 6, 17)
as1.assistir(f1)

as2 = Assinante()
as2.setNome('Ryan')
as2.setPlano(plano_assinante=p1)
as2.setDataNascimento(2003, 4, 10)
as2.assistir(f2)

#criando netflix
n1 = Netflix()
n1.comprar(add_filme=f1)
n1.comprar(add_filme=f2)

n1.assinar(add_assinante=as1)
n1.assinar(add_assinante=as2)

n1.planos(add_planos=p1)
n1.planos(add_planos=p2)

f1.adicionar(add_ator=a1)
f1.adicionar(add_ator=a3)

f2.adicionar(add_ator=a4)
f2.adicionar(add_ator=a5)

as1.assistir(add_filme=f1)
as2.assistir(add_filme=f2)
print('Pagamentos:')
n1.pagar(as1, 50.0, 20)
n1.pagar(as2, 30.0)
print('\n')
print('___ Atores Criados ___')
print(a1)
print('\n')
print(a2)
print('\n')
print(a3)
print('\n')
print(a4)
print('\n')
print(a5)

print('\n')

print('___ Filmes Criados ___')
print(f1)
print('\n')
print(f2)

print('\n')

print('___ Planos Criados ___')
print(p1)
print('\n')
print(p2)

print('\n')

print('___ Assinantes Criados ___')
print(as1)
print('\n')
print(as2)

print('\n')

print('___ Netflix Criadas ___')
print(f'{n1.listFilmes}\n')
print(f'{n1.listAssinantes}\n')
print(f'{n1.listPlanos}\n')
