from zooAnimales.animal import Animal

class Reptil(Animal):

    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Animal.sumarAnimal()
        self.mov = "reptar"
        Reptil.listado.append(self)
    
    @classmethod
    def getListado(cls):
        return cls.listado

    @classmethod
    def setListado(cls, listado):
        cls.listado = listado
    
    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    
    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls.listado)
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        nuevoani = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.listado.append(nuevoani)
        Reptil.iguanas += 1
        return nuevoani
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        nuevoani = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.listado.append(nuevoani)
        Reptil.serpientes += 1
        return nuevoani   