from C_sort import *
import os, sys

def accumulator(csv_files):
	if not isinstance(csv_files, list): raise TypeError("Argument must be list")
	results = C_sort(csv_files[0])
	results.empty_cleanse()
	print("{0}: {1}".format(csv_files[0], len(results.contents)))
	for i in range(1, len(csv_files)):
		print("Processing {0}...".format(csv_files[i]))
		temp = C_sort(csv_files[i])
		temp.empty_cleanse()
		print("{0}: {1}".format(csv_files[i], len(temp.contents)))
		results + temp 
	results.export("spiffs_jan2020.csv")

if __name__ == "__main__":
	t_dir = sys.argv[1]
	print(t_dir)
	if "C:\\" not in t_dir: t_dir = os.getcwd() + '\\' + t_dir
	print(t_dir)
	items = os.listdir(t_dir)
	print(items)
	
	#should fix so it only looks at the last four elements in the filename string
	csv_files = [t_dir + "\\" + elem for elem in items if ".csv" in elem]
	print(csv_files)
	accumulator(csv_files)



