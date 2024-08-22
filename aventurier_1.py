import pygame
import math
from animated_sprites import AnimatedSprite


pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
player_dimensions = pygame.image.load("./Sprites/Adventurer_2_Sprites/adventurer-idle-2-00.png")
player_width = player_dimensions.get_width()
player_height = player_dimensions.get_height()
background = pygame.image.load("./Background/NewNewForest.jpg")
background_music = pygame.mixer.music.load("./Musics/monde_1.mp3")
stabbing_sound_1 = pygame.mixer.Sound("./Sounds/slash_1.mp3")
stabbing_sound_2 = pygame.mixer.Sound("./Sounds/slash_2.mp3")
slime_die_sound = pygame.mixer.Sound("./Sounds/slime_die.mp3")
slime_hurt_sound = pygame.mixer.Sound("./Sounds/slime_hurt.mp3")
slime_attack_sound = pygame.mixer.Sound("./Sounds/slime_attack.mp3")
background_width = background.get_width()
background_height = background.get_height()
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / background_width) + 1
screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Aventurier I")
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.4)
slime_pos = pygame.Vector2(SCREEN_WIDTH / 1.1, SCREEN_HEIGHT / 1.15)
player_hitbox = pygame.Rect(player_pos.x, player_pos.y, player_width, player_height)
clock = pygame.time.Clock()


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
    scale=5
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
    scale=5
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
    scale=5
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
    scale=5
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
    scale=5
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
    animation_time=0.06 
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
slime_sprite = slime_idle
slime_vie = 2
die_ticks = 15
all_sprites = pygame.sprite.Group(sprite, slime_sprite)
running = True
while running:
    
    keyspressed = pygame.key.get_pressed()
    dt = clock.tick(FPS) / 1900
    
    if keyspressed[pygame.K_d]:
        if die_ticks != 0:
            if player_pos.x < slime_pos.x - 150:
                if sprite != walkLeft:
                    all_sprites.remove(sprite)
                    all_sprites.add(walkLeft)
                    sprite = walkLeft
                player_pos.x += 1000 * dt
            else:
                if sprite != hurt:
                    all_sprites.remove(sprite)
                    all_sprites.add(hurt)
                    sprite = hurt
                player_pos.x -= 560 * dt
        else:
            if sprite != walkLeft:
                    all_sprites.remove(sprite)
                    all_sprites.add(walkLeft)
                    sprite = walkLeft
            player_pos.x += 1000 * dt   
    elif keyspressed[pygame.K_a]:
        if sprite != attack_1:
            all_sprites.remove(sprite)
            all_sprites.add(attack_1)
            sprite = attack_1
            stabbing_sound_1.play()
        player_pos.x -= 560 * dt
    elif keyspressed[pygame.K_z]:
        if sprite != attack_2:
            all_sprites.remove(sprite)
            all_sprites.add(attack_2)
            sprite = attack_2
            stabbing_sound_1.play()
        player_pos.x -= 560 * dt
    elif keyspressed[pygame.K_e]:
        if sprite != attack_3:
            all_sprites.remove(sprite)
            all_sprites.add(attack_3)
            sprite = attack_3
            stabbing_sound_2.play()
        player_pos.x -= 560 * dt
    elif keyspressed[pygame.K_SPACE]:
        if sprite != jump:
            all_sprites.remove(sprite)
            all_sprites.add(jump)
            sprite = jump
        player_pos.y -= 300 * dt
    elif all_sprites.has(slime_attack):
        if sprite != hurt:
            all_sprites.remove(sprite)
            all_sprites.add(hurt)
            sprite = hurt
        player_pos.x -= 560 * dt      
    else:
        if sprite != idle:
            all_sprites.remove(sprite)
            all_sprites.add(idle)
            sprite = idle
        player_pos.x -= 560 * dt
        
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    for i in range(0, tiles):
        screen.blit(background, (i * background_width + scroll, 0))


        
    if slime_vie > 0:   
        if slime_pos.x >= player_pos.x + 1500:
            if slime_sprite != slime_idle:
                all_sprites.remove(slime_sprite)
                all_sprites.add(slime_idle)
                slime_sprite = slime_idle
            slime_pos.x -= 560 * dt
        elif slime_pos.x > player_pos.x + 150:
            if slime_sprite != slime_move:
                all_sprites.remove(slime_sprite)
                all_sprites.add(slime_move)
                slime_sprite = slime_move
            slime_pos.x -= 1400 * dt   
        elif (all_sprites.has(attack_1) or all_sprites.has(attack_2) or all_sprites.has(attack_3)) and 0 < slime_pos.x - player_pos.x <= 150:
            if slime_sprite != slime_hurt:
                all_sprites.remove(slime_sprite)
                all_sprites.add(slime_hurt)
                slime_sprite = slime_hurt
                slime_vie -= 1
                slime_attack_sound.stop()
                slime_hurt_sound.play()
            slime_pos.x -= 560 * dt
        elif 0 < slime_pos.x - player_pos.x <= 150:
            if slime_sprite != slime_attack:
                all_sprites.remove(slime_sprite)
                all_sprites.add(slime_attack)
                slime_sprite = slime_attack
                slime_attack_sound.play(-1, 0, 0)
            slime_pos.x -= 560 * dt   
        else:
            if slime_sprite != slime_idle:
                all_sprites.remove(slime_sprite)
                all_sprites.add(slime_idle)
                slime_sprite = slime_idle
            slime_pos.x -= 560 * dt
    else:
        if slime_sprite != slime_die:
            all_sprites.remove(slime_sprite)
            all_sprites.add(slime_die)
            slime_sprite = slime_die
            slime_attack_sound.stop()
            slime_die_sound.play()
        slime_pos.x -= 560 * dt
        if die_ticks == 0:
            all_sprites.remove(slime_die)
        else:
            die_ticks -= 1       
        
    scroll -= 5
    
    if abs(scroll) > background_width:
        scroll = 0
        
    
    sprite.move(player_pos.x,player_pos.y)
    slime_sprite.move(slime_pos.x, slime_pos.y)
    dt = clock.tick(FPS) / 1900
    all_sprites.update(dt)        
    all_sprites.draw(screen)       
    pygame.display.update()

pygame.quit()            