import math
from srcs.formageometrica import FormaGeometrica

class Circunferencia(FormaGeometrica):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio

    def calcularArea(self):
        return math.pi * math.pow(self.__raio, 2)

    def calcularPerimetro(self):
        return 2 * math.pi * self.__raio

    def __str__(self):
        return (f"A circunferência de cor {self.cor} com raio {self.__raio} "
                f"tem área = {self.calcularArea():.2f} e perímetro = {self.calcularPerimetro():.2f}.")
