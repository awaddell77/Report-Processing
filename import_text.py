from text_l import *
from text_wc import *
import os, csv
from C_sort import r_csv
from w_csv import w_csv
def import_text(fname, header_line=0, delims_locs=[]):
	#remember that python is zero indexed but excel/notpad isn't
	#line 0 in notepad is 1
	t_data = text_l(fname)[header_line:]
	return t_data
def space_locate(t_data, header_x=0, header_y= 0):
	locs = set()
	for line in range(header_y, len(t_data)):
		for i in range(header_x, len(t_data[line])):
			print(line)

			if t_data[line][i] == ' ' and i-1 not in locs : 
				print("{0} is blank.".format(t_data[line][i]))
				locs.add(i)
			if  t_data[line][i] == ' ' and i-1 in locs: locs.remove(i-1)

			if t_data[line][i] != ' ' and i in locs: locs.remove(i)
	return locs
def insert_delim(t_data,locs, header_line=0, delim = '\t'):
	if len(delim) >= 2: locs = [locs[i] + (len(delim)-1) for i in range(0, len(locs))]
	#above code does not work for any value of length of delim greater than 2
	else: locs = [locs[i] + 1 for i in range(0, len(locs))]
	for line in range(header_line, len(t_data)):
		new_ln = ''
		for i in range(0, len(t_data[line])):
			if i not in locs:new_ln += t_data[line][i]
			else: 
				new_ln += delim + t_data[line][i]
				#if not line: 
		t_data[line] = new_ln
	return t_data
def export(t_data,fname = 'new_rep.txt'):
	text_wc(t_data, fname,1)

def main(fname, header_line, locs=[99,111,129, 147,162]):
	t_data = import_text('super_test.txt',4)
	#defaults to product sales summary columns when locs is blank
	t_data = insert_delim(t_data, locs, header_line)
	text_wc(t_data, 'super_test.csv')
#h = import_text('super_test.txt',4)

#locs = space_locate(h, 0, 0)
#subtract two if using text editor to identify columns
#subtract three if using two chars

locs = [99,111,129, 147,162]
#h = insert_delim(h, locs)
h = insert_delim(h, locs, 4)
text_wc(h, 'super_test.csv')


