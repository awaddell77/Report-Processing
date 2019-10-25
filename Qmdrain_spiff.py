from Spiff_report2 import *


class Qmdrain_spiff(Spiff_report):
	def __init__(self, spiff_name, fname_eclipse, fname_master):
		super().__init__(spiff_name, fname_eclipse, fname_master)
		#self.e_data.add_crit("Spiff Match")
		#self.e_data.add_crit("CatMatch")
		#self.m_data.add_crit("CatMatchM")

	def transform_eclipse(self, t_dict, key):
		temp = t_dict[key].split(' ')
		#temp = t_dict.split(' ')
		if not len(temp): return
		for i in range(0, len(temp)):
			if '.' in temp[i]:
				t_dict['CatMatch'] = temp[i]
				return
				
	def transform_master(self, t_dict, key):
		temp = t_dict[key]
		t_dict["CatMatchM"] = temp.replace(' ', '')
		return
	def cust_clean(self):
		for i in range(0, len(self.e_data)): self.e_data.transform_index(i, 'DESC', self.transform_eclipse)
		for i in range(0, len(self.m_data)): self.m_data.transform_index(i, 'Item #',self.transform_master)
	def cust_match(self):
		for i in range(0, len(self.e_data)):
			temp = self.e_data.get_index(i)
			catnum = temp["CatMatch"]
			loc = self.m_data.search('CatMatchM', catnum)
			if not loc:
				temp['Spiff Match'] = "N/A"
				continue
			spiff = self.m_data.get_index(loc)['Spiff Amount']
			temp['Spiff Match'] = spiff
			
'''try: 
	m_inst = Qmdrain_spiff("qmdrain_eclipse2019.csv", "qmdrain_master2019.csv")
except FileNameError as FE:
	print("FILENAMEERROR:{0}".format(FE))'''
#m_inst = Qmdrain_spiff('QMDRAIN', "qmdrain_eclipse2019.csv", "qmdrain_master2019.csv")
#m_inst.clean()
#m_inst.match()
#m_inst.export_matches('qmdraintest.csv')
#m_inst.export_master('qmdraintestmast.csv')


