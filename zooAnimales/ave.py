from typing import List
from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre: str = "", edad: int = 0, habitat: str = "", genero: str = "",
                 colorPlumas: str = ""):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        Ave.listado.append(self)
        Animal.totalAnimales[2]+=1

    def setColorPlumas(self, color: str) -> None:
        self.colorPlumas = color

    def getColorPlumas(self) -> str:
        return self.colorPlumas

    @classmethod
    def cantidadAves(cls) -> int:
        return len(cls.listado)

    def movimiento(self) -> str:
        return "volar"

    @classmethod
    def crearHalcon(cls,nombre: str, edad: int, genero: str) -> 'Ave':
        cls.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crearAguila(cls,nombre: str, edad: int, genero: str) -> 'Ave':
        cls.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")