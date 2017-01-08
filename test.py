from PIL import Image
import numpy
from pytesseract import *
from imageReader import *
im = Image.open("sample4.tiff")
im = im.convert("L")
im = im.crop((168, 213, 173, 218))
im.show()
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