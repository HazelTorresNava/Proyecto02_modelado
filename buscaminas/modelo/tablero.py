import random

from modelo.casilla import Casilla
from collections import deque

class Tablero:
    def __init__(self, filas, columnas, total_minas=0 ):
        ''' Inicializa un tablero de Buscaminas con las dimensiones especificadas y el número total de minas. '''
        self.filas = filas
        self.columnas= columnas 
        self.total_minas = total_minas
        self.observadores = []
        self.matriz = [[Casilla() for _ in range(columnas)] for _ in range(filas)]
        self.juego_terminado = False
        self.victoria = False 
        self.casillas_descubiertas = 0

    def colocar_minas(self):
        ''' Coloca minas aleatoriamente en el tablero. '''
        minas_colocadas = 0
        while minas_colocadas < self.total_minas:
            c =random.randint(0, self.columnas-1) 
            f = random.randint(0, self.filas-1) 
            if self.matriz[f][c].tiene_mina == False:
                self.matriz[f][c].tiene_mina = True
                minas_colocadas += 1

    def calcular_minas_vecinas(self):
        ''' Calcula el número de minas vecinas para cada casilla del tablero. '''
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c].minas_vecinas = self.contar_vecinos(f, c)

    def contar_vecinos(self, f, c):
        ''' Cuenta el número de minas vecinas a la casilla en la posición (f, c). '''
        if self.matriz[f][c].tiene_mina:
            return -1
        contador = 0
        for i in range(max(0, f-1), min(self.filas, f+2)):
            for j in range(max(0, c-1), min(self.columnas, c+2)):
                if (i != f or j != c) and self.matriz[i][j].tiene_mina:
                    contador += 1
        return contador

    def descubrir(self, f,  c):
        '''' Descubre la casilla en la posición (f, c) y propaga el descubrimiento si es necesario. '''
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
        self.notificar_observadores()

    def propagar_descubrimiento(self, f, c):
        '''' Propaga el descubrimiento de casillas vecinas si la casilla actual no tiene minas vecinas. '''
        cola = deque([(f, c)])
        while cola:
            fila_actual, columna_actual = cola.popleft()
            for i in range(max(0, fila_actual-1), min(self.filas, fila_actual+2)):
                for j in range(max(0, columna_actual-1), min(self.columnas, columna_actual+2)):
                    if (i != fila_actual or j != columna_actual) and not self.matriz[i][j].esta_descubierta and not self.matriz[i][j].tiene_bandera:
                        self.matriz[i][j].esta_descubierta = True
                        self.casillas_descubiertas += 1
                        if self.matriz[i][j].minas_vecinas == 0:
                            cola.append((i, j))

    def alternar_bandera(self, f, c):
        ''' Alterna el estado de la bandera en la casilla en la posición (f, c). '''
        if self.juego_terminado or self.matriz[f][c].esta_descubierta:
            return
        self.matriz[f][c].alternar_bandera()
        self.notificar_observadores()

    def agregar_observador(self, observador):
        ''' Agrega un observador al tablero. '''
        self.observadores.append(observador)

    def notificar_observadores(self):
        ''' Notifica a todos los observadores sobre un cambio en el tablero. '''
        for observador in self.observadores:
            observador.actualizar(self)