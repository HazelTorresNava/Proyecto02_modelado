try:
    from .controlador.controlador import Controlador
    from .vista.vista_tk import vista_tk
except ImportError:
    from controlador.controlador import Controlador
    from vista.vista_tk import vista_tk


if __name__ == "__main__":
    vista = vista_tk(None)

    controlador = Controlador(vista)
    vista.controlador = controlador

    vista.crear_interfaz()
    vista.root.mainloop()
