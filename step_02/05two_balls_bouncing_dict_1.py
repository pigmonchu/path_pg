import pygame as pg
pg.init()

pantalla_ppal = pg.display.set_mode((800, 600))
pg.display.set_caption("Mueve una bola")


bola1 = {
    "x": 400,
    "y": 300,
    "vx": 1,
    "vy": -3,
    "color": (255, 255, 255)
}

bola2 = {
    "x": 400,
    "y": 300,
    "vx": 1,
    "vy": 1,
    "color": (0, 255, 255)
}

def update(bola):
    bola['x'] += bola['vx']
    bola['y'] += bola['vy']

    if bola['x'] > 800:
        bola['vx'] = -1
    if bola['y'] > 600:
        bola['vy'] = -1

    if bola['x'] < 0:
        bola['vx'] = 1
    if bola['y'] < 0:
        bola['vy'] = 1


def draw(bola, pantalla):
    pg.draw.circle(pantalla, bola["color"], (bola["x"], bola["y"]), 12)

game_over = False

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
            break

    update(bola1)
    update(bola2)
     
    pantalla_ppal.fill((255, 124, 125))
    draw(bola1, pantalla_ppal)  
    draw(bola2, pantalla_ppal)  

    pg.display.flip()

pg.quit()

