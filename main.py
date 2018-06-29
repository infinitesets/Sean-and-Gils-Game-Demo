import pygame as pg
import random
from Settings import *
from Sprites import *
from Frame1 import *
from Frame2 import *
from Frame3 import *

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

        #pg.mixer.music.load(shoot_sound)
        #pg.mixer.music.play()

    def load_data(self):
        pass

    def new(self):
        #Start a new game
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.bullets = pg.sprite.Group()
        self.frame_one = Frame_1(g)
        self.frame_two = Frame_2(g)
        self.frame_three = Frame_3(g)
        self.frame_1 = True
        self.frame_2 = False
        self.frame_3 = False
        self.win = False
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
        #pg.mouse.get_pos()
        self.all_sprites.update()
        if self.frame_1 == True:
            self.frame_one.update(g)
        elif self.frame_2 == True:
            self.frame_two.update(g)
        elif self.frame_3 == True:
            self.frame_three.update(g)
        if self.player.health <= 0:
            self.playing = False


    def events(self):
        #Game loop events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()
                if event.key == pg.K_SPACE:
                    self.player.shoot(self)
                if event.key == pg.K_p:
                    self.pause()
                if event.key == pg.K_ESCAPE:
                    self.pause()
        '''elif event.type == pg.MOUSEMOTION:
            print("Mouse at (%d, %d)" % event.pos)'''

    def draw(self):
        #Game loop draw
        if self.frame_1 == True:
            self.screen.blit(self.frame_one.background, (0, 0))
            self.frame_one.all_sprites.draw(self.screen)
            self.all_sprites.draw(self.screen)
            self.draw_interface()
            if self.frame_two.chatted == True and self.frame_one.touch == True:
                self.draw_text("[E]", 20, WHITE, 183, HEIGHT - 330)
            if self.frame_one.win == True:
                self.screen.blit(self.frame_one.background, (0, 0))
                self.frame_one.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.dialogue2("MYSTERIOUS VOICE:", "What's the password?", "", "Press [E] to continue...", 315, 170)
                self.screen.blit(self.frame_one.background, (0, 0))
                self.frame_one.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.choice3("[K]itten Mittens", "[F]lower Shoppe", "[R]obyn's Nest", self.frame_one.cat,
                             self.frame_one.plant, self.frame_one.bird, 315, 170)
                if self.frame_one.kitten == True:
                    self.screen.blit(self.frame_one.background, (0, 0))
                    self.frame_one.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.dialogue2("MYSTERIOUS VOICE:", "WRONG", "You lose...", "Press [E] to continue...", 315, 170)
                    self.playing = False
                elif self.frame_one.flower == True:
                    self.screen.blit(self.frame_one.background, (0, 0))
                    self.frame_one.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.dialogue2("MYSTERIOUS VOICE:", "Nice...", "You won kid...", "Press [E] to continue...", 315, 170)
                    self.win = True
                    self.playing = False
                elif self.frame_one.robin == True:
                    self.screen.blit(self.frame_one.background, (0, 0))
                    self.frame_one.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.dialogue2("MYSTERIOUS VOICE:", "WRONG", "You lose...", "Press [E] to continue...", 315, 170)
                    self.playing = False

            if self.frame_one.interact == True:
                self.draw_text("[E]", 20, WHITE, 420, HEIGHT - 330)
            if self.frame_one.chat == True and self.frame_one.talked == False:
                self.dialogue("OLD MAN:", "Hey boy!", "", "Press [E] to continue...", 250, 200)
                self.screen.blit(self.frame_one.background, (0, 0))
                self.frame_one.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.dialogue("OLD MAN:", "Go run to that convenience store", "and buy me a pack of cigs, will ya?", "Press [E] to continue...",
                              250, 200)
                self.screen.blit(self.frame_one.background, (0, 0))
                self.frame_one.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.choice("[Y]es", "[N]o", self.frame_one.yeah, self.frame_one.nah, 250, 200)
                if self.frame_one.yes == True:
                    self.screen.blit(self.frame_one.background, (0, 0))
                    self.frame_one.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.frame_one.talked = True
                    self.player.money += 5
                    self.dialogue("OLD MAN:", "You know the ones I like.", "You received $5.",
                                  "Press [E] to continue...",
                                  250, 200)
                elif self.frame_one.no == True:
                    self.screen.blit(self.frame_one.background, (0, 0))
                    self.frame_one.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.dialogue("OLD MAN:", "Leave an old man to die without his", "smokes.",
                                  "Press [E] to continue...",
                                  250, 200)
            elif self.frame_one.chat == True and self.frame_one.talked == True and self.frame_one.yes == True and \
                    self.frame_three.cigarette_b == False and self.frame_three.beer_b == False:
                self.screen.blit(self.frame_one.background, (0, 0))
                self.frame_one.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.dialogue("OLD MAN:", "You get me the cigs?", "", "Press [E] to continue...", 250, 200)
            elif self.frame_one.chat == True and self.frame_one.talked == True and self.frame_one.yes == True and \
                    self.frame_three.cigarette_b == True and self.frame_three.beer_b == False:
                self.screen.blit(self.frame_one.background, (0, 0))
                self.frame_one.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.dialogue("OLD MAN:", "You are a saint and a scholar.", "Take this kid. Have a wild night.", "Press [E] to continue...", 250, 200)
                self.win = True
                self.playing = False
            elif self.frame_one.chat == True and self.frame_one.talked == True and self.frame_one.yes == True and \
                 self.frame_three.cigarette_b == False and self.frame_three.beer_b == True:
                self.screen.blit(self.frame_one.background, (0, 0))
                self.frame_one.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.dialogue("OLD MAN:", "HaHa! You knew I wanted a cold one.", "But where are my cigs kid.",
                              "Press [E] to continue...", 250, 200)
                self.win = True
                self.playing = False
            elif self.frame_one.chat == True and self.frame_one.talked == True and self.frame_one.yes == True and \
                 self.frame_three.cigarette_b == True and self.frame_three.beer_b == True:
                self.screen.blit(self.frame_one.background, (0, 0))
                self.frame_one.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.dialogue("OLD MAN:", "Is it my birthday?", "Thanks kid.",
                              "Press [E] to continue...", 250, 200)
                self.win = True
                self.playing = False

        elif self.frame_2 == True:
            self.screen.blit(self.frame_two.background, (self.frame_two.stage_pos_x, 0))
            if self.frame_two.enter1 == 1:
                self.draw_text("[E]", 20, WHITE, 163, 410)
            if self.frame_two.enter2 == 1:
                self.draw_text("[E]", 20, WHITE, 648, 410)
            self.frame_two.all_sprites.draw(self.screen)
            self.all_sprites.draw(self.screen)
            if self.frame_two.interact == True:
                self.draw_text("[E]", 20, WHITE, 488, HEIGHT - 160)
            if self.frame_two.talked == True and self.frame_two.chat == True:
                self.screen.blit(self.frame_two.background, (self.frame_two.stage_pos_x, 0))
                self.frame_two.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.dialogue("SKETCHY MAN:", "Be careful out there kid...", "",
                              "Press [E] to continue...", 340, HEIGHT - 260)
                self.screen.blit(self.frame_two.background, (self.frame_two.stage_pos_x, 0))
                self.frame_two.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.dialogue("SKETCHY MAN:", "Remember F L O W E R S H O P P E", "",
                              "Press [E] to continue...", 340, HEIGHT - 260)
                self.frame_two.chat = False

            elif self.frame_two.chat == True and self.frame_two.talked == False:
                self.frame_two.chat = False
                self.draw_interface()
                self.dialogue("SKETCHY MAN:", "Hey, you look like a guy who likes", "to know.", "Press [E] to continue...", 340, HEIGHT - 260)
                self.screen.blit(self.frame_two.background, (self.frame_two.stage_pos_x, 0))
                self.frame_two.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.dialogue("SKETCHY MAN:", "I got some info for ya', that is...", "if you pay me 10 bucks.",
                              "Press [E] to continue...", 340, HEIGHT - 260)
                self.screen.blit(self.frame_two.background, (self.frame_two.stage_pos_x, 0))
                self.frame_two.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.choice("[Y]es", "[N]o", self.frame_two.yeah, self.frame_two.nah, 340, HEIGHT - 260)
                if self.frame_two.yes == True and self.player.money >= 10:
                    self.frame_two.chatted = True
                    self.frame_two.talked = True
                    self.screen.blit(self.frame_two.background, (self.frame_two.stage_pos_x, 0))
                    self.frame_two.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.player.money -= 10
                    self.dialogue("SKETCHY MAN:", "Hehe, it'll be worth it.", "Trust me.",
                                  "Press [E] to continue...", 340, HEIGHT - 260)
                    self.screen.blit(self.frame_two.background, (self.frame_two.stage_pos_x, 0))
                    self.frame_two.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.dialogue("SKETCHY MAN:", "Last door on the left,", "password is FLOWERSHOPPE.",
                                  "Press [E] to continue...", 340, HEIGHT - 260)
                    self.frame_two.yes = False
                elif self.frame_two.yes == True and self.player.money < 10:
                    self.screen.blit(self.frame_two.background, (self.frame_two.stage_pos_x, 0))
                    self.frame_two.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.frame_two.yes = False
                    self.dialogue("SKETCHY MAN:", "What are you trying to pull?", "Come back when you have the dough.",
                                  "Press [E] to continue...", 340, HEIGHT - 260)
                elif self.frame_two.no == True:
                    self.screen.blit(self.frame_two.background, (self.frame_two.stage_pos_x, 0))
                    self.frame_two.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.dialogue("SKETCHY MAN:", "Get outta here...", "",
                                  "Press [E] to continue...", 340, HEIGHT - 260)


        elif self.frame_3 == True:
            self.screen.blit(self.frame_three.background, (0, 0))
            self.frame_three.all_sprites.draw(self.screen)
            self.all_sprites.draw(self.screen)
            if self.frame_three.interact == True:
                self.draw_text("[E]", 20, WHITE, self.frame_three.clerk.pos.x - 5, self.frame_three.clerk.pos.y - 100)
            if self.frame_three.chat == True:
                self.draw_interface()
                self.dialogue("CLERK:", "What can I get for you?", "", "Press [E] to continue...", 500, 200)
                self.screen.blit(self.frame_three.background, (0, 0))
                self.frame_three.all_sprites.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_interface()
                self.choice2("[C]igarettes - $5", "[B]eer - $5", "[N]evermind", self.frame_three.cigarettes, self.frame_three.beers, self.frame_three.nevermind, 500, 200)
                if self.frame_three.cigarette == True and self.player.money >= 5:
                    self.screen.blit(self.frame_three.background, (0, 0))
                    self.frame_three.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    #self.frame_one.talked = True
                    self.player.money -= 5
                    self.frame_three.cigarette_b = True
                    self.frame_three.cigarette = False
                    self.dialogue("CLERK:", "Enjoy one of life's simple pleasures.", "You received Cigarettes.",
                                  "Press [E] to continue...",
                                  500, 200)
                elif self.frame_three.cigarette == True and self.player.money < 5:
                    self.screen.blit(self.frame_three.background, (0, 0))
                    self.frame_three.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.frame_three.cigarette = False
                    # self.frame_one.talked = True
                    self.dialogue("CLERK:", "Sorry. You don't have enough money", "to purchase cigarettes.",
                                  "Press [E] to continue...",
                                  500, 200)
                elif self.frame_three.beer == True and self.player.money >= 5:
                    self.screen.blit(self.frame_three.background, (0, 0))
                    self.frame_three.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.player.money -= 5
                    self.frame_three.beer_b = True
                    self.frame_three.beer = False
                    self.dialogue("CLERK:", "Cheers.", "You received beer.",
                                  "Press [E] to continue...",
                                  500, 200)
                elif self.frame_three.beer == True and self.player.money < 5:
                    self.screen.blit(self.frame_three.background, (0, 0))
                    self.frame_three.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.frame_three.beer = False
                    # self.frame_one.talked = True
                    self.dialogue("CLERK:", "Sorry. You don't have enough money", "to purchase beer.",
                                  "Press [E] to continue...",
                                  500, 200)
                elif self.frame_three.nothing == True:
                    self.screen.blit(self.frame_three.background, (0, 0))
                    self.frame_three.all_sprites.draw(self.screen)
                    self.all_sprites.draw(self.screen)
                    self.draw_interface()
                    self.dialogue("CLERK:", "Ok.", "",
                                  "Press [E] to continue...",
                                  500, 200)

        self.draw_interface()
        pg.display.flip()

    def show_start_screen(self):
        #Game start screen
        self.screen.fill(LIGHT_BLUE)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Prototype", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("Double Cross Creek Studios presents", 36, WHITE, WIDTH / 2, HEIGHT * 1 / 8)
        pg.display.flip()
        self.wait_for_key()

    def draw_interface(self):
        if self.player.health >= 50:
            self.draw_text_one("HEALTH", 20, WHITE, 7, 0)
            pg.draw.rect(self.screen, GREEN, (7, 25, self.player.health, 15))
        elif self.player.health >= 20:
            self.draw_text_one("HEALTH", 20, YELLOW, 7, 0)
            pg.draw.rect(self.screen, YELLOW, (7, 25, self.player.health, 15))
        else:
            self.draw_text_one("HEALTH", 20, RED, 7, 0)
            pg.draw.rect(self.screen, RED, (7, 25, self.player.health, 15))
        self.draw_text_one("$" + str(self.player.money), 20, WHITE, 760, 0)

    def show_go_screen_lose(self):
        #Game over screen
        if not self.running:
            return
        self.screen.fill(LIGHT_BLUE)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 7)
        self.draw_text("You Lost", 38, WHITE, WIDTH/2, HEIGHT / 4)
        self.draw_text("Double Cross Creek Studios", 36, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Thanks you for playing", 22, WHITE, WIDTH/2, HEIGHT / 2 + 50)
        #self.draw_text("Score: " + str(self.score), 22, white, width / 2, height / 2)
        self.draw_text("Press any key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen_win(self):
        #Game over screen
        if not self.running:
            return
        self.screen.fill(LIGHT_BLUE)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 7)
        self.draw_text("You Won!", 38, WHITE, WIDTH/2, HEIGHT / 4)
        self.draw_text("Double Cross Creek Studios", 36, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Thanks you for playing", 22, WHITE, WIDTH/2, HEIGHT / 2 + 50)
        #self.draw_text("Score: " + str(self.score), 22, white, width / 2, height / 2)
        self.draw_text("Press any key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def pause(self):
        paused = True

        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        paused = False
                    elif event.key == pg.K_q:
                        pg.quit()
                        quit()
            self.screen.fill(BLACK)
            self.draw_text("Paused", 75, WHITE, 400, 200)
            self.draw_text("Press C to continue or Q to quit.", 25, WHITE, 400, 400)
            self.draw_interface()
            pg.display.update()
            self.clock.tick(5)

    def draw_text_one(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def dialogue(self, character, first, second, third, x, y):
        paused = True

        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_e:
                        paused = False
                        self.frame_one.chat = False
            box = pg.image.load(path.join(img_dir, "Dialougebox_v1.png")).convert()
            box.set_colorkey(BLACK)
            boxx = box.get_rect()
            boxx.midtop = (x, y)
            self.draw_text_one(character, 13, WHITE, x - 120, y + 20)
            self.draw_text_one(first, 13, WHITE, x - 120, y + 35)
            self.draw_text_one(second, 13, WHITE, x - 120, y + 50)
            self.draw_text_one(third, 13, WHITE, x - 120, y + 65)
            self.screen.blit(box, boxx)
            pg.display.update()
            self.clock.tick(5)

    def dialogue2(self, character, first, second, third, x, y):
        paused = True

        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_e:
                        paused = False
                        self.frame_one.chat = False
            box = pg.image.load(path.join(img_dir, "Dialougebox_v1.png")).convert()
            box = pg.transform.flip(box, True, False)
            box.set_colorkey(BLACK)
            boxx = box.get_rect()
            boxx.midtop = (x, y)
            self.draw_text_one(character, 13, WHITE, x - 100, y + 20)
            self.draw_text_one(first, 13, WHITE, x - 100, y + 35)
            self.draw_text_one(second, 13, WHITE, x - 100, y + 50)
            self.draw_text_one(third, 13, WHITE, x - 100, y + 65)
            self.screen.blit(box, boxx)
            pg.display.update()
            self.clock.tick(5)

    def choice(self, answer1, answer2, function1, function2, x, y):
        paused = True

        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_y:
                        paused = False
                        function1()

                    if event.key == pg.K_n:
                        paused = False
                        function2()

            box = pg.image.load(path.join(img_dir, "Dialougebox_v1.png")).convert()
            box.set_colorkey(BLACK)
            boxx = box.get_rect()
            boxx.midtop = (x, y)
            self.draw_text_one(answer1, 13, WHITE, x - 120, y + 20)
            self.draw_text_one(answer2, 13, WHITE, x - 120, y + 35)
            self.screen.blit(box, boxx)
            pg.display.update()
            self.clock.tick(5)

    def choice2(self, answer1, answer2, answer3, function1, function2, function3, x, y):
        paused = True

        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        paused = False
                        function1()

                    if event.key == pg.K_b:
                        paused = False
                        function2()

                    if event.key == pg.K_n:
                        paused = False
                        function3()

            box = pg.image.load(path.join(img_dir, "Dialougebox_v1.png")).convert()
            box.set_colorkey(BLACK)
            boxx = box.get_rect()
            boxx.midtop = (x, y)
            self.draw_text_one(answer1, 13, WHITE, x - 120, y + 20)
            self.draw_text_one(answer2, 13, WHITE, x - 120, y + 35)
            self.draw_text_one(answer3, 13, WHITE, x - 120, y + 50)
            self.screen.blit(box, boxx)
            pg.display.update()
            self.clock.tick(5)

    def choice3(self, answer1, answer2, answer3, function1, function2, function3, x, y):
        paused = True

        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_k:
                        paused = False
                        function1()

                    if event.key == pg.K_f:
                        paused = False
                        function2()

                    if event.key == pg.K_r:
                        paused = False
                        function3()

            box = pg.image.load(path.join(img_dir, "Dialougebox_v1.png")).convert()
            box = pg.transform.flip(box, True, False)
            box.set_colorkey(BLACK)
            boxx = box.get_rect()
            boxx.midtop = (x, y)
            self.draw_text_one(answer1, 13, WHITE, x - 100, y + 20)
            self.draw_text_one(answer2, 13, WHITE, x - 100, y + 35)
            self.draw_text_one(answer3, 13, WHITE, x - 100, y + 50)
            self.screen.blit(box, boxx)
            pg.display.update()
            self.clock.tick(5)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(5)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    waiting = False

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    if g.win == False:
        g.show_go_screen_lose()
    elif g.win == True:
        g.show_go_screen_win()

pg.quit()