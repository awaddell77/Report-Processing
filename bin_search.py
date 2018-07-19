
from math import floor
def bin_search(lst, val):
	left = 0
	right = len(lst)-1
	while left <= right:
		mid = floor((right + left) / 2)
		if lst[mid] < val: left = mid + 1
		elif lst[mid] > val: right = mid - 1
		else: return mid
	return
