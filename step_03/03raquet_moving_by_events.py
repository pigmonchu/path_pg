import pygame as pg
pg.init()

pantalla_ppal = pg.display.set_mode((800, 600))
pg.display.set_caption("Pong")


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

class Racket:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    
    def draw(self, pantalla):
        pg.draw.rect(pantalla, self.color, (self.x, self.y, self.w, self.h))


bola = Ball(400, 300, 1, 1, (255, 255, 255))
raqueta = Racket(400, 300, 100, 20, (50, 255, 50))

game_over = False

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
            break

        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_LEFT:
                raqueta.x -= 5
            if evento.key == pg.K_RIGHT:
                raqueta.x += 5

    #bola.update()

    pantalla_ppal.fill((255, 124, 125))
    bola.draw(pantalla_ppal)
    raqueta.draw(pantalla_ppal)


    pg.display.flip()

pg.quit()

