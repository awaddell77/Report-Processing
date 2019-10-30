from Rep_process import *
#for product sales reports (detail) that list serial numbers

class Ps_serials(Rep_process):
	def __init__(self, fname):
		super().__init__(fname)
	def main(self):
		header = self.data.get_header()
		acceptable = ['SN', 'SN#']
		try:
			loc = header.index('ShipDate')
		except ValueError as VE:
			print("No ShipDate column found")
		for i in range(0, len(self.data)):

			#if self.data[i][loc] == 'SN' or self.data[i][loc] == 'SN#':
			if self.data[i][loc] in acceptable:
				self.data[i][loc] += str(self.data[i][loc+1]) + str(self.data[i][loc + 2])
				self.data[i][loc+1], self.data[i][loc+2] = '', ''
		self.export()
		return
		#not tested



m_inst = Ps_serials('prodsalessertest.csv')
h= m_inst.data
temp = h[1][9]
temp = str(round(float(temp.replace('*', ''))))
res = m_inst.thousand_sep(temp)
print("Before: ", temp)
print("After: ", res)
#m_inst.main()




