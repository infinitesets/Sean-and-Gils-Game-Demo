#Sprite classes
import pygame as pg
from Settings import *
from os import path
vec = pg.math.Vector2

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
#song = path.join(snd_dir, 'song.mp3')
#shoot_sound = path.join(snd_dir, 'Laser_Shoot19.wav')


class Player(pg.sprite.Sprite):
    def __init__(self, main):
        self.main = main
        self.health = 100
        self.money = 0
        self.walking = False

        pg.sprite.Sprite.__init__(self)
        self.direction = "right"
        self.index = 0
        self.images = []
        self.left_images = []
        self.right_images = []

        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame1.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame2.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame3.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame4.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame5.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "VideoGame_Character_frame6.png")).convert())

        for img in self.images:
            new_image = pg.transform.scale(img, (144, 120))
            self.right_images.append(new_image)


        for img in self.images:
            img = pg.transform.flip(img, True, False)
            new_image = pg.transform.scale(img, (144, 120))
            self.left_images.append(new_image)

        self.image = self.right_images[self.index]
        self.last_update = pg.time.get_ticks()

        for img in self.right_images:
            img.set_colorkey(WHITE)
        for img in self.left_images:
            img.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.pos = vec(200, HEIGHT - 170)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.real_pos = self.pos.x

    def jump(self):
        #Jump only if standing on a platform
        self.rect.x += 1
        if self.main.frame_1 == True:
            hits = pg.sprite.spritecollide(self.main.player, self.main.frame_one.ground, False)
        elif self.main.frame_2 == True:
            hits = pg.sprite.spritecollide(self.main.player, self.main.frame_two.ground, False)
        elif self.main.frame_3 == True:
            hits = pg.sprite.spritecollide(self.main.player, self.main.frame_three.ground, False)
        self.rect.x -=1
        if hits and self.main.frame_1 or self.main.frame_3:
            self.vel.y = PLAYER_JUMP
        elif hits and self.main.frame_2:
            self.vel.y = FRAME_TWO_JUMP

    def update(self):
        self.walking = False
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        now = pg.time.get_ticks()
        if keys[pg.K_LEFT]:
            self.direction = "left"
            self.walking = True
            self.acc.x = -PLAYER_ACC
            if now - self.last_update > PLAYER_ANIMATION:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
        if keys[pg.K_RIGHT]:
            self.direction = "right"
            self.walking = True
            self.acc.x = PLAYER_ACC
            if now - self.last_update > PLAYER_ANIMATION:
                self.last_update = now
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0

        if self.direction == "right" and self.walking == True:
            self.image = self.right_images[self.index]
        elif self.direction == "left" and self.walking == True:
            self.image = self.left_images[self.index]
        elif self.direction == "right" and self.walking == False:
            self.image = self.right_images[0]
            self.index = 0
        elif self.direction == "left" and self.walking == False:
            self.image = self.left_images[0]
            self.index = 0

        if self.vel == 0:
            self.index = 0
            self.image = self.images[self.index]

        #Apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION

        #Equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.real_pos += self.vel.x + 0.5 * self.acc.x

        self.rect.midbottom = self.pos

    def shoot(self, main):

        if main.player.direction == "right":
            bullet = Bullet(main.player.pos.x + 65, main.player.pos.y - 73, main)
        elif main.player.direction == "left":
            bullet = Bullet(main.player.pos.x - 65, main.player.pos.y - 73, main)
        main.all_sprites.add(bullet)
        main.bullets.add(bullet)
        #pg.mixer.music.play()

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, main):
        self.main = main
        pg.sprite.Sprite.__init__(self)
        bullet_img = pg.image.load(path.join(img_dir, "laserRed.png")).convert()
        bullet_img_right = pg.transform.rotate(bullet_img, 270)
        bullet_img_left = pg.transform.rotate(bullet_img, 90)

        if main.player.direction == "right":
            self.image = bullet_img_right
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
            self.speedx = 10
        elif main.player.direction == "left":
            self.image = bullet_img_left
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
            self.speedx = -10

    def update(self):
        self.rect.x += self.speedx
        #Kill if it moves off the top of the screen
        if self.main.frame_1 == True:
            if self.rect.centerx > 670 or self.rect.centerx < 130:
                self.kill()
        elif self.main.frame_2 == True:
            if self.rect.centerx > 800 or self.rect.centerx < -50:
                self.kill()
        elif self.main.frame_3 == True:
            if self.rect.centerx > 720 or self.rect.centerx < 80:
                self.kill()

class Enemy(pg.sprite.Sprite):
    def __init__(self, main):
        self.main = main
        self.images = []
        self.attack_images = []
        self.left_images = []
        self.right_attack_images = []
        self.left_attack_images = []
        self.index = 0
        self.health = 100
        self.attacking = False
        pg.sprite.Sprite.__init__(self)

        self.images.append(pg.image.load(path.join(img_dir, "Protagonist_frame1_v2.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "Protagonist_frame2_v2.png")).convert())
        self.images.append(pg.image.load(path.join(img_dir, "Protagonist_frame3_v2.png")).convert())

        self.attack_images.append(pg.image.load(path.join(img_dir, "ProtagonistMeleeAnimation_Frame1and7.png")).convert())
        self.attack_images.append(
            pg.image.load(path.join(img_dir, "Protagonist_meleeanimation_frame2.png")).convert())
        self.attack_images.append(
            pg.image.load(path.join(img_dir, "ProtagonistMeleeAnimation_frame3.png")).convert())
        self.attack_images.append(
            pg.image.load(path.join(img_dir, "Protagonist_meleeanimation_Frame4.png")).convert())
        self.attack_images.append(
            pg.image.load(path.join(img_dir, "Protagonist_meleeanimation_Frame5.png")).convert())
        self.attack_images.append(
            pg.image.load(path.join(img_dir, "Protagonist_meleeanimation_Frame6.png")).convert())

        self.last_update = pg.time.get_ticks()

        for img in self.images:
            img.set_colorkey(WHITE)
            img = pg.transform.scale(img, (72, 120))
            new_image = pg.transform.flip(img, True, False)
            self.left_images.append(new_image)

        for img in self.attack_images:
            img.set_colorkey(WHITE)
            img = pg.transform.scale(img, (72, 120))
            self.right_attack_images.append(img)
            new_image = pg.transform.flip(img, True, False)
            self.left_attack_images.append(new_image)

        self.image = self.left_images[self.index]

        self.rect = self.image.get_rect()

        self.pos = vec(1780, HEIGHT - 9)

    def update(self):
        now = pg.time.get_ticks()

        if now - self.last_update > ENEMY_ANIMATION and self.main.player.pos.x <= self.pos.x and self.attacking == False:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.left_images[self.index]
        elif now - self.last_update > ENEMY_ANIMATION and self.main.player.pos.x > self.pos.x and self.attacking == False:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        elif now - self.last_update > ENEMY_ANIMATION and self.main.player.pos.x  <= self.pos.x and self.attacking == True:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.attack_images):
                self.index = 0
            self.image = self.left_attack_images[self.index]
        elif now - self.last_update > ENEMY_ANIMATION and self.main.player.pos.x > self.pos.x and self.attacking == True:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.attack_images):
                self.index = 0
            self.image = self.right_attack_images[self.index]

        if self.main.player.pos.x <= self.pos.x:
            self.pos.x += -2.5
        elif self.main.player.pos.x > self.pos.x:
            self.pos.x += 2.5

        self.rect.midbottom = self.pos

class OldMan(pg.sprite.Sprite):
    def __init__(self, main):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0

        self.images.append(main.spritesheet.get_image(636, 28, 60, 120))
        self.images.append(main.spritesheet.get_image(706, 28, 60, 120))

        self.image = self.images[self.index]
        self.last_update = pg.time.get_ticks()

        for img in self.images:
            img.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.pos = vec(425, HEIGHT -180)

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > CHAR_ANIMATION:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

        self.rect.midbottom = self.pos

class Clerk(pg.sprite.Sprite):
    def __init__(self, main):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.order = [0, 0, 1, 0, 2]

        self.images.append(main.spritesheet.get_image(27, 27, 60, 70))
        self.images.append(main.spritesheet.get_image(95, 26, 60, 70))
        self.images.append(main.spritesheet.get_image(163, 27, 60, 70))

        self.image = self.images[0]
        self.last_update = pg.time.get_ticks()

        for img in self.images:
            img.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.pos = vec(650, HEIGHT - 194)

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > CHAR_ANIMATION:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.order):
                self.index = 0
            self.image = self.images[self.order[self.index]]

        self.rect.midbottom = self.pos

class Sketchy(pg.sprite.Sprite):
    def __init__(self, main):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.order = [0, 1, 0, 2, 3, 4, 3]

        self.images.append(main.spritesheet.get_image(251, 28, 60, 120))
        self.images.append(main.spritesheet.get_image(326, 28, 60, 120))
        self.images.append(main.spritesheet.get_image(396, 28, 60, 120))
        self.images.append(main.spritesheet.get_image(464, 28, 60, 120))
        self.images.append(main.spritesheet.get_image(541, 28, 60, 120))

        self.image = self.images[self.order[self.index]]
        self.last_update = pg.time.get_ticks()

        for img in self.images:
            img.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.pos = vec(2035, HEIGHT - 9)

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > CHAR_ANIMATION:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.order):
                self.index = 0
            self.image = self.images[self.order[self.index]]

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

class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        #grab an image out of a larger spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0,0), (x, y, width, height))
        return image
