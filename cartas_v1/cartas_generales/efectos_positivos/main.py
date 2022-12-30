# import os 
# import random
# archivos = os.listdir("cartas_files")
# archivos_aleatorio = random.choice(archivos)
# print(archivos)

global descripcion, HP, ATQ, DEF, EXP
with open("Ayuda_de_Wuyu.txt", "r", encoding="utf-8") as f: 
    lineas = f.readlines()
    descripcion = lineas[0]
    HP = lineas[1]
    ATQ = lineas[2]
    DEF = lineas[3]
    EXP =lineas[4]    