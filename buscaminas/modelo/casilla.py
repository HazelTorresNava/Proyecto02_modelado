class Casilla:
        def __init__(self, tiene_mina=False, minas_vecinas=0, esta_descubierta=False, tiene_bandera=False):
            ''' Inicializa una casilla del tablero de Buscaminas con las propiedades especificadas. '''
            self.tiene_mina = tiene_mina 
            self.minas_vecinas = minas_vecinas 
            self.esta_descubierta = esta_descubierta 
            self.tiene_bandera = tiene_bandera 


        def alternar_bandera(self):
            ''' Alterna el estado de la bandera en la casilla. '''
            if not self.esta_descubierta:
                self.tiene_bandera = not self.tiene_bandera
