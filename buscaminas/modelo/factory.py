from .tablero import Tablero

class FabricaTableros:

    configuraciones = {
        "facil" : (9, 9 , 10),
        "intermedio" : (16, 16, 40),
        "dificil" : (16, 30, 99)
        }
    
    @staticmethod
    def crear_tablero(nivel):
        ''' Crea un tablero de Buscaminas con las dimensiones especificadas y el número total de minas. '''
        if nivel in FabricaTableros.configuraciones:
            filas, columnas, total_minas = FabricaTableros.configuraciones[nivel]
            tablero = Tablero(filas, columnas, total_minas)
            tablero.colocar_minas()
            tablero.calcular_minas_vecinas()
            return tablero
        else:
            raise ValueError(f"Nivel desconocido: {nivel}. Niveles válidos: {list(FabricaTableros.configuraciones.keys())}")