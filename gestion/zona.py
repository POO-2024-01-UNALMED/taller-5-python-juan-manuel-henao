
from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre: str = "",zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales= []

    def setNombre(self, nombre: str) -> None:
        self.nombre = nombre

    def getNombre(self) -> str:
        return self.nombre

    def setZoo(self, zoo) -> None:
        self.zoo = zoo

    def getZoo(self):
        return self.zoo

    def setAnimales(self, animales: list) -> None:
        self.animales = animales

    def getAnimales(self) -> list:
        return self.animales

    def agregarAnimales(self, animal: Animal) -> None:
        self.animales.append(animal)

    def cantidadAnimales(self) -> int:
        return len(self.animales)