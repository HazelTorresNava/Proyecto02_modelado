import random

from modelo.casilla import Casilla
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