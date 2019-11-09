
def thousand_sep(item):
	temp = ''
	s_len = len(item)
	if s_len <= 3: return item
	#if end_point < 0: end_point = len(item)-1
	#else: dec = item.split('.')[1]
	
	pivot = s_len-3
	for i in range(s_len, 0, -3): 

		print("{0}:{1}".format(str(pivot), str(i)))
		print(item[pivot:i])
		#if pivot is 0 that means there is less than 3 left meaning that no new comma is needed
		if not pivot: temp = item[pivot:i] + temp
		else: temp = ',' + item[pivot:i] + temp
		if pivot < 3: pivot = 0
		else: pivot -= 3
	return temp
test_n = '7000000001'
res = thousand_sep(test_n)
print("RESULT: ", res)
#print(thousand_sep(test_n))