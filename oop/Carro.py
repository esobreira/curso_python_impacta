class Carro(object):
    tipo = None

    def __init__(self, caminho):
        self.caminho = caminho

    def andar(self):
        print('Andando pela', self.caminho)


class Fusca(Carro):
    tipo = "Fusca"
    
    def correr(self):
        super(Fusca, self).andar()


class Ferrari(Carro):
    tipo = "Ferrari"

    def andar(self):
        print('Correndo pra kct', 'pelo', self.caminho)