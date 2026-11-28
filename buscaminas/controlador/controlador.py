try:
    from ..modelo.factory import FabricaTableros
except ImportError:
    from modelo.factory import FabricaTableros


class Controlador:

    def __init__(self, vista=None):
        self.vista = vista
        self.tablero = None

    def seleccionar_dificultad(self, nivel):
        """Crea un tablero con la dificultad especificada."""
        self.tablero = FabricaTableros.crear_tablero(nivel)
        self.tablero.agregar_observador(self.vista)
        self.vista.construir_tablero(self.tablero)
        self.vista.actualiza_tiempo(self.tablero)

    def descubrir_casilla(self, f, c):
        """Descubre la casilla en la posición (f, c) del tablero."""
        self.tablero.descubrir(f, c)

    def colocar_bandera(self, f, c):
        """Coloca o quita una bandera en la casilla en la posición (f, c)."""
        self.tablero.alternar_bandera(f, c)