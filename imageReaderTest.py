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
		
		im2_reading = read_image("sample2.png")
		expected_reading_im2 = [2, 30, 7, 6, 33, 13, 4, 6, 8, 6, 11, 3, 13, 7, 4, 8, 10, 7, 9, 2, 9, 4, 7, 3, 6, 7, 1, 2, 1, 1, 7, 5, 2, 4, 2, 10, 8, 5, 4, 8, 3, 10, 7, 7, 7, 12, 7, 10, 6, 6, 2, 2, 4, 6, 10, 21, 6, 6, 14, 57, 22]
		self.assertEqual(im2_reading, expected_reading_im2)

		im3_reading = read_image("sample3.png")
		expected_reading_im3 = [0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.assertEqual(im3_reading, expected_reading_im3)

		im4_reading = read_image("sample4.tiff")
		expected_reading_im4 = [49, 199, 136, -22, 32, 42, 56, 2, 0, 0, 0, 10, 5, 0, 0, -27, 0, 10, 10, 0, 0, 0, 0, 100, 361, 172, 10, 10, 162, 123, 70]
		self.assertEqual(im4_reading, expected_reading_im4)

if __name__ == '__main__':
	unittest.main()

