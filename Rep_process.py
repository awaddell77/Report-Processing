from C_sort import *

class Rep_process:
	def __init__(self, fname):
		self.fname = fname
		self.data = C_sort(self.fname)

	def main(self):
		pass
	def clean_numbers(self):
		for i in range(1, len(self.data)):
			for i_2 in range(0, len(self.data[i])):

				temp = self.data[i][i_2]
				temp = temp.replace('*', '')
				
				if not temp: continue
				#if '.' in temp: temp = str(round(float(temp)))

				try:
					int(temp)
				except ValueError:
					n_temp = temp.split('.')
					if len(n_temp) == 2 and n_temp[0].isdigit() and n_temp[1].isdigit():
						temp = str(round(float(temp)))
					else: continue

				finally:
					self.data[i][i_2] = self.thousand_sep(temp)
				#print("Now it is: {0}".format(self.data[i][i_2]))
	def test(self):
		for i in range(0, len(self.data)):
			print(self.data[i])

	def str_to_num(self, item):
		if item.isalnum(): return item
		if '.' in item: return round(float(item))
	def thousand_sep(self, item):
		#does not support decimals
		if '.' in item: return item
		if not item.isdigit(): return item

		temp = ''
		s_len = len(item)
		if s_len <= 3: return item
		
		pivot = s_len-3
		for i in range(s_len, 0, -3): 

			#print("{0}:{1}".format(str(pivot), str(i)))
			#print(item[pivot:i])
			#if pivot is 0 that means there are 3 or less numbers left meaning that no new comma is needed
			if not pivot: temp = item[pivot:i] + temp
			else: temp = ',' + item[pivot:i] + temp
			if pivot < 3: pivot = 0
			else: pivot -= 3
		return temp
		


	def export(self):

		temp, ext = self.fname.split('.')[0], self.fname.split('.')[1]
		temp += '_new' + '.' + ext
		self.data.export(temp)

