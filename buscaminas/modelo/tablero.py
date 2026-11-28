import random

try:
    from .casilla import Casilla
except ImportError:
    from modelo.casilla import Casilla

from collections import deque


class Tablero:
    def __init__(self, filas, columnas, total_minas=0):
        """Inicializa un tablero de Buscaminas con las dimensiones especificadas."""
        self.filas = filas
        self.columnas = columnas
        self.total_minas = total_minas
        self.observadores = []
        self.matriz = [[Casilla() for _ in range(columnas)] for _ in range(filas)]
        self.juego_terminado = False
        self.victoria = False
        self.casillas_descubiertas = 0

    def colocar_minas(self):
        """Coloca minas aleatoriamente en el tablero."""
        minas_colocadas = 0
        if self.total_minas > self.filas * self.columnas:
            raise ValueError("El número de minas no puede superar el número de casillas")

        while minas_colocadas < self.total_minas:
            c = random.randint(0, self.columnas - 1)
            f = random.randint(0, self.filas - 1)
            if not self.matriz[f][c].tiene_mina:
                self.matriz[f][c].tiene_mina = True
                minas_colocadas += 1

    def calcular_minas_vecinas(self):
        """Calcula el número de minas vecinas de cada casilla."""
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c].minas_vecinas = self.contar_vecinos(f, c)

    def contar_vecinos(self, f, c):
        """Cuenta las minas vecinas a una casilla."""
        if self.matriz[f][c].tiene_mina:
            return -1

        contador = 0
        for i in range(max(0, f - 1), min(self.filas, f + 2)):
            for j in range(max(0, c - 1), min(self.columnas, c + 2)):
                if (i != f or j != c) and self.matriz[i][j].tiene_mina:
                    contador += 1
        return contador

    def _coordenadas_validas(self, f, c):
        return 0 <= f < self.filas and 0 <= c < self.columnas

    def descubrir(self, f, c):
        """Descubre una casilla y propaga el descubrimiento si corresponde."""
        if not self._coordenadas_validas(f, c):
            return
        if self.juego_terminado or self.matriz[f][c].esta_descubierta or self.matriz[f][c].tiene_bandera:
            return

        if self.matriz[f][c].tiene_mina:
            self.juego_terminado = True
            self.victoria = False
            self.notificar_observadores()
            return

        self.matriz[f][c].esta_descubierta = True
        self.casillas_descubiertas += 1

        if self.matriz[f][c].minas_vecinas == 0:
            self.propagar_descubrimiento(f, c)

        if self.casillas_descubiertas == (self.filas * self.columnas) - self.total_minas:
            self.juego_terminado = True
            self.victoria = True

        self.notificar_observadores()

    def propagar_descubrimiento(self, f, c):
        """Propaga el descubrimiento desde una casilla sin minas vecinas."""
        cola = deque([(f, c)])

        while cola:
            fila_actual, columna_actual = cola.popleft()
            for i in range(max(0, fila_actual - 1), min(self.filas, fila_actual + 2)):
                for j in range(max(0, columna_actual - 1), min(self.columnas, columna_actual + 2)):
                    casilla = self.matriz[i][j]
                    if ((i != fila_actual or j != columna_actual)
                            and not casilla.esta_descubierta
                            and not casilla.tiene_bandera
                            and not casilla.tiene_mina):
                        casilla.esta_descubierta = True
                        self.casillas_descubiertas += 1
                        if casilla.minas_vecinas == 0:
                            cola.append((i, j))

    def alternar_bandera(self, f, c):
        """Alterna el estado de la bandera de una casilla."""
        if not self._coordenadas_validas(f, c):
            return
        if self.juego_terminado or self.matriz[f][c].esta_descubierta:
            return

        self.matriz[f][c].alternar_bandera()
        self.notificar_observadores()

    def agregar_observador(self, observador):
        """Agrega un observador al tablero."""
        self.observadores.append(observador)

    def notificar_observadores(self):
        """Notifica a todos los observadores sobre un cambio."""
        for observador in self.observadores:
            observador.actualizar(self)