from random import choice
# Metodo para leer el archvio .txt donde se alojan las cartas blancas.
# Igualemnte toma una linea random del archivo y lo guarda en la variable resultadoW.
def cardWhite(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f: 
          lineas = f.read().splitlines()
          return choice(lineas)
    except FileNotFoundError:
      print("No se ha podido encontrar el archivo.")
    except IndexError:
     print("El archivo no contiene información.")  
     
# Metodo para leer el archvio .txt donde se alojan las cartas negras.
# Igualemnte toma una linea random del archivo y lo guarda en la variable resultadoB.
def cardBlack(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f: 
          lineas = f.read().splitlines()
        return choice(lineas)
    except FileNotFoundError:
      print("No se ha podido encontrar el archivo.")
    except IndexError:
     print("El archivo no contiene información.") 

# Metodo para leer el archvio .txt donde se alojan las cartas negras con doble pick.
# Igualemnte toma una linea random del archivo y lo guarda en la variable resultadoB2.
def cardBlack2Pick(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f: 
          lineas = f.read().splitlines()
        return choice(lineas)
    except FileNotFoundError:
      print("No se ha podido encontrar el archivo.")
    except IndexError:
     print("El archivo no contiene información.")      


# Variable contenedora del archivo .txt
nombre_archivo = "files/cardWhite.txt"  
# Objeto contenedora de la carta tomada.
resultadoW = cardWhite(nombre_archivo)
resultadoW2 = cardWhite(nombre_archivo)

# Variable contenedora del archivo .txt
nombre_archivo2 = "files/cardBlack.txt" 
# Objeto contenedora de la carta tomada. 
resultadoB = cardBlack(nombre_archivo2)

nombre_archivo3 = "files/cardBlack2.txt"  
resultadoB2 = cardBlack2Pick(nombre_archivo3)

# Variable contenedora de modificacion del caracter "_" para 
# las cartas de doble pick. Esto toma dos resultadosW para colocarlo en resultadoB2.


mensaje = resultadoB2.replace("_", resultadoW)
print(mensaje)



# print(resultadoB)
# print(resultadoB2)
