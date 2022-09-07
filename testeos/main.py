# from random import choice
# def linea_aleatoria(archivo):
#     try:
#         with open(archivo, "r", encoding="utf-8") as f: 
#           lineas = f.read().splitlines()
#           return choice(lineas)
#     except FileNotFoundError:
#       return None

# nombre_archivo = "myfile.txt"  
# resultadoW = linea_aleatoria(nombre_archivo)      
# mensaje = "Hola Mundo!"

# mensaje2 = "Así es, mate a  "

# mensaje2 += "Deuda aplastante. "

# mensaje2 += "¿Como, preguntas? "

# mensaje2 += "Traumas con el papá."

# print(mensaje2)
r = "si"
mensaje8 = "Así es, mate a _"
mensaje8a = mensaje8.replace("_", r)
print(mensaje8a)
