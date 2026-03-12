import pgzrun
import random

FONT_option = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
center_x=WIDTH / 2
center_y=HEIGHT / 2
CENTRE = (center_x , center_y)
final_level=6
start_speed=6
items=["bag", "battery", "bottle", "chips"]

game_over= False
game_complete= True
current_level= 1
items = []
animations = []

def draw():
    global items, current_level, game_over, game_complete
    screen.blit("bg", (0,0))
    if game_over:
        display_message("Game Over, try again?")
    if game_complete:
        display_message("Game Complete!, Well Done")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(num_of_extra):
    items_to_make = get_option_to_create(num_of_extra)
    new_items = create_items(items_to_make)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(num_of_extra):
    items_to_make=[]
    for i in range(0, num_of_extra):
        random_select=random.choice(items)
        items_to_make.append(random_select)
    return items_to_make

def create_items():
    new_items=[]
    for i in items_to_make:
        new_item=Actor(option + "img")
        new_items.append(new_item)
    return new_items

def layout_items(items_to_lay):
    number_of_gaps = len(items_to_lay) + 1
    gap_size= WIDTH / number_of_gaps
    random.shuffle(items_to_lay)
    for index, item in enumerate(items_to_lay):
        new_x_pos=index*gap_size
        item.x=new_x_pos

def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        duration = start_speed - current_level
        i.anchor = ("center", "bottom")
        animation = animate(i, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)
    
def handle_game_over():
    global game_over
    game_over=True

def on_mouse_click(pos):
    global items

    for i in items:
        if item.collidepoint(pos):
            if "bag" in items:
                items.remove(i)

                if len (items) == 0:
                    level_up()

def level_up():
    global currrent_level, game_complete
    if current_level == final_level:
        game_complete=True
    else:
        current_level +=1

def display_message(message):
    screen.draw.text(message, center=CENTRE, fontize=60, color="white")

pgzrun.go()