import random
def attack(attacker, attacked):
    #Solo si el personaje esta vivo, podra ser atacado
    if attacked['health'] >= 0:
        #Dependiendo de la velocidad del atacado, este recibira danho o no
        if random.randint(1, 100) >  attacked['speed']:
            attacked['health'] -= attacker['damage']
            print('La vida de {} ha sido reducida a: {} por '.format(attacked['name'], attacked['health'], attacker['name']))
   

player = {'health': 100, 'damage': 40, 'speed': 80, 'name': 'hamed'}
enemy1 = {'health': 100, 'damage': 15, 'speed': 20, 'name': 'enemy1'}
enemy2 = {'health': 100, 'damage': 15, 'speed': 35, 'name': 'enemy2'}
enemy3 = {'health': 100, 'damage': 15, 'speed': 40, 'name': 'enemy3'}

while player['health'] > 0:
    if (enemy1['health'] + enemy2['health'] + enemy3['health'] ) > 0:
        attack(player, enemy1)
        attack(player, enemy2)
        attack(player, enemy3)
        attack(enemy1, player)
        attack(enemy2, player)
        attack(enemy3, player)
    else:
        print('el jugador elimino a todos los personajes')
        break
else:
    print("El jugador finalizo la partida con {} de vida".format(player['health']))