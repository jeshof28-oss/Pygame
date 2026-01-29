import pgzrun
import random

WIDTH=500
HEIGHT=500

bees=[]
for i in range(5):
    be=Actor("bee")
    be.pos=random.randint(70,(WIDTH-70)),random.randint(70,(HEIGHT-70))
    bees.append(be)

def draw():
    for be in bees:
        be.draw()

pgzrun.go()