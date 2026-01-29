import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
Game_over=False

bee=Actor("bee")
bee.pos=100,100

flower=Actor("flower")
flower.pos=200,200

def draw():
    screen.blit("background", (0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score: "+ str(score), color="black", topleft=(10,10))
    if Game_over:
        screen.fill("blue")
        screen.draw.text("Time's up! Your final score - "+ str(score), midtop=(300,5), fontsize=40, color="black")

def time_up():
    global Game_over
    Game_over = True

def place_flower():
    flower.x = randint(70, (WIDTH-70))
    flower.y = randint(70, (HEIGHT-70))

def update():
    global score

    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2

    collect_flower=bee.colliderect(flower)

    if collect_flower:
        score=score+1
        place_flower()

clock.schedule(time_up, 60.0)

pgzrun.go()