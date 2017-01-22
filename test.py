from PIL import Image
import numpy
from pytesseract import *
from imageReader import *

try:
	list = []
	list[5] = 1
except IndexError:
	print("exception caught")
# im = Image.open("sample1.png")
# im = im.convert("L")
# pix = im.load()
# print(pix[187, 114])
# print(pix[187, 115])

# im = im.crop((113, 186, 119, 189))
# print(im.size)
# im.show()
# print(im.size)
# pix = im.load()
# for y in range(im.size[1]):
# 	for x in range(im.size[0]):
# 		print(x, y, pix[x,y])
# print(pix[81, 218])

# read_image("sample3.png")
# print(pix[75,30])
# for y in range(im.size[1]):
# 	for x in range(im.size[0]):
# 		if(pix[x,y][0] > 0):
# 			pix[x,y] = (255,255,255,255)
# im.show()
# text = pytesseract.image_to_string(im)
# print (text + "haha")