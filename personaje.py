import time
import random

class Ataque:
    def __init__(self, nombre, daño, prob_critico):
        self.nombre = nombre
        self.daño = daño
        self.prob_critico = prob_critico

class Personaje:
    def __init__(self, nombre, vitalidad, agilidad):
        self.agilidad = agilidad
        self.nombre = nombre
        self.vitalidad = vitalidad
    
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def esta_vivo(self):
        return self.vitalidad > 0
    
class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, agilidad, daño, ataque_esp):
        super().__init__(nombre, vitalidad, agilidad)
        self.daño = daño
        self.ataque_esp = ataque_esp
    
    def atacar_jugador(self, jugador):
        if random.randint(1, 100) >  jugador.agilidad: 
            print(f"Enemigo {self.nombre} atacando a jugador {jugador.nombre} con daño: {self.daño}")
            jugador.recibir_daño(self.daño, self)
    
    def recibir_daño(self, daño):
        self.vitalidad -= daño
        #print("{} tiene {} puntos de vida".format(self.nombre, self.vitalidad))

class Jugador(Personaje):
    def __init__(self, nombre, vitalidad, agilidad, habilidades, prob_contrataque): #habilidades sera un diccionario con todos los ataques
        super().__init__(nombre, vitalidad, agilidad)
        self.prob_contrataque = prob_contrataque
        self.habilidades = habilidades

    def atacar(self, ataque:Ataque, enemigo: Enemigo):
        if random.randint(1, 100) <  enemigo.agilidad:
            daño_recibido = ataque.daño
            if random.randint(1, 100) <=  ataque.prob_critico:
                print("\n -------------------------------------------------------------------------------------------")
                print("GOLPE CRITICO")
                print("\n -------------------------------------------------------------------------------------------")
                daño_recibido*=2
            enemigo.recibir_daño(daño_recibido)
            print("Se ha ejecutado {} sobre {} por valor de {} puntos de vida".format(ataque.nombre, enemigo.nombre, daño_recibido))
    
    def recibir_daño(self, daño, enemigo: Enemigo):
        self.vitalidad -= daño
        if random.randint(1, 100) <  self.prob_contrataque:
            self.atacar(self.habilidades['contrataque'], enemigo)

    def listar_ataques(self):     
        for value in self.habilidades.values():
            print(f"Puedo {value.nombre}")

jugador = Jugador("Juan", 100, 80, {"contrataque": Ataque("contrataque", 15, 100), "ataque basico": Ataque("ataque basico", 10, 40)}, 80)
jugador.listar_ataques()
jugador.saludo()

enemigo = Enemigo("Raul", 50, 30, 10, 70)

while jugador.esta_vivo():
    if not enemigo.esta_vivo():
        break;
    enemigo.atacar_jugador(jugador)
    print(f"vitalidad {jugador.nombre}: {jugador.vitalidad}")
    time.sleep(1)
    #jugador.atacar(jugador.habilidades["ataque basico"], enemigo)

print("El jugador {} finalizo la partida con: {}".format(jugador.nombre, jugador.vitalidad))

# EJERCICIO:
# Modificar este programa para agregar las siguientes caracteristicas:
# 1. Agregar logica de daño aleatorio al enemigo.
# 2. Agregar lógica de contraataque del jugador.
# 3. Agregar posibilidad de daño crítico en contra ataque del jugador.

