import pgzrun
from time import time
from random import randint

WIDTH = 800
HEIGHT = 600
sats = []
number_of_sats = 8
lines=[]
next_sat=0

start_time=0
total_time=0
end_time=0

def create_sats():
    global start_time
    for i in range(number_of_sats):
        satellite=Actor("satellite")
        satellite.pos=randint(40,WIDTH-40),randint(40, HEIGHT-40)
        sats.append(satellite)

    start_time=time()

def draw():
    global total_time

    screen.blit("space", (0,0))
    number=1
    for satellite in sats:
        screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1]+20))
        satellite.draw()
        number=number + 1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_sat < number_of_sats:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)

def update():
    pass

def on_mouse_down(pos):
    global next_sat,lines

    if next_sat < number_of_sats:
        if sats[next_sat].collidepoint(pos):
            if next_sat:
                lines.append((sats[next_sat-1].pos,sats[next_sat].pos))
            next_sat=next_sat+1
        else:
            lines=[]
            next_sat=0

create_sats()
pgzrun.go()

# HW: Replace satellites with *different* planets