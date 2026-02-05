import pgzrun
import pygame
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
Game_over=False

ash=Actor("ash")
ash.pos=100,100


pokeball=Actor("pokeball")

ash._surf=pygame.transform.scale(ash._surf,(100,100))
ash._update_pos()
pokeball._surf=pygame.transform.scale(pokeball._surf,(100,100))
pokeball._update_pos()
pokeball.pos=300,300

def draw():
    screen.blit("background", (0,0))
    pokeball.draw()
    ash.draw()
    screen.draw.text("Score: "+ str(score), color="black", topleft=(10,10))
    if Game_over:
        screen.fill("blue")
        screen.draw.text("Time's up! Your final score - "+ str(score), midtop=(300,5), fontsize=40, color="black")

def time_up():
    global Game_over
    Game_over = True

def place_pokeball():
    pokeball.x = randint(70, (WIDTH-70))
    pokeball.y = randint(70, (HEIGHT-70))

def update():
    global score

    if keyboard.left:
        ash.x=ash.x-2
    if keyboard.right:
        ash.x=ash.x+2
    if keyboard.up:
        ash.y=ash.y-2
    if keyboard.down:
        ash.y=ash.y+2

    collect_pokeball=ash.colliderect(pokeball)

    if collect_pokeball:
        score=score+1
        place_pokeball()

clock.schedule(time_up, 60.0)

pgzrun.go()