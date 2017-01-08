import numpy

is_debug_on = True

def read_digit_sequence(arr):
	'''This function reads a list of single digit

	The function scans the pixels column by column to partition digits. Each single digit starts
	with a column containing black pixel and ends with a column containing no black pixel. Then the
	function reads each digit to return the digit represented.

	Args:
	arr (int): The 2D numpy array to represent the pixel values.

	Returns:
	int: The digit represented by the pixel
	-1 for error.
	'''

	if is_debug_on :
		print("\nread_digit_sequence with param:\n")
		# print(arr)
		print("\nsize of param:\n")
		print(arr.shape)

	# Each digit read from the pixels
	result = []

	# The column been scanned right now
	current_column = 0

	# Starting and ending column of a digit, reset to -1 after find a digit
	starting_column = -1
	ending_column = -1

	while(current_column < arr.shape[1]) :
		if is_debug_on :
			print("read_digit_sequence: line 36 , current_column is ", current_column)

		while(starting_column == -1 and current_column < arr.shape[1]) :
			has_one = False
			for i in range(arr.shape[0]):
				if (arr[i][current_column] == 1):
					has_one = True
					break

			if has_one :
				starting_column = current_column

			current_column += 1

		if is_debug_on :
			print("read_digit_sequence: line 51 , current_column is ", current_column)

		while(ending_column == -1 and current_column < arr.shape[1]) :
			has_no_one = True
			for i in range(arr.shape[0]):
				if (arr[i][current_column] == 1):
					has_no_one = False
					break

			if has_no_one :
				ending_column = current_column

			current_column += 1

		if is_debug_on :
			print("read_digit_sequence: line 66 , current_column is ", current_column)

		if (starting_column == -1):
			continue

		if (ending_column == -1):
			ending_column = arr.shape[1] - 1

		temp = numpy.zeros((arr.shape[0], ending_column - starting_column + 1))

		for x in range(arr.shape[0]):
			for y in range(temp.shape[1]):
				temp[x][y] = arr[x][starting_column + y]

		digit = pixel_array_to_digit(temp)

		if (digit == -1) :
			print("Error: pixel_array_to_digit returns -1")
			return -1

		result.append(digit)
		starting_column = -1
		ending_column = -1

	final_result = 0

	if is_debug_on :
		print("read_digit_sequence: adding up final result, count ", len(result))

	for x in range(len(result)):
		if is_debug_on :
			print("adding : ", result[x] * (10 ** (len(result) - x - 1)))
		final_result += result[x] * (10 ** (len(result) - x - 1))

	return final_result

def verify_digit_pixels(arr, digit, left_most_x, left_most_y):
	'''This function verifies whether the digit returned by pixel_array_to_digit is correct.

	The function checks all expected black pixels to verify the reading.If the digit
	read is wrong, return -1

	Args:
	arr(int):The 2D numpy array to represent the pixel values.
	arr[row][column] is the pixel values at that row and column
	digit(int): digit read by pixel pixel_array_to_digit
	left_most_x: row number of left upper most black pixel
	left_most_x: column number of left upper most black pixel

	Returns:
	int: digit if read correctly, else return -1
	'''

	if is_debug_on:
		print("verify_digit_pixels is called with param (arr, digit, left_most_x, left_most_y)")
		print(arr, digit, left_most_x, left_most_y)

	if(digit == 1):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 4][left_most_y + 1] == 1):
			return 1

	if(digit == 2):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y] == 1
		   and arr[left_most_x + 4][left_most_y] == 1
		   and arr[left_most_x + 4][left_most_y + 1] == 1
		   and arr[left_most_x + 4][left_most_y + 2] == 1
		   and arr[left_most_x + 4][left_most_y + 3] == 1):
			return 2

	if(digit == 3):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y + 3] == 1
		   and arr[left_most_x + 4][left_most_y] == 1
		   and arr[left_most_x + 4][left_most_y + 1] == 1
		   and arr[left_most_x + 4][left_most_y + 2] == 1):
			return 3

	if(digit == 4):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 2][left_most_y + 3] == 1
		   and arr[left_most_x + 3][left_most_y + 3] == 1
		   and arr[left_most_x + 4][left_most_y + 3] == 1):
			return 4

	if(digit == 5):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y + 3] == 1
		   and arr[left_most_x + 4][left_most_y] == 1
		   and arr[left_most_x + 4][left_most_y + 1] == 1
		   and arr[left_most_x + 4][left_most_y + 2] == 1):
			return 5

	if(digit == 6):
		if(arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x - 1][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 1][left_most_y + 2] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 3] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1):
			return 6

	if(digit == 7):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 4][left_most_y + 1] == 1):
			return 7

	if(digit == 8):
		if(arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x - 1][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 1][left_most_y + 2] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 3] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1):
			return 8

	if(digit == 9):
		if(arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x - 1][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 1][left_most_y + 2] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y + 3] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1):
			return 9

	if(digit == 0):
		if(arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x - 1][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 3] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1):
			return 0

	# -2 for $
	if(digit == -2):
		if(arr[left_most_x - 2][left_most_y + 2] == 1
		   and arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x - 1][left_most_y + 2] == 1
		   and arr[left_most_x - 1][left_most_y + 3] == 1
		   and arr[left_most_x - 1][left_most_y + 4] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 1][left_most_y + 2] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 2][left_most_y + 4] == 1
		   and arr[left_most_x + 3][left_most_y] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y + 3] == 1
		   and arr[left_most_x + 4][left_most_y + 2] == 1):
			return 0

	return -1

def pixel_array_to_digit(arr):
	'''This function converts pixel array into corresponding digits

	The input is 2d binary array with 1 indicating black pixel and 0 indicating
	background pixel. The function first identifies the left most pixel(using the
	upper pixel if tied). Then the function compares the relative position of black
	pixels to determine the digit the pixels is representing. If the function cannot
	determine the digit, -1 will be returned to indicate error. 
	
	Args:
	arr (int): The 2D numpy array to represent the pixel values.
	arr[row][column] is the pixel values at that row and column
	Returns:
	int: The digit read from the pixels.
		-1 if the digit cannot be determined.
		0 if the digit is $.(for computational convenience)

	Throws:
		IndexError

	'''

	if is_debug_on:
		print("pixel_array_to_digit is called with param (arr)")
		for x in range (arr.shape[0]):
			print(arr[x])

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

	if (left_most_x == -1 or left_most_y == -1):
		print("pixel_array_to_digit cannot find black pixel with arr")
		print(arr)
		return -1

	# Use a decision tree to decide on the digit represented
	# A flow chart is available on https://github.com/greed-is-good/figure_extraction_task

	if (arr[left_most_x][left_most_y + 1] == 0):
		# {0,4,6,8,9,$}
		if (arr[left_most_x + 1][left_most_y] == 0):
			# {8,9,$}
			if (arr[left_most_x + 2][left_most_y] == 1):
				return verify_digit_pixels(arr, 8, left_most_x, left_most_y)
			else :
				# {9,$}
				if (arr[left_most_x][left_most_y + 2] == 0):
					return verify_digit_pixels(arr, 9, left_most_x, left_most_y)
				else :
					# 0 for $
					return verify_digit_pixels(arr, -2, left_most_x, left_most_y)

		else :
			# {0,4,6}
			if (arr[left_most_x][left_most_y + 3] == 0):
				return verify_digit_pixels(arr, 6, left_most_x, left_most_y)
			else :
				# {0,4}
				if(arr[left_most_x + 2][left_most_y + 1] == 0):
					return verify_digit_pixels(arr, 0, left_most_x, left_most_y)
				else :
					return verify_digit_pixels(arr, 4, left_most_x, left_most_y)

	else :
		# {1,2,3,5,7}
		if (arr[left_most_x + 4][left_most_y] == 0):
			# {1,7}
			if (arr[left_most_x + 1][left_most_y + 1] == 0):
				return verify_digit_pixels(arr, 7, left_most_x, left_most_y)
			else :
				return verify_digit_pixels(arr, 1, left_most_x, left_most_y)

		else:
			# {2,3,5}
			if (arr[left_most_x + 1][left_most_y] == 0):
				# {2,3}
				if (arr[left_most_x + 3][left_most_y] == 0):
					return verify_digit_pixels(arr, 3, left_most_x, left_most_y)
				else :
					return verify_digit_pixels(arr, 2, left_most_x, left_most_y)

			else:
				return verify_digit_pixels(arr, 5, left_most_x, left_most_y)






