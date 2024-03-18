from typing import List



class Animal:
    totalAnimales = [0,0,0,0,0,0]

    def __init__(self, nombre: str = "", edad: int = 0, habitat: str = "", genero: str = ""):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        Animal.totalAnimales[0] += 1
        self.zonas= []

    @classmethod
    def getTotalAnimales() -> int:
        return Animal.totalAnimales[0]

    @classmethod
    def setTotalAnimales(totalAnimales: int) -> None:
        Animal.totalAnimales[0] = totalAnimales

    def getNombre(self) -> str:
        return self.nombre

    def setNombre(self, nombre: str) -> None:
        self.nombre = nombre

    def getEdad(self) -> int:
        return self.edad

    def setEdad(self, edad: int) -> None:
        self.edad = edad

    def getHabitat(self) -> str:
        return self.habitat

    def setHabitat(self, habitat: str) -> None:
        self.habitat = habitat

    def getGenero(self) -> str:
        return self.genero

    def setGenero(self, genero: str) -> None:
        self.genero = genero

    def getZona(self) -> List:
        return self.zonas

    def setZona(self, zona: List) -> None:
        self.zonas = zona

    def movimiento(self) -> str:
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls) -> str:
        m = cls.totalAnimales[1]
        a = cls.totalAnimales[2]
        r = cls.totalAnimales[3]
        p = cls.totalAnimales[4]
        an = cls.totalAnimales[5]
        return f"Mamiferos : {m}\nAves : {a}\nReptiles : {r}\nPeces : {p}\nAnfibios : {an}"

    def toString(self) -> str:
        info_zona = f", la zona en la que me ubico es {self.zonas[0].getNombre()}, en el {self.zonas[0].getZoo().getNombre()}" if self.zonas else ""
        return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}{info_zona}"