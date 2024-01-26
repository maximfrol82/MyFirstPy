from map import Map
import time
import os
from helicopter import Helicopter as Helico
import keyboard
from clouds import Clouds
import json

TICK_SLEEP = 0.005
TREE_UPDATE = 50
FIRE_UPDATE = 50
CLOUDS_UPDATE = 100
MAP_W, MAP_H = 10, 10

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)

field.generate_forest(3,10)
field.generate_river(5)
field.generate_river(3)
field.generate_river(2)
field.add_fire()
field.generate_upgrade_shop()
field.generate_hospital()

tick = 1

helico = Helico(MAP_W, MAP_H)

MOVES = {'w':(-1, 0), 'd':(0, 1), 's':(1, 0), 'a':(0, -1)}

def read_key(): 
    dx, dy = 0, 0 
    global helico, tick, field, clouds
    if keyboard.is_pressed('w'):
        dx, dy = MOVES['w'][0], MOVES['w'][1]
    elif keyboard.is_pressed('d'):
        dx = MOVES['d'][0]
        dy = MOVES['d'][1]
    elif keyboard.is_pressed('s'):
        dx = MOVES['s'][0]
        dy = MOVES['s'][1]  
    elif keyboard.is_pressed('a'):
        dx = MOVES['a'][0]
        dy = MOVES['a'][1]
    elif keyboard.is_pressed('u'):
        data = {
                "helicopter" : helico.export_data(),
                "clouds" : clouds.export_data(),
                "field" : field.export_data(),
                "tick" : tick
                }
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    elif keyboard.is_pressed('l'):
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            helico.import_data(data["helicopter"])
            tick = data["tick"] or 0
            field.import_data(data["field"])
            clouds.import_data(data["clouds"])
    elif keyboard.is_pressed('p'):
        os.system("clear")
        print('QUIT FROM GAME')
        exit(0)
    helico.move(dx, dy)


while True:
    os.system("clear")
    print('TICK', tick)
    read_key()
    if(tick % TREE_UPDATE == 0):
        field.generate_tree()
    if(tick % FIRE_UPDATE == 0):
        field.update_fires()
    if(tick % CLOUDS_UPDATE == 0):
        clouds.update_clouds()
    field.process_helico(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    tick += 1
    time.sleep(TICK_SLEEP)