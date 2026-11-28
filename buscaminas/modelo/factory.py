try:
    from .tablero import Tablero
except ImportError:
    from modelo.tablero import Tablero


class FabricaTableros:

    configuraciones = {
        "facil": (9, 9, 10),
        "intermedio": (16, 16, 40),
        "dificil": (16, 30, 99),
    }

    @staticmethod
    def crear_tablero(nivel):
        """Crea un tablero con la dificultad especificada."""
        if nivel not in FabricaTableros.configuraciones:
            raise ValueError(
                f"Nivel desconocido: {nivel}. "
                f"Niveles válidos: {list(FabricaTableros.configuraciones.keys())}"
            )

        filas, columnas, total_minas = FabricaTableros.configuraciones[nivel]
        tablero = Tablero(filas, columnas, total_minas)
        tablero.colocar_minas()
        tablero.calcular_minas_vecinas()
        return tablero