# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from turtle import heading
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas, 0, 1000, 200, 400)
    draw_ground(canvas, 0, 1000, 0, 200)
    for x in range(100, 1000, 100):
        draw_pine(canvas, x, 150, 100)

    for y in range(50, 1000, 100):
        draw_pine(canvas, y, 50, 100)

    for c in range(50, 300, 40):
        draw_clound(canvas, c, 350, 70)

    for d in range(400, 800, 40):
        draw_clound(canvas, d, 280, 70)

    draw_sun(canvas, 700, 380, 100)

    # for x in range(100, 300, 20):
    #draw_pine(canvas, x, 350, 20)

    draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


def draw_sky(canvas, width_start, width_end, bottom, height):
    sky_height = height
    left_sky = width_start
    bottom_sky = bottom
    right_sky = width_end
    sky_top = bottom + sky_height

    draw_rectangle(canvas, left_sky, bottom_sky,
                   right_sky, sky_top, fill="deepSkyBlue3")


def draw_ground(canvas, width_start, width_end, bottom, height):
    ground_height = height
    left_ground = width_start
    bottom_ground = bottom
    right_ground = width_end
    ground_top = bottom + ground_height

    draw_rectangle(canvas, left_ground, bottom_ground,
                   right_ground, ground_top, fill="darkGreen")


def draw_clound(canvas, center_x, bottom, height):
    clound_width = height / 2
    clound_height = height / 1
    left_clound = center_x - clound_width
    bottom_clound = bottom
    right_clound = center_x + clound_width
    clound_top = bottom + clound_height

    draw_oval(canvas, left_clound, bottom_clound,
              right_clound, clound_top, width=0, fill="white")


def draw_sun(canvas, center_x, bottom, height):
    clound_width = height / 2
    clound_height = height / 1
    left_clound = center_x - clound_width
    bottom_clound = bottom
    right_clound = center_x + clound_width
    clound_top = bottom + clound_height

    draw_oval(canvas, left_clound, bottom_clound,
              right_clound, clound_top, width=0, fill="yellow1")


def draw_pine(canvas, center_x, bottom, height):
    # Draw the trunk of the tree
    trunk_width = height / 10
    trunk_height = height / 6
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk,
                   right_trunk, trunk_top, fill="tan4")

    # Draw the Skirt of the Tree
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x,
                 peak_y, skirt_right, skirt_bottom, fill="forestGreen")


def draw_grid(canvas, width, height, interval):
    # Draw a vertical lines
    # posição / altura / posição / comprimento
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    # Draw a horizontal lines
    label_x = 15
    for y in range(interval, width, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")


# Call the main function so that
# this program will start executing.
main()
