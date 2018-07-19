from C_sort import *
from dictionarify import *

class Spiff_report:
	def __init__(self, fname_master, fname_sales):
		self.fname_master = fname_master
		self.fname_sales = fname_sales
		self.m_data = C_sort(fname_master)
		self.s_data = C_sort(fname_sales)
		self.matches = dictionarify(fname_sales)
	def clean(self):
		self.cust_clean()
	def cust_clean(self):
		pass
	def cat_extract(self):
		
	def match_cats(self):
		self.cust_match_cats(self)