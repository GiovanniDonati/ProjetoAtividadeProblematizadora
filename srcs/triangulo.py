from srcs.formageometrica import FormaGeometrica

class Triangulo(FormaGeometrica):
    def __init__(self, cor, lado1, lado2, lado3):
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    @property
    def lado1(self):
        return self.__lado1

    @property
    def lado2(self):
        return self.__lado2

    @property
    def lado3(self):
        return self.__lado3

    def calcularArea(self):
        # Fórmula de Heron
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return (s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3)) ** 0.5

    def calcularPerimetro(self):
        return self.__lado1 + self.__lado2 + self.__lado3

    # def exibirDados(self):
    def __str__(self):
        return (f"O triângulo de cor {self.cor} com lados {self.__lado1}, {self.__lado2} e {self.__lado3} "
                f"tem área = {self.calcularArea():.2f} e perímetro = {self.calcularPerimetro():.2f}.")
    
    #OBS:
    #Heron de Alexandria é o responsável por elaborar uma fórmula matemática que calcula a área de um triângulo em função das medidas dos seus três lados. A fórmula de Heron de Alexandria é muito útil nos casos em que não sabemos a altura do triângulo, mas temos a medida dos lados.
# Em um triângulo de lados medindo a, b e c podemos calcular a sua área utilizando a fórmula de Heron:
# S = (a + b + c) / 2
# Área = √(S * (S - a) * (S - b) * (S - c))
# Onde S é o semiperímetro do triângulo.
# Para calcular o semiperímetro do triângulo, basta somar as medidas dos três lados e dividir por 2.