from collections import deque
import math

# Clase para manejar todas las ramas de las matemáticas
class Matematica:
    def __init__(self):
        self.stack = []  # pila
        self.queue = deque()  # cola
    
    # Aritmética: Suma, resta, multiplicación y división
    def aritmetica(self, a, b):
        return {
            'suma': a + b,
            'resta': a - b,
            'multiplicación': a * b,
            'división': a / b if b != 0 else 'División por cero no permitida'
        }
    
    # Álgebra: Resolver una ecuación de primer grado ax + b = 0
    def algebra(self, a, b):
        if a != 0:
            return f"La solución es x = {-b / a}"
        else:
            return "No es una ecuación válida (a no puede ser 0)"
    
    # Geometría: Calcular el área y perímetro de un círculo
    def geometria(self, radio):
        area = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio
        return {'área': area, 'perímetro': perimetro}
    
    # Trigonometría: Calcular seno, coseno y tangente de un ángulo en radianes
    def trigonometria(self, angulo):
        return {
            'seno': math.sin(angulo),
            'coseno': math.cos(angulo),
            'tangente': math.tan(angulo)
        }
    
    # Cálculo: Derivada sencilla f(x) = x^2 -> f'(x) = 2x
    def calculo_diferencial(self, x):
        return 2 * x
    
    # Teoría de Números: Verificar si un número es primo usando recursión
    def es_primo(self, n, divisor=None):
        if divisor is None:
            divisor = n - 1
        if divisor == 1:
            return True
        if n % divisor == 0:
            return False
        return self.es_primo(n, divisor - 1)
    
    # Estadística: Promedio y varianza de una lista de datos
    def estadistica(self, datos):
        n = len(datos)
        promedio = sum(datos) / n
        varianza = sum((x - promedio) ** 2 for x in datos) / n
        return {'promedio': promedio, 'varianza': varianza}
    
    # Matemática Discreta: Colas para tareas pendientes
    def agregar_tarea(self, tarea):
        self.queue.append(tarea)
    
    def siguiente_tarea(self):
        if self.queue:
            return self.queue.popleft()
        return "No hay tareas pendientes."
    
    # Topología: Usar una pila para guardar operaciones
    def agregar_operacion(self, operacion):
        self.stack.append(operacion)
    
    def deshacer_operacion(self):
        if self.stack:
            return self.stack.pop()
        return "No hay operaciones que deshacer."
    
    # Análisis: Ejemplo con series (Suma de una serie geométrica infinita)
    def suma_serie_geometrica(self, a, r, n):
        # Suma de los primeros n términos de la serie a + ar + ar^2 + ...
        if abs(r) < 1:
            return a / (1 - r)  # Suma infinita para |r| < 1
        else:
            return sum(a * r ** i for i in range(n))

# Ejecución del programa con ejemplos de cada rama

matematicas = Matematica()

# Aritmética
print("Aritmética:", matematicas.aritmetica(8, 4))

# Álgebra
print("Álgebra:", matematicas.algebra(2, 5))

# Geometría
print("Geometría:", matematicas.geometria(3))

# Trigonometría
print("Trigonometría:", matematicas.trigonometria(math.pi / 4))  # 45 grados en radianes

# Cálculo diferencial
print("Cálculo diferencial:", matematicas.calculo_diferencial(5))

# Teoría de números
print("Es primo 13:", matematicas.es_primo(13))

# Estadística
datos = [1, 2, 3, 4, 5]
print("Estadística:", matematicas.estadistica(datos))

# Matemática Discreta (Cola)
matematicas.agregar_tarea("Terminar reporte")
matematicas.agregar_tarea("Revisar código")
print("Siguiente tarea:", matematicas.siguiente_tarea())

# Topología (Pilas)
matematicas.agregar_operacion("Operación 1")
matematicas.agregar_operacion("Operación 2")
print("Deshacer operación:", matematicas.deshacer_operacion())

# Análisis (Suma de serie geométrica infinita)
print("Suma de serie geométrica:", matematicas.suma_serie_geometrica(1, 0.5, 10))
