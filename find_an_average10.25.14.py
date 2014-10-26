#!/usr/bin/env python 
"""
This is an application built to import a data file, average and return a value
"""
import numpy

def read_file(file_name):
	with open(file_name, 'r') as f:
		f.readline()
		f.readline()
		num = f.readline().split('|')[-1] 
		print num

		# def f():
		# 	i += 0 
		# 	while True if f() > 0	
		# 		yield 


# new code...  
		with open(data, 'r') as f:

			total = 0

			for i, line in enumerate(f.readlines()[2:]):
				if i in line >= 0:
					yield average.(total)
				else:
					return 




#generator 

		#

	#data = f.read()
	f.close()
	#return data


def split_data(x):
	data_count = {}
	data_list = x.split("|")

	for word in data_list:
		# if word in data_count:
		# 	data_count[word] +=1 
		# else:
		# 	data_count[word] = 1
		print word
	return data_count	

def main():
	read_file("data.txt")
	#data_dictionary = split_data(data)
# 	print data_dictionary
	# sorted_data = sorted([(value,key) for (key,value) in data_dictionary.items()])
	# sorted_data.reverse()
	# print sorted_data[0:9]

if __name__ == '__main__':
	main()
	

