import pygame
from sys import exit
from random import randint, choice
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet_image = pygame.image.load('graphics/sonic.png').convert_alpha()
        sprite_sheet_image = pygame.transform.flip(sprite_sheet_image, True, False)

        sonic_run1 = pygame.Surface((70, 75), pygame.SRCALPHA, 32).convert_alpha()
        sonic_run1.blit(sprite_sheet_image,(0, 0), (200, 270, 70, 75))
        
        sonic_run2 = pygame.Surface((70, 75), pygame.SRCALPHA, 32).convert_alpha()
        sonic_run2.blit(sprite_sheet_image,(0, 0), (470, 270, 70, 75))

        sonic_run3 = pygame.Surface((70, 75), pygame.SRCALPHA, 32).convert_alpha()
        sonic_run3.blit(sprite_sheet_image,(0, 0), (550, 270, 70, 75))
        
        self.player_run = [sonic_run1, sonic_run2, sonic_run3, sonic_run2] # player's animation cycles
        self.player_index = 0

        self.player_jump = pygame.Surface((60, 65), pygame.SRCALPHA, 32).convert_alpha()
        self.player_jump.blit(sprite_sheet_image,(0, 0), (40, 550, 60, 65))

        self.player_slide = pygame.Surface((75, 50), pygame.SRCALPHA, 32).convert_alpha()
        self.player_slide.blit(sprite_sheet_image,(0, 0), (375, 100, 75, 50))

        self.image = self.player_run[self.player_index]
        self.rect = self.image.get_rect(midbottom = (120, 300))

        self.gravity = 0

        self.slide = False
        self.slide_duration = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.bottom >= 300:
            self.gravity = -19
            self.jump_sound.play()
        
        elif keys[pygame.K_DOWN] and self.rect.bottom >= 300:
            self.slide = True
       
    def reset_position(self):
        if game_active == False:
            self.jump_sound.stop()
            self.rect.bottom = 300

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity # move player up
        if self.rect.bottom >= 300: # keeps player from falling under the ground
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump

        elif self.slide:
            i = 0
            self.rect.bottom = 320
            self.image = self.player_slide
            self.slide = False
        
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_run):
                self.player_index = 0
            self.image = self.player_run[int(self.player_index)]

    def update(self):
        self.reset_position()
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Companion(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet_image = pygame.image.load('graphics/tails.png').convert_alpha()
        sprite_sheet_image = pygame.transform.flip(sprite_sheet_image, True, False)

        tails_fly1 = pygame.Surface((36, 40), pygame.SRCALPHA, 32).convert_alpha()
        tails_fly1.blit(sprite_sheet_image,(0, 0), (359, 750, 36, 40))
        tails_fly1 = pygame.transform.scale(tails_fly1, (65, 70))

        tails_fly2 = pygame.Surface((36, 40), pygame.SRCALPHA, 32).convert_alpha()
        tails_fly2.blit(sprite_sheet_image,(0, 0), (315, 750, 36, 40))
        tails_fly2 = pygame.transform.scale(tails_fly2, (65, 70))

        tails_fly3 = pygame.Surface((36, 40), pygame.SRCALPHA, 32).convert_alpha()
        tails_fly3.blit(sprite_sheet_image,(0, 0), (279, 750, 36, 40))
        tails_fly3 = pygame.transform.scale(tails_fly3, (65, 70))

        self.companion_fly = [tails_fly1, tails_fly2, tails_fly3]
        self.companion_index = 0

        self.image = self.companion_fly[self.companion_index]
        self.rect = self.image.get_rect(midbottom = (35, 175))
    
    def animation(self):   
        self.companion_index += 0.1
        if self.companion_index >= len(self.companion_fly):
            self.companion_index = 0
        self.image = self.companion_fly[int(self.companion_index)]

    def update(self):
        self.animation()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet_image = pygame.image.load('graphics/eggman.png').convert_alpha()

        eggman1 = pygame.Surface((50, 48), pygame.SRCALPHA, 32).convert_alpha()
        eggman1.blit(sprite_sheet_image,(0, 0), (60, 46, 50, 48))
        eggman1 = pygame.transform.scale(eggman1, (105, 100))

        eggman2 = pygame.Surface((50, 48), pygame.SRCALPHA, 32).convert_alpha()
        eggman2.blit(sprite_sheet_image,(0, 0), (288, 46, 50, 48))
        eggman2 = pygame.transform.scale(eggman2, (105, 100))

        eggman3 = pygame.Surface((50, 48), pygame.SRCALPHA, 32).convert_alpha()
        eggman3.blit(sprite_sheet_image,(0, 0), (392, 46, 50, 48))
        eggman3 = pygame.transform.scale(eggman3, (105, 100))

        self.companion_fly = [eggman1, eggman2, eggman3, eggman1, eggman1, eggman1]
        self.companion_index = 0

        self.image = self.companion_fly[self.companion_index]
        self.rect = self.image.get_rect(midbottom = (740, 160))
    
    def animation(self):   
        self.companion_index += 0.1
        if self.companion_index >= len(self.companion_fly):
            self.companion_index = 0
        self.image = self.companion_fly[int(self.companion_index)]

    def update(self):
        self.animation()
       
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        sprite_sheet_image = pygame.image.load('graphics/badniks.png').convert_alpha()

        if type == 'spike_sky':
            spike1 = pygame.image.load('graphics/spike.png').convert_alpha()
            spike1 = pygame.transform.scale(spike1, (60, 60))
            spike2 = spike1

            self.frames = [spike1, spike2]
            y_pos = 245
        
        elif type == 'spike_ground':
            spike1 = pygame.image.load('graphics/spike.png').convert_alpha()
            spike1 = pygame.transform.scale(spike1, (60, 60))
            spike2 = spike1

            self.frames = [spike1, spike2]
            y_pos = 290

        elif type == 'bat':
            sprite_sheet_image = pygame.transform.flip(sprite_sheet_image, True, False)
            bat1 = pygame.Surface((40, 34), pygame.SRCALPHA, 32).convert_alpha()
            bat1.blit(sprite_sheet_image,(0, 0), (100, 500, 40, 34))
            bat1 = pygame.transform.scale(bat1, (75, 65))
            
            bat2 = pygame.Surface((37, 34), pygame.SRCALPHA, 32).convert_alpha()
            bat2.blit(sprite_sheet_image,(0, 0), (139, 500, 37, 34))
            bat2 = pygame.transform.scale(bat2, (75, 65))

            self.frames = [bat1, bat2]
            y_pos = 245

        elif type == 'bee':
            bee1 = pygame.Surface((45, 27), pygame.SRCALPHA, 32).convert_alpha()
            bee1.blit(sprite_sheet_image,(0, 0), (12, 112, 45, 27))
            bee1 = pygame.transform.scale(bee1, (80, 40))
            
            bee2 = pygame.Surface((45, 27), pygame.SRCALPHA, 32).convert_alpha()
            bee2.blit(sprite_sheet_image,(0, 0), (57, 112, 45, 27))
            bee2 = pygame.transform.scale(bee2, (80, 40))

            self.frames = [bee1, bee2]
            y_pos = 245

        elif type == 'bug':
            bug1 = pygame.Surface((41, 32), pygame.SRCALPHA, 32).convert_alpha()
            bug1.blit(sprite_sheet_image,(0, 0), (56, 72, 41, 32))
            bug1 = pygame.transform.scale(bug1, (75, 65))
            
            bug2 = pygame.Surface((41, 32), pygame.SRCALPHA, 32).convert_alpha()
            bug2.blit(sprite_sheet_image,(0, 0), (12, 72, 41, 32))
            bug2 = pygame.transform.scale(bug2, (75, 65))

            self.frames = [bug1, bug2]
            y_pos = 300

        elif type == 'crab':
            crab1 = pygame.Surface((45, 32), pygame.SRCALPHA, 32).convert_alpha()
            crab1.blit(sprite_sheet_image,(0, 0), (12, 376, 45, 32))
            crab1 = pygame.transform.scale(crab1, (85, 60))
            
            crab2 = pygame.Surface((45, 32), pygame.SRCALPHA, 32).convert_alpha()
            crab2.blit(sprite_sheet_image,(0, 0), (57, 376, 45, 32))
            crab2 = pygame.transform.scale(crab2, (85, 60))

            self.frames = [crab1, crab2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index > len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, 'White')
    score_rect = score_surface.get_rect(center = (400, 30))
    screen.blit(score_surface, score_rect)
    return current_time
    
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

# Setups
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Sonic Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/font.ttf', 50)
game_active = False
start_time = 0
score = 0
playlist = ['audio/song1.mp3', 'audio/song2.mp3', 'audio/song3.mp3', 'audio/song4.mp3']
pygame.mixer.music.load(choice(playlist))
pygame.mixer.music.play(loops=-1)

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

companion = pygame.sprite.GroupSingle()
companion.add(Companion())

boss = pygame.sprite.GroupSingle()
boss.add(Boss())

obstacle_group = pygame.sprite.Group()

# Backgrounds
sky_image = pygame.image.load('graphics/sky.jpg').convert_alpha()
ground_image = pygame.image.load('graphics/ground.png').convert_alpha()

sky_surface = pygame.transform.scale(sky_image, (800, 295))

ground_surface = pygame.Surface((200, 50), pygame.SRCALPHA, 32).convert_alpha()
ground_surface.blit(ground_image,(0, 0), (20, 97, 800, 50))
ground_surface = pygame.transform.scale(ground_surface, (800, 150))

# Variables for scrolling ground
scroll = 0
tiles = math.ceil(800 / ground_surface.get_width()) + 1

# Intro screen
menu = pygame.image.load('graphics/menu.jpg').convert_alpha()
menu = pygame.transform.scale(menu, (800, 400))

game_message = test_font.render('Press SPACE to Start', False, 'White')
game_message_rect = game_message.get_rect(center = (550, 23))

# Timer
obstacle_timer = pygame.USEREVENT + 1 # + 1 is needed, don't ask
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Randomly spawn obstacles
        if game_active:
            if event.type == obstacle_timer and game_active:
                obstacle_group.add(Obstacle(choice(['spike_sky', 'spike_ground', 'bug', 'crab', 'bee', 'bat'])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0)) # attach test surface onto display surface
        
        # Ground scrolling
        i = 0
        while(i < tiles):
            screen.blit(ground_surface, (ground_surface.get_width()*i + scroll, 295))
            i += 1
        scroll -= 8
        if abs(scroll) > ground_surface.get_width():
            scroll = 0

        score = display_score()

        player.draw(screen) # draw the sprite from class
        player.update() # update the sprite from class

        companion.draw(screen)
        companion.update()
        companion.update()

        boss.draw(screen)
        boss.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()

        #Collision
        game_active = collision_sprite()
    
    # Game over screen
    else:
        player.update() # reset player's position after game over

        screen.blit(menu, (0, 0))

        score_message = test_font.render(f'Your Score: {score}', False, (255, 255, 255))
        score_message_rect = score_message.get_rect(center = (550, 23))
        
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
    
    pygame.display.update() # update everything
    clock.tick(60) # max frame rate is 60FPS
