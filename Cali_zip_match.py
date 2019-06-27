#match zip


from Spiff_report import *


class Cali_zip_match(Spiff_report):
	def __init__(self, fname_master, fname_sales):
		super().__init__(fname_master, fname_sales)
		#self.s_data_crits.append('PN')
	def extract_codes_from_both(self):
		for i in range(0, len(self.m_data)):
			d = self.m_data.get_index(i)
			temp = d["DESC"]
			temp = temp.split(' ')
			temp = temp[1]
			temp = temp.strip(' ').replace('-', '').replace('_', '')
			self.m_data.data[i]['Extract_Code'] = temp #will have to fix this once an Dict_lst a modify method, users shouldn't be able to access data directly
	    #@TODO: implement transformations for sales spiff code data 



	def phase_one(self):
		for i in range(len(self.s_data)-1, -1, -1):
			city_name = self.s_data[i]['City Name']
			res = self.m_data.search('City Name', city_name)
			if res:
				self.s_data[i]["ZIP Code"] = self.m_data.get_index(res)['ZIP Code']
				
				#self.matched.add(self.s_data.pop(i))
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
	def export_cust(self):
		self.export(self.s_data)




m_inst = Cali_zip_match('cali_zip.csv', 'CA city.csv')
m_inst.phase_one()
m_inst.export_cust()
#m_inst.reintegrate()

#m_inst.export_master('calizip_unmatched.csv')
#m_inst.export_matches('calizip_matches.csv')




