from unittest import TestCase
from modelo.tablero import Tablero

class TestTablero(TestCase):

    def setUp(self):  
        self.t = Tablero(3, 3, 1)  # Crear un tablero de 3x3 con 1 mina
        self.t.matriz[0][2].tiene_mina = True  # Colocar la mina en el tablero
        self.t.calcular_minas_vecinas()

    def test_expansion_y_bandera(self):

        self.t.alternar_bandera(2, 2)  # Colocar una bandera en la casilla (2,2)
        # Descubrir la casilla (0,0) que no tiene mina y debería propagar el descubrimiento
        self.t.descubrir(0, 0)
        # Verificar que las casillas (0,0), (0,1), (1,0), (1,1) estén descubiertas
        self.assertTrue(self.t.matriz[0][0].esta_descubierta)
        self.assertTrue(self.t.matriz[0][1].esta_descubierta)
        self.assertTrue(self.t.matriz[1][0].esta_descubierta)
        self.assertTrue(self.t.matriz[1][1].esta_descubierta)
        # Verificar que la casilla (2,2) con bandera no esté descubierta
        self.assertFalse(self.t.matriz[2][2].esta_descubierta)
        # Verificar que la casilla (0,2) con mina no esté descubierta
        self.assertFalse(self.t.matriz[0][2].esta_descubierta)
        self.assertEqual(self.t.casillas_descubiertas, 7)
        # Verificar que la casilla (0,2) con mina no esté descubierta
        self.assertFalse(self.t.matriz[0][2].esta_descubierta)

    def test_derrota_por_mina(self):
        # Descubrir la casilla (0,2) que tiene una mina
        self.t.descubrir(0, 2)
        # Verificar que el juego haya terminado y que no haya victoria
        self.assertTrue(self.t.juego_terminado)
        self.assertFalse(self.t.victoria)

    def test_victoria(self):
        # Verificar que el juego no haya terminado y que no haya victoria
        self.assertFalse(self.t.juego_terminado)
        self.assertFalse(self.t.victoria)
        # Descubrir todas las casillas excepto la que tiene la mina
        for f in range(3):
            for c in range(3):
                if not self.t.matriz[f][c].tiene_mina:
                    self.t.descubrir(f, c)
        # Verificar que el juego haya terminado y que haya victoria
        self.assertTrue(self.t.juego_terminado)
        self.assertTrue(self.t.victoria)
