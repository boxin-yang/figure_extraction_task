# figure_extraction_task

## Requirements

- Python 2 (2.7.9 is used for development)
- TODO: Find a suitable DB

## Overview

The task is to extract values from the graph plot in png files. The data is given as many folders, each name following the pattern project_* .
Inside each folder, two pictures named ~_dailybackers.png and ~_dailypledges.png are to be extracted.
For each plot, there are many coloums of data. Each column is tagged with a number and the task is to extract those numbers and store them into the database.

## Algorithms to extract number

This task is highly specialized to extract graph plots of similar format. The algorithm for obtaining data is described below with reference to the graph.
![My image](https://raw.githubusercontent.com/greed-is-good/image/master/2912609_dailybackers.png)

	1. Identify the position of horizontal axis and vertical axis.
		1.1 Traverse the middle row of pixels from left
		1.2 Once encounter a black pixel, test the column whether it is the vertical axis. If not, keep traversing and report error if failed to locate vertical axis.
		1.3 Traverse the middle column of pixels from bottom and identify the horizontal axis similar to 1.2

	2. Identify position of each column in the graph by scannning the pixels below horizontal axis. There is a short vertical line beneath each column in the graph.

	3. For each column, idenfity the position of the data figure. For example, in the graph shown above, on date 10-22 the Backers on that day is 2 and that figure is in the middle of the column.
		2.1 First identify the height of the column by finding out where is the top edge of the column. The column might be above or below the horizontal axis and there might not be a column if the number is 0.
		2.2 After idenfitying the edge of the column, find the position of the data figure. The position of the figure can be in the middle of the column, above the edge of the column, below the edge of the column.
		2.3 Find the data figure and extract the pixels.

	3. After obtaining the data pixels, use digit extraction algorithm to read the number.

## Digit Extraction Algorithm

As all the numbers are printed within 5 * 5 pixels square with fixed shape, we can analyse the pixels to identify the digits.

The first job is to crop out each digit and runs the extraction algorithm on each of them. The end of a digit is identified as a non-black column.(If a vertical pixel column is all non-black, the column marks the end of a digit)

For each digit, we can identify them by looking at its pixel orientation. The pixels are considered to be binary(black pixel and non-black pixel)


![My image](https://raw.githubusercontent.com/greed-is-good/image/master/0.png)
![My image](https://raw.githubusercontent.com/greed-is-good/image/master/1.png)
![My image](https://raw.githubusercontent.com/greed-is-good/image/master/2.png)
![My image](https://raw.githubusercontent.com/greed-is-good/image/master/3.png)
![My image](https://raw.githubusercontent.com/greed-is-good/image/master/4.png)
![My image](https://raw.githubusercontent.com/greed-is-good/image/master/5.png)
![My image](https://raw.githubusercontent.com/greed-is-good/image/master/6.png)
![My image](https://raw.githubusercontent.com/greed-is-good/image/master/7.png)
![My image](https://raw.githubusercontent.com/greed-is-good/image/master/8.png)
![My image](https://raw.githubusercontent.com/greed-is-good/image/master/9.png)


We first identify the left upper most black pixel by traversing the pixels. Then identify the digit represented by following flow chart. [x][y] is the most left upper black pixel. 1 represents black pixel and 0 represents non-black pixel.
![My image](https://raw.githubusercontent.com/greed-is-good/image/master/Flow_chart.png)

TODO: After identifying the digit, we might test more pixels to ensure we have correctly identify the digit.

## Database

There will be two tables for this task.One will record whether a project folder has been successfully processed while the other record the becker and pledges.
TODO: find out proper Database(PostgreSQL or SQLite)
TODO: draw EM diagram for two tables

## Contributors:
- @boxin (a0107354@u.nus.edu)