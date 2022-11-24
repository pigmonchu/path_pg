import pygame as pg
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

        

bola1 = Ball(400, 300, 1, 1, (255, 255, 255))
bola2 = Ball(400, 300, 1, -1, (0, 255, 255))

game_over = False

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
            break

    bola1.update()
    bola2.update()
     
    pantalla_ppal.fill((255, 124, 125))
    bola1.draw(pantalla_ppal)
    bola2.draw(pantalla_ppal) 

    pg.display.flip()

pg.quit()

