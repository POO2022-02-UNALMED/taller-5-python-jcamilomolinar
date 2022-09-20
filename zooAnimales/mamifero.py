from zooAnimales.animal import Animal

class Mamifero(Animal):

    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Animal.sumarAnimal()
        Mamifero.listado.append(self)
        Animal.mam += 1
    
    @classmethod
    def getListado(cls):
        return cls.listado
    
    @classmethod
    def setListado(cls, listado):
        cls.listado = listado
    
    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    
    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        nuevoani = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.listado.append(nuevoani)
        Mamifero.caballos += 1
        return nuevoani

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        nuevoani = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.listado.append(nuevoani)
        Mamifero.leones += 1
        return nuevoani
    
    def movimiento(self):
        return self.mov