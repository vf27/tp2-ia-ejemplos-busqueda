# TP2 - Inteligencia Artificial
# Busqueda primero en anchura del punto de montaje A sobre la horizontal H.
# Cada estado es una posicion medida en pasos desde B. B es la posicion 0,
# los valores positivos quedan a la derecha y los negativos a la izquierda.

from collections import deque

ALCANCE = 10  # pasos que el brazo puede recorrer a cada lado de B


def siguientes_posiciones(posicion):
    if posicion == 0:
        siguientes = [1, -1]
    elif posicion > 0:
        siguientes = [posicion + 1]
    else:
        siguientes = [posicion - 1]
    return [p for p in siguientes if abs(p) <= ALCANCE]


def buscar(punto_a):
    cola = deque([0])
    revisadas = 0
    while cola:
        posicion = cola.popleft()
        revisadas += 1
        if posicion == punto_a:
            print("  posicion", posicion, "-> encuentra A")
            return posicion, revisadas
        print("  posicion", posicion, "-> no encuentra A")
        for siguiente in siguientes_posiciones(posicion):
            cola.append(siguiente)
    return None, revisadas


def probar(titulo, punto_a):
    print(titulo)
    posicion, revisadas = buscar(punto_a)
    if posicion is None:
        print("  A quedo fuera del alcance del brazo.", revisadas, "posiciones revisadas")
    else:
        print("  A esta en la posicion", posicion, "-", revisadas, "posiciones revisadas")
    print()


probar("Caso 1: el block se corrio 4 pasos a la izquierda", -4)
probar("Caso 2: el block se corrio 2 pasos a la derecha", 2)
probar("Caso 3: el block se corrio mas que el alcance del brazo", 15)
