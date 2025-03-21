import pygame as pg

win = pg.display.set_mode((500, 500))

clock = pg.time.Clock()

run = True

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    win.fill((250,0,0))
    pg.display.update()
    clock.tick(60)

pg.quit()