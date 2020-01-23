
from Dictify import *
from Dict_lst import Dict_lst


def find_match(dct, key, val):
	  
	if int(dct[key]) * 100 == val: return True
def match(tax_fname, eclipse_fname):
	tax_data, eclipse_data = Dict_lst(Dictify(tax_fname).main()), Dict_lst(Dictify(eclipse_fname).main())
	eclipse_data.add_crit('New Rate')
	
	for i in range(0, len(eclipse_data)):
		temp = eclipse_data.get_index(i)
		print("Processing {0}...".format(temp['ZIP']) + ' '*20, end = '\r')

		e_rate = temp['Rate']

		for i_2 in range(0, len(tax_data)):
			temp_tax = tax_data.get_index(i_2)
			if temp['ZIP'] == temp_tax['Destination Zip'] and temp['ST'] == temp_tax['Destination State'] and float(temp['Rate']) != float(temp_tax['Combined Rate']) * 100:
				temp['New Rate'] = float(temp_tax['Combined Rate']) * 100
				break
			elif temp['ZIP'] == temp_tax['Destination Zip'] and temp['ST'] == temp_tax['Destination State'] and float(temp['Rate']) == float(temp_tax['Combined Rate']) * 100:
				temp['New Rate'] = "Unchanged"
	eclipse_data.export()


	return tax_data, eclipse_data


def match_to_vertex(tax_fname_old, tax_fname_new):
	change_count = 0
	tax_data_old, tax_data_new = Dict_lst(Dictify(tax_fname_old).main()), Dict_lst(Dictify(tax_fname_new).main())
	tax_data_new.add_crit('New Rate')
	
	for i in range(0, len(tax_data_new)):
		temp = tax_data_new.get_index(i)
		print("Processing {0}...".format(temp['Destination Zip']) + ' '*20, end = '\r')

		e_rate = temp['Combined Rate']

		for i_2 in range(0, len(tax_data_old)):
			temp_tax = tax_data_old.get_index(i_2)
			if temp['Destination Zip'] == temp_tax['Destination Zip'] and temp['Destination State'] == temp_tax['Destination State'] and float(temp['Combined Rate']) != float(temp_tax['Combined Rate']) :
				temp['New Rate'] = float(temp_tax['Combined Rate'])
				change_count += 1

				break
			elif temp['Destination Zip'] == temp_tax['Destination Zip'] and temp['Destination State'] == temp_tax['Destination State'] and float(temp['Combined Rate']) == float(temp_tax['Combined Rate']):
				temp['New Rate'] = "Unchanged"
				break
	tax_data_new.export()
	print()
	print("{0} changes detected".format(change_count))


	return tax_data_old, tax_data_new





#tax_d, eclipse_d = match('jan_tax_all.csv', 'eclipse_tax_jan.csv')
tax_d, tax_d_new = match_to_vertex('december_2019_tax.csv', 'jan_tax_all.csv')