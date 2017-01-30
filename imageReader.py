import numpy
from PIL import Image
from digitReader import read_digit_sequence

is_debug_on = True
error_return = -100000

def is_a_digit_pixel(black_pixel_value, val):
	if (black_pixel_value == 0):
		return val == 0
	else :
		return val <= 114

def is_a_horizontal_axis_pixel(val):
	return (val == 0) or (val == 11) or (val == 20)

def is_a_pixel_to_indicate_column_under_horizontal_axis(val):
	return (val == 0) or (val == 9)

def read_image(image_name):
	'''This function reads a graph plot.

	'''
	
	# Load the image
	im = Image.open(image_name)
	im = im.convert("L")
	pixels = im.load()
	
	if is_debug_on:
		print("read_image is called with file name ", image_name)
		print("dimension", im.size)

	middle_coloum = im.size[0] / 2
	middle_row = im.size[1] / 2

	# scan for vertical axis
	current_column = 0
	vertical_axis = -1

	while(current_column < im.size[0] and vertical_axis == -1):
		if (pixels[current_column, middle_row] != 0) :
			current_column += 1
			continue

		black_pixel_count = 0
		for x in range(-30, 30):
			if (pixels[current_column, middle_row + x] == 0):
				black_pixel_count += 1

		if (black_pixel_count > 50) :
			# found the axis
			vertical_axis = current_column
		else :
			current_column += 1
	
	if is_debug_on:
		print("vertical axis is at ", vertical_axis)

	# scan for horizontal axis
	current_row = im.size[1] - 1
	horizontal_axis = -1

	while(current_row > 0 and horizontal_axis == -1):
		if not is_a_horizontal_axis_pixel(pixels[middle_coloum, current_row]) :
			current_row -= 1
			continue

		black_pixel_count = 0
		for x in range(-30, 30):
			if is_a_horizontal_axis_pixel(pixels[middle_coloum + x, current_row]):
				black_pixel_count += 1

		if (black_pixel_count > 50) :
			# found the axis
			horizontal_axis = current_row
		else :
			current_row -= 1
	
	if is_debug_on:
		print("horizontal axis is at ", horizontal_axis)


	if (vertical_axis == -1 or horizontal_axis == -1):
		print("Error: cannot find axis")
		return
	# scan for all columns in the graph
	# this is done by scanning the pixel row below horizontal axis
	current_column = vertical_axis

	graph_columns = []
	
	while (current_column < im.size[0]):
		if is_a_pixel_to_indicate_column_under_horizontal_axis(pixels[current_column, horizontal_axis + 1]):
			graph_columns.append(current_column)

		current_column += 1
	
	if is_debug_on:
		print("found following number of columns in the graph ", len(graph_columns))

	# column_distance is used in read_column to avoid unexpected reading beyond column
	if (len(graph_columns) > 1):
		column_distance = graph_columns[1] - graph_columns[0] 
	else :
		column_distance = graph_columns[0] - vertical_axis
	
	if is_debug_on:
		print(graph_columns)
		print("column distance is", column_distance)
	
	graph_data = []
	
	has_error = False
	pos = 0

	for x in graph_columns:
		if is_debug_on:
			pos += 1
			print("Now read column", pos)
		data = read_column(x, column_distance, horizontal_axis, vertical_axis, pixels)
		graph_data.append(data)
		if (data == error_return) :
			has_error = True

	if has_error:
		print("Error: pixel_array_to_digit returns error_return")
	
	if is_debug_on :
		print(image_name, "Data read for each column is (column, data)")
		for x in range (len(graph_data)):
			print(x + 1, graph_data[x])

	return graph_data

def read_column(col, column_distance, horizontal_axis, vertical_axis, pixels):
	'''This function reads the data of the column in the graph

	Found out that digits might be printed in grey with L value 104 or 114
	'''
	if is_debug_on:
		print("read_column called with param: col, column_distance, horizontal_axis, vertical_axis", col, column_distance, horizontal_axis, vertical_axis)
	
	# Find the first black pixel above the vertical axis
	# Start searching 3 pixels above the axis to avoid searching axis label
	# search black pixels first
	curr_row = horizontal_axis - 3
	first_black_pixel = -1
	black_pixel_value = -1

	while (curr_row > 50):
		if (pixels[col, curr_row] != 0):
			curr_row -= 1
		else :
			first_black_pixel = curr_row
			break

	# Check +1 -1 column for black pixel
	if first_black_pixel == -1:
		curr_row = horizontal_axis - 1

		while(curr_row > 50):
			if ((pixels[col - 1, curr_row] != 0) and (pixels[col + 1, curr_row] != 0)):
				curr_row -= 1
			else :
				first_black_pixel = curr_row
				break

	if (first_black_pixel != -1):
		black_pixel_value = 0
	else:
		# if no black pixels are found
		curr_row = horizontal_axis - 3

		# check for grey pixel
		while (curr_row > 50):
			if (pixels[col, curr_row] > 114):
				curr_row -= 1
			else :
				first_black_pixel = curr_row
				black_pixel_value = pixels[col, curr_row]
				break

		# Check +1 -1 column for grey pixel, else return 0 as 0 is not printed in some graphs
		if first_black_pixel == -1:
			curr_row = horizontal_axis - 1

			while(curr_row > 50):
				if ((pixels[col - 1, curr_row] > 114) and (pixels[col + 1, curr_row] > 114)):
					curr_row -= 1
				else :
					first_black_pixel = curr_row
					black_pixel_value = min(pixels[col - 1, curr_row], pixels[col + 1, curr_row])
					break

	# if no dark pixels detected
	if (first_black_pixel == -1):
		return 0
	
	if is_debug_on:
		print("read_column: first_black_pixel found is at row", first_black_pixel, "black pixel value is", black_pixel_value)

	# from this first black pixel find the crop that contains the digit
	upper = -1
	lower = -1
	left = -1
	right = -1

	# Some axis has unwanted black pixels above horizontal axis(e.g. sample4.tiff)
	need_to_prune_pixels_above_horizontal_axis = False

	# if first black pixel is close to horizontal axis, just take horizontal_axis - 1 as the lower bound
	if (horizontal_axis - first_black_pixel < 10):
		lower = horizontal_axis - 1

		# bizzare behavior in test9.png, where a black pixel is 2 rows above the horizontal axis
		if (pixels[col, horizontal_axis - 2] == 0
		    and not (is_a_digit_pixel(black_pixel_value, pixels[col - 1, horizontal_axis - 2])
		      or is_a_digit_pixel(black_pixel_value, pixels[col + 1, horizontal_axis - 2])
		      or is_a_digit_pixel(black_pixel_value, pixels[col - 1, horizontal_axis - 3])
		      or is_a_digit_pixel(black_pixel_value, pixels[col, horizontal_axis - 3])
		      or is_a_digit_pixel(black_pixel_value, pixels[col + 1, horizontal_axis - 3])
		      or is_a_digit_pixel(black_pixel_value, pixels[col + 1, horizontal_axis - 3]))):
			need_to_prune_pixels_above_horizontal_axis = True
			if is_debug_on:
				print("Need to prune pixels above horizontal axis")

	# find upper
	curr_row = first_black_pixel
	while (curr_row > 0) :
		if is_a_digit_pixel(black_pixel_value, pixels[col, curr_row]):
			curr_row -= 1
			continue

		# If the row has more black pixel, not finished yet
		# checking for first column is partial to avoid touching vertical axis
		if (col - vertical_axis < column_distance) :
			if (is_a_digit_pixel(black_pixel_value, pixels[col + 1, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 2, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 3, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 4, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 5, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 6, curr_row])):
				curr_row -= 1
				continue
		else:
			if (is_a_digit_pixel(black_pixel_value, pixels[col - 6, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col - 5, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col - 4, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col - 3, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col - 2, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col - 1, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 1, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 2, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 3, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 4, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 5, curr_row])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 6, curr_row])):
				curr_row -= 1
				continue

		# If the column has more black pixel, not finished yet
		if (is_a_digit_pixel(black_pixel_value, pixels[col, curr_row - 1])
			or is_a_digit_pixel(black_pixel_value, pixels[col, curr_row - 2])
			or is_a_digit_pixel(black_pixel_value, pixels[col, curr_row - 3])
			or is_a_digit_pixel(black_pixel_value, pixels[col, curr_row - 4])
			or is_a_digit_pixel(black_pixel_value, pixels[col, curr_row - 5])
			or is_a_digit_pixel(black_pixel_value, pixels[col + 1, curr_row - 1])
			or is_a_digit_pixel(black_pixel_value, pixels[col + 2, curr_row - 1])
			or is_a_digit_pixel(black_pixel_value, pixels[col - 1, curr_row - 1])
			or is_a_digit_pixel(black_pixel_value, pixels[col - 2, curr_row - 1])
			or is_a_digit_pixel(black_pixel_value, pixels[col + 1, curr_row - 2])
			or is_a_digit_pixel(black_pixel_value, pixels[col + 2, curr_row - 2])
			or is_a_digit_pixel(black_pixel_value, pixels[col - 1, curr_row - 2])
			or is_a_digit_pixel(black_pixel_value, pixels[col - 2, curr_row - 2])):
			curr_row -= 1
			continue

		upper = curr_row
		break

	# find lower
	if lower == -1 :
		curr_row = first_black_pixel + 1
		while (curr_row < horizontal_axis) :
			# print("curr_row", curr_row)
			if(is_a_digit_pixel(black_pixel_value, pixels[col, curr_row])):
				curr_row += 1
				continue

			if (col - vertical_axis < column_distance) :
				if (is_a_digit_pixel(black_pixel_value, pixels[col + 1, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col + 2, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col + 3, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col + 4, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col + 5, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col + 6, curr_row])):
					curr_row += 1
					continue
			else:
				if (is_a_digit_pixel(black_pixel_value, pixels[col - 6, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col - 5, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col - 4, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col - 3, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col - 2, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col - 1, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col + 1, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col + 2, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col + 3, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col + 4, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col + 5, curr_row])
					or is_a_digit_pixel(black_pixel_value, pixels[col + 6, curr_row])):
					curr_row += 1
					continue
			
			# If the column has more black pixel, not finished yet
			if (is_a_digit_pixel(black_pixel_value, pixels[col, curr_row + 1])
				or is_a_digit_pixel(black_pixel_value, pixels[col, curr_row + 2])
				or is_a_digit_pixel(black_pixel_value, pixels[col, curr_row + 3])
				or is_a_digit_pixel(black_pixel_value, pixels[col, curr_row + 4])
				or is_a_digit_pixel(black_pixel_value, pixels[col, curr_row + 5])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 1, curr_row + 1])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 2, curr_row + 1])
				or is_a_digit_pixel(black_pixel_value, pixels[col - 1, curr_row + 1])
				or is_a_digit_pixel(black_pixel_value, pixels[col - 2, curr_row + 1])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 1, curr_row + 2])
				or is_a_digit_pixel(black_pixel_value, pixels[col + 2, curr_row + 2])
				or is_a_digit_pixel(black_pixel_value, pixels[col - 1, curr_row + 2])
				or is_a_digit_pixel(black_pixel_value, pixels[col - 2, curr_row + 2])):
				curr_row += 1
				continue

			lower = curr_row
			break
	
	if (lower == -1):
		if is_debug_on:
			print("lower reading is -1")
		return error_return

	middle = (upper + lower) / 2
	if is_debug_on:
		print("read_column upper, lower, middle", upper, lower, middle)

	# find left
	if (col - vertical_axis < column_distance):
		left = vertical_axis + 3
	else :
		curr_column = col - 1
		while (col - curr_column < column_distance) :
			# use 3 points for efficient testing
			if(is_a_digit_pixel(black_pixel_value, pixels[curr_column, upper + 1])
			   or is_a_digit_pixel(black_pixel_value, pixels[curr_column, lower - 1])
			   or is_a_digit_pixel(black_pixel_value, pixels[curr_column, middle])):
				curr_column -= 1
				continue

			has_no_black_pixel = True
			for x in range(3):
				if not has_no_black_pixel:
					break
				for y in range(upper, lower + 1):
					if (is_a_digit_pixel(black_pixel_value, pixels[curr_column - x, y])):
						has_no_black_pixel = False
						break
					
			if has_no_black_pixel:
				left = curr_column
				break
			else:
				curr_column -= 1
		
	# find right
	curr_column = col + 1
	while (curr_column - col < column_distance) :
		# use 3 points for efficient testing
		if(is_a_digit_pixel(black_pixel_value, pixels[curr_column, upper + 1])
		   or is_a_digit_pixel(black_pixel_value, pixels[curr_column, lower - 1])
		   or is_a_digit_pixel(black_pixel_value, pixels[curr_column, middle])):
			curr_column += 1
			continue

		has_no_black_pixel = True
		for x in range(3):
			if not has_no_black_pixel:
				break
			for y in range(upper, lower + 1):
				if (is_a_digit_pixel(black_pixel_value, pixels[curr_column + x, y])):
					has_no_black_pixel = False
					break
				
		if has_no_black_pixel:
			right = curr_column
			break
		else:
			curr_column += 1
	
	if is_debug_on:
		print("read_column finds the crop (left, upper, right, lower)",left, upper, right, lower)

	if (left == -1 or right == -1):
		return error_return

	# if cropping goes to another column, high chance of reading overlap
	if (col - left >= column_distance or right - col >= column_distance):
		print("Error: reading overlaps with another column")
		return error_return
	
	pixels_arr = numpy.zeros((lower - upper + 1, right - left + 1))

	for x in range (pixels_arr.shape[0]):
		for y in range(pixels_arr.shape[1]):
			if(is_a_digit_pixel(black_pixel_value, pixels[left + y,upper + x])):
				pixels_arr[x][y] = 1

	if need_to_prune_pixels_above_horizontal_axis:
		# if this flag is on, lower = horizontal_axis - 1
		pixels_arr[pixels_arr.shape[0] - 1][col - left] = 0
		pixels_arr[pixels_arr.shape[0] - 2][col - left] = 0

	try_with_original_pixel = read_digit_sequence(pixels_arr)
	
	if(try_with_original_pixel !=error_return):
		return try_with_original_pixel

	# If the current orientation returns invalid value, rotate the digit and read again
	# Number could be in upright or rotated position in the graph
	pixels_arr_rotate = numpy.zeros((pixels_arr.shape[1], pixels_arr.shape[0]))

	height = pixels_arr.shape[0] - 1

	for x in range (pixels_arr.shape[0]):
		for y in range(pixels_arr.shape[1]):
			if(pixels_arr[x][y] == 1):
				pixels_arr_rotate[y][height - x] = 1
	
	try_with_rotated_pixel = read_digit_sequence(pixels_arr_rotate)
	return try_with_rotated_pixel









