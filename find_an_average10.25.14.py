#!/usr/bin/env python 
"""
This is an application built to import a data file, average and return a value
"""
import csv
# import numpy

# def read_file(file_name):
# 	with open(file_name, 'r') as f:
# 		# f.readline()
# 		# f.readline()
# 		num = f.readline().split('|')[-1] 
# 		# print num



# # new code...  ??
# 		with open(data, 'r') as f:

# 			total = 0

# 			for i, line in enumerate(f.readlines()[2:]):
# 				if i in line >= 0:
# 					yield average.(total)
# 				else:
# # 					return 
# data ='data.txt'

# incomes = [int(line.split("|")[-1].strip())

#             for line in open(data,'r').readlines()[2:]

#             if line.split("|")[-1].strip().isalnum()]

# avg_income = sum(incomes) / len(incomes)

# print avg_income


def process():
	with open('data.txt', 'r') as f:
		f.readline()
		f.readline()
		column = []
		for row in csv.reader(f, delimiter='|', skipinitialspace=True):
			data = row[-1]
			try:
				data = float(data)
			except ValueError as err:
				print(err)
				print(data)
			else:
				if data != -999999999:
					column.append(data)
	return sum(column)




	# while True:
	# 	for i, line in enumerate(f.readlines()[2:]):
	# 		if i in line >=0:
	# 			yield = data
	# 	data_items_seen += len(data)
	# 	running_sum += sum(data)
	# 	print ('{}'.format(running_sum / float(data_items_seen)))
	#data = f.read()
	# f.close()
	



# def split_data(x):
# 	data_count = {}
# 	data_list = x.split("|")

# 	for word in data_list:
# 		# if word in data_count:
# 		# 	data_count[word] +=1 
# 		# else:
# 		# 	data_count[word] = 1
# 		print word
# 	return data_count	

def main():

	print process()

if __name__ == '__main__':
	main()
	

