import pygame as pg
pg.init()

pantalla_ppal = pg.display.set_mode((800, 600))
pg.display.set_caption("Mueve una bola")

game_over = False
x = 400
y = 300
while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
            break

    x += 1
    y += 1
    
    pantalla_ppal.fill((255, 124, 125))
    pg.draw.circle(pantalla_ppal, (255, 255, 255), (x, y), 12)  

    pg.display.flip()

pg.quit()

