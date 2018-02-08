#Sprite classes
import pygame as pg
from Settings import *
from os import path
vec = pg.math.Vector2

img_dir = path.join(path.dirname(__file__), 'img')

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.direction = "right"
        self.index = 0
        self.images = []
        self.left_images = []

        self.images.append(pg.image.load(path.join(img_dir, "Protagonist_frame1_v2.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "Protagonist_frame2_v2.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "Protagonist_frame3_v2.png")).convert())

        for img in self.images:
            new_image = pg.transform.flip(img, True, False)
            self.left_images.append(new_image)

        self.image = self.images[self.index]
        self.last_update = pg.time.get_ticks()

        for img in self.images:
            img.set_colorkey(WHITE)
        for img in self.left_images:
            img.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.pos = vec(15, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.real_pos = self.pos.x

    def jump(self):
        #Jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -=1
        if hits:
            self.vel.y = PLAYER_JUMP

    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if len(keys) == 0:
            self.index = 0
        now = pg.time.get_ticks()
        if keys[pg.K_LEFT]:
            self.direction = "left"
            self.acc.x = -PLAYER_ACC
            if now - self.last_update > 200:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
        if keys[pg.K_RIGHT]:
            self.direction = "right"
            self.acc.x = PLAYER_ACC
            if now - self.last_update > 200:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
        if self.direction == "right":
            self.image = self.images[self.index]
        elif self.direction == "left":
            self.image = self.left_images[self.index]
        if keys[pg.K_UP]:
            self.jump()

        if self.vel == 0:
            self.index = 0
            self.image = self.images[self.index]

        #Apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION

        #Equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.real_pos += self.vel.x + 0.5 * self.acc.x

        #Keep player on frame
        if self.real_pos >= 2360:
            self.pos.x = 760
        if self.real_pos < 26:
            self.pos.x = 26

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Frame_2_Background:
    def __init__(self):
        self.background = pg.image.load(path.join(img_dir, 'Frame 2_v1.png')).convert()
        self.stage_width = 2400
        self.stage_pos_x = 0
        self.start_scroll_pos_x = WIDTH / 2

