"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jaclyn Setina.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    print("--------")
    top_left_point = rectangle.get_upper_left_corner()
    saved_top_left_x = top_left_point.x
    top_left_y = top_left_point.y

    WIDTH = rectangle.get_width()
    HEIGHT = rectangle.get_height()

    for k in range(n): # for each row...
        top_left_x = saved_top_left_x

        for j in range(k+1): # for each rectangle in the row...
            # draw the rectangle
            loop_top_left_pt = rg.Point(top_left_x, top_left_y)
            loop_bottom_right_pt = rg.Point(top_left_x + WIDTH, top_left_y + HEIGHT)
            loop_rect = rg.Rectangle(loop_top_left_pt, loop_bottom_right_pt)
            loop_rect.attach_to(window)
            window.render(0.1)
            # figure out next starting point for the next rectangle
            top_left_x += WIDTH

        saved_top_left_x = saved_top_left_x - WIDTH / 2
        top_left_y = top_left_y - HEIGHT

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
