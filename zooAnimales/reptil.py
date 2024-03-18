from typing import List
from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre: str = "", edad: int = 0, habitat: str = "", genero: str = "",
                 colorEscamas: str = "", largoCola: int = 0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil.listado.append(self)
        Animal.totalAnimales[3]+=1

    def setColorEscamas(self, escamas: str) -> None:
        self.colorEscamas = escamas

    def getColorEscamas(self) -> str:
        return self.colorEscamas

    def setLargoCola(self, largo: int) -> None:
        self.largoCola = largo

    def getLargoCola(self) -> int:
        return self.largoCola

    @classmethod
    def cantidadReptiles(cls) -> int:
        return len(cls.listado)

    def movimiento(self) -> str:
        return "reptar"

    @classmethod
    def crearIguana(cls,nombre: str, edad: int, genero: str) -> 'Reptil':
        cls.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crearSerpiente(cls,nombre: str, edad: int, genero: str) -> 'Reptil':
        cls.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)