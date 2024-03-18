from typing import List
from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre: str = "", edad: int = 0, habitat: str = "", genero: str = "",
                 pelaje: bool = False, patas: int = 0):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)
        Animal.totalAnimales[1]+=1

    @classmethod
    def getListado(cls) -> List['Mamifero']:
        return cls.listado

    @classmethod
    def setListado(cls,listado: List['Mamifero']) -> None:
        cls.listado = listado

    def isPelaje(self) -> bool:
        return self.pelaje

    def setPelaje(self, pelaje: bool) -> None:
        self.pelaje = pelaje

    def getPatas(self) -> int:
        return self.patas

    def setPatas(self, patas: int) -> None:
        self.patas = patas

    @classmethod
    def cantidadMamiferos(cls) -> int:
        return len(cls.listado)

    @classmethod
    def crearCaballo(cls,nombre: str, edad: int, genero: str) -> 'Mamifero':
        cls.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @classmethod
    def crearLeon(cls,nombre: str, edad: int, genero: str) -> 'Mamifero':
        cls.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)