from Spiff_report2 import *

'''NOTE THAT THIS ASSUMES THAT THE SKU DIRECTLY FOLLOWS EITHER "PREMIER COPPER" OR JUST "PREMIER" '''
class Pcp_spiff(Spiff_report):
	def __init__(self, spiff_name, fname_eclipse, fname_master):
		super().__init__(spiff_name, fname_eclipse, fname_master)

	def transform_eclipse(self, t_dict, key):
		temp = t_dict[key].split(' ')
		if not len(temp): return
		targ = ''
		#due to shoddy data entry standards this (and other arbitrary conditions) have to be in here
		#otherwise we could just go straight to temp[2]
		if temp[0] == "PREMIER" and temp[1] != "COPPER": targ = temp[1]
		else: targ = temp[2]
		t_dict['CatMatch'] = str(targ).replace('-', '')
		return
	def transform_master(self, t_dict, key):
		temp = str(t_dict[key])
		t_dict["CatMatchM"] = temp.replace('-', '')
		return
	def cust_clean(self):
		for i in range(0, len(self.e_data)): self.e_data.transform_index(i, 'PRODUCT_DESC', self.transform_eclipse)
		for i in range(0, len(self.m_data)): self.m_data.transform_index(i, 'SKU', self.transform_master)
	def cust_match(self):
		for i in range(0, len(self.e_data)):
			temp = self.e_data.get_index(i)
			catnum = temp["CatMatch"]
			loc = self.m_data.search('CatMatchM', catnum)
			if not loc:
				temp["Spiff Match"] = 'N/A'
				continue
			spiff = self.m_data.get_index(loc)['Spiff Amount']
			temp['Spiff Match'] = spiff
'''
m_inst = Pcp_spiff('PCP', "pcpeclipse2019.csv", "pcpmaster2019.csv" )
m_inst.clean()
m_inst.match()
m_inst.export_matches('asdfsad')
'''