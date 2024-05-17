class Nodo:
    def __init__(self, estado, jugador):
        self.estado = estado
        self.jugador = jugador
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

'''
def construir_arbol(estado, jugador):
    nodo_actual = Nodo(estado, jugador)

    # Verificar si el juego ha terminado
    if estado.juego_terminado():
        return nodo_actual

    # Generar todos los posibles movimientos
    posibles_movimientos = estado.obtener_posibles_movimientos()

    # Construir recursivamente el árbol para cada posible movimiento
    for movimiento in posibles_movimientos:
        nuevo_estado = estado.aplicar_movimiento(movimiento, jugador)
        nuevo_jugador = otro_jugador(jugador)
        hijo = construir_arbol(nuevo_estado, nuevo_jugador)
        nodo_actual.agregar_hijo(hijo)

    return nodo_actual'''