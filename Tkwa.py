#script for TKWA reports
from C_sort import *
import sys
class Tkwa:
	def __init__(self, fname):
		self.fname = fname
		self.data = C_sort(self.fname)
		self.fills = []

	def process(self, header_start=0):
		header = self.data.get_header(header_start)
		target_index = ''
		targ_col = 'Product........................'
		for i in range(0, len(header)):
			if header[i] == targ_col or targ_col in header[i]: target_index = i
		if not target_index: raise RuntimeError("Could not find Product column")
		col = self.data.col_grab(target_index)
		next_start = header_start+1
		for i in range(0, len(col)):
			#reads through cells
			if "Total for" in col[i]:
				#grabs the name of the buy/price line
				name = self.comp_name_grab(col[i])
				self.fills.append([name, next_start, i-1])
				next_start = i + 2
		for sects in self.fills:
			self.data.fill_column(0, sects[0], sects[1], sects[2])
	def export(self, fname="TKWA Report.csv"):
		w_csv(self.data.contents, fname)





	def comp_name_grab(self, cell):
		return cell.split(' ')[2]

if __name__ == "__main__":
	if sys.argv[1] in ['help', '?', 'h', '-h']:
		print("python.exe Tkwa.py [file name (including path if not in working directory)]")
		print("Example: python Tkwa.py example.csv")
	else:
		m_inst = Tkwa(sys.argv[1])
		m_inst.process()
		#cn for custom name
		if '-cn' in sys.argv: m_inst.export(sys.argv[sys.argv.index('-cn') + 1])
		else: m_inst.export()
