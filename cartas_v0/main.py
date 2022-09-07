from random import choice
def linea_aleatoria(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f: 
          lineas = f.read().splitlines()
          return choice(lineas)
    except FileNotFoundError:
      return None
    
def linea_aleatoria2(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f: 
          lineas = f.read().splitlines()
        return choice(lineas)
    except FileNotFoundError:
      return None

nombre_archivo = "files/myfile.txt"  
resultadoW = linea_aleatoria(nombre_archivo)
nombre_archivo2 = "files/cardBlack.txt"  
resultadoB = linea_aleatoria2(nombre_archivo2)

print(resultadoB +" "+ resultadoW)
