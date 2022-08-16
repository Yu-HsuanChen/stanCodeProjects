"""
File: draw_line
Name: Joanne Chen
-------------------------
TODO: To draw a line between two mouse clicks.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
number = 0
x1 = 0
y1 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global number
    global x1
    global y1
    # first click
    if number == 0:
        circle = GOval(5, 5, x=mouse.x, y=mouse.y)
        window.add(circle)
        x1 = mouse.x
        y1 = mouse.y
        number += 1
    # second click
    elif number == 1:
        # remove the circle made by first click
        circle = window.get_object_at(x1+5/2, y1+5/2)
        window.remove(circle)
        x2 = mouse.x
        y2 = mouse.y
        line = GLine(x0=x1+5/2, y0=y1+5/2, x1=x2, y1=y2)
        window.add(line)
        number -= 1


if __name__ == "__main__":
    main()
