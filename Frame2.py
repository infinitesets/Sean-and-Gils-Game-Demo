import pygame as pg
from Settings import *
from Sprites import *
from os import path

class Frame_2:
    def __init__(self, main):
        self.interact = False
        self.chat = False
        self.chatted = False
        self.yes = False
        self.no = False
        self.talked = False

        self.all_sprites = pg.sprite.Group()
        self.ground = pg.sprite.Group()
        self.door_1 = pg.sprite.Group()
        self.door_2 = pg.sprite.Group()

        self.sketch = pg.sprite.Group()
        self.s_man = Sketchy(main)
        self.sketch.add(self.s_man)
        self.all_sprites.add(self.s_man)

        self.enemies = pg.sprite.Group()
        self.enemy = Enemy(main)
        self.enemies.add(self.enemy)
        self.all_sprites.add(self.enemy)

        self.enter1 = 0
        self.enter2 = 0
        self.walls = pg.sprite.Group()
        self.wall = Platform(0, 0, 0, 600)
        self.wall2 = Platform(790, 0, 100, 600)
        self.all_sprites.add(self.wall)
        self.walls.add(self.wall)
        self.all_sprites.add(self.wall2)
        self.walls.add(self.wall2)

        self.floor = Platform(0, HEIGHT - 7, 2450, 3)
        self.door1 = Platform(139, 453, 50, 115)
        self.door2 = Platform(628, 453, 50, 115)
        self.all_sprites.add(self.floor)
        self.ground.add(self.floor)
        self.all_sprites.add(self.door1)
        self.door_1.add(self.door1)
        self.all_sprites.add(self.door2)
        self.door_2.add(self.door2)
        self.background = pg.image.load(path.join(img_dir, "Frame 2_v1.png")).convert()
        self.stage_width = 2350
        self.stage_pos_x = 0
        self.start_scroll_pos_x = WIDTH / 2

    def update(self, main):
        self.all_sprites.update()
        self.enemy.attacking = False

        hits = pg.sprite.spritecollide(main.player, self.ground, False)
        if hits:
            main.player.pos.y = hits[0].rect.top + 1
            main.player.vel.y = 0

        if main.player.real_pos <= self.start_scroll_pos_x:
            main.player.real_pos = main.player.pos.x
            self.stage_pos_x = 0
        elif main.player.real_pos > self.stage_width - self.start_scroll_pos_x:
            main.player.pos.x = main.player.real_pos - self.stage_width + WIDTH
            self.stage_pos_x = -1550
        else:
            main.player.pos.x = self.start_scroll_pos_x
            self.stage_pos_x += (-main.player.vel.x - main.player.acc.x)
            self.s_man.pos.x += (-main.player.vel.x - main.player.acc.x)
            self.enemy.pos.x += (-main.player.vel.x - main.player.acc.x)

        door1_hit = pg.sprite.spritecollide(main.player, self.door_1, False)
        if door1_hit:
            self.enter1 = 1
            keyss = pg.key.get_pressed()
            if keyss[pg.K_e]:
                main.frame_2 = False
                main.frame_1 = True
                main.player.pos = vec(620, HEIGHT - 170)
                main.player.direction = "left"
        else:
            self.enter1 = 0

        door2_hit = pg.sprite.spritecollide(main.player, self.door_2, False)
        if door2_hit:
            self.enter2 = 1
            keyss = pg.key.get_pressed()
            if keyss[pg.K_e]:
                main.frame_2 = False
                main.frame_3 = True
                main.player.pos = vec(100, HEIGHT - 101)
                main.player.direction = "right"
        else:
            self.enter2 = 0

        main.player.rect.centerx = main.player.pos.x
        for wall in pg.sprite.spritecollide(main.player, self.walls, False):
            if main.player.vel.x > 0:
                main.player.rect.right = wall.rect.left
                main.player.real_pos = 2280
            elif main.player.vel.x < 0:
                main.player.rect.left = wall.rect.right
            main.player.pos.x = main.player.rect.centerx

        hit = pg.sprite.spritecollide(main.player, self.sketch, False)
        if hit:
            self.interact = True
            keyss = pg.key.get_pressed()
            if keyss[pg.K_e]:
                self.chat = True
                if main.player.pos.x < self.s_man.pos.x:
                    self.s_man.image = self.s_man.images[0]
                else:
                    self.s_man.image = self.s_man.images[2]
                self.interact = False
        else:
            self.interact = False

        hurt = pg.sprite.spritecollide(main.player, self.enemies, False)
        if hurt:
            main.player.health -= 1
            self.enemy.attacking = True

        attack = pg.sprite.groupcollide(main.bullets, self.enemies, True, False)
        if attack:
            self.enemy.health -= 10

        if self.enemy.health <= 0:
            self.enemy.kill()
            main.player.money += 5
            self.enemy.health = 1

    def yeah(self):
        self.chat = False
        self.yes = True

    def nah(self):
        self.chat = False
        self.no = True