import pygame as pg
from Settings import *
from Sprites import *
from os import path

class Frame_3:
    def __init__(self, main):
        self.background = pg.image.load(path.join(img_dir, "Frame3.png")).convert()
        self.all_sprites = pg.sprite.Group()
        self.main = main

        self.interact = False
        self.chat = False
        self.cigarette = False
        self.cigarette_b = False
        self.beer = False
        self.beer_b = False
        self.nothing = False

        self.ground = pg.sprite.Group()

        self.store = pg.sprite.Group()

        self.clerk = Clerk(main)
        self.store.add(self.clerk)
        self.all_sprites.add(self.clerk)

        self.walls = pg.sprite.Group()
        self.wall = Platform(735, 0, 110, 600)
        self.all_sprites.add(self.wall)
        self.walls.add(self.wall)

        self.exits = pg.sprite.Group()
        self.exit = Platform(0, 0, 10, 600)
        self.all_sprites.add(self.exit)
        self.exits.add(self.exit)

        self.floor = Platform(0, HEIGHT - 100, 800, 3)
        self.all_sprites.add(self.floor)
        self.ground.add(self.floor)

    def update(self, main):
        self.all_sprites.update()
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
            main.player.pos = vec(650, HEIGHT - 7)
            main.player.real_pos = 2200
            main.frame_2 = True
            main.frame_3 = False

        hit = pg.sprite.spritecollide(main.player, self.store, False)
        if hit:
            self.interact = True
            keyss = pg.key.get_pressed()
            if keyss[pg.K_e]:
                self.chat = True
                if main.player.pos.x < self.clerk.pos.x:
                    self.clerk.image = self.clerk.images[2]
                else:
                    self.clerk.image = self.clerk.images[0]
                self.interact = False
        else:
            self.interact = False

    def cigarettes(self):
        self.cigarette = True
        self.chat = False

    def beers(self):
        self.beer = True
        self.chat = False

    def nevermind(self):
        self.nothing = True
        self.chat = False