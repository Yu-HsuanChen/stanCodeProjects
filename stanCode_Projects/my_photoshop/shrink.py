"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,the file path of the original image
    :return img: SimpleImage,the shrink image
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(b_img.width):
        for y in range(b_img.height):
            img_p = img.get_pixel(x*2+1, y*2+1)
            # if 4 pixels as team,only choose the lower right one
            b_img_p = b_img.get_pixel(x, y)
            b_img_p.red = img_p.red
            b_img_p.green = img_p.green
            b_img_p.blue = img_p.blue
    return b_img


def main():
    """
    This program can shrink the original image to
    the half of its size.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
