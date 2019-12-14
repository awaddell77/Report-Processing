
from Rep_process import *
class Cat_extract(Rep_process):
	def __init__(self, fname, ):
		super().__init__(fname)
	def main(self):
		#requires pn, desc, and cat# columns (in that order)
		for i in range(0, len(self.data)):
			if not self.data[i][2]:
				#self.data[i][2] = self.extract_cat(self.data[i][1]) 
				#temp = self.extract_cat(self.data[i][1])
				#if not temp: self.data[i]
				self.data[i].append(self.extract_cat(self.data[i][1])) 
		self.export()
	
	def extract_cat(self, cell):
		temp = cell.replace('(', ' ').replace(')', ' ')
		temp = temp.split(' ')
		for i in range(0, len(temp)):
			if not temp[i].isalpha() and  len(temp[i]) >2 and self.str_check(temp[i]): 
				return temp[i]
		def_cat = ' '.join(temp[1:])
		if len(def_cat) > 40: def_cat = def_cat[:40]
		return def_cat
	def str_check(self, text):
		#other ascii symbols (like /, &, and others) also make a string alpha-numeric 
		#need to check for those 
		temp_b = False
		#the function that calls this has already checked to see if the
		#string is is non-numeric via the isalpha() method
		#this is to check for false positives (like "BBBB-AAAA", which would be deemed alphanumeric despite containing no numbers)
		if '-' not in text: return True 

		temp = text.split('-')
		
		for i in range(0, len(temp)):
			if not temp[i].isalpha(): temp_b = True
		return temp_b

m_tst = Cat_extract("cat_test.csv")
m_tst.main()
