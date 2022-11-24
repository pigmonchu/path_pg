import pygame as pg
pg.init()

WIDTH = 800
HEIGHT = 600

pantalla_ppal = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")


class Ball:
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radio = 12

    def update(self):
        self.x += self.vx
        self.y += self.vy

        if self.x > WIDTH - self.radio or self.x < self.radio:
            self.vx = -self.vx
        if self.y > HEIGHT - self.radio or self.y < self.radio:
            self.vy = -self.vy

    def draw(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.x, self.y), self.radio)

class Racket:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    
    def draw(self, pantalla):
        pg.draw.rect(pantalla, self.color, (self.x, self.y, self.w, self.h))


    def update(self):
        if pg.key.get_pressed()[pg.K_LEFT] and self.x > 0:
            self.x -= 5
        if pg.key.get_pressed()[pg.K_RIGHT] and self.x < WIDTH - self.w:
            self.x += 5

bola = Ball(400, 300, 1, 1, (255, 255, 255))
raqueta = Racket(400, 300, 100, 20, (50, 255, 50))

game_over = False

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
            break

   
    bola.update()
    raqueta.update()

    pantalla_ppal.fill((255, 124, 125))
    bola.draw(pantalla_ppal)
    raqueta.draw(pantalla_ppal)


    pg.display.flip()

pg.quit()

