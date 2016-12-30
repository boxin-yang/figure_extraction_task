from PIL import Image
import numpy
from pytesseract import *
from imageReader import *
im = Image.open("sample3.png")
im = im.convert("L")
# im = im.crop((79, 210, 83, 219))
# im.show()
# pix = im.load()
# print(pix[81, 217])
# print(pix[81, 218])

read_image("sample3.png")
# print(pix[75,30])
# for y in range(im.size[1]):
# 	for x in range(im.size[0]):
# 		if(pix[x,y][0] > 0):
# 			pix[x,y] = (255,255,255,255)
# im.show()
# text = pytesseract.image_to_string(im)
# print (text + "haha")