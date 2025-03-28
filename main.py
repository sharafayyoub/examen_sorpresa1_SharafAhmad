from superclase.Punto import Punto
from subclase.rectangulo import Rectangulo

def imprimir_puntos(puntos):
    """Imprime una lista de puntos."""
    print("Puntos:")
    for nombre, punto in puntos.items():
        print(f"{nombre}: {punto}")

def imprimir_cuadrantes(puntos):
    """Imprime el cuadrante de cada punto."""
    print("\nCuadrantes:")
    for nombre, punto in puntos.items():
        print(f"{nombre}: {punto.cuadrante()}")

def imprimir_vectores(punto1, punto2):
    """Imprime los vectores entre dos puntos."""
    print("\nVectores:")
    print(f"Vector {punto1} -> {punto2}: {punto1.vector(punto2)}")
    print(f"Vector {punto2} -> {punto1}: {punto2.vector(punto1)}")

def imprimir_distancias(puntos, referencia):
    """Imprime las distancias de varios puntos a un punto de referencia."""
    print("\nDistancias:")
    for nombre, punto in puntos.items():
        print(f"Distancia de {nombre} a {referencia}: {punto.distancia(referencia)}")

def imprimir_rectangulo(rectangulo):
    """Imprime las propiedades de un rectángulo."""
    print("\nRectángulo:")
    print(f"Base: {rectangulo.base()}")
    print(f"Altura: {rectangulo.altura()}")
    print(f"Área: {rectangulo.area()}")

def main():
    # Crear puntos
    a = Punto(2, 3)
    b = Punto(5, 5)
    c = Punto(-3, -1)
    d = Punto(0, 0)
    puntos = {"a": a, "b": b, "c": c, "d": d}

    # Imprimir puntos
    imprimir_puntos(puntos)

    # Imprimir cuadrantes
    imprimir_cuadrantes(puntos)

    # Imprimir vectores entre puntos
    imprimir_vectores(a, b)

    # Imprimir distancias desde el origen (punto d)
    imprimir_distancias({"a": a, "b": b, "c": c}, d)

    # Crear un rectángulo y consultar sus propiedades
    rectangulo = Rectangulo(a, b)
    imprimir_rectangulo(rectangulo)

if __name__ == "__main__":
    main()

