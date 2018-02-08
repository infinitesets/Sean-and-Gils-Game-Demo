import pygame as pg
import random
from Settings import *
from Sprites import *

class Game:
    def __init__(self):
        #Initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        #Start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.frame_2_background = Frame_2_Background()
        self.all_sprites.add(self.player)
        self.p1 = Platform(0, HEIGHT - 18, 2400, 18)
        #self.door1 = Platform()
        self.all_sprites.add(self.p1)
        self.platforms.add(self.p1)
        self.run()

    def run(self):
        #Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #Game loop update
        pg.mouse.get_pos()
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.pos.y = hits[0].rect.top + 1
            self.player.vel.y = 0

        if self.player.real_pos < self.frame_2_background.start_scroll_pos_x:
            self.player.real_pos = self.player.pos.x
        elif self.player.real_pos > self.frame_2_background.stage_width - self.frame_2_background.start_scroll_pos_x:
            self.player.pos.x = self.player.real_pos - self.frame_2_background.stage_width + WIDTH
        else:
            self.player.pos.x = self.frame_2_background.start_scroll_pos_x
            self.frame_2_background.stage_pos_x += (-self.player.vel.x + 0.5 * self.player.acc.x)

    def events(self):
        #Game loop events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        #Game loop draw
        self.screen.blit(self.frame_2_background.background, (self.frame_2_background.stage_pos_x, 0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        #Game start screen
        pass

    def show_go_screen(self):
        #Game over screen
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()