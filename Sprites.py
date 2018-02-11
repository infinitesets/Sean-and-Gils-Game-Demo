#Sprite classes
import pygame as pg
from Settings import *
from os import path
vec = pg.math.Vector2

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
song_frame_1 = path.join(snd_dir, 'waterfront dining2.ogg')
song_frame_2 = path.join(snd_dir, 'waterfront dining.ogg')

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.direction = "right"
        self.index = 0
        self.images = []
        self.left_images = []

        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame1.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame2.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame3.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame4.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame5.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame6.png")).convert())

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
        if keys[pg.K_SPACE]:
            self.shoot()

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
        if self.real_pos >= 2270:
            self.pos.x = 730
        if self.real_pos < 80:
            self.pos.x = 80

        self.rect.midbottom = self.pos

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.right)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)

class OldMan(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.images.append(pg.image.load(path.join(img_dir, "OldMan_frame1_v1.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "OldMan_frame2_v1.png")).convert())

        for img in self.images:
            new_image = pg.transform.flip(img, True, False)
            self.images.append(new_image)

        self.image = self.images[self.index]
        self.last_update = pg.time.get_ticks()

        for img in self.images:
            img.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.pos = vec(15, HEIGHT / 2)
        self.rect.midbottom = self.pos

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 200:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.bullet_img = pg.image.load(path.join(img_dir, "laserRed.png")).convert()
        self.real_bullet = pg.transform.rotate(self.bullet_img, 90)
        self.image = self.real_bullet
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.midleft = y
        self.rect.midleft = x
        self.speedx = 10

    def update(self):
        self.rect.x += self.speedx
        if self.rect.bottom < -50 or self.rect.top > WIDTH + 50:
            self.kill()

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
        self.background2 = pg.image.load(path.join(img_dir, 'vapor.png')).convert()
        self.stage_width = 2350
        self.stage_pos_x = 0
        self.start_scroll_pos_x = WIDTH / 2

