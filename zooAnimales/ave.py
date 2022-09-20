from zooAnimales.animal import Animal

class Ave(Animal):

    listado = []
    halcones = 0
    aguilas = 0


    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Animal.sumarAnimal()
        self.mov = "volar"
        Ave.listado.append(self)
        Animal.ave += 1

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    @classmethod
    def getListado(cls):
        return cls.listado

    @classmethod
    def setListado(cls, listado):
        cls.listado = listado
    
    @classmethod
    def cantidadAves(cls):
        return len(cls.listado)
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        nuevoani = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.listado.append(nuevoani)
        Ave.halcones += 1
        return nuevoani
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        nuevoani = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.listado.append(nuevoani)
        Ave.aguilas += 1
        return nuevoani
    
    def movimiento(self):
        return self.mov