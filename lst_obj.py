#test

class lst_obj:
	def __init__(self, lst_data = [1,2,3,4,5,6]):
		self.lst_data = lst_data
		self.end = len(lst_data)
	def  __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n < self.end:
			res = self.lst_data[self.n]
			self.n += 1
			return res
		else:
			raise StopIteration

m_inst = lst_obj()
for elem in m_inst:
	print(elem)