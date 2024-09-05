
# Clear! Below, I present an example of how to delve deeper into the topic of Arithmetic using advanced object-oriented programming concepts, such as classes, inheritance, polymorphism and abstraction. In this case, we are going to create a hierarchy of classes for different arithmetic operations that represent the four basic operations (addition, subtraction, multiplication and division), using abstraction and polymorphism.

# Key Concepts:
# Abstraction: Let's create an abstract base class to represent a generic arithmetic operation.
# Inheritance: Specific operations such as addition, subtraction, multiplication and division will inherit from this base class.
# Polymorphism: Each child class will have its own implementation of the method to perform the arithmetic operation, but they will all share the same interface.
# Operator overloading: We will implement operator overloading to allow the use of arithmetic operators (+, -, *, /) between objects.

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


# Code explanation:
# Abstraction:

# The OperacionArithmetica class is an abstract class that defines an abstract method operate(). This means that any subclass that inherits from this class must implement this method.
# The class contains the attributes value1 and value2, which represent the operands of the arithmetic operations.
# Inheritance:

# The Addition, Subtraction, Multiplication and Division classes inherit from OperacionAritmetica and provide their own implementations of the operate() method.
# Polymorphism:

# Thanks to abstraction, all arithmetic operations share the same interface (operate()), which allows us to treat objects of these classes interchangeably in situations such as operator overloading.
# This is clearly seen when we add, subtract, multiply or divide two operations with each other, which demonstrates polymorphism.
# Operator overload:

# We have overloaded the +, -, * and / operators to allow addition, subtraction, multiplication and division between objects of type ArithmeticOperation. Each of these operators calls the operate() function of the corresponding objects to perform the operations.
# Exception handling:

# In the Division class, a check is included to prevent division by zero. If you try to divide by zero, an error message is returned instead of throwing an exception.



# Advantages of this approach:
# Extensibility: We can add new arithmetic operations without modifying the existing code. For example, we could easily implement a class for potentiation or square root.
# Reusability: Base classes and shared methods allow code to be more reusable.
# Maintenance: It is easier to maintain, since any change to the base class affects all operations consistently.
# This example shows how you can combine advanced object-oriented programming (OOP) concepts in Python to create a flexible and scalable system that goes deep into arithmetic.