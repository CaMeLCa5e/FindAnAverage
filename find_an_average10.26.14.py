#!/usr/bin/env python 
"""
This is an application built to import a data file, average and return a specific value.
"""
import csv
from sys import argv

script, filename = argv

def process():
	with open(filename, 'r') as f:

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
					column.append(data)

	return sum(column)

def main():
	print process()

if __name__ == '__main__':
	main()
	

