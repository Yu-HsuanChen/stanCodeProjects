"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(bg_img, fg_img):
    """
    :param bg_img:SimpleImage, the background image
    :param fg_img:SimpleImage, the figure image in green screen
    :return:SimpleImage, the image combines bg_img and fg_img by
          replacing the green pixels in fg_img with pixels from
          bg_img
    """
    for x in range(fg_img.width):
        for y in range(fg_img.height):
            bg_img_p = bg_img.get_pixel(x, y)
            fg_img_p = fg_img.get_pixel(x, y)
            if fg_img_p.green > fg_img_p.red*2 and fg_img_p.green > fg_img_p.blue*2:
                # green screen
                fg_img_p.red = bg_img_p.red
                fg_img_p.green = bg_img_p.green
                fg_img_p.blue = bg_img_p.blue
    return fg_img


def main():
    """
    This program can make a new image that replace the green screen
     in one image with the background from another image.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
