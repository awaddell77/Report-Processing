#mapping function
#factory-ish design 
import Fleurco_spiff, Pcp_spiff, Qmdrain_spiff, Mti_spiff, Jason_spiff, Crosswater_ammara_spiff, Delta_brizo_spiff, Barclay_spiff, Mtnplbg_spiff
def spiff_match_creator(spiff_type, eclipse_file, master_file):
	if spiff_type == 'Fleurco':
		return Fleurco_spiff.Fleurco_spiff('Fleurco', eclipse_file, master_file)
	if spiff_type == 'PCP':
		return Pcp_spiff.Pcp_spiff('PCP', eclipse_file, master_file)
	if spiff_type == 'QMDRAIN':
		return Qmdrain_spiff.Qmdrain_spiff('QMDRAIN', eclipse_file, master_file)
	if spiff_type == 'MTI':
		return Mti_spiff.Mti_spiff('MTI', eclipse_file, master_file)
	if spiff_type == 'Jason':
		return Jason_spiff.Jason_spiff('Jason', eclipse_file, master_file)
	if spiff_type == 'Crosswater/Ammara':
		return Crosswater_ammara_spiff.Crosswater_ammara_spiff('Crosswater_ammara', eclipse_file, master_file)
	if spiff_type == 'Delta/Brizo':
		return Delta_brizo_spiff.Delta_brizo_spiff('Delta_Brizo', eclipse_file, master_file)
	if spiff_type == 'Barclay':
		return Barclay_spiff.Barclay_spiff('Barclay', eclipse_file, master_file)
	if spiff_type == 'MTNPLBG':
		return Mtnplbg_spiff.Mtnplbg_spiff('MTNPLBG', eclipse_file, master_file)


def spiff_match_creator_b(spiff_type, eclipse_file, master_file):
	spiff_classes = { 'Fleurco':Fleurco_spiff.Fleurco_spiff, 'PCP':Pcp_spiff.Pcp_spiff, 
					'QMDRAIN':Qmdrain_spiff.Qmdrain_spiff, 'MTI':Mti_spiff.Mti_spiff, 
					'Jason':Jason_spiff.Jason_spiff, 'Crosswater/Ammara':Crosswater_ammara_spiff.Crosswater_ammara_spiff,
					'Delta/Brizo':Delta_brizo_spiff.Delta_brizo_spiff, 'Barclay':Barclay_spiff.Barclay_spiff, 
					'MTNPLBG':Mtnplbg_spiff.Mtnplbg_spiff


	}
	return spiff_classes[spiff_type](spiff_type.replace('/','_'), eclipse_file, master_file)
