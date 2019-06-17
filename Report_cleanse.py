from C_sort import *
from dictionarify import *
from S_format import *
from w_csv import *
class Report_cleanse:
	def __init__(self, fname):
		self.fname = fname
		self.data = dictionarify(fname)
	def cleanse(self, empty_key):
		#if method discovers that there is no value for the given key then it removes the dict from data
		for i in range(len(self.data)-1, 0, -1):
			if not self.data[i].get(empty_key, ''): del self.data[i]

	def export(self, fname = 'report_file.csv' ):
		#if c: crit = c
		#else: 
		crit = list(self.data[0].keys())
		res = [crit]
		for i in range(0, len(self.data)):
			res.append(S_format(self.data[i]).d_sort(crit))
		w_csv(res, fname)


