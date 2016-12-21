import numpy

def partition_into_single_digit(arr):
	'''This function partition a sequence of digits into a list of single digit
	Args:
	arr (int): The 2D numpy array to represent the pixel values.

	Returns:
	int: The digit represented by the pixel
	'''
def pixel_array_to_digit(arr):
	'''This function converts pixel array into corresponding digits

	The input is 2d binary array with 1 indicating black pixel and 0 indicating
	background pixel. The function first identifies the left most pixel(using the
	upper pixel if tied). Then the function compares the relative position of black
	pixels to determine the digit the pixels is representing. If the function cannot
	determine the digit, -1 will be returned to indicate error. 
	
	Args:
	arr (int): The 2D numpy array to represent the pixel values.

	Returns:
	int: The digit read from the pixels.
		-1 if the digit cannot be determined.
		-2 if the digit is $.

	Throws:
		IndexError

	'''

	# A valid pixel has at least 5 rows, 2 coloums
	if (arr.shape[1] < 5 or arr.shape[0] < 2) :
		print("pixel_array_to_digit with param ", arr, ": invalid input dimensions")
		return -1

	left_most_x = -1;
	left_most_y = -1;

	# Traverse the array to find the left upper most pixel
	for y in range(arr.shape[1]):
		for x in range(arr.shape[0]):
			if(arr[x][y] == 1):
				left_most_x = x
				left_most_y = y

			if left_most_x != -1:
				break
	
		if left_most_y != -1:
			break

	# Use a decision tree to decide on the digit represented
	# A flow chart is available on https://github.com/greed-is-good/figure_extraction_task

	if (arr[left_most_x][left_most_y + 1] == 0):
		# {0,4,6,8,9,$}
		if (arr[left_most_x + 1][left_most_y] == 0):
			# {8,9,$}
			if (arr[left_most_x + 2][left_most_y] == 1):
				return 8
			else :
				# {9,$}
				if (arr[left_most_x][left_most_y + 2] == 0):
					return 9
				else :
					# -2 for $
					return -2

		else :
			# {0,4,6}
			if (arr[left_most_x][left_most_y + 3] == 0):
				return 6
			else :
				# {0,4}
				if(arr[left_most_x + 2][left_most_y + 1] == 0):
					return 0
				else :
					return 4

	else :
		# {1,2,3,5,7}
		if (arr[left_most_x + 4][left_most_y] == 0):
			# {1,7}
			if (arr[left_most_x + 1][left_most_y + 1] == 0):
				return 7
			else :
				return 1

		else:
			# {2,3,5}
			if (arr[left_most_x + 1][left_most_y] == 0):
				# {2,3}
				if (arr[left_most_x + 3][left_most_y] == 0):
					return 3
				else :
					return 2

			else:
				return 5






