import pygame
import math
from animated_sprites import AnimatedSprite
import random


pygame.init()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width() * scale
        height = image.get_height() * scale
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    
    def draw(self):
        pos = pygame.mouse.get_pos()
        
        screen.blit(self.image, (self.rect.x, self.rect.y))

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
player_dimensions = pygame.image.load("./Sprites/Adventurer_2_Sprites/adventurer-idle-2-00.png")     #fait apparaître le premier sprite
player_width = player_dimensions.get_width()                                                         #prend la longueur du spirte
player_height = player_dimensions.get_height()                                                       #prend la largeur du sprite
background = pygame.image.load("./Background/NewNewForest.jpg")                                      #load le background du jeu
background_music = pygame.mixer.music.load("./Musics/monde_2.mp3")                                   #load la musique du jeu                                                                                                     
death_music = pygame.mixer.Sound("./Musics/death_music.mp3")                                         
stabbing_sound_1 = pygame.mixer.Sound("./Sounds/slash_1.mp3")                                       
stabbing_sound_2 = pygame.mixer.Sound("./Sounds/slash_2.mp3")
slime_die_sound = pygame.mixer.Sound("./Sounds/slime_die.mp3")
slime_hurt_sound = pygame.mixer.Sound("./Sounds/slime_hurt.mp3")
slime_attack_sound = pygame.mixer.Sound("./Sounds/slime_attack.mp3")
death_sound = pygame.mixer.Sound("./Sounds/death_sound.mp3")
death_background = pygame.image.load("./Background/dark_forest.png")
new_death_background = pygame.transform.scale(death_background, (1280 , 720))
background_width = background.get_width()
background_height = background.get_height()
death_button_image = pygame.image.load("./Images/game_over.png")
death_button = Button(380, 20, death_button_image, scale=0.15)
scroll = 0
player_lives = 9
tiles = math.ceil(SCREEN_WIDTH / background_width) + 1
screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Aventurier I")
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.4)
slime_pos = pygame.Vector2(SCREEN_WIDTH / 1.1, SCREEN_HEIGHT / 1.15)
player_hitbox = pygame.Rect(player_pos.x, player_pos.y, player_width, player_height)
clock = pygame.time.Clock()
death_music_played = False
death_sound_played = False
pygame.font.init()
acc_font = pygame.font.SysFont('arial',20)

walkLeft = AnimatedSprite(
    player_pos.x,
    player_pos.y,
    images = [
        "./Sprites/Adventurer_2_Sprites/adventurer-run-00.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-run-01.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-run-02.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-run-03.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-run-04.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-run-05.png"
    ],
    scale=5,
    animation_time=0.025
)

idle = AnimatedSprite(
    
    player_pos.x,
    player_pos.y,
    images = [
        "./Sprites/Adventurer_2_Sprites/adventurer-idle-2-00.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-idle-2-01.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-idle-2-02.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-idle-2-03.png"    
    ],
    scale=5  
)

attack_1 = AnimatedSprite(
    player_pos.x,
    player_pos.y,
    images = [
        "./Sprites/Adventurer_2_Sprites/adventurer-attack1-00.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack1-01.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack1-02.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack1-03.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack1-04.png"
    ],
    scale=5,
    animation_time=0.025,
    loop=False
)

attack_2 = AnimatedSprite(
    player_pos.x,
    player_pos.y,
    images = [
        "./Sprites/Adventurer_2_Sprites/adventurer-attack2-00.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack2-01.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack2-02.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack2-03.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack2-04.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack2-05.png"
    ],
    scale=5,
    animation_time=0.025,
    loop=False
)

attack_3 = AnimatedSprite(
    player_pos.x,
    player_pos.y,
    images = [
        "./Sprites/Adventurer_2_Sprites/adventurer-attack3-00.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack3-01.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack3-02.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack3-03.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack3-04.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-attack3-04.png"
    ],
    scale=5,
    animation_time=0.025,
    loop=False
)

jump = AnimatedSprite(
    player_pos.x,
    player_pos.y,
    images = [
        "./Sprites/Adventurer_2_Sprites/adventurer-jump-00.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-jump-01.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-jump-02.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-jump-03.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-fall-00.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-fall-01.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-crouch-02.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-crouch-03.png"
    ],
    scale=5,
    animation_time=0.015,
    loop=False
)

hurt = AnimatedSprite(
    player_pos.x,
    player_pos.y,
    images = [
        "./Sprites/Adventurer_2_Sprites/adventurer-hurt-00.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-hurt-01.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-hurt-02.png"
    ],
    scale=5,
    animation_time=0.07 
)

die = AnimatedSprite(
    player_pos.x,
    player_pos.y,
    images = [
        "./Sprites/Adventurer_2_Sprites/adventurer-die-00.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-die-01.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-die-02.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-die-03.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-die-04.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-die-05.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-die-06.png"
    ],
    scale=5,
    animation_time=0.07 
)

die_scene = AnimatedSprite(
    player_pos.x,
    player_pos.y,
    images = [
        "./Sprites/Adventurer_2_Sprites/adventurer-die-04.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-die-05.png",
        "./Sprites/Adventurer_2_Sprites/adventurer-die-06.png"
    ],
    scale=5,
    animation_time=0.07 
)

slime_attack = AnimatedSprite(
    slime_pos.x,
    slime_pos.y,
    images = [
        "./Sprites/Slime_1_Sprites/slime-attack-0.png",
        "./Sprites/Slime_1_Sprites/slime-attack-1.png",
        "./Sprites/Slime_1_Sprites/slime-attack-2.png",
        "./Sprites/Slime_1_Sprites/slime-attack-3.png",
        "./Sprites/Slime_1_Sprites/slime-attack-4.png"
    ],
    scale=3 
)

slime_idle = AnimatedSprite(
    slime_pos.x,
    slime_pos.y,
    images = [
        "./Sprites/Slime_1_Sprites/slime-idle-0.png",
        "./Sprites/Slime_1_Sprites/slime-idle-1.png",
        "./Sprites/Slime_1_Sprites/slime-idle-2.png",
        "./Sprites/Slime_1_Sprites/slime-idle-3.png"
    ],
    scale=3
)

slime_move = AnimatedSprite(
    slime_pos.x,
    slime_pos.y,
    images = [
        "./Sprites/Slime_1_Sprites/slime-move-0.png",
        "./Sprites/Slime_1_Sprites/slime-move-1.png",
        "./Sprites/Slime_1_Sprites/slime-move-2.png",
        "./Sprites/Slime_1_Sprites/slime-move-3.png"
    ],
    scale=3 
)

slime_die = AnimatedSprite(
    slime_pos.x,
    slime_pos.y,
    images = [
        "./Sprites/Slime_1_Sprites/slime-die-0.png",
        "./Sprites/Slime_1_Sprites/slime-die-1.png",
        "./Sprites/Slime_1_Sprites/slime-die-2.png",
        "./Sprites/Slime_1_Sprites/slime-die-3.png"
    ],
    scale=3,
    animation_time=0.06,
    loop=False 
)

slime_hurt = AnimatedSprite(
    slime_pos.x,
    slime_pos.y,
    images = [
        "./Sprites/Slime_1_Sprites/slime-hurt-0.png",
        "./Sprites/Slime_1_Sprites/slime-hurt-1.png",
        "./Sprites/Slime_1_Sprites/slime-hurt-2.png",
        "./Sprites/Slime_1_Sprites/slime-hurt-3.png"
    ],
    scale=3
)
pygame.mixer.music.play()
sprite = idle
slime_sprite = None
slime_vie = 2
slime_die_ticks = 15
player_die_ticks = 150
all_sprites = pygame.sprite.Group(sprite)
running = True
distance = 0
attack_pressed = False
is_attacking = False
is_dead = False
attack_frame_played = False
jump_pressed = False
is_jumping = False

while running:
         
    ticks = pygame.time.get_ticks()
    keyspressed = pygame.key.get_pressed()
    dt = clock.tick(FPS) / 1900
    
    if sprite != die and sprite != die_scene:
        if keyspressed[pygame.K_d]:
            if slime_die_ticks != 0:
                if player_pos.x < slime_pos.x - 150:
                    if sprite != walkLeft and not is_attacking and not is_jumping:
                        all_sprites.remove(sprite)
                        all_sprites.add(walkLeft)
                        sprite = walkLeft
                        sprite.index = 0
                        sprite.finished = False
                    elif player_pos.x < 1100:
                        player_pos.x += 1000 * dt
                        distance += 2
                    else:
                        distance += 1
                else:
                    if sprite != hurt and not is_attacking and not is_jumping:
                        all_sprites.remove(sprite)
                        all_sprites.add(hurt)
                        sprite = hurt
                        sprite.index = 0
                        sprite.finished = False
                    player_pos.x -= 560 * dt
            else:
                if sprite != walkLeft and not is_attacking and not is_jumping:
                        all_sprites.remove(sprite)
                        all_sprites.add(walkLeft)
                        sprite = walkLeft
                        sprite.index = 0
                        sprite.finished = False
                elif player_pos.x < 1100:
                    distance += 2
                else:
                    distance += 1
                player_pos.x += 1000 * dt   
            
        elif all_sprites.has(slime_attack) and player_pos.x > -90:
            if sprite != hurt and not is_attacking and not is_jumping:
                all_sprites.remove(sprite)
                all_sprites.add(hurt)
                sprite = hurt
                sprite.index = 0
                sprite.finished = False
            player_pos.x -= 560 * dt
            player_lives -= 0.1
            
        elif player_pos.x <= -90 or player_lives <= 0:
            if sprite != die:
                all_sprites.remove(sprite)
                all_sprites.add(die)
                sprite = die
                sprite.index = 0
                sprite.finished = False      
        else:
            if sprite != idle and not is_attacking and not is_jumping:
                all_sprites.remove(sprite)
                all_sprites.add(idle)
                sprite = idle
                sprite.index = 0
                sprite.finished = False
            player_pos.x -= 560 * dt
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and not attack_pressed and not is_dead and not is_jumping:
                attack_pressed = True
                is_attacking = True
                if sprite != attack_1:
                    all_sprites.remove(sprite)
                    all_sprites.add(attack_1)
                    sprite = attack_1
                    sprite.index = 0
                    sprite.finished = False  
                    stabbing_sound_1.play()
                #player_pos.x -= 560 * dt
            elif event.key == pygame.K_z and not attack_pressed and not is_dead and not is_jumping:
                attack_pressed = True
                is_attacking = True
                if sprite != attack_2:
                    all_sprites.remove(sprite)
                    all_sprites.add(attack_2)
                    sprite = attack_2
                    sprite.index = 0
                    sprite.finished = False  
                    stabbing_sound_1.play()
                #player_pos.x -= 560 * dt
            elif event.key == pygame.K_e and not attack_pressed and not is_dead and not is_jumping:
                attack_pressed = True
                is_attacking = True
                if sprite != attack_3:
                    all_sprites.remove(sprite)
                    all_sprites.add(attack_3)
                    sprite = attack_3
                    sprite.index = 0
                    sprite.finished = False 
                    stabbing_sound_2.play()
                #player_pos.x -= 560 * dt
            elif event.key == pygame.K_SPACE and not jump_pressed and not is_dead and not is_attacking and not sprite == hurt:
                jump_pressed = True
                is_jumping = True
                if sprite != jump:
                    all_sprites.remove(sprite)
                    all_sprites.add(jump)
                    sprite = jump
                    sprite.index = 0
                    sprite.finished = False
                player_pos.x -= 560 * dt
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                attack_pressed = False
            elif event.key == pygame.K_z:
                attack_pressed = False 
            elif event.key == pygame.K_e:
                attack_pressed = False
            elif event.key == pygame.K_SPACE:
                jump_pressed = False
                
    if (is_attacking and sprite.finished):
        all_sprites.remove(sprite)
        all_sprites.add(idle)
        sprite = idle
        sprite.index = 0
        sprite.finished = False
        is_attacking = False
        
    if (is_jumping and not sprite.finished):
        if sprite.index < 2:
            player_pos.y -= 3000 * dt
        elif sprite.index >= 6:
            player_pos.y += 3000 * dt
        
    if (is_jumping and sprite.finished):
        all_sprites.remove(sprite)
        all_sprites.add(idle)
        sprite = idle
        sprite.index = 0
        sprite.finished = False
        is_jumping = False
            
    for i in range(0, tiles):
        if sprite != die and sprite != die_scene and player_lives > 0:
            screen.blit(background, (i * background_width + scroll, 0))
        else:
            is_dead = True
            all_sprites.remove(hurt)
            all_sprites.add(die)
            sprite = die
            screen.fill("Black")
            pygame.mixer.music.stop()
            death_sound_played = True
            if player_die_ticks == 0:
                all_sprites.remove(sprite)
                all_sprites.add(die_scene)
                sprite = die_scene
                death_sound.stop()
                screen.blit(new_death_background, (0, 0))
                death_button.draw()
                slime_die_sound.stop()  
                death_music_played = True
                death_music.set_volume(0.2)   
            else:
                player_die_ticks -= 1 
       
    if slime_sprite is not None:   
        if slime_vie > 0 and sprite != die and sprite != die_scene and player_lives != 0:   
            if slime_pos.x >= player_pos.x + 1500:
                if slime_sprite != slime_idle:
                    all_sprites.remove(slime_sprite)
                    all_sprites.add(slime_idle)
                    slime_sprite = slime_idle
                    slime_sprite.index = 0
                    slime_sprite.finished = False
                slime_pos.x -= 560 * dt
            elif slime_pos.x > player_pos.x + 150:
                if slime_sprite != slime_move:
                    all_sprites.remove(slime_sprite)
                    all_sprites.add(slime_move)
                    slime_sprite = slime_move
                    slime_sprite.index = 0
                    slime_sprite.finished = False
                slime_pos.x -= 1400 * dt   
            elif (all_sprites.has(attack_1) or all_sprites.has(attack_2) or all_sprites.has(attack_3)) and 0 < slime_pos.x - player_pos.x <= 150:
                if slime_sprite != slime_hurt:
                    all_sprites.remove(slime_sprite)
                    all_sprites.add(slime_hurt)
                    slime_sprite = slime_hurt
                    slime_sprite.index = 0
                    slime_sprite.finished = False
                    slime_vie -= 1
                    slime_attack_sound.stop()
                    slime_hurt_sound.play()
                slime_pos.x -= 560 * dt
            elif 0 < slime_pos.x - player_pos.x <= 150:
                if slime_sprite != slime_attack:
                    all_sprites.remove(slime_sprite)
                    all_sprites.add(slime_attack)
                    slime_sprite = slime_attack
                    slime_sprite.index = 0
                    slime_sprite.finished = False
                    slime_attack_sound.play(-1, 0, 0)
                slime_pos.x -= 560 * dt   
            else:
                if slime_sprite != slime_idle:
                    all_sprites.remove(slime_sprite)
                    all_sprites.add(slime_idle)
                    slime_sprite = slime_idle
                    slime_sprite.index = 0
                    slime_sprite.finished = False
                slime_pos.x -= 560 * dt
        else:
            if slime_sprite != slime_die:
                all_sprites.remove(slime_sprite)
                all_sprites.add(slime_die)
                slime_sprite = slime_die
                slime_sprite.index = 0
                slime_sprite.finished = False
                slime_attack_sound.stop()
                if slime_pos.x - player_pos.x < 1500:
                    slime_die_sound.play()
            slime_pos.x -= 560 * dt
            if slime_die_ticks == 0:
                all_sprites.remove(slime_die)
                slime_sprite = None
            else:
                slime_die_ticks -= 1
    else:
        valeur = random.randint(1, 100)
        if valeur <= 5:
            all_sprites.add(slime_idle)
            slime_sprite = slime_idle
            slime_sprite.index = 0
            slime_sprite.finished = False
            slime_pos.x = player_pos.x + 1500
            slime_vie = 2
            slime_die_ticks = 15
        
    scroll -= 5
    
    if abs(scroll) > background_width:
        scroll = 0
        
    if death_music_played == True :
        if not pygame.mixer.get_busy():
            death_music.play()
            death_music_played = False
            
    if death_sound_played == True:
        if not pygame.mixer.get_busy():
            death_sound.play()
            death_sound_played = False
    
    sprite.move(player_pos.x,player_pos.y)
    if slime_sprite is not None:
        slime_sprite.move(slime_pos.x, slime_pos.y)
    dt = clock.tick(FPS) / 1900
    all_sprites.update(dt)        
    all_sprites.draw(screen)
    acc = acc_font.render(f"Distance : {distance}", True, (255, 255, 255))
    screen.blit(acc, (10, 10))     
    pygame.display.update()
    print(ticks)

pygame.quit()            