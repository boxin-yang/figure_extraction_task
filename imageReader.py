import numpy
from PIL import Image

is_debug_on = True

def read_image(image_name):
	'''This function reads a graph plot.

	'''

	if is_debug_on:
		print("read_image is called with file name ", image_name)

	im = Image.open(image_name)
	im = im.convert("L")

	pixels = im.load()

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

		if (black_pixel_count > 55) :
			# found the axis
			vertical_axis = current_column
		else :
			current_column += 1
	if is_debug_on:
		print("vertical axis is at ", vertical_axis)

	# scan for horizontal axis
	current_row = im.size[1] - 1
	horizontal_axis = -1

	while(current_row >0 and horizontal_axis == -1):
		if (pixels[middle_coloum, current_row] != 0) :
			current_row -= 1
			continue

		black_pixel_count = 0
		for x in range(-30, 30):
			if (pixels[middle_coloum + x, current_row] == 0):
				black_pixel_count += 1

		if (black_pixel_count > 55) :
			# found the axis
			horizontal_axis = current_row
		else :
			current_row -= 1
	
	if is_debug_on:
		print("horizontal axis is at ", horizontal_axis)


	# scan for all columns
	current_column = vertical_axis

	graph_columns = []
	
	while (current_column < im.size[0]):
		if(pixels[current_column, horizontal_axis + 1] == 0):
			graph_columns.append(current_column)

		current_column += 1
	
	if is_debug_on:
		print("found following columns in the graph ", len(graph_columns))

	if (len(graph_columns) > 1):
		column_distance = graph_columns[1] - graph_columns[0] 
	else :
		column_distance = graph_columns[0] - vertical_axis
	
	graph_data = []

	for x in graph_columns:
		data = read_column(x, column_distance, horizontal_axis, pixels)
		graph_data.append(data)

	if is_debug_on:
		print("Data read for each column is (column, data)")
		for x in range (len(graph_data)):
			print(x, graph_data[x])


def read_column(col, column_distance, horizontal_axis, pixels):
	'''This function reads the data of the column
	'''
	if is_debug_on:
		print("read_column called with param", col, column_distance, horizontal_axis)
	curr_row = horizontal_axis - 1
	first_black_pixel = -1

	while (curr_row > 0):
		if (pixels[col, curr_row] != 0):
			curr_row -= 1
		else :
			first_black_pixel = curr_row
			break

	if is_debug_on:
		print("read_column: first_black_pixel found is at row", first_black_pixel)

	# from this first black pixel find the crop that 
	upper = -1
	lower = -1
	left = -1
	right = -1

	# find upper
	curr_row = first_black_pixel
	while (curr_row > 0) :
		if(pixels[col, curr_row] == 0):
			curr_row -= 1
			continue

		# If the row has more black pixel, not finished yet
		if (pixels[col - 4, curr_row] == 0
			or pixels[col - 3, curr_row] == 0
			or pixels[col - 2, curr_row] == 0
			or pixels[col - 1, curr_row] == 0
			or pixels[col + 1, curr_row] == 0
			or pixels[col + 2, curr_row] == 0
			or pixels[col + 3, curr_row] == 0
			or pixels[col + 3, curr_row] == 0
			):
			curr_row -= 1
			continue

		# If the column has more black pixel, not finished yet
		if (pixels[col, curr_row - 1] == 0
			or pixels[col, curr_row - 2] == 0
			or pixels[col, curr_row - 3] == 0
			or pixels[col, curr_row - 4] == 0
			or pixels[col, curr_row - 5] == 0):
			curr_row -= 1
			continue

		upper = curr_row
		# print("upper ", upper)
		break

	# find lower
	curr_row = first_black_pixel + 1
	while (curr_row < horizontal_axis) :
		if(pixels[col, curr_row] == 0):
			curr_row += 1
			continue

		# If the row has more black pixel, not finished yet
		if (pixels[col - 4, curr_row] == 0
			or pixels[col - 3, curr_row] == 0
			or pixels[col - 2, curr_row] == 0
			or pixels[col - 1, curr_row] == 0
			or pixels[col + 1, curr_row] == 0
			or pixels[col + 2, curr_row] == 0
			or pixels[col + 3, curr_row] == 0
			or pixels[col + 3, curr_row] == 0
			):
			curr_row += 1
			continue

		# Do not check for more columns as first black pixel is close to horizontal axis
		# Alternatively, we can take horizontal aixs as lower
		lower = curr_row
		# print("lower ", lower)
		break

	middle = (upper + lower) / 2
	
	# find left
	curr_column = col - 1
	while (col - curr_column < (column_distance / 2)) :
		# use 3 points for efficient testing
		if(pixels[curr_column, upper] == 0
		   or pixels[curr_column, lower] == 0
		   or pixels[curr_column, middle] == 0):
			curr_row -= 1
			continue

		has_no_black_pixel = True
		for x in range(3):
			if not has_no_black_pixel:
				break
			for y in range(upper, lower + 1):
				if (pixels[curr_column - x, y] == 0):
					has_no_black_pixel == False
					break
				
		if has_no_black_pixel:
			left = curr_column
			break
		else:
			curr_column -= 1
	
	print("left", left)
	
	# find right
	curr_column = col + 1
	while (curr_column - col < (column_distance / 2)) :
		# use 3 points for efficient testing
		if(pixels[curr_column, upper] == 0
		   or pixels[curr_column, lower] == 0
		   or pixels[curr_column, middle] == 0):
			curr_row += 1
			continue

		has_no_black_pixel = True
		for x in range(3):
			if not has_no_black_pixel:
				break
			for y in range(upper, lower + 1):
				if (pixels[curr_column + x, y] == 0):
					has_no_black_pixel == False
					break
				
		if has_no_black_pixel:
			left = curr_column
			break
		else:
			curr_column += 1

	if is_debug_on:
		print("read_column finds the crop (left, upper, right, lower)",left, upper, right, lower)
	return 0









