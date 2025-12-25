<<<<<<< HEAD
import pgzrun
import random
WIDTH = 500
HEIGHT = 500

def draw():
    r = 255
    g = 0
    b = random.randint(0,255)

    width = WIDTH 
    height = HEIGHT -300

    for i in range(20):
        rect=Rect((50,50),(width, height))
        rect.center=(150,150)
        screen.draw.rect(rect,(r,g,b))

        r-=10
        g+=10

        width-=10
        height+=10
pgzrun.go()


    
=======
import pgzrun
import random
WIDTH = 500
HEIGHT = 500

def draw():
    r = 255
    g = 0
    b = random.randint(0,255)

    width = WIDTH 
    height = HEIGHT -300

    for i in range(20):
        rect=Rect((50,50),(width, height))
        rect.center=(150,150)
        screen.draw.rect(rect,(r,g,b))

        r-=10
        g+=10

        width-=10
        height+=10
pgzrun.go()

    
>>>>>>> 4783bfb507bd008c0c6dc085b26dee2fa966e349
