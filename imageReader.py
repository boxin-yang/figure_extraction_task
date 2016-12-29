import numpy

is_debug_on = False

def read_image(image_name):
	'''This function reads a graph plot.

	'''
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

	print("vertical axis is at ", vertical_axis)





