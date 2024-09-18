from srcs.formageometrica import FormaGeometrica

class Retangulo(FormaGeometrica):

    def __init__(self, cor, lado1, lado2):
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2

    def calcularArea(self):
        return 0  # Substituir por lógica

    def calcularPerimetro(self):
        return 0  # Substituir por lógica

    def exibirDados(self):
        return (f"O retângulo de cor {self.cor} com medidas {self.__lado1} e {self.__lado2} "
                f"tem área = {self.calcularArea()} e perímetro = {self.calcularPerimetro()}.")
