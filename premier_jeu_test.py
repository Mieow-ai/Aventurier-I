import pygame
from pygame_functions import clock, changeSpriteImage, makeSprite, screenSize, tick, setBackgroundColour, moveSprite, showSprite, killSprite, setBackgroundImage
from aspose.imaging import*
import os
from PIL import Image


pygame.init()

screen = screenSize(884 , 864)
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
slime_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0
Frame = 0
nextFrame = clock()

testSpriteWalkDown = makeSprite("./Sprites/Walk/walk_down.png", 8)
testSpriteWalkUp = makeSprite("./Sprites/Walk/walk_up.png", 8)
testSpriteWalkRight = makeSprite("./Sprites/Walk/walk_right_down.png", 8)
testSpriteWalkLeft = makeSprite("./Sprites/Walk/walk_left_down.png", 8)
testSpriteIdle = makeSprite("./Idle/idle_down.png", 8)
SlimeSprite = makeSprite("./Sprites/slime-Sheet.png", 21)
setBackgroundImage("./Background/Forest.png")

sprite = testSpriteIdle

while running: 

    keys = pygame.key.get_pressed()
    
    if clock() > nextFrame:
        Frame = (Frame+1)%8
        nextFrame += 80

    if keys[pygame.K_z]:
        if sprite != testSpriteWalkUp:
            sprite.kill()
            sprite = testSpriteWalkUp
        player_pos.y -= 300 * dt
    elif keys[pygame.K_s]:
        if sprite != testSpriteWalkDown:
            sprite.kill()
            sprite = testSpriteWalkDown
        player_pos.y += 300 * dt
    elif keys[pygame.K_q]:
        if sprite != testSpriteWalkLeft:
            sprite.kill()
            sprite = testSpriteWalkLeft
        player_pos.x -= 300 * dt
    elif keys[pygame.K_d]:
        if sprite != testSpriteWalkRight:
            sprite.kill()
            sprite = testSpriteWalkRight
        player_pos.x += 300 * dt
    else:
        if sprite != testSpriteIdle:
            sprite.kill()
            sprite = testSpriteIdle
    sprite.move(player_pos.x,player_pos.y,True)
    showSprite(sprite)
    changeSpriteImage(sprite, Frame)
    
    
    
    dt = tick(25) / 1900

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()            