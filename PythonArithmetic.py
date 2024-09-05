from abc import ABC, abstractmethod

# Clase abstracta que representa una operación aritmética
class OperacionAritmetica(ABC):
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    # Método abstracto que debe ser implementado por las subclases
    @abstractmethod
    def operar(self):
        pass
    
    # Sobrecarga de operadores para que podamos sumar, restar, etc. directamente entre objetos
    def __add__(self, other):
        if isinstance(other, OperacionAritmetica):
            return self.operar() + other.operar()
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, OperacionAritmetica):
            return self.operar() - other.operar()
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, OperacionAritmetica):
            return self.operar() * other.operar()
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, OperacionAritmetica):
            return self.operar() / other.operar() if other.operar() != 0 else 'División por cero'
        return NotImplemented


# Subclase que implementa la operación de suma
class Suma(OperacionAritmetica):
    def operar(self):
        return self.valor1 + self.valor2

# Subclase que implementa la operación de resta
class Resta(OperacionAritmetica):
    def operar(self):
        return self.valor1 - self.valor2

# Subclase que implementa la operación de multiplicación
class Multiplicacion(OperacionAritmetica):
    def operar(self):
        return self.valor1 * self.valor2

# Subclase que implementa la operación de división
class Division(OperacionAritmetica):
    def operar(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero no permitida."


# Ejemplo de uso del sistema aritmético
def main():
    suma = Suma(10, 5)
    resta = Resta(10, 5)
    multiplicacion = Multiplicacion(10, 5)
    division = Division(10, 5)

    print("Suma: ", suma.operar())  # 10 + 5
    print("Resta: ", resta.operar())  # 10 - 5
    print("Multiplicación: ", multiplicacion.operar())  # 10 * 5
    print("División: ", division.operar())  # 10 / 5

    # Polimorfismo: Operaciones entre objetos
    print("Suma de Suma y Resta: ", suma + resta)  # (10 + 5) + (10 - 5)
    print("Multiplicación de Suma y Resta: ", suma * resta)  # (10 + 5) * (10 - 5)
    print("División de Suma y Multiplicación: ", suma / multiplicacion)  # (10 + 5) / (10 * 5)

    # Ejemplo de división por cero
    division_cero = Division(10, 0)
    print("División por cero: ", division_cero.operar())  # Manejo de división por cero


if __name__ == "__main__":
    main()
