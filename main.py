from srcs.retangulo import Retangulo

from srcs.circunferencia import Circunferencia

from srcs.triangulo import Triangulo


retangulo1 = Retangulo("azul", 10, 20)
# print("Área = ", retangulo1.calcularArea())
# print("Perímetro = ", retangulo1.calcularPerimetro())

retangulo2 = Retangulo("vermelha", 3, 4)
# print(retangulo2.exibirDados())

# retangulo2 = Retangulo("azul", 10, 20)
# print(f"O retângulo de lados {retangulo1.lado1} e {retangulo1.lado2} tem a cor {retangulo1.cor}.")
# print("Sua área é", retangulo1.calcularArea(), "e seu perímetro é", retangulo1.calcularPerimetro(), ".")

# Passo 5
circunferencia = Circunferencia("laranja", 2)
# print(circunferencia.exibirDados())

triangulo = Triangulo("verde", 3, 4, 5)

#Construir uma lista em main e utilizar o método append para inserir os objetos de retângulo e de circunferência na lista.

lista_formas = []
lista_formas.append(retangulo1)
lista_formas.append(retangulo2)
lista_formas.append(circunferencia)
lista_formas.append(triangulo)

for forma in lista_formas:
    print(forma)