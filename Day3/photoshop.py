from PIL import Image
from PIL import ImageFilter


def apply_filter(image, filter):
    pixels = [filter(p) for p in image.getdata()]
    nim = Image.new("RGB", image.size)
    nim.putdata(pixels)
    return nim


def open_image(filename):
    image = Image.open(filename)
    if image == None:
        print("Specified input file " + filename + " cannot be opened.")
        return Image.new("RGB", (400, 400))
    else:
        print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
        return image.convert("RGB")


def restart():
    a = input("Would you like to do another operation?")
    if a == 'Yes':
        choices()
    if a == 'No':
        quit()


def identity(pixel):
    r, g, b = pixel
    return(r, g, b)


def invert(pixel):
    r, g, b = pixel
    finished = (255 - r, 255 - g, 255 - b)
    return finished


def darken(pixels):
    r, g, b = pixels
    r = int(r * 0.25)
    g = int(g * 0.25)
    b = int(b * 0.25)
    return(r, g, b)
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
    r, g, b = pixel
    if r < 128:
        r = 255 - r
    if g < 128:
        g = 255 - g
    if b < 128:
        b = 255 - b
    return (r, g, b)
    pass


def flip(imageX):
    type = input("Would you like to flip the image vertically or horizontally?")
    if type == 'Vertically':
        img = Image.open(imageX).transpose(Image.FLIP_TOP_BOTTOM)
    if type == 'Horizontally':
        img = Image.open(imageX).transpose(Image.FLIP_LEFT_RIGHT)
    img.show()
    return img


def blur(imageX):
    r = int(input("What do you want the radius to be?"))
    print(imageX)
    original_image = Image.open(imageX)
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=r))
    blurred_image.show()
    return blurred_image


def sharpen(imageX):
    inpt_radius = int(input("What would you like the radius to be?"))
    inpt_percent = int(input("Enter sharpening percentage."))
    inpt_threshold = int(input("Enter a sharpening threshold."))
    sharper_image = Image.open(imageX)
    sharper_image = sharper_image.filter(ImageFilter.UnsharpMask(radius = inpt_radius, percent = inpt_percent, threshold = inpt_threshold))
    sharper_image.show()
    return sharper_image


def cropper(imageX):
    start_x = int(input("Enter a starting value for x."))
    start_y = int(input("Enter a starting value for y."))
    end_x = int(input("Enter an ending value for x."))
    end_y = int(input("Enter an ending value for y."))
    imgd = Image.open(imageX)
    area = (start_x, start_y, end_x, end_y)
    cropped_img = imgd.crop(area)
    cropped_img.show()
    return cropped_img


def load_and_go(fname, filterfunc):
    image = open_image(fname)
    nimage = apply_filter(image, filterfunc)
    image.show()
    nimage.show()
    a = input("What would you like to call this new image? Enter the file ending as well.")
    nimage.save(a)


def choices():
    choice = input("Which operation would you like to do? You can 'Darken', 'Brighten', 'Invert', 'Grayscale',"
                   "'Posterize', 'Solarize', 'Flip', 'Blur', 'Sharpen', or 'Crop'.")
    input_file = input("Which photo would you like to change?")
    if choice == 'Darken':
        load_and_go(input_file, darken)
    if choice == 'Brighten':
        load_and_go(input_file, brighten)
    if choice == 'Invert':
        load_and_go(input_file, invert)
    if choice == 'Grayscale':
        load_and_go(input_file, gray_scale)
    if choice == 'Posterize':
        load_and_go(input_file, posterize)
    if choice == 'Solarize':
        load_and_go(input_file, solarize)
    if choice == 'Flip':
        b = flip(input_file)
        a = input("What would you like to call this new image?")
        b.save(a)
    if choice == 'Blur':
        c = blur(input_file)
        a = input("What would you like to call this new image?")
        c.save(a)
    if choice == 'Sharpen':
        b = sharpen(input_file)
        a = input("What would you like to call this new image?")
        b.save(a)
    if choice == 'Crop':
        b = cropper(input_file)
        a = input("What would you like to call this new image?")
        b.save(a)


if __name__ == "__main__":
    choices()
while True:
    restart()

