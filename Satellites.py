import pgzrun
from time import time
from random import randint

WIDTH = 800
HEIGHT = 600
sats = []
number_of_sats = 0
lines=[]
next_sat=0

start_time=0
total_time=0
end_time=0

def create_sats():
    global start_time
    for i in range(number_of_sats):
        satellite=Actor("sat")
        satellite.pos=randint(40,WIDTH-40),randint(40, HEIGHT-40)
        sats.append(satellite)

    start_time=time()

def draw():
    global total_time

    screen.blit("backgrouund", (0,0))
    number=1
    for satellite in sats:
        screen.draw.text(str(number), (satellite.pos[0]), satellite.pos[1])
        satellite.draw()
        number=number + 1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_sat < number_of_sats:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
