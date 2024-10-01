from srcs.formageometrica import FormaGeometrica

class Retangulo(FormaGeometrica):

    def __init__(self, cor, lado1, lado2):
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2

    @property
    def lado1(self):
        return self.__lado1

    @property
    def lado2(self):
        return self.__lado2

    def calcularArea(self):
        lado1 = self.__lado1
        lado2 = self.__lado2
        return lado1 * lado2

    def calcularPerimetro(self):
        lado1 = self.__lado1
        lado2 = self.__lado2
        return 2 * (lado1 + lado2)

    # def exibirDados(self):
    def __str__(self):
        return (f"O retângulo de cor {self.cor} com medidas {self.__lado1} e {self.__lado2} "
                f"tem área = {self.calcularArea()} e perímetro = {self.calcularPerimetro()}.")
