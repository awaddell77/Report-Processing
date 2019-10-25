from Spiff_report2 import *

class Fleurco_spiff(Spiff_report):
	def __init__(self, spiff_name, fname_eclipse, fname_master):
		super().__init__(spiff_name, fname_eclipse, fname_master)

	def transform_eclipse(self, t_dict, key):
		temp = t_dict[key].split(' ')
		#temp = t_dict.split(' ')
		#if no spaces then it just returns the description as is
		if len(temp) <= 1: t_dict['CatMatch'] = temp[0]

		else: t_dict['CatMatch'] = temp[1].replace('-', '')
		return
	def transform_master(self, t_dict, key):
		temp = t_dict[key]
		t_dict['CatMatchM'] = temp.replace('-', '')
		return
	def cust_clean(self):
		for i in range(0, len(self.e_data)): self.e_data.transform_index(i, 'DESC', self.transform_eclipse)
		for i in range(0, len(self.m_data)): self.m_data.transform_index(i, 'PRODUCT CODE', self.transform_master)
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