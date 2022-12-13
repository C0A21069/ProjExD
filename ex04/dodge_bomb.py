import pygame as pg
import sys
import random

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

    bm_sfc = pg.Surface((20, 20))
    bm_sfc.set_colorkey(0, 0)
    pg.draw.circle(bm_sfc, (255, 0, 0), (10, 10), 10)
    bm_rct = bm_sfc.get_rect()
    bm_rct.center = random.randint(0, 1600), random.randint(0, 900)

    blbm_sfc = pg.Surface((20, 20)) #青い球を生成
    blbm_sfc.set_colorkey(0, 0)
    pg.draw.circle(blbm_sfc, (0, 0, 255), (10, 10), 10)
    blbm_rct = bm_sfc.get_rect()
    blbm_rct.center = random.randint(0, 1600), random.randint(0, 900)

    vx, vy = 1, 1
    ix, iy = 1, 1
    t = 1
    # rx, ry = 20, 20
    # cx, cy = 10, 10
    clock = pg.time.Clock()
    pg.time.set_timer(25, 5000) #5秒ごとにイベント
    # pg.time.set_timer(26, 15000) #15秒ごとにイベント
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        scrn_sfc.blit(tori_sfc, tori_rct)
        scrn_sfc.blit(bm_sfc, bm_rct)
        scrn_sfc.blit(blbm_sfc, blbm_rct)
        key_dct = pg.key.get_pressed()
        bm_rct.move_ip(vx, vy)
        blbm_rct.move_ip(ix, iy)
        # bm_rct.inflate_ip(rx, ry)
        def key_down(t):
            if key_dct[pg.K_UP]:
                tori_rct.centery -= t
            if key_dct[pg.K_DOWN]:
                tori_rct.centery += t
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx -= t
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx += t
        key_down(t)
        if check_bound(tori_rct, bg_rct) != (1, 1):
            key_down(-t)
        x, y = check_bound(bm_rct, bg_rct)
        vx *= x
        vy *= y
        xx, yy = check_bound(blbm_rct, bg_rct)
        ix *= xx
        iy *= yy
        for event in pg.event.get():
            if event.type == 25: #爆弾速度二倍
                vx *= 2
                vy *= 2
            # if event.type == 26: #爆弾大きさ二倍
            #     rx *= 2
            #     ry *= 2
            #     cx *= 2
            #     cy *= 2
            #     pg.draw.circle(bm_sfc, (255, 0, 0), (cx, cy), 10)
            if event.type == pg.QUIT:
                return

        if tori_rct.colliderect(blbm_rct):#青い球に当たったら速度を5に
            t = 5
            ix, iy = 0, 0
            blbm_rct.clamp_ip(tori_rct)

        if tori_rct.colliderect(bm_rct):
            return
        pg.display.update()
        clock.tick(2000)

def check_bound(obj_rct, scr_rct):
    x, y = 1, 1
    if obj_rct.left < scr_rct.left or obj_rct.right > scr_rct.right:
        x = -1
    if obj_rct.top < scr_rct.top or obj_rct.bottom > scr_rct.bottom:
        y = -1
    return x, y


        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()