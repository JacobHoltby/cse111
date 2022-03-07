# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from turtle import width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    min_diam = 2
    max_diam = 5

    # Draw 100 circles, each with
    # a random location and diameter.
    scene_width = 800
    scene_height = 500
    # canvas = start_drawing("Scene", scene_width, scene_height)

    for i in range(100):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(250, 500)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
            fill="ivory1")
    # finish_drawing(canvas)
    # draw_stars(canvas, scene_width, scene_height, 100, 100)
    draw_cloud(canvas, 100, 325, 200, 100)
    draw_cloud(canvas, 400, 325, 400, 150)
    draw_cloud(canvas, 75, 300, 100, 50)
    draw_cloud(canvas, 60, 400, 150, 25)

    for x in range(100, 800, 100):
        draw_pine_tree(canvas, x, scene_height / 3 - 10, 80)
    
    draw_pine_tree(canvas, 550, 100, 250)
    draw_pine_tree(canvas, 250, 100, 200) 

    # draw_grid(canvas, scene_width, scene_height, 50)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    #draw the sky and all the objects in the sky
    draw_rectangle(canvas, 0, scene_height / 3, 
    scene_width, scene_height, width = 0, fill = "midnight blue")

def draw_ground(canvas, scene_width, scene_height):
    #draw the ground and all the objects on the ground
    draw_rectangle(canvas, 0, 0, 
    scene_width, scene_height / 3, width = 0, fill = "chartreuse4")



# def draw_stars(canvas, scene_width, scene_height, star_size, num_stars):
#     for i in range(num_stars):
#         x = random.randint(0, scene_width)
#         y = random.randint(scene_height / 3, scene_height)
#         draw_oval(canvas, x, y, x + star_size, y + star_size, fill = "black")

def draw_cloud(canvas, x, y, cloud_width, cloud_height):
    
    draw_oval(canvas, x, y, x + cloud_width, y + cloud_height, width = 0, fill = "seashell4")

def draw_pine_tree(canvas, center_x, bottom, height):
    # draw the trunk of the tree
    trunk_width = height / 10
    trunk_height = height / 6
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="tan4")

    # draw the skirt of the tree
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x,
    peak_y, skirt_right, skirt_bottom, fill="darkGreen")

def draw_grid(canvas, width, height, interval):
    # draw vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    # draw horizontal lines
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")


# Call the main function so that
# this program will start executing.
main()