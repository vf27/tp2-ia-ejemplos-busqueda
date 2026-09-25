# TP2 - Inteligencia Artificial
# Busqueda heuristica primero el mejor del punto de montaje A sobre la horizontal H.
# Cada estado es una posicion en pasos desde B: B es 0, la derecha positiva y la izquierda negativa.
# Se incluyeron los valores de la posicion de A y del alcance del brazo para que al ejecutarlo corran los tres casos.

ALCANCE = 10  # hasta donde llega el brazo a cada lado de B
PROFUNDIDAD_ALOJAMIENTO = 5  # cuanto se hunde el brazo sobre la perforacion, dato de la pieza
PROFUNDIDAD_OTRO_REBAJE = 3  # otro hueco de la cara, menos profundo que el alojamiento


def profundidad(posicion, punto_a, otro_rebaje):  # lo que mide el brazo al tocar
    medida = PROFUNDIDAD_ALOJAMIENTO - abs(posicion - punto_a)  # mas hondo cerca de A
    if otro_rebaje is not None:
        medida = max(medida, PROFUNDIDAD_OTRO_REBAJE - abs(posicion - otro_rebaje))
    return max(medida, 0)  # lejos de los huecos la cara es plana


def buscar(punto_a, otro_rebaje=None):  # avanzo hacia el lado que mide mas hondo
    posicion = 0  # arranco en B
    recorrido = [posicion]
    while True:
        actual = profundidad(posicion, punto_a, otro_rebaje)
        if actual == PROFUNDIDAD_ALOJAMIENTO:  # llegue al alojamiento
            return posicion, recorrido
        mejor = None
        for vecina in (posicion - 1, posicion + 1):  # toco a los dos lados y comparo
            if abs(vecina) > ALCANCE:
                continue  # descarto lo que el brazo no alcanza
            if mejor is None or profundidad(vecina, punto_a, otro_rebaje) > profundidad(mejor, punto_a, otro_rebaje):
                mejor = vecina
        if profundidad(mejor, punto_a, otro_rebaje) <= actual:
            return None, recorrido  # ninguna vecina mejora, me quedo trabado
        posicion = mejor
        recorrido.append(posicion)


def simular_caso(titulo, punto_a, otro_rebaje=None):  # punto_a es el dato que el robot no conoce
    print(titulo)
    posicion, recorrido = buscar(punto_a, otro_rebaje)
    print("  recorrido:", " ".join(str(p) for p in recorrido))
    if posicion is None:
        print("  El brazo quedo detenido sin llegar a A.", len(recorrido), "posiciones revisadas")
    else:
        print("  A esta en la posicion", posicion, "-", len(recorrido), "posiciones revisadas")
    print()


simular_caso("Caso 1: el block se corrio 4 pasos a la izquierda", -4)
simular_caso("Caso 2: el block se corrio 2 pasos a la derecha", 2)
simular_caso("Caso 3: hay otro rebaje en la cara, 2 pasos a la derecha de B", -6, 2)
