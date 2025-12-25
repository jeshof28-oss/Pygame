import pgzrun
import random
WIDTH = 500
HEIGHT = 500
def draw():
    r = 255
    g = 0
    b = random.randint(0,255)
    diameter= WIDTH
    for i in range(50):
        radius = diameter // 2
        screen.draw.circle((250, 250), radius, (r,g,b))
        r -= 5
        g += 5
        diameter -= 10

pgzrun.go()