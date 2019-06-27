from Sel_session import *
from dictionarify import *
import time
#results = []
class Zip_load:
	def __init__(self, source_file):
		self.source_file = dictionarify(source_file)
		self.results = []

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
h = zip_load()
print(h)



	

