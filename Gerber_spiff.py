from C_sort import *
from dictionarify import *
from Dict_up import *
from Dict_lst import *
from w_csv import *
'''
Phase One: Match cat #s that are already extracted in the master to those in the sales file 


'''


class Gerber_spiff:
	def __init__(self, fname_master, fname_sales):
		self.fname_master = fname_master
		self.fname_sales = fname_sales
		#position in the original csvs is irrelevant so dictionarify can be used
		self.m_data = dictionarify(fname_master)
		self.s_data = dictionarify(fname_sales)
		self.m_data_csv = C_sort(fname_master) #for testing only, need to be able to grab a single column
		self.matched = []
		self.testing1 =  self.m_data_csv.dict_pair(4, 1)
		self.test2 = Dict_lst(self.m_data)
		self.phase_zero_res = []
	def cat_extract(self, desc):
		desc_lst = desc.split(" ")
		if self.has_number(desc_lst[1]) and '.' not in desc_lst[1] and '-' in desc_lst[1]:
			return desc_lst[1]
		return ''


	def phase_zero(self):
		for i in range(0, len(self.test2.data)):
			if not self.test2.data[i]['CAT #']:
				self.test2.data[i]['CAT #'] = self.cat_extract(self.test2.data[i]['DESC'])
				self.phase_zero_res.append(self.test2.data[i])
			else: self.test2.data[i]['CAT #'] = self.test2.data[i]['CAT #'].strip(' ')
	def phase_one_match(self):
		cat_id_to_p_id = self.m_data_csv.dict_pair(4, 1)
		self.testing1 = cat_id_to_p_id
		self.test2.sort('CAT #')
		for i in range(len(self.s_data)-1, -1, -1):
			#res = cat_id_to_p_id.get(self.s_data[i]['Cat#'], '')

			res = self.test2.b_search("CAT #", self.s_data[i]["Cat#"].strip(' '))
			#print("Matched {0} to {1}".format(self.s_data[i]['Cat#'], self.test2.data[res]))
			self.s_data[i]["K_ID"] = '' 
			if res is not None:
				new = self.s_data[i]
				self.s_data[i]['K_ID'] = self.test2.get_index(res)['PRODUCT_ID']
				self.matched.append(new)
				index = i
				print("Index is ", str(res))
				print("Deleting {0}. It's cat # is {1} and the element that is being moved has {2}".format(
					self.test2.get_index(res)["DESC"], self.test2.get_index(res)["CAT #"], new['Cat#']))
				#del self.m_data[res[1]]
		print("Matched {0} items".format(len(self.matched)))
	def phase_two_match(self):
		for i in range(0, len(self.s_data)):
			if not self.s_data[i]['K_ID']:
				print('Processing {0}'.format(self.s_data[i]['Desc ']))
				new = self.s_data[i]['Cat#'].replace('-', '')
				res = self.test2.b_search('CAT #', new)
				if res is not None: 
					self.s_data[i]['K_ID'] = self.test2.get_index(res)['PRODUCT_ID']
					print("Paired {0} with {1}".format(self.test2.get_index(res)['DESC'], self.s_data[i]['Desc ']))

	def phase_three_match(self):
		for i in range(0, len(self.s_data)):
			if not self.s_data[i]['K_ID']:
				print('Processing {0}'.format(self.s_data[i]['Desc ']))
				new = self.text_cleanse(self.s_data[i]['Cat#'])
				print('New text is {0}'.format(new))
				res = self.test2.b_search('CAT #', new)
				if res is not None: 
					self.s_data[i]['K_ID'] = self.test2.get_index(res)['PRODUCT_ID']
					print("3Paired {0} with {1}".format(self.test2.get_index(res)['DESC'], self.s_data[i]['Desc ']))
	def text_cleanse(self, s):
		new_s = ''
		for i in s:
			if i.isdigit() or i == '-': 
				new_s += i
		if new_s[0] == '-':
			new_s = new_s[1:]
		return new_s

	def has_number(self, desc):
		for i in desc:
			try: 
				int(i)
			except ValueError as VE:
				pass
			else:
				return True
		return False
	def count_desc(self):
		count = 0
		for i in range(0, len(self.s_data)):

			if self.s_data[i]['K_ID'] and self.s_data[i]['Keller PN#'] and self.s_data[i]['Keller PN#'] != self.s_data[i]['K_ID']:
				print("{0} is not the same as {1}".format(self.s_data[i]['K_ID'], self.s_data[i]['Keller PN#']))
				count += 1
		print("{0} out of {1} don't match up.".format(count, len(self.s_data)))


		
	def match_cats(self):
		self.cust_match_cats(self)
	def export(self, data, c= ['Pline','Keller PN#', 'Desc ', 'Cat#', 'NEW SPIFF AMOUNTS', 'LIST PRICE PC1', 'LIST PRICE PC2', 'TOTAL', 'K_ID']):
		if c: crit = c
		else: crit = list(data[0].keys())
		res = [crit]
		for i in data:
			res.append(S_format(i).d_sort(crit))
		w_csv(res, "sales_file.csv")


m_inst = Gerber_spiff('gerbermast.csv', 'GerpluSpiffList2018.csv')
m_inst.phase_zero()
m_inst.phase_one_match()
m_inst.phase_two_match()
m_inst.phase_three_match()
m_inst.export(m_inst.s_data)
m_inst.count_desc()