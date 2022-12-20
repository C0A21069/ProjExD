import pygame as pg
import random
import sys

color = {"black":(0, 0, 0), "red":(255, 0, 0), "yellow":(255, 255, 0), "blue":(0, 0, 255)}

class Screen:
    def __init__(self, title, wh, fig_path):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(fig_path)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
}

    def __init__(self, path, ratio, xy):
        self.sfc = pg.image.load(path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((rad*2, rad*2)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) 

class Enemy: #敵キャラ
    vy = +1

    def __init__(self, path, ratio, xy):
        self.sfc = pg.image.load(path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.left, self.rct.centery = xy
        self.xy = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, xy, scr): #上下に動く
        if (self.rct.left, self.rct.centery) == xy:
            Enemy.vy *= random.choice([-1, 1])
        self.rct.move_ip(0, Enemy.vy)
        if check_bound(self.rct, scr.rct) != (+1, +1):
            Enemy.vy *= -1
        self.blit(scr)
        

class Shot: #たまでてくる
    def __init__(self, color, rad, obj):
        self.sfc = pg.Surface((rad*2, rad*2)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = obj.left
        self.rct.centery = obj.centery

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def player(self, scr): #自分
        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_SPACE]:
            self.rct.move_ip(-1, 0)
            self.blit(scr)
            
    def enemy(self, scr): #敵
        s = random.randint(0, 100)
        # if s % 3 == 0:
        self.rct.move_ip(-1, 0)
        self.blit(scr)




def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    # 練習１
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 練習３
    tori = Bird("fig/6.png", 2.0, (1300, 400))
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    tori.update(scr)

    chimp = Enemy("fig/chimp.png", 4.0, (0, 450)) #敵
    

    # 練習５
    bomb = Bomb(color["red"], 10, (+1, +1), scr)
    bomb.update(scr)

    tori_shot = Shot(color["blue"], 10, tori.rct) #こうかとんの球
    chimp_shot = Shot(color["yellow"], 10, chimp.rct) #敵の弾

    # 練習２
    while True:
        scr.blit() 
        chimp.update(chimp.xy, scr)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        tori.update(scr) # 練習3

        # 練習６
        bomb.update(scr)

        tori_shot.player(scr)
        chimp_shot.enemy(scr)

        # 練習８
        if tori.rct.colliderect(bomb.rct):
            return
 
        if chimp.rct.colliderect(tori_shot.rct): #敵がこうかとんの球に接触
            return

        if tori.rct.colliderect(chimp_shot.rct): #こうかとんが敵の球に接触
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()