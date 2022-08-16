"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename:str, the file path of the original fire image
    :return: SimpleImage,the image that shows the area of fire
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        # the bound to ensure it is the area on fire
        if pixel.red > avg:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img


def main():
    """
    This program can detect the area on fire and mark
     as the red area and the left area will be shown
     as grey color.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
