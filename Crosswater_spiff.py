from Spiff_report import *


class Crosswater_spiff(Spiff_report):
	def __init__(self, fname_master, fname_sales):
		super().__init__(fname_master, fname_sales)
		self.s_data_crits.append('PN')
	def extract_codes_from_both(self):
		for i in range(0, len(self.m_data)):
			d = self.m_data.get_index(i)
			temp = d["DESC"]
			temp = temp.split(' ')
			temp = temp[1]
			temp = temp.strip(' ').replace('-', '').replace('_', '')
			self.m_data.data[i]['Extract_Code'] = temp #will have to fix this once an Dict_lst a modify method, users shouldn't be able to access data directly
	    #@TODO: implement transformations for sales spiff code data 


	def phase_alpha(self):
		#initial matches
		for i in range(len(self.s_data)-1, -1, -1):
			pcode = self.s_data[i]['Product Code']
			res = self.m_data.mult_search(['CAT#', 'USER2', 'ALT1'], pcode)
			self.s_data[i]["PN"] = ''

			self.s_data[i]['Phase'] = ''
			if res:
				self.s_data[i]["PN"] = self.m_data.get_index(res)['PN#']
				self.s_data[i]["Phase"] = '0'
				self.matched.add(self.s_data.pop(i))
				self.m_data.del_index(res)


			if not res:
				res = self.m_data.mult_search(['CAT#', 'USER2', 'ALT1', 'Extract_Code'], self.trans_pc(pcode))
				if res:
					self.s_data[i]["PN"] = self.m_data.get_index(res)['PN#']
					self.s_data[i]["Phase"] = '0'
					self.matched.add(self.s_data.pop(i))
					self.m_data.del_index(res)

		self.status_report()
	def phase_one(self):
		for i in range(len(self.s_data)-1, -1, -1):
			pcode = self.s_data[i]['Product Code']
			res = self.m_data.find_cond(self.is_in, 'DESC', pcode + ' ')
			if res:
				self.s_data[i]["PN"] = self.m_data.get_index(res)['PN#']
				self.s_data[i]["Phase"] = '1'
				self.matched.add(self.s_data.pop(i))
				self.m_data.del_index(res)
		self.status_report()

	def phase_two(self):
		pass
	def cat_extract(self, desc):
		return 
	def trans_pc(self, pcode):
		pcode = pcode.replace('-', '')
		pcode = pcode.replace('_', '')
		return pcode
	def is_in(self, d, key, val):
		if val in d[key]: return True
		return False



m_inst = Crosswater_spiff('crosswater_master.csv', 'cwater_sales.csv')
m_inst.extract_codes_from_both()
m_inst.phase_alpha()
m_inst.phase_one()
m_inst.reintegrate()
m_inst.export_master('cwater_unmatched.csv')
m_inst.export_matches('cwater_matches.csv')




