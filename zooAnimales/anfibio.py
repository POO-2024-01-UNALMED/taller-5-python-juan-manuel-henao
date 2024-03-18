from typing import List
from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre: str = "", edad: int = 0, habitat: str = "", genero: str = "",
                 colorPiel: str = "", venenoso: bool = False):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Anfibio.listado.append(self)
        Animal.totalAnimales[5]+=1

    def setColorPiel(self, colorPiel: str) -> None:
        self.colorPiel = colorPiel

    def getColorPiel(self) -> str:
        return self.colorPiel

    def setVenenoso(self, venenoso: bool) -> None:
        self.venenoso = venenoso

    def isVenenoso(self) -> bool:
        return self.venenoso

    @classmethod
    def cantidadAnfibios(cls) -> int:
        return len(cls.listado)

    def movimiento(self) -> str:
        return "saltar"

    @classmethod
    def crearRana(cls,nombre: str, edad: int, genero: str) -> 'Anfibio':
        cls.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra(cls,nombre: str, edad: int, genero: str) -> 'Anfibio':
        cls.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)