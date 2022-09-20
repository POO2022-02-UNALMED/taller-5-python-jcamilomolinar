from zooAnimales.animal import Animal

class Pez(Animal):

    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Animal.sumarAnimal()
        self.mov = "nadar"
        Pez.listado.append(self)
        Animal.pez += 1

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
    
    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas  
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        nuevoani = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.listado.append(nuevoani)
        Pez.salmones += 1
        return nuevoani

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        nuevoani = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.listado.append(nuevoani)
        Pez.bacalaos += 1
        return nuevoani

    def movimiento(self):
        return self.mov