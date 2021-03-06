#!/usr/bin/env python 
"""
This is an application built to import a data file, 
average and return a specific value.
"""
import csv
from sys import argv


def process(filename):
	"""Returns the average value from the last column of filename"""
	with open(filename, 'r', 1) as f:
		total = 0.0
		number_of_lines = 0

		#skip the first two lines
		f.readline()			
		f.readline()

		column = []
		
		#split by pipes, and take out whitespace
		for row in csv.reader(f, delimiter='|', skipinitialspace=True):   
			data = row[-1]
			try:
				data = float(data)

			#Notify if data error
			except ValueError as err: 
				print(err)
			
			else:
				if data != -999999999:
					total += data
					number_of_lines+= 1

	return total/number_of_lines

if __name__ == '__main__': 
	del argv[0]
	if not argv:
		print("Error: need filename arg")
	else:
		filename = argv[0]
		print process(filename)


