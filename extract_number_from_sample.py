from PIL import Image

"""
	This class crops sample.png to obtain images of numbers.
"""

im = Image.open("sample.png")
test = im.crop((84,154,94,165))
test = test.convert("RGBA")

pix = test.load()

for y in range(test.size[1]):
	for x in range(test.size[0]):
		if(pix[x,y][0] > 0):
			pix[x,y] = (255,255,255,255)
im.show()
