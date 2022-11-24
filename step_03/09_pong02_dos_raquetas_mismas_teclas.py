import pygame as pg
pg.init()

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

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
        if pg.key.get_pressed()[pg.K_UP] and self.y > 0:
            self.y -= 5
        if pg.key.get_pressed()[pg.K_DOWN] and self.y < HEIGHT - self.h:
            self.y += 5

bola = Ball(WIDTH // 2, HEIGHT // 2, 1, 1, YELLOW)
raqueta1 = Racket(WIDTH - 40, (HEIGHT - 100) // 2, 20, 100, WHITE)
raqueta2 = Racket(20, (HEIGHT - 100) // 2, 20, 100, WHITE)
game_over = False

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
            break

   
    bola.update()
    raqueta1.update()
    raqueta2.update()

    pantalla_ppal.fill(BLACK)
    bola.draw(pantalla_ppal)
    raqueta1.draw(pantalla_ppal)
    raqueta2.draw(pantalla_ppal)


    pg.display.flip()

pg.quit()

