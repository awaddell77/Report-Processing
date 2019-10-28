#mapping function
#factory-ish design 
import Fleurco_spiff, Pcp_spiff, Qmdrain_spiff
def spiff_match_creator(spiff_type, eclipse_file, master_file):
	if spiff_type == 'Fleurco':
		return Fleurco_spiff('Fleurco', eclipse_file, master_file)
	if spiff_type == 'PCP':
		return Pcp_spiff.Pcp_spiff('PCP', eclipse_file, master_file)
	if spiff_type == 'QMDRAIN':
		return Qmdrain_spiff('QMDRAIN', eclipse_file, master_file)

