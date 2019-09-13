from C_sort import *
import sys


def main(fname,col_number):
	s_inst = C_sort(fname).export_column_as_row(col_number)
	return


if __name__ == "__main__":
	#main(filename, col_number)
	main(sys.argv[1], int(sys.argv[2])) 

