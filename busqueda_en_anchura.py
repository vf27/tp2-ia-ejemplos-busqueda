# TP2 - Inteligencia Artificial
# Busqueda primero en anchura del punto de montaje A sobre la horizontal H.
# Cada estado es una posicion en pasos desde B: B es 0, la derecha positiva y la izquierda negativa.
# Se incluyeron los valores de la posicion de A y del alcance del brazo para que al ejecutarlo corran los tres casos.

from collections import deque

ALCANCE = 10  # hasta donde llega el brazo a cada lado de B


def siguientes_posiciones(posicion):  # a donde puedo ir desde aca
    if posicion == 0:
        siguientes = [1, -1]  # desde B abro los dos lados
    elif posicion > 0:
        siguientes = [posicion + 1]  # sigo para el mismo lado, atras ya revise
    else:
        siguientes = [posicion - 1]
    return [p for p in siguientes if abs(p) <= ALCANCE]  # descarto lo que el brazo no alcanza


def buscar(punto_a):  # busco A sin saber de que lado quedo
    cola = deque([0])  # arranco en B
    recorrido = []
    while cola:
        posicion = cola.popleft()  # saco la que entro primero
        recorrido.append(posicion)
        if posicion == punto_a:  # toco la superficie y encuentro la perforacion
            return posicion, recorrido
        for siguiente in siguientes_posiciones(posicion):
            cola.append(siguiente)  # las agrego al final para no adelantar niveles
    return None, recorrido  # se vacio la cola, A quedo fuera del alcance


def simular_caso(titulo, punto_a):  # punto_a es el dato que el robot no conoce
    print(titulo)
    posicion, recorrido = buscar(punto_a)
    print("  recorrido:", " ".join(str(p) for p in recorrido))
    if posicion is None:
        print("  A quedo fuera del alcance del brazo.", len(recorrido), "posiciones revisadas")
    else:
        print("  A esta en la posicion", posicion, "-", len(recorrido), "posiciones revisadas")
    print()


simular_caso("Caso 1: el block se corrio 4 pasos a la izquierda", -4)
simular_caso("Caso 2: el block se corrio 2 pasos a la derecha", 2)
simular_caso("Caso 3: el block se corrio mas que el alcance del brazo", 15)
