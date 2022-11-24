import pygame as pg
pg.init()

pantalla_ppal = pg.display.set_mode((800, 600))
pg.display.set_caption("Hello pygame")

game_over = False

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
            break

    pantalla_ppal.fill((255, 125, 125))
    pg.display.flip()


pg.quit()