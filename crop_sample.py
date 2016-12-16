from PIL import Image

"""

This class crops sample.png to obtain images of numbers.

"""

# extract digit 1, 2, 3 from sample1.png
# each digit is croped into a 10*10 png image in black and white
# each digit is rotated if necessary to be positioned upright
im_sample1 = Image.open("sample1.png")

# crop number 1
digit_pixels = im_sample1.crop((112,184,122,194))

# Convert image to black and white mode
digit_pixels = digit_pixels.convert("L")

# Rotate the image anti-clockwise for 270 degree
digit_pixels = digit_pixels.rotate(270)
# digit_pixels.show()
digit_pixels.save("1.png", format='png')

# crop number 2
digit_pixels = im_sample1.crop((85,154,95,164))
digit_pixels = digit_pixels.convert("L")
digit_pixels = digit_pixels.rotate(270)
# digit_pixels.show()
digit_pixels.save("2.png", format='png')

# crop number 3
digit_pixels = im_sample1.crop((875,123,885,133))
digit_pixels = digit_pixels.convert("L")
digit_pixels = digit_pixels.rotate(270)
# digit_pixels.show()
digit_pixels.save("3.png", format='png')

# extract digit 4, 5, 6, 7, 8, 9, 0 from sample2.png
im_sample2 = Image.open("sample2.png")

# crop number 4
digit_pixels = im_sample2.crop((161,198,171,208))
digit_pixels = digit_pixels.convert("L")
# digit_pixels.show()
digit_pixels.save("4.png", format='png')

# crop number 5
digit_pixels = im_sample2.crop((506,206,516,216))
digit_pixels = digit_pixels.convert("L")
digit_pixels = digit_pixels.rotate(270)
# digit_pixels.show()
digit_pixels.save("5.png", format='png')


# crop number 6
digit_pixels = im_sample2.crop((203,204,213,214))
digit_pixels = digit_pixels.convert("L")
digit_pixels = digit_pixels.rotate(270)
# digit_pixels.show()
digit_pixels.save("6.png", format='png')

# crop number 7
digit_pixels = im_sample2.crop((106,203,116,213))
digit_pixels = digit_pixels.convert("L")
digit_pixels = digit_pixels.rotate(270)
# digit_pixels.show()
digit_pixels.save("7.png", format='png')

# crop number 8
digit_pixels = im_sample2.crop((189,201,199,211))
digit_pixels = digit_pixels.convert("L")
digit_pixels = digit_pixels.rotate(270)
# digit_pixels.show()
digit_pixels.save("8.png", format='png')

# crop number 9
digit_pixels = im_sample2.crop((327,200,337,210))
digit_pixels = digit_pixels.convert("L")
digit_pixels = digit_pixels.rotate(270)
# digit_pixels.show()
digit_pixels.save("9.png", format='png')

# crop number 0
digit_pixels = im_sample2.crop((92,163,102,173))
digit_pixels = digit_pixels.convert("L")
digit_pixels = digit_pixels.rotate(270)
# digit_pixels.show()
digit_pixels.save("0.png", format='png')

