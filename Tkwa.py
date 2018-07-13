#script for TKWA reports
from C_sort import *
class Tkwa:
	def __init__(self, fname):
		self.fname = fname
		self.data = C_sort(self.fname)
		self.fills = []

	def process(self, header_start=0):
		header = self.data.get_header(header_start)
		target_index = ''
		for i in range(0, len(header)):
			if header[i] == 'Product........................': target_index = i
		col = self.data.col_grab(target_index)
		next_start = header_start+1
		for i in range(0, len(col)):
			if "Total for" in col[i]:
				name = self.comp_name_grab(col[i])
				self.fills.append([name, next_start, i])
				next_start = i + 2
		for sects in self.fills:
			self.data.fill_column(0, sects[0], sects[1], sects[2])
	def export(self, fname="TKWA Report.csv"):
		w_csv(self.data.contents, fname)





	def comp_name_grab(self, cell):
		return cell.split(' ')[2]


