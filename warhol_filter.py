"""
This program generates the Warhol effect based on the original image.
"""
import random
from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'


def main():
    final_image = copying_patch()
    # TODO: your code here.
    # This is an example which should generate a pinkish patch
    final_image.show()


def copying_patch():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    for row in range(N_ROWS):
        for col in range(N_COLS):
            patch = make_recolored_patch(1.5, 1 * row, 1.5 * col)
            for y in range(patch.height):
                for x in range(patch.width):
                    pixel_to_copy = patch.get_pixel(x, y)
                    final_image.set_pixel(x + (col * patch.width), y + (row * patch.height), pixel_to_copy)
    return final_image


def make_recolored_patch(red_scale, green_scale, blue_scale):
    """

    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch

    """

    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch




if __name__ == '__main__':
    main()
