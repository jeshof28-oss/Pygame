import pgzrun
import random

FONT_option = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
center_x = WIDTH / 2
center_y = HEIGHT / 2
CENTRE = (center_x, center_y)

final_level = 6
start_speed = 6

item_names = ["bag", "battery", "bottle", "chips"]

game_over = False
game_complete = False
current_level = 1

items = []
animations = []


def draw():
    screen.blit("bg", (0, 0))

    if game_over:
        display_message("Game Over! You clicked the wrong item")
    elif game_complete:
        display_message("Level Complete!")
    else:
        for item in items:
            item.draw()


def update():
    global items

    if len(items) == 0 and not game_over:
        items = make_items(current_level)


def make_items(num_of_extra):
    items_to_make = get_option_to_create(num_of_extra)
    new_items = create_items(items_to_make)

    layout_items(new_items)
    animate_items(new_items)

    return new_items


def get_option_to_create(num_of_extra):
    items_to_make = ["bag"]

    for i in range(num_of_extra):
        random_select = random.choice(item_names)
        items_to_make.append(random_select)

    return items_to_make


def create_items(items_to_make):
    new_items = []

    for option in items_to_make:
        new_item = Actor(option + "img")
        new_items.append(new_item)

    return new_items


def layout_items(items_to_lay):
    number_of_gaps = len(items_to_lay) + 1
    gap_size = WIDTH / number_of_gaps

    random.shuffle(items_to_lay)

    for index, item in enumerate(items_to_lay):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos
        item.y = 0


def animate_items(items_to_animate):
    global animations

    for i in items_to_animate:
        duration = start_speed - (current_level * 0.5)

        i.anchor = ("center", "bottom")

        animation = animate(i,
                            duration=duration,
                            y=HEIGHT,
                            on_finished=handle_game_over)

        animations.append(animation)


def handle_game_over():
    global game_over
    game_over = True


def on_mouse_down(pos):
    global items, current_level, game_complete, game_over

    for item in items:
        if item.collidepoint(pos):

            if "bag" in item.image:
                items.remove(item)

                if len(items) == 0:
                    level_up()
            else:
                game_over = True


def level_up():
    global current_level, game_complete

    if current_level == final_level:
        game_complete = True
    else:
        current_level += 1


def display_message(message):
    screen.draw.text(message,
                     center=CENTRE,
                     fontsize=60,
                     color="white")


pgzrun.go()