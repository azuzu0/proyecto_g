import re
from cartas_generales.efectos_positivos.main import descripcion, HP, ATQ, DEF, EXP

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.experiencia = 0
        self.nivel = 1

    def cartas_bonus(self):
        if "HP" in descripcion:
            patron = r'\d+'
            linea = HP
            numero = re.findall(patron,linea)
            primer_elemento = numero[0]
            numero_entero = int(primer_elemento)
            vida_total = self.vida + numero_entero
            self.vida = vida_total
        
        if "ATQ" in descripcion:
            patron = r'\d+'
            linea = ATQ
            numero = re.findall(patron,linea)
            primer_elemento = numero[0]
            numero_entero = int(primer_elemento)
            ataque_total = self.ataque + numero_entero
            self.ataque = ataque_total 
            
        if "DEF" in descripcion:
            patron = r'\d+'
            linea = DEF
            numero = re.findall(patron,linea)
            primer_elemento = numero[0]
            numero_entero = int(primer_elemento)
            defensa_total = self.defensa + numero_entero
            self.defensa = defensa_total
            
        if "EXP" in descripcion:
            patron = r'\d+'
            linea = EXP
            numero = re.findall(patron,linea)
            primer_elemento = numero[0]
            numero_entero = int(primer_elemento)
            exp_total = self.experiencia + numero_entero
            self.experiencia = exp_total
            
    def atacar(self, objetivo):
        global daño
        daño = self.ataque - objetivo.defensa
        if daño > 0:
            objetivo.recibir_ataque(daño)
            return True

    def recibir_ataque(self, daño):
        global vida_resultante
        self.vida -= daño
        if self.vida <= 0:
            self.vida = 0
            return True
    
    def esta_vivo(self):
        return self.vida > 0

    def ganar_experiencia(self, experiencia):
        self.experiencia += experiencia
        while self.experiencia >= 100:
            self.experiencia -= 100
            self.nivel += 1
            print(self.nombre + " ha subido al nivel " + str(self.nivel))


    def recuperar_vida(self, cantidad):
        self.vida += cantidad
        if self.vida > 100:
            self.vida = 100
        print(self.nombre + " ha recuperado " + str(cantidad) + " puntos de vida.")

        
personaje1 = Personaje("Mauricio", 100, 20, 10)
personaje2 = Personaje("Juan", 100, 10, 5)


# while personaje1.esta_vivo() and personaje2.esta_vivo():
    
#     if personaje1.atacar(personaje2):
#         print(personaje1.nombre + " ataco a " + personaje2.nombre + " haciendole " + str(daño) + " de daño y dejandolo con " + str(personaje2.vida) + " puntos de vida.")
#     else:
#         if personaje1.esta_vivo is not True:
#             print(personaje1.nombre + " ha muerto.")
#         elif daño == 0:
#             print(personaje1.nombre + " fallo el ataque a " + personaje2.nombre)
    
#     if personaje2.atacar(personaje1):
#         print(personaje2.nombre + " ataco a " + personaje1.nombre + " haciendole " + str(daño) + " de daño y dejandolo con " + str(personaje1.vida) + " puntos de vida.")
#     else:
#         if personaje2.esta_vivo() is not True: 
#             print(personaje2.nombre + " ha muerto.")  
#         elif daño == 0:    
#             print(personaje2.nombre + " fallo el ataque a " + personaje1.nombre)


personaje1.cartas_bonus()
print(personaje1.vida)
print(personaje1.ataque)
print(personaje1.defensa)


