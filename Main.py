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
        self.font_name = pg.font.match_font(FONT_NAME)
        self.frame_1 = False
        self.frame_3 = False
        pg.mixer.music.load(song_frame_2)
        pg.mixer.music.play(-1)

    def new(self):
        #Start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.door1 = pg.sprite.Group()
        self.door2 = pg.sprite.Group()
        self.old_man_g = pg.sprite.Group()
        self.player = Player(self)
        self.frame_2_background = Frame_2_Background()
        self.all_sprites.add(self.player)
        self.p1 = Platform(0, HEIGHT - 3, 2450, 3)
        self.door_1 = Platform(139, 453, 50, 115)
        self.door_2 = Platform(628, 453, 50, 115)
        self.all_sprites.add(self.p1)
        self.platforms.add(self.p1)
        self.all_sprites.add(self.door_1)
        self.door1.add(self.door_1)
        self.all_sprites.add(self.door_2)
        self.door2.add(self.door_2)
        """self.old_man = OldMan()
        self.all_sprites.add(self.old_man)
        self.old_man_g.add(self.old_man)"""
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

        door1_hit = pg.sprite.spritecollide(self.player, self.door1, False)
        if door1_hit:
            self.enter1 = 1
            keyss = pg.key.get_pressed()
            if keyss[pg.K_e]:
                self.frame_1 = True
                pg.mixer.music.load(song_frame_1)
                pg.mixer.music.play(-1)

        else:
            self.enter1 = 0

        door2_hit = pg.sprite.spritecollide(self.player, self.door2, False)
        if door2_hit:
            self.enter2 = 1
            keyss = pg.key.get_pressed()
            if keyss[pg.K_e]:
                self.frame_3 = True
        else:
            self.enter2 = 0


        if self.frame_1 == False and self.frame_3 == False:
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
            '''elif event.type == pg.MOUSEMOTION:
                print("Mouse at (%d, %d)" % event.pos)'''

    def draw(self):
        #Game loop draw
        if self.frame_1 == False and self.frame_3 == False:
            self.screen.blit(self.frame_2_background.background, (self.frame_2_background.stage_pos_x, 0))
            if self.enter1 == 1:
                self.draw_text("Press E to Enter", 20, YELLOW, 159, 410)
            if self.enter2 == 1:
                self.draw_text("Press E to Enter", 20, YELLOW, 648, 410)
        elif self.frame_1 == True:
            self.screen.fill(BLACK)
            #self.screen.blit(self.frame_2_background.background2, (0, 0))
            self.draw_text("WELCOME FRIEND", 50, LIGHT_BLUE, 450, 50)
            self.draw_text("WELCOME FRIEND", 50, RED, 500, 100)
            self.draw_text("WELCOME FRIEND", 50, RED, 500, 150)
            self.draw_text("WELCOME FRIEND", 50, RED, 500, 200)
            self.draw_text("WELCOME FRIEND", 50, YELLOW, 400, 250)
            self.draw_text("WELCOME FRIEND", 50, GREEN, 500, 300)
            self.draw_text("212-PIMPSQUAD", 100, WHITE, 400, 400)
        elif self.frame_3 == True:
            self.screen.fill(GREEN)
            self.draw_text("BUY RAMEN", 50, LIGHT_BLUE, 450, 50)
            self.draw_text("BUY RAMEN", 50, LIGHT_BLUE, 500, 100)
            self.draw_text("BUY RAMEN", 50, LIGHT_BLUE, 500, 150)
            self.draw_text("BUY RAMEN", 50, LIGHT_BLUE, 500, 200)
            self.draw_text("BUY RAMEN", 50, LIGHT_BLUE, 400, 250)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        #Game start screen
        self.screen.fill(LIGHT_BLUE)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Prototype", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Play any key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        #Game over screen
        if not self.running:
            return
        self.screen.fill(LIGHT_BLUE)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        #self.draw_text("Score: " + str(self.score), 22, white, width / 2, height / 2)
        self.draw_text("Play any key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(5)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()