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
		read_image("sample1.png")
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

