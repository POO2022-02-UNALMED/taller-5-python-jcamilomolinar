from zooAnimales.animal import Animal

class Anfibio(Animal):

    listado = []
    ranas = 0
    salamandras = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Animal.sumarAnimal()
        self.mov = "saltar"
        Anfibio.listado.append(self)
    
    @classmethod
    def getListado(cls):
        return cls.listado

    @classmethod
    def setListado(cls, listado):
        cls.listado = listado
    
    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    
    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.listado)
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        nuevoani = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.listado.append(nuevoani)
        Anfibio.ranas += 1
        return nuevoani
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        nuevoani = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.listado.append(nuevoani)
        Anfibio.salamandras += 1
        return nuevoani
    
    def movimiento(self):
        return self.mov