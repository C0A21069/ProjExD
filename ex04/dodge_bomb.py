import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_sfc = pg.transform.rotozoom(bg_sfc, 0, 1.0)
    bg_rct = bg_sfc.get_rect()
    bg_rct.center = 800, 450
    tori_sfc = pg.image.load("fig/5.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        scrn_sfc.blit(tori_sfc, tori_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()