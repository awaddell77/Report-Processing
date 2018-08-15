from C_sort import *
from dictionarify import *
from Dict_lst import *
from Dictify import *
from w_csv import *
from S_format import *
import math, random
class Spiff_report:
	def __init__(self, fname_master, fname_sales):
		self.fname_master = fname_master
		self.fname_sales = fname_sales
		self.m_data = Dict_lst(dictionarify(fname_master))
		self.s_data = Dictify(fname_sales).main()
		self.s_data_crits = Dictify(fname_sales).just_header()
		self.matched = Dict_lst()

	def clean(self):
		self.cust_clean()
	def cust_clean(self):
		pass
	def cat_extract(self):
		pass
		
	def match_cats(self):
		self.cust_match_cats(self)
	def status_report(self):
		print("{0} matches found.".format(len(self.matched)))
		print("Sales / Master: {0} / {1}".format(len(self.s_data), len(self.m_data)))
	def reintegrate(self):
		self.matched.add_lst(self.s_data)
	def export_sales(self, fname):
		self.export(self.s_data, None, fname)
	def export_master(self, fname):
		self.export(self.m_data.data, None, fname)
	def export_matches(self, fname):
		self.s_data_crits = list(self.s_data[0].keys())
		self.export(self.matched.data, self.s_data_crits, fname)
	def sample_unmatched(self, level = .05):
		if len(self.m_data) == 0: return
		sample_size = math.ceil(len(self.m_data) * level)
		sample = []
		indexes = set()
		#use data structures not algos
		while len(indexes) < sample_size:
			index = random.randint(0, len(self.m_data))
			indexes.add(index)
		for index in indexes: sample.append(self.m_data.get_index(index))
		return sample


		
	def export(self, data, c= [], fname = 'report_file.csv' ):
		if c: crit = c
		else: crit = list(data[0].keys())
		res = [crit]
		for i in data:
			res.append(S_format(i).d_sort(crit))
		w_csv(res, fname)

