from Sel_session import *
from dictionarify import *
import time
from w_csv import *
from S_format import *
#results = []
class Zip_load:
	def __init__(self, source_file, state = 'CA'):
		self.source_file = dictionarify(source_file)
		self.state = state

		self.results = []
		self.browser = Sel_session()

	def main(self):
		#self.browser.go_to('https://tools.usps.com/zip-code-lookup.htm?bycitystate')
		s_length = len(self.source_file)
		for i in range(0, s_length):
			self.browser.go_to('https://tools.usps.com/zip-code-lookup.htm?bycitystate')
			city = self.source_file[i]['City Name']
			print("Processing {0}, #{1} out of {2}".format(city, i+1,s_length ))
			self.results.extend(self.get_zips(city))



	def get_zips(self, city_name):
		results = []
		self.browser.js("document.getElementById('tCity-city-state').value = '{0}';".format(city_name))
		self.browser.js("document.getElementById('tState-city-state').value = '{0}';".format(self.state))
		self.browser.js("document.getElementById('zip-by-city-and-state').click();")
		self.browser.w_load()
		time.sleep(2)
		site = self.browser.source()
		
		
		#print("TARGET IS", target)
		try:
			target = site.find('div', {'id':'zipByCityStateDiv'})
			elements = target.find_all('div', {'class':'city-state-result'})
			#if not target: return
		
		except AttributeError:
			
			results.append({'City Name':city_name,'ZIP Code':'N/A'})
			return results
		

		for i in range(0, len(elements)):
			#print("aaaa", elements[i].find('strong').text)
			results.append({'City Name':city_name,'ZIP Code':elements[i].find('strong').text})
		if not results: results.append({'City Name':city_name, 'ZIP Code':'N/A'})
		print(results)
		return results
	def export(self, c= [], fname = 'ca_zip_file.csv' ):
		if c: crit = c
		else: crit = list(self.results[0].keys())
		res = [crit]
		for i in self.results:
			res.append(S_format(i).d_sort(crit))
		w_csv(res, fname)



def zip_load(source_file = ''):
	results = []
	url = 'https://tools.usps.com/zip-code-lookup.htm?bycitystate'
	m_inst = Sel_session()
	m_inst.go_to(url)
	#city_data = dictionarify(source_file= '')
	m_inst.js("document.getElementById('tCity-city-state').value = 'Redding';")
	m_inst.js("document.getElementById('tState-city-state').value = 'CA';")
	m_inst.js("document.getElementById('zip-by-city-and-state').click();")
	m_inst.w_load()
	#time.sleep(5)
	#m_inst.js("document.getElementById('zipByCityStateDiv').click();")
	
	#gets length of list
	#iterates through via the index
	#city_zip_cnt = m_inst.js("return document.getElementById('zipByCityStateDiv').children[0].length;")
	site = m_inst.source()
	target = site.find('div', {'id':'zipByCityStateDiv'})
	elements = target.find_all('div', {'class':'city-state-result'})
	for i in range(0, len(elements)):
		results.append(elements[i].find('strong').text)
	return results
m_inst = Zip_load('cities.csv')
m_inst.main()
print(m_inst.results)
m_inst.export()



	

