import math

class Punto:
    def __init__(self, x=0, y=0):
        """Inicializa un punto en el plano cartesiano."""
        self.x = x
        self.y = y

    def __str__(self):
        """Devuelve una representación en cadena del punto."""
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        """
        Determina el cuadrante en el que se encuentra el punto.
        Retorna:
            - 1 si está en el primer cuadrante.
            - 2 si está en el segundo cuadrante.
            - 3 si está en el tercer cuadrante.
            - 4 si está en el cuarto cuadrante.
            - 0 si está en el origen o sobre un eje.
        """
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0

    def vector(self, otro):
        """
        Calcula el vector entre este punto y otro.
        Parámetros:
            - otro: Otro punto (instancia de la clase Punto).
        Retorna:
            - Una tupla (dx, dy) que representa el vector.
        """
        return (otro.x - self.x, otro.y - self.y)

    def distancia(self, otro):
        """
        Calcula la distancia euclidiana entre este punto y otro.
        Parámetros:
            - otro: Otro punto (instancia de la clase Punto).
        Retorna:
            - La distancia como un número flotante.
        """
        return math.sqrt((otro.x - self.x) ** 2 + (otro.y - self.y) ** 2)
    
    

    