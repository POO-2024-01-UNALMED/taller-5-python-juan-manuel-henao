from typing import List
from gestion.zona import Zona

class Zoologico:
    def __init__(self, nombre: str = "", ubicacion: str = ""):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas: List = []

    def setNombre(self, nombre: str) -> None:
        self.nombre = nombre

    def getNombre(self) -> str:
        return self.nombre

    def setUbicacion(self, ubicacion: str) -> None:
        self.ubicacion = ubicacion

    def getUbicacion(self) -> str:
        return self.ubicacion

    def setZona(self, zonas: List) -> None:
        self.zonas = zonas

    def getZona(self) -> List:
        return self.zonas
    
    
    def agregarZonas(self, zona:Zona) -> None:
        zona.setZoo(self)
        self.zonas.append(zona)

    def cantidadTotalAnimales(self) -> int:
        cantidad = 0
        for zona in self.zonas:
            cantidad += zona.cantidadAnimales()
        return cantidad