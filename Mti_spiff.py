from Spiff_report2 import *


class Mti_spiff(Spiff_report):
	def __init__(self, spiff_name, fname_eclipse, fname_master):
		super().__init__(spiff_name, fname_eclipse, fname_master)
		self.r_bucket = set()
	def transform_eclipse(self, t_dict, key):

		temp = t_dict[key]
		t_dict['Original_SKU'] = ''
		for elem in self.r_bucket: temp = temp.replace(elem+' ', '')
		
		temp = temp.split(' ')
		if len(temp) <= 1: return
		if temp[0] != 'MTI': targ = temp[0]
		#required because this company allows salesmen to create the products and so a lot of dumb arbitrary crap gets added like "*CUSTOM*" just before the cat# in the description
		elif '*' in temp[1]: targ = temp[2]
		else: targ = temp[1]
		
		#next it isolates the base
		t_dict['CatMatch'] = str(targ).split('-')[0]
		t_dict['Original_SKU'] = str(targ)
		return
	def transform_master(self, t_dict, key):
		#adding series names to object to aid with parsing since the naming conventions are so haphazard
		#CHECK THIS FIRST IF THERE ARE ANY ISSUES WITH MATCHES
		#Could definitely mangle 
		temp = t_dict['Description'].split(' ')[0]
		if temp: self.r_bucket.add(temp.upper())
		#no transformations required (?)
		
		t_dict['CatMatchM'] = t_dict[key]

		return
	def cust_clean(self):
		for i in range(0, len(self.m_data)): self.m_data.transform_index(i, 'No.', self.transform_master)
		for i in range(0, len(self.e_data)): self.e_data.transform_index(i, 'DESC', self.transform_eclipse)
		
	def cust_match(self):
		for i in range(0, len(self.e_data)):
			temp = self.e_data.get_index(i)
			catnum = temp["CatMatch"]
			loc = self.m_data.search('CatMatchM', catnum)
			if loc < 0:
				temp["Spiff Match"] = 'N/A'
				continue
			spiff = self.m_data.get_index(loc)['Spiff Amount']
			temp['Spiff Match'] = spiff
'''			
m_inst = Mti_spiff('MTI', 'mtieclipse.csv', 'mti_master.csv')
m_inst.clean()
m_inst.match()
m_inst.export_matches()'''