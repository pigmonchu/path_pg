import pygame as pg
pg.init()

pantalla_ppal = pg.display.set_mode((800, 600))
pg.display.set_caption("Pong")

game_over = False
x = 400
y = 300
while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
            break
    
    pantalla_ppal.fill((255, 124, 125))
    pg.draw.rect(pantalla_ppal, (123, 255, 123), (x, y, 100, 20))  

    pg.display.flip()

pg.quit()

