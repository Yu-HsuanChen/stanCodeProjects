"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the original simpleimage
    :return: the blurred simpleimage
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_pixel = new_img.get_pixel(x, y)
            sum_red = 0
            sum_blue = 0
            sum_green = 0
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixel_x = x+i
                    pixel_y = y+j
                    if 0 <= pixel_x < img.width and 0 <= pixel_y < img.height:
                        pixel = img.get_pixel(pixel_x, pixel_y)
                        sum_red += pixel.red
                        sum_blue += pixel.blue
                        sum_green += pixel.green
                        count += 1
            new_pixel.red = sum_red/count
            new_pixel.blue = sum_blue/count
            new_pixel.green = sum_green/count
    return new_img


def main():
    """
    TODO: To get the blurred image from the input image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
