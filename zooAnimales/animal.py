from zooAnimales import Mamifero, Ave, Reptil, Pez, Anfibio

class Animal:

    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        self.mov = "desplazarse"
        Animal.totalAnimales += 1
    
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero
    
    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona
    
    @classmethod
    def getTotalAnimales(cls):
        return cls.totalAnimales
    
    @classmethod
    def sumarAnimal(cls):
        cls.totalAnimales += 1

    @classmethod
    def totalPorTipo(cls):
        muestra = "Mamiferos: {}\n" + "Aves: {}\n" + "Reptiles: {}\n" + "Peces: {}\n" + "Anfibios: {}"
        return muestra.format(len(Mamifero.getListado()), len(Ave.getListado()), len(Reptil.getListado()), len(Pez.getListado()), len(Anfibio.getListado()))

    def __str__(self):
        if self._zona == None:
            muestra = "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}"
            return muestra.format(self._nombre, self._edad, self._habitat, self._genero)
        else:
            muestra = "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}, la zona en la que me ubico es {}, en el {}"
            return muestra.format(self._nombre, self._edad, self._habitat, self._genero, self._zona.getNombre(), self._zona.getZoo().getNombre())
    
    def movimiento(self):
        return self.mov