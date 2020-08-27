from Pessoa import Pessoa
from Carro import Carro
from Carro import Fusca
from Carro import Ferrari

class minha_classe(Pessoa):
    pass

    # def __init__(self):
    #     self.nome = ""
    #     self.sexo = ''
    #     self.idade = 0

    # def andar(self):
    #     print("andar")

    # def comer(self):
    #     print("comer")

    # def dormir(self):
    #     print("dormir")

    # def meuMetodo2(self, valor):
    #     self.outroAtributo = valor
    #     print(self.outroAtributo)


def criaObjeto():
    p = Pessoa()
    p.nome = "João"
    #p.salvar()
    p.salvar('Eberton')
    #print(p.nome)

    print('-----------------')

    c = Carro(caminho = 'Estrada')
    print(c.tipo)
    print(c.caminho)
    c.andar()

    print('-----------------')

    f = Fusca(caminho = 'Calçada')
    print(f.tipo)
    print(f.caminho)
    f.correr()

    print('-----------------')

    fer = Ferrari(caminho = 'Autódromo')
    print(fer.tipo)
    #print(f.caminho)
    fer.andar()

criaObjeto()