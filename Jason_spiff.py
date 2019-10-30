from Spiff_report2 import *

class Jason_spiff(Spiff_report):
	def __init__(self, spiff_name, fname_eclipse, fname_master):
		super().__init__(spiff_name, fname_eclipse, fname_master)
	def transform_eclipse(self, t_dict, key):
		temp = t_dict[key].split(' ')[1]
