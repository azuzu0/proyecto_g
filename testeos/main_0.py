from random import choice
cartas_white = {
    "cartasW": [],
    "identificaciones": []
}
tamano = 5
class Contador(object):
  def __init__(self, inicial=0):
    self.numero = inicial

  def siguiente(self):
    self.numero += 1
    return self.numero

cuenta = Contador()
for i in range(5):
   print(cuenta.siguiente())

def cardWhite(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f: 
          lineas = f.read().splitlines()
          return choice(lineas)
    except FileNotFoundError:
      return None

nombre_archivo = "files/cardWhite.txt"  
resultadoW = cardWhite(nombre_archivo)

for i in range(tamano):
    cartas = resultadoW
    identificacion = cuenta
    cartas_white["cartasW"].append(cartas)
    cartas_white["identificaciones"].append(identificacion)      

for i in range(tamano):
    # print("Mostrando los datos de la persona", i + 1)
    print("Carta:", cartas_white["cartasW"][i])
    print("Identificación:", cartas_white["identificaciones"][i])
