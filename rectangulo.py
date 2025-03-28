from Punto import Punto

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        """
        Inicializa un rectángulo definido por dos puntos: el inicial (esquina inferior izquierda)
        y el final (esquina superior derecha).
        """
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def __str__(self):
        """Devuelve una representación en cadena del rectángulo."""
        return f"Rectangulo({self.punto_inicial}, {self.punto_final})"

    def base(self):
        """
        Calcula la base del rectángulo.
        Retorna:
            - La distancia horizontal entre los puntos inicial y final.
        """
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        """
        Calcula la altura del rectángulo.
        Retorna:
            - La distancia vertical entre los puntos inicial y final.
        """
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        """
        Calcula el área del rectángulo.
        Retorna:
            - El área como un número flotante.
        """
        return self.base() * self.altura()