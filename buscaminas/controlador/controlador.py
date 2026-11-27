from modelo.factory import FabricaTableros

class Controlador:

    def __init__(self, vista):
        self.vista = vista
        self.tablero = None



    def seleccionar_dificultad(self, nivel):
        ''' Crea un tablero de Buscaminas con la dificultad especificada. '''
        self.tablero = FabricaTableros.crear_tablero(nivel)
        self.tablero.agregar_observador(self.vista)
        self.vista.construir_tablero(self.tablero)
        self.vista.actualiza_tiempo(self.tablero) #check ?

    def descubrir_casilla(self, f, c):
        ''' Descubre la casilla en la posición (f, c) del tablero. '''
        self.tablero.descubrir(f, c)
        self.vista.actualizar(self.tablero, f, c)

        
    def colocar_bandera(self, f, c):
        ''' Coloca o quita una bandera en la casilla en la posición (f, c) del tablero. '''
        self.vista.actualizar(self.tablero)
        self.tablero.alternar_bandera(f, c)