from PIL import Image
import numpy as np
from imageReader import *
import unittest
"""
	This class test imageReader
"""

class imageReaderTest(unittest.TestCase):

	# Test read_digit_sequence
	def test_read_axis(self):
		im1_reading = read_image("sample1.png")
		expected_reading_im1 = [2, 1, 0, 1, 1, 1, 0, 2, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 3, 0]
		self.assertEqual(im1_reading, expected_reading_im1)
		

		# read_image("sample2.png")
		# read_image("sample3.png")
		# read_image("sample4.png")

		# im = Image.open("sample3.png")
		# print(im.size)
		# Test column 75
		# im = im.crop((70, 0 , 80, 400))
		# im.show()

		# Test row 220
		# im = im.crop((70, 210 , 180, 230))
		# im.show()
if __name__ == '__main__':
	unittest.main()

