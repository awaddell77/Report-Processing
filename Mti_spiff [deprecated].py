#mti spiff
from C_sort import *
from Dict_lst import *
from dictionarify import *
from w_csv import *
from S_format import *
from Dictify import *
class Mti_spiff:
	def __init__(self, m_fname, s_fname):
		self.m_data = Dict_lst(dictionarify(m_fname))
		self.s_data = Dictify(s_fname).main()
		self.matched = Dict_lst()
		self.key_words = {}
		self.old_matches = Dict_lst(dictionarify('OldMTI.csv'))
	def phase_one(self):
		self.m_data.sort('MTI_SKU')

		for i in range(len(self.s_data)-1, -1, -1):
			self.s_data[i]['Phase'] = ''
			self.s_data[i]['Matched_w'] = ''
			index = self.m_data.b_search('MTI_SKU', self.s_data[i]['No.'])
			self.s_data[i]['K_ID'] = ''
			if index:
				self.s_data[i]['K_ID'] = self.m_data.get_index(index)['PRODUCT_ID']
				self.s_data[i]['Phase'] = '1'
				self.s_data[i]['Matched_w'] =  self.m_data.get_index(index)['DESC']
				self.matched.add(self.s_data.pop(i))
				self.m_data.del_index(index)
		print("Matched {0} items".format(len(self.matched)))
	def phase_two(self, alt_crits = ['CAT #', 'ALT1', 'USER FIELD 2']):
		for i in range(len(self.s_data)-1, -1, -1):
			index = self.m_data.mult_search(alt_crits, self.s_data[i]['No.'])
			if index:
				self.s_data[i]['Phase'] = '2'
				self.matched.add(self.s_data.pop(i))
				self.m_data.del_index(index)
		print("Matched {0} items".format(len(self.matched)))
	def phase_four(self):
		for i in range(len(self.s_data)-1, -1, -1):
			self.m_data.sort('DESC')
			index = self.m_data.find_cond(self.contains_sku, "DESC", self.s_data[i]["No."])
			if index:
				self.s_data[i]['Phase'] = '3'
				self.s_data[i]['K_ID'] = self.m_data.get_index(index)['PRODUCT_ID']
				self.s_data[i]['Matched_w'] = self.m_data.get_index(index)['DESC']
				self.matched.add(self.s_data.pop(i))
				self.m_data.del_index(index)
		print("Matched {0} items".format(len(self.matched)))
	def phase_three(self):
		self.old_matches.sort('MTI')

		for i in range(len(self.s_data)-1, -1, -1):
			self.s_data[i]['Phase'] = ''
			self.s_data[i]['Matched_w'] = ''
			index = self.old_matches.b_search('MTI', self.s_data[i]['No.'])
			self.s_data[i]['K_ID'] = ''
			if index:
				self.s_data[i]['K_ID'] = self.old_matches.get_index(index)['K_ID']
				self.s_data[i]['Phase'] = '4'
				self.matched.add(self.s_data.pop(i))
				self.old_matches.del_index(index)
		print("Matched {0} items".format(len(self.matched)))
	def desc_trans(self, desc):
		n_desc = desc.split(' ')
	def normalize_case(self, d, key):
		if isinstance(d[key], str):
			d[key] = d[key].lower()
	def sku_trans(self):
		self.m_data.sort('MTI_SKU')
		for i in range(len(self.s_data)-1, -1, -1):
			self.s_data[i]['Alt No.'] = self.s_data[i]['No.'].replace('AEA', '')
			index = self.m_data.b_search('MTI_SKU', self.s_data[i]['Alt No.'])
			if index:
				self.s_data[i]['K_ID'] = self.m_data.get_index(index)['PRODUCT_ID']
				self.s_data[i]['Phase'] = '5'
				self.matched.add(self.s_data.pop(i))
				self.m_data.del_index(index)


	def phase_five(self):
		#transforms remnants
		#for i in range(0, len(m_data)):
		res = []
		ind = -1
		for i in range(0, len(self.m_data)):
			#self.m_data.transform_index(i, 'MTI_SKU'. self.normalize_case)
			lower_c = self.m_data.get_index(i)['MTI_SKU'].lower()
			res.append(lower_c)		

		for i in range(len(self.s_data)-1, -1, -1):
			val = self.s_data[i]['No.'].lower()
			if  val in res:
				self.s_data[i]['K_ID'] = self.m_data.get_index(res.index(val))['PRODUCT_ID']
				self.s_data[i]['Phase'] = '6'
				self.s_data[i]['Matched_w'] = self.m_data.get_index(res.index(val))['DESC']
				self.matched.add(self.s_data.pop(i))
				print("Matched {0}".format(self.m_data.get_index(res.index(val))['DESC']))

				self.m_data.del_index(res.index(val))
				res.remove(val)


	def contains_name(self):
		pass
	def contains_sku(self, d, key, val):
		if val + '-' in d[key] or val + ' ' in d[key]: return True
		return False
	def keyword_id(self):
		for i in range(0, len(self.s_data)):
			names = self.s_data[i]["Description"].split(" ")
			print(names)
			for n in names:
				if n not in self.key_words: 
					
					self.key_words[n] = 0
				else: 
					print("ADDING 1 TO {0}".format(self.key_words[n]))
					self.key_words[n] = self.key_words[n] + 1
	def sales_keyword(self):
		names = set()
		for i in range(0, len(self.s_data)):
			n = self.s_data[i]["Description"].split(" ")[0]
			names.add(n)
		return names
	def reintegrate(self):
		self.matched.add_lst(self.s_data)


	def export(self, data, c= []):
		if c: crit = c
		else: crit = list(data[0].keys())
		res = [crit]
		for i in data:
			res.append(S_format(i).d_sort(crit))
		w_csv(res, "sales_file.csv")



m_inst = Mti_spiff('mti_master.csv', 'mti_sales.csv')
m_inst.phase_one()
m_inst.phase_two()

m_inst.phase_three()
m_inst.phase_four()
m_inst.phase_five()
m_inst.sku_trans()

m_inst.reintegrate()

m_inst.export(m_inst.matched.data, ['No.', 'Description', 'Series', 'Package', 'Search Description', "Matched_w", 'Phase', 'Spiff Amount', "K_ID"])
