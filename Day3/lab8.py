'''
Created on Oct 25, 2011
Modified on Oct 31, 2012
Modified on Mar 4, 2017 by Susan Rodger

@author: rcd, alexandrudutu, ola
'''
from PIL import Image


# alternatively, try the line below
# import Image    # standard python image library


def apply_filter(image, filter):
    '''
    Create and return a NEW image, based on a
    transform of each pixel in the given image using the given filter
    image is an open Image object
    filter is a function to apply to each pixel in image
    return new image, same size, to which filter has been applied to each pixel of image
    '''
    pixels = [filter(p) for p in image.getdata()]
    nim = Image.new("RGB", image.size)
    nim.putdata(pixels)
    return nim


def open_image(filename):
    '''
    opens the given image and converts it to RGB format
    returns a default image if the given one cannot be opened
    filename is the name of a PNG, JPG, or GIF image file
    '''
    image = Image.open(filename)
    if image == None:
        print("Specified input file " + filename + " cannot be opened.")
        return Image.new("RGB", (400, 400))
    else:
        print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
        return image.convert("RGB")


'''
During this lab a pixel is a tuple of 3 values (R, G, B)
representing the red, green, and blue components of a color
that each range from [0-255] inclusive. 
The filter functions:
    - take one pixel as an argument,
    - modify the channels of the pixel and
    - return the transformed pixel
'''


def identity(pixel):
    '''
    returns a pixel that is unchanged from the original
    '''
    r, g, b = pixel
    return (r, g, b)


def invert(pixel):
    '''
    returns a pixel where every pixel channel is 255 minus its value
    '''
    r, g, b = pixel
    return (255 - r, 255 - g, 255 - b)


def darken(pixel, input_file):
    """
    returns a pixel whose red, green, and blue values are all 90% of those given
    """
    r, g, b = pixel
    r = int(r * 0.75)
    g = int(g * 0.75)
    b = int(b * 0.75)
    print(r, g, b)
    pass


def brighten(pixel):
    r, g, b = pixel
    r = int(r * 1.25)
    g = int(g * 1.25)
    b = int(b * 1.25)
    return (r, g, b)
    pass


def gray_scale(pixel):
    r, g, b = pixel
    r = int((r + g + b)/3)
    g = int((r + g + b)/3)
    b = int((r + g + b)/3)
    return (r, g, b)
    pass


def posterize(pixel):
    """
    returns a pixel whose red, green, and blue values are all changed in
    the following way:
     - divide channel's range into 4 equal pieces (i.e., 0-63, 64-127, 128-191, 192-255)
     - set the channel's value to a fixed value within that range (i.e., 50, 100, 150, 200)
    """
    r, g, b = pixel
    if 63 >= r >= 0:
        r = 50
    if 63 >= g >= 0:
        g = 50
    if 63 >= b >= 0:
        b = 50
    if 127 >= r >= 64:
        r = 100
    if 127 >= g >= 64:
        g = 100
    if 127 >= b >= 64:
        b = 100
    if 191 >= r >= 128:
        r = 150
    if 191 >= g >= 128:
        g = 150
    if 191 >= b >= 128:
        b = 150
    if 255 >= r >= 192:
        r = 200
    if 255 >= g >= 192:
        g = 200
    if 255 >= b >= 192:
        b = 200
    return (r, g, b)


def solarize(pixel):
    """
    returns a pixel whose red, green, and blue values are all changed in
    the following way:
     - if the value is less than 128, set it to 255 - the original value.
     - if the value is 128 or greater, don't change it.
    """
    r, g, b = pixel
    if r < 128:
        r = 255 - r
    if g < 128:
        g = 255 - g
    if b < 128:
        b = 255 - b
    return (r, g, b)
    pass


def denoise(pixel):
    r, g, b = pixel
    r = int(r * 10)
    g = 0
    b = 0
    return (r, g, b)
    pass


def denoise2(pixel):
    r, g, b = pixel
    r = 0
    g = int(g * 20)
    b = int(b * 20)
    return (r, g, b)
    pass


def denoise3(pixel):
    r, g, b = pixel
    if r == 255 and g == 0 and b == 0:
        r = 0
    if r == 255 and g == 255 and b == 255:
        r = 0
        g = 0
        b = 0
    return (r, b, g)
    pass


def load_and_go(fname, filterfunc):
    image = open_image(fname)
    nimage = apply_filter(image, filterfunc)
    image.show()
    nimage.show()
    '''
    processedImage.jpg is the name of the file
    the image is saved in. The first time you do 
    this you may have to refresh to see it.
    '''
    nimage.save("processedImage.jpg")


if __name__ == "__main__":
    ''' Change the name of the file and the function
        to apply to the file in the line below
    '''
    input_file = "clue.bmp"
    a = input("Which editing method would you like to use?")
    if a == 'darken':
        load_and_go(input_file, darken)
    if a == 'brighten':
        load_and_go(input_file, brighten)
    if a == 'invert':
        load_and_go(input_file, invert)
    if a == 'grayscale':
        load_and_go(input_file, gray_scale)
    if a == 'posterize':
        load_and_go(input_file, posterize)
    if a == 'solarize':
        load_and_go(input_file, solarize)
    if a == 'denoise1':
        load_and_go(input_file, denoise)
    if a == 'denoise2':
        load_and_go(input_file, denoise2)
    if a == 'denoise3':
        load_and_go(input_file, denoise3)
    else:
        a = input("Your input is not recognized.")