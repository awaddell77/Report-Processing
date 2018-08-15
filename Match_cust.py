from Spiff_report import *
import re
class Match_cust(Spiff_report):
	def __init__(self, fname_master, fname_target):
		super().__init__(fname_master, fname_target)
		self.clean_crit = ['$ ','*','/P']
	def clean_mast(self):
		for i in range(0, len(self.m_data)):
			self.m_data.transform_index(i, 'Name', self.clean_f)
			self.m_data.transform_index(i, 'Name', self.clean_f2)
	def clean_f(self, d, key):
		d[key] = re.sub('(\*\*.+\*\*)', '', d[key]).strip(' ')

	def clean_f2(self, d, key):
		rep_lst = self.clean_crit
		for elem in rep_lst:
			d[key] = d[key].replace(elem, '')
			
		d[key] = d[key].strip(' ')
	def is_in(self, d, key, val):
		if val in d[key]: return True
		return False


	def match(self):
		for i in range(len(self.s_data)-1, -1, -1):
			self.s_data[i]['Cust ID'] = ''

			self.m_data.sort('Name')
			index = self.m_data.b_search('Name', self.s_data[i]["Name"])
			if index:
				self.s_data[i]['Cust ID'] = self.m_data.get_index(index)['Customer_ID']
				self.m_data.del_index(index)
				self.matched.add(self.s_data.pop(i))
	def match_ph2(self):
		for i in range(len(self.s_data)-1, -1, -1):
			

			self.m_data.sort('Name')
			index = self.m_data.find_cond(self.is_in, 'Name', self.s_data[i]["Name"])
			if index:
				self.s_data[i]['Cust ID'] = self.m_data.get_index(index)['Customer_ID']
				self.m_data.del_index(index)
				self.matched.add(self.s_data.pop(i))
	def match_addr(self):
		for i in range(len(self.s_data)-1, -1, -1):
			index = self.m_data.search('ADDRESS1', self.s_data[i]['Address 1'])
			if not index and self.s_data[i]['Address 2']: 
				index = self.m_data.search('ADDRESS1', self.s_data[i]['Address 2'])
				if not index: index = self.m_data.search('Address2', self.s_data[i]['Address 2'])


			if index:
				self.m_data.get_index(i)
				self.s_data[i]['Cust ID'] = self.m_data.get_index(index)['Customer_ID']
				self.m_data.del_index(index)
				self.matched.add(self.s_data.pop(i))
	def match_no_bizdes(self):
		for i in range(len(self.s_data)-1, -1, -1):
			

			self.m_data.sort('Name')
			index = self.m_data.find_cond(self.is_in, 'Name', self.rem_biz_deg(self.s_data[i]))
			if index:
				self.s_data[i]['Cust ID'] = self.m_data.get_index(index)['Customer_ID']
				self.m_data.del_index(index)
				self.matched.add(self.s_data.pop(i))
	def rem_biz_deg(self, d):
		biz_degs = [' LLC', ', LLC',' INC', ', INC']
		#comma issue?
		name = d['Name']
		if ',' in name: name = name.replace(',', '')


		for des in biz_degs:
			if des + '.' in name: return name.replace(des+'.', '').strip(' ')
			if des in name: return name.replace(des, '').strip(' ')

		return name


	def export_matches(self, fname):
		self.s_data_crits = ['Line#', 'Name', 'Attn', 'Address 1', 'Address 2', 'City', 'State', 'Zip', 'Cust ID']
		self.export(self.matched.data, self.s_data_crits, fname)


m_inst = Match_cust('cust_mast.csv', 'tbmod.csv')
m_inst.clean_mast()
m_inst.match()
m_inst.status_report()
print("ON TO PHASE 1.5")
m_inst.clean_crit.append('.')
m_inst.clean_mast()
m_inst.match()
m_inst.status_report()
print("PHASE 2")
m_inst.match_ph2()
m_inst.status_report()
print("PHASE 3")
m_inst.match_addr()
m_inst.status_report()
print("PHASE 4")
m_inst.match_no_bizdes()
m_inst.status_report()
m_inst.reintegrate()


