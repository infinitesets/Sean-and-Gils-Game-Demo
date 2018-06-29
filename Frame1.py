import pygame as pg
from Settings import *
from Sprites import *
from os import path

class Frame_1():
    def __init__(self, main):
        self.all_sprites = pg.sprite.Group()

        self.interact = False
        self.chat = False
        self.yes = False
        self.no = False
        self.talked = False
        self.touch = False
        self.win = False
        self.kitten = False
        self.flower = False
        self.robin = False

        self.ground = pg.sprite.Group()

        self.door = pg.sprite.Group()

        self.walls = pg.sprite.Group()
        self.old = pg.sprite.Group()
        self.wall = Platform(0, 0, 110, 600)
        self.all_sprites.add(self.wall)
        self.walls.add(self.wall)

        self.exits = pg.sprite.Group()
        self.exit = Platform(710, 0, 10, 600)
        self.all_sprites.add(self.exit)
        self.exits.add(self.exit)

        self.old_man = OldMan(main)
        self.old.add(self.old_man)
        self.all_sprites.add(self.old_man)

        self.floor = Platform(0, HEIGHT - 170, 800, 3)
        self.all_sprites.add(self.floor)
        self.ground.add(self.floor)

        self.background = pg.image.load(path.join(img_dir, "Frame 1.png")).convert()

    def update(self, main):
        self.all_sprites.update()
        self.touch = False

        if main.frame_two.chatted == True:
            self.secret = Platform(165, 300, 38, 100)
            self.all_sprites.add(self.secret)
            self.door.add(self.secret)

        hitto = pg.sprite.spritecollide(main.player, self.door, False)
        if hitto:
            self.touch = True

        if self.touch == True:
            keyss = pg.key.get_pressed()
            if keyss[pg.K_e]:
                self.win = True

        hits = pg.sprite.spritecollide(main.player, self.ground, False)
        if hits:
            main.player.pos.y = hits[0].rect.top + 1
            main.player.vel.y = 0

        main.player.rect.centerx = main.player.pos.x
        for wall in pg.sprite.spritecollide(main.player, self.walls, False):
            if main.player.vel.x > 0:
                main.player.rect.right = wall.rect.left
            elif main.player.vel.x < 0:
                main.player.rect.left = wall.rect.right
            main.player.pos.x = main.player.rect.centerx

        for exitz in pg.sprite.spritecollide(main.player, self.exits, False):
            main.player.pos = vec(180, HEIGHT - 7)
            main.player.real_pos = 180
            main.frame_1 = False
            main.frame_2 = True

        hit = pg.sprite.spritecollide(main.player, self.old, False)
        if hit:
            self.interact = True
            keyss = pg.key.get_pressed()
            if keyss[pg.K_e]:
                self.chat = True
                if main.player.pos.x < self.old_man.pos.x:
                    self.old_man.image = self.old_man.images[1]
                else:
                    self.old_man.image = self.old_man.images[0]
                self.interact = False
        else:
            self.interact = False

        '''self.player.rect.centery = self.player.pos.y
        for wall in pg.sprite.spritecollide(self.player, self.walls, False):
            if self.player.vel.y > 0:
                self.player.rect.bottom = wall.rect.top
            elif self.player.vel.y < 0:
                self.player.rect.top = wall.rect.bottom'''

    def yeah(self):
        self.chat = False
        self.yes = True
        self.talked = True

    def nah(self):
        self.chat = False
        self.no = True

    def cat(self):
        self.kitten = True

    def plant(self):
        self.flower = True

    def bird(self):
        self.robin = True