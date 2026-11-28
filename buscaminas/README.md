# Buscaminas


## Funcionalidades

- Selección gráfica de dificultad: Fácil, Intermedio y Difícil.
- Descubrimiento de casillas mediante clic izquierdo.
- Colocación y eliminación de banderas mediante clic derecho.
- Expansión automática de las casillas vacías conectadas.
- Cuenta automática del tiempo de partida.
- Detección de victoria y derrota.
- Regreso automático al menú de niveles después de finalizar una partida.

## Arquitectura

- `modelo/`: contiene las casillas, el tablero, las minas y las reglas del juego.
- `vista/`: contiene la interfaz gráfica creada con Tkinter.
- `controlador/`: comunica la vista con el modelo.
- `main.py`: inicia la aplicación.
- `tests/`: contiene las pruebas unitarias del tablero.

## Requisitos

- Sistema operativo compatible con Python y Tkinter.
- Python 3.8 o posterior.
- Tkinter instalado.
- No se requieren paquetes externos de Python.

En sistemas Linux basados en Debian o Ubuntu, si Tkinter no está instalado puede agregarse con:

```bash
sudo apt update
sudo apt install python3-tk
```

## Instalación

1. Clonar o descargar el proyecto.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Asegurarse de que se utiliza Python 3:

```bash
python3 --version
```

No es necesario instalar dependencias externas.

## Ejecutar el juego

Desde la carpeta `buscaminas`:

```bash
cd /ruta/al/proyecto/buscaminas
python3 main.py
```

También puede ejecutarse como módulo desde la carpeta padre:

```bash
cd /ruta/al/proyecto
python3 -m buscaminas.main
```

Al iniciar la aplicación:

1. Seleccione un nivel de dificultad.
2. Use clic izquierdo para descubrir una casilla.
3. Use clic derecho para colocar o quitar una bandera.
4. Descubra todas las casillas que no contienen minas para ganar.
5. Si descubre una mina, la partida termina como derrota.
6. Después del resultado, la aplicación vuelve al menú de selección.

## Dificultades

| Nivel | Filas | Columnas | Minas |
|---|---:|---:|---:|
| Fácil | 9 | 9 | 10 |
| Intermedio | 16 | 16 | 40 |
| Difícil | 16 | 30 | 99 |

## Ejecutar las pruebas

Desde la carpeta `buscaminas`:

```bash
python3 -m unittest discover -s tests -v
```

Las pruebas verifican la expansión, la colocación de banderas, las victorias y las derrotas.