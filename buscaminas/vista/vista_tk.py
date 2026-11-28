import tkinter as tk
from tkinter import messagebox


class vista_tk:

    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Buscaminas")
        self.botones = []
        self.botones_menu = []
        self.segundos = 0
        self.reloj_corriendo = False
        self.resultado_mostrado = False
        self.etiqueta_tiempo = tk.Label(self.root, text="Tiempo: 0")

    def crear_interfaz(self):
        """Muestra el menú de selección de dificultad."""
        self.mostrar_menu()

    def mostrar_menu(self):
        """Elimina el tablero y muestra las opciones de dificultad."""
        self.reloj_corriendo = False
        self.resultado_mostrado = False

        for fila_botones in self.botones:
            for boton in fila_botones:
                boton.destroy()
        self.botones = []

        for widget in self.botones_menu:
            widget.destroy()
        self.botones_menu = []

        self.etiqueta_tiempo.grid_forget()
        self.root.title("Buscaminas - Seleccionar nivel")

        titulo = tk.Label(self.root, text="Seleccione la dificultad", font=("TkDefaultFont", 12, "bold"))
        titulo.pack(pady=(20, 10))
        self.botones_menu.append(titulo)

        niveles = (
            ("Fácil", "facil"),
            ("Intermedio", "intermedio"),
            ("Difícil", "dificil"),
        )
        for texto, nivel in niveles:
            boton = tk.Button(
                self.root,
                text=texto,
                width=18,
                command=lambda nivel=nivel: self.controlador.seleccionar_dificultad(nivel),
            )
            boton.pack(pady=5)
            self.botones_menu.append(boton)

    def construir_tablero(self, tablero):
        """Construye una cuadrícula nueva para el tablero indicado."""
        for widget in self.botones_menu:
            widget.destroy()
        self.botones_menu = []

        for fila_botones in self.botones:
            for boton in fila_botones:
                boton.destroy()
        self.botones = []

        self.segundos = 0
        self.reloj_corriendo = False
        self.resultado_mostrado = False
        self.etiqueta_tiempo.config(text="Tiempo: 0")
        self.root.title("Buscaminas")

        for f in range(tablero.filas):
            fila_botones = []
            for c in range(tablero.columnas):
                boton = tk.Button(
                    self.root,
                    width=3,
                    height=1,
                    command=lambda f=f, c=c: self.controlador.descubrir_casilla(f, c),
                )
                boton.bind(
                    "<Button-3>",
                    lambda _event, f=f, c=c: self.controlador.colocar_bandera(f, c),
                )
                boton.grid(row=f, column=c)
                fila_botones.append(boton)
            self.botones.append(fila_botones)

        self.etiqueta_tiempo.grid(
            row=tablero.filas,
            column=0,
            columnspan=tablero.columnas,
        )

    def actualizar(self, tablero):
        """Actualiza los botones y muestra el resultado al terminar."""
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
                elif tablero.juego_terminado and not tablero.victoria and casilla.tiene_mina:
                    boton.config(text="*", state="disabled", disabledforeground="red")
                elif casilla.tiene_bandera:
                    boton.config(text="|>", fg="blue")
                else:
                    boton.config(text="", fg="black")

        if not tablero.juego_terminado:
            if not self.reloj_corriendo:
                self.reloj_corriendo = True
                self.actualizar_tiempo()
            return

        self.reloj_corriendo = False
        if not self.resultado_mostrado:
            self.resultado_mostrado = True
            if tablero.victoria:
                mensaje = "Felicidades! Eres un champion!!!!!."
            else:
                mensaje = "Has perdido! echàle ganas hijo."

            messagebox.showinfo("Fin del juego", mensaje, parent=self.root)
            self.mostrar_menu()

    def actualiza_tiempo(self, tablero=None):
        """Reinicia el cronómetro al crear un tablero."""
        if tablero is not None:
            self.segundos = 0
            self.etiqueta_tiempo.config(text="Tiempo: 0")

    def actualizar_tiempo(self):
        """Incrementa el cronómetro mientras la partida siga activa."""
        if self.reloj_corriendo:
            self.segundos += 1
            self.etiqueta_tiempo.config(text=f"Tiempo: {self.segundos}")
            self.root.after(1000, self.actualizar_tiempo)
