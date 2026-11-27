import tkinter as tk
class vista_tk:

    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Buscaminas")
        self.botones = []
        self.crear_interfaz()


    def actualizar(self, tablero):
            for f in range(tablero.filas):
                for c in range(tablero.columnas):
                    casilla = tablero.matriz[f][c]
                    boton = self.botones[f][c]

                    if casilla.esta_descubierta:
                        if casilla.tiene_mina:
                            boton.config(text="*", state="disabled", disabledforeground="red")
                        else:
                            texto = str(casilla.minas_vecinas) if casilla.minas_vecinas > 0 else " "
                            boton.config(text=texto, state="disabled", disabledforeground="black")
                    else:
                        if tablero.juego_terminado and not tablero.victoria and casilla.tiene_mina:
                            boton.config(text="*", state="disabled", disabledforeground="red")
                        elif casilla.tiene_bandera:
                            boton.config(text="|>", fg="blue")
                        else:
                            boton.config(text="", fg="black")

    def construir_botones(self, tablero):
        for f in range(tablero.filas):
            fila_botones = []
            for c in range(tablero.columnas):
                boton = tk.Button(self.root, width=3, height=1,
                command=lambda f=f, c=c: self.controlador.descubrir_casilla(f, c))
                boton.bind("<Button-3>", lambda event, f=f, c=c: self.controlador.colocar_bandera(f, c))
                boton.grid(row=f, column=c)
                fila_botones.append(boton)
            self.botones.append(fila_botones)


    #???????
    def actualiza_tiempo(self, tablero):
        self.segundos = 0
        self.reloj_corriendo  = False
        self.root.after(1000, self.actualizar_tiempo)


