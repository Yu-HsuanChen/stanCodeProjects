"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:str, the file path of the original image
    :return:SimpleImage,the image shows the original image
            and the mirrored image
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            b1_p = b_img.get_pixel(x, y)
            b2_p = b_img.get_pixel(x, b_img.height-1-y)
            b1_p.red = img_p.red
            b1_p.green = img_p.green
            b1_p.blue = img_p.blue
            b2_p.red = img_p.red
            b2_p.green = img_p.green
            b2_p.blue = img_p.blue
    return b_img


def main():
    """
    This program can make a mirrored image of the original
    image by creating a blank image(height is two times longer
    than the original image)and copying the upper pixels to
    the lower pixels.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
