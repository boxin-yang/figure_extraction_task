from PIL import Image
import numpy as np
from digitReader import pixel_array_to_digit
import unittest
"""
	This class test pixel_array_to_digit in digitReader
"""

class digitReaderTest(unittest.TestCase):

	def test_digit_0(self):
		fileName = "0.png"
		expectedValue = 0

		im = Image.open(fileName)
		im = im.convert("L")
		pixel = im.load()

		binary_pixel = np.zeros((im.size[0],im.size[1]))

		for y in range(im.size[1]):
			for x in range(im.size[0]):
				if (pixel[x,y] == 0) :
					binary_pixel[y][x] = 1

		result = pixel_array_to_digit(binary_pixel)
		self.assertEqual(result, expectedValue)	

	def test_digit_1(self):
		fileName = "1.png"
		expectedValue = 1

		im = Image.open(fileName)
		im = im.convert("L")
		pixel = im.load()

		binary_pixel = np.zeros((im.size[0],im.size[1]))

		for y in range(im.size[1]):
			for x in range(im.size[0]):
				if (pixel[x,y] == 0) :
					binary_pixel[y][x] = 1

		result = pixel_array_to_digit(binary_pixel)
		self.assertEqual(result, expectedValue)	

	def test_digit_2(self):
		fileName = "2.png"
		expectedValue = 2

		im = Image.open(fileName)
		im = im.convert("L")
		pixel = im.load()

		binary_pixel = np.zeros((im.size[0],im.size[1]))

		for y in range(im.size[1]):
			for x in range(im.size[0]):
				if (pixel[x,y] == 0) :
					binary_pixel[y][x] = 1

		result = pixel_array_to_digit(binary_pixel)
		self.assertEqual(result, expectedValue)	
	
	def test_digit_3(self):
		fileName = "3.png"
		expectedValue = 3

		im = Image.open(fileName)
		im = im.convert("L")
		pixel = im.load()

		binary_pixel = np.zeros((im.size[0],im.size[1]))

		for y in range(im.size[1]):
			for x in range(im.size[0]):
				if (pixel[x,y] == 0) :
					binary_pixel[y][x] = 1

		result = pixel_array_to_digit(binary_pixel)
		self.assertEqual(result, expectedValue)	
	
	def test_digit_4(self):
		fileName = "4.png"
		expectedValue = 4

		im = Image.open(fileName)
		im = im.convert("L")
		pixel = im.load()

		binary_pixel = np.zeros((im.size[0],im.size[1]))

		for y in range(im.size[1]):
			for x in range(im.size[0]):
				if (pixel[x,y] == 0) :
					binary_pixel[y][x] = 1

		result = pixel_array_to_digit(binary_pixel)
		self.assertEqual(result, expectedValue)	
	
	def test_digit_5(self):
		fileName = "5.png"
		expectedValue = 5

		im = Image.open(fileName)
		im = im.convert("L")
		pixel = im.load()

		binary_pixel = np.zeros((im.size[0],im.size[1]))

		for y in range(im.size[1]):
			for x in range(im.size[0]):
				if (pixel[x,y] == 0) :
					binary_pixel[y][x] = 1

		result = pixel_array_to_digit(binary_pixel)
		self.assertEqual(result, expectedValue)	
	
	def test_digit_6(self):
		fileName = "6.png"
		expectedValue = 6

		im = Image.open(fileName)
		im = im.convert("L")
		pixel = im.load()

		binary_pixel = np.zeros((im.size[0],im.size[1]))

		for y in range(im.size[1]):
			for x in range(im.size[0]):
				if (pixel[x,y] == 0) :
					binary_pixel[y][x] = 1

		result = pixel_array_to_digit(binary_pixel)
		self.assertEqual(result, expectedValue)	
	
	def test_digit_7(self):
		fileName = "7.png"
		expectedValue = 7

		im = Image.open(fileName)
		im = im.convert("L")
		pixel = im.load()

		binary_pixel = np.zeros((im.size[0],im.size[1]))

		for y in range(im.size[1]):
			for x in range(im.size[0]):
				if (pixel[x,y] == 0) :
					binary_pixel[y][x] = 1

		result = pixel_array_to_digit(binary_pixel)
		self.assertEqual(result, expectedValue)	
	
	def test_digit_8(self):
		fileName = "8.png"
		expectedValue = 8

		im = Image.open(fileName)
		im = im.convert("L")
		pixel = im.load()

		binary_pixel = np.zeros((im.size[0],im.size[1]))

		for y in range(im.size[1]):
			for x in range(im.size[0]):
				if (pixel[x,y] == 0) :
					binary_pixel[y][x] = 1

		result = pixel_array_to_digit(binary_pixel)
		self.assertEqual(result, expectedValue)	
	
	def test_digit_9(self):
		fileName = "9.png"
		expectedValue = 9

		im = Image.open(fileName)
		im = im.convert("L")
		pixel = im.load()

		binary_pixel = np.zeros((im.size[0],im.size[1]))

		for y in range(im.size[1]):
			for x in range(im.size[0]):
				if (pixel[x,y] == 0) :
					binary_pixel[y][x] = 1

		result = pixel_array_to_digit(binary_pixel)
		self.assertEqual(result, expectedValue)	

if __name__ == '__main__':
	unittest.main()

