# figure_extraction_task

## Requirements

- Python 2 (2.7.9 is used for development)
- TODO: Find a suitable DB

## Overview

The task is to extract values from the graph plot in png files. The data is given by many folders, each name following the pattern project_*.
Inside each folder, two pictures named ~_dailybackers.png and ~_dailypledges.png are to be extracted.
For each plot, the horizontal axis specifies the date and there is one column for each date. Each column is tagged with a number and the task is to extract those numbers and store them into the database.

## Algorithms to extract number

As current library on the Internet cannot properly extract figures for this task, we have to devise an algorithm to extract numbers. Taking the following backers graph for illustration purposes.

![My image](https://raw.githubusercontent.com/greed-is-good/image/master/2912609_dailybackers.png)

	1. Identify the number of columns(days) and their positions in the graph
		1.1 Uses the vertical short line beneath the horizontal axis to identify all the columns(Using dashed grid in the graph may be troublesome as some cloumns cover the entire vertical dashed grid) 
		1.2 Read one date figure below horizontal axis and find its relative position to the columns to find the mapping between date and column

	2. For each column, idenfity the position of the data figure. For example, in the graph shown above, on date 10-22 the Backers on that day is 2 and that figure is in the middle of the column.
		2.1 First identify the height of the column by finding out where is the top edge of the column. The column might be above or below the horizontal axis and there might not be a column is the number is 0.
		2.2 After idenfitying the edge of the column, find the position of the data figure. The position of the figure can be in the middle of the column, above the edge of the column, below the edge of the column.
		2.3 Find the data figure and extract the pixels.

	3. After obtaining the pixels for figure extraction, use external library to read the image. Currently will test out PyTesser and OCROPUS. If both are not working well, will consider Machine learning library such as Tensorflow.

## Database

There will be two tables for this task.One will record whether a project folder has been successfully processed while the other record the becker and pledges.
TODO: find out proper Database(PostgreSQL or SQLite)
TODO: draw EM diagram for two tables

## Contributors:
- @boxin (a0107354@u.nus.edu)