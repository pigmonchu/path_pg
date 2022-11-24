import pygame as pg
from random import randint, choice
pg.init()

pantalla_ppal = pg.display.set_mode((800, 600))
pg.display.set_caption("Mueve una bola")


class Ball:
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    def update(self):
        self.x += self.vx
        self.y += self.vy

        if self.x > 800 or self.x < 0:
            self.vx = -self.vx
        if self.y > 600 or self.y <0:
            self.vy = -self.vy

    def draw(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.x, self.y), 12)

        
game_over = False

bolas = []
for i in range(randint(2,26)):
    bola = Ball(randint(1,799), 
                randint(1, 599), 
                randint(1,5)*choice((-1, 1)),
                randint(1,5)*choice((-1, 1)),
                (randint(0, 255), randint(0, 255), randint(0, 255)))
    bolas.append(bola)


while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
            break

    pantalla_ppal.fill((255, 124, 125))
    for bola in bolas:
        bola.update()
        bola.draw(pantalla_ppal)

    pg.display.flip()

pg.quit()

