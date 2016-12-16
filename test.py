from PIL import Image
import numpy
from pytesseract import *

im = Image.open("2.png")

pix = im.load()

for y in range(im.size[1]):
	for x in range(im.size[0]):
		if(pix[x,y][0] > 0):
			pix[x,y] = (255,255,255,255)
im.show()
# text = pytesseract.image_to_string(im)
# print (text + "haha")