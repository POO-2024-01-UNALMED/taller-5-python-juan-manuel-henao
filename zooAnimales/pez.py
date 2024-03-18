from typing import List
from zooAnimales.animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre: str = "", edad: int = 0, habitat: str = "", genero: str = "",
                 colorEscamas: str = "", cantidadAletas: int = 0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.listado.append(self)
        Animal.totalAnimales[4]+=1

    def setColorEscamas(self, colorEscamas: str) -> None:
        self.colorEscamas = colorEscamas

    def getColorEscamas(self) -> str:
        return self.colorEscamas

    def setCantidadAletas(self, cantidadAletas: int) -> None:
        self.cantidadAletas = cantidadAletas

    def getCantidadAletas(self) -> int:
        return self.cantidadAletas

    @classmethod
    def cantidadPeces(cls) -> int:
        return len(cls.listado)

    def movimiento(self) -> str:
        return "nadar"

    @classmethod
    def crearSalmon(cls,nombre: str, edad: int, genero: str) -> 'Pez':
        cls.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(cls,nombre: str, edad: int, genero: str) -> 'Pez':
        cls.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)