#because excel is absolutely worthless 
from C_sort import *
from dictionarify import *
from export_dictionarify import *
import sys
def combine_csvs(fname1, fname2):
	data = dictionarify(fname1) +  dictionarify(fname2)
	export_dictionarify(data)
	return

if __name__ == "__main__":
	combine_csvs(sys.argv[1], sys.argv[2])
	

