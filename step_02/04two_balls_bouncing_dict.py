import pygame as pg
pg.init()

pantalla_ppal = pg.display.set_mode((800, 600))
pg.display.set_caption("Mueve una bola")

game_over = False

bola1 = {
    "x": 400,
    "y": 300,
    "vx": 1,
    "vy": 1,
    "color": (255, 255, 255)
}

bola2 = {
    "x": 400,
    "y": 300,
    "vx": 1,
    "vy": -1,
    "color": (0, 255, 255)
}


while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
            break

    bola1['x'] += bola1['vx']
    bola1['y'] += bola1['vy']

    if bola1['x'] > 800:
        bola1['vx'] = -1
    if bola1['y'] > 600:
        bola1['vy'] = -1

    if bola1['x'] < 0:
        bola1['vx'] = 1
    if bola1['y'] < 0:
        bola1['vy'] = 1
    

    bola2['x'] += bola2['vx']
    bola2['y'] += bola2['vy']

    if bola2['x'] > 800:
        bola2['vx'] = -1
    if bola2['y'] > 600:
        bola2['vy'] = -1

    if bola2['x'] < 0:
        bola2['vx'] = 1
    if bola2['y'] < 0:
        bola2['vy'] = 1
    
    
    pantalla_ppal.fill((255, 124, 125))

    pg.draw.circle(pantalla_ppal, bola1["color"], (bola1["x"], bola1["y"]), 12)  
    pg.draw.circle(pantalla_ppal, bola2["color"], (bola2["x"], bola2["y"]), 12)  

    pg.display.flip()

pg.quit()

