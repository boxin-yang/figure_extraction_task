from PIL import Image
import numpy
from pytesseract import *
from imageReader import *


im = Image.open("test12.png")
im = im.convert("L")
# im = im.crop((140, 212, 150, 220))
# im.show()
print(im.size)
pix = im.load()
for x in range(800):
	print(x, 221, pix[x, 221])
# for x in range(8):
# 	for y in range(9):
# 		print(x, y, pix[y,x])

# try:
# 	list = []
# 	list[5] = 1
# except IndexError:
# 	print("exception caught")


# im = Image.open("test2.png")

# im = im.convert("L")
# # print(pix[187, 114])
# # print(pix[187, 115])

# im = im.crop((170, 200, 180, 210))
# im.show()
# pix = im.load()
# for x in range(9):
# 	for y in range(5):
# 		print(x, y, pix[y,x])

# im = Image.open("test2.png")

# im = im.convert("L")
# # # print(pix[187, 114])
# # # print(pix[187, 115])

# im = im.crop((165, 190, 171, 210))
# pix = im.load()
# for x in range(19):
# 	for y in range(5):
# 		print(x, y, pix[y,x])
# # print(im.size)
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
