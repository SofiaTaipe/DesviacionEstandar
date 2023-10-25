from math import sqrt

class ExceptionDatos(Exception):
    pass

class Estadistica:
    def __init__(self):
        self.__numeros = self.validarNumeros(numeros)

    @property
    def numeros(self):
        return self.__numeros

    @numeros.setter
    def numeros(self, numeros):
        self.__numeros = numeros

    def validarNumeros(self, numeros):
        if numeros is not None:
            for numero in numeros:
                if not isinstance(numero, int) and not isinstance(numero, float):
                    raise ValueError
            return numeros
        else:
            raise ExceptionDatos

    def media(self):
        if len(self.__numeros) == 0:
            raise ExceptionDatos
        suma = 0
        for valor in self.__numeros:
            suma += valor
        return suma / len(self.__numeros)

    def DesviacionEstandar(self):
        media = self.media()
        suma = 0
        for valor in self.__numeros:
            suma += (valor - media) ** 2
        radicando = suma / (len(self.__numeros) - 1)
        return sqrt(radicando)




