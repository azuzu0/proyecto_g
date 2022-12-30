from random import choice
file_cardWhite = "files/cardWhite.txt"
file_cardBlack2 = "files/cardBlack2.txt"
# Metodo para leer el archvio .txt donde se alojan las cartas blancas.
# Igualemnte toma una linea random del archivo y lo guarda en la variable resultadoW.

def cardWhite(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.read().splitlines()
            return lineas
    except FileNotFoundError:
        print("No se ha podido encontrar el archivo.")

# Metodo para leer el archvio .txt donde se alojan las cartas negras.
# Igualemnte toma una linea random del archivo y lo guarda en la variable resultadoB.

def cardBlack(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.read().splitlines()
        return choice(lineas)
    except FileNotFoundError:
        print("No se ha podido encontrar el archivo.")

# Metodo para leer el archvio .txt donde se alojan las cartas negras con doble pick.
# Igualemnte toma una linea random del archivo y lo guarda en la variable resultadoB2.


def cardBlack2Pick(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.read().splitlines()
        return choice(lineas)
    except FileNotFoundError:
        print("No se ha podido encontrar el archivo.")
