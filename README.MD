# Roteiro de Desenvolvimento

Este projeto é desenvolvido para a disciplina, conforme o roteiro indicado. O projeto consiste em criar uma estrutura utilizando **Python** e **POO** para simular formas geométricas e calcular suas áreas e perímetros.

## Estrutura de Pastas

A estrutura de pastas no **Pycharm** ou **Replit** deve seguir o seguinte formato:

```
ProjetoAtividadeProblematizadora/
│
├── srcs/
│   ├── formageometrica.py
│   ├── retangulo.py
│   ├── circunferencia.py
│   ├── triangulo.py
│
└── main.py
```

---

## Passos

### 1. Criação do projeto e estrutura

- Crie o projeto chamado **ProjetoAtividadeProblematizadora**.
- Dentro da pasta **srcs**, crie um arquivo chamado **formageometrica.py** com a seguinte classe abstrata:

```python
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    def __init__(self, cor):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    def alterarCor(self, cor):
        self.__cor = cor

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

    @abstractmethod
    def exibirDados(self)
        pass
```

Esta será a superclasse das formas geométricas.

### 2. Criação da classe `Retangulo`

- Crie o arquivo **retangulo.py** e nele construa a classe **Retangulo** utilizando herança de **FormaGeometrica**.
- Inicialmente, os métodos de cálculo de área e perímetro devem retornar `0`:

```python
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
```

### 3. Testes no arquivo `main.py`

- Crie o arquivo **main.py** para instanciar objetos da classe **Retangulo** e testar os métodos:

```python
from srcs.retangulo import Retangulo

retangulo1 = Retangulo("azul", 10, 20)
print("Área = ", retangulo1.calcularArea())
print("Perímetro = ", retangulo1.calcularPerimetro())

retangulo2 = Retangulo("vermelha", 3, 4)
print(retangulo2.exibirDados())
```

### 4. Expondo atributos com `@property`

- Utilize o **@property** para expor os atributos `__lado1` e `__lado2` fora da classe **Retangulo**. O arquivo **main.py** deve exibir algo como:

```python
from srcs.retangulo import Retangulo

retangulo1 = Retangulo("azul", 10, 20)
print(f"O retângulo de lados {retangulo1.lado1} e {retangulo1.lado2} tem a cor {retangulo1.cor}.")
print("Sua área é", retangulo1.calcularArea(), "e seu perímetro é", retangulo1.calcularPerimetro(), ".")
```

### 5. Criar a classe `Circunferencia`

- Crie a classe **Circunferencia** com o atributo **raio** e implemente os métodos de área e perímetro usando **math.pi** e **math.pow**.

Exemplo de como o **main.py** deve ficar:

```python
from srcs.circunferencia import Circunferencia

circunferencia = Circunferencia("laranja", 2)
print(circunferencia.exibirDados())
```

O resultado deve ser formatado com 2 casas decimais.

### 6. Implementação de `__str__`

- Renomeie o método `exibirDados()` para `__str__()` em todas as classes, permitindo exibir a forma geométrica diretamente.

### 7. Lista de Formas

- Crie uma lista em **main.py** e insira objetos de **Retangulo** e **Circunferencia**. Use um loop `for` para exibir os dados de cada forma da lista:

```python
formas = [retangulo1, retangulo2, circunferencia]
for forma in formas:
    print(forma)
```

---

## Entrega

A entrega deve ser feita seguindo estas etapas:

1. Compactar o projeto em **.zip** (caso esteja utilizando Pycharm ou Replit).
2. Fazer um vídeo apresentando o projeto e postá-lo no **YouTube**.
3. Submeter o link do vídeo e o arquivo **.zip** do projeto.

---

**Boa sorte e bom trabalho!**
