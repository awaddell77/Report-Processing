from C_sort import *
from dictionarify import *
from Dict_lst import *
from Dictify import *
from w_csv import *
from S_format import *
import math, random, datetime,os
class Spiff_report:
	def __init__(self, spiff_name, fname_eclipse='', fname_master='', **kwargs):
		#spiff_name is used as part of file names so it cannot have periods in it
		#probably should also check for system specific forbidden characters as well
		if '.' not in spiff_name: self.spiff_name = spiff_name
		else: raise SpiffNameError(spiff_name)
		#the eclipse file is the report produced by the system that contains the PN and description
		self.fname_eclipse = fname_eclipse
		#the master file is the document sent by the vendor that contains the spiff amounts and cat#s/keys/etc
		self.fname_master = fname_master
		self._matches = 0
		if not kwargs.get('t_dir',False): self.t_dir = os.getcwd()
		else: self.t_dir = kwargs['t_dir'] 
		self.session_id = spiff_session_id()
		if fname_eclipse and fname_master:
				self.e_data = Dict_lst(Dictify(fname_eclipse).main())
				#self.m_data = Dictify(fname_master).main()
				self.m_data = Dict_lst(Dictify(fname_master).main())
				#self.m_data_crits = Dictify(fname_master).just_header()
				self.m_data_crits = list(self.m_data.header)
				self.e_data.add_crit("Spiff Match")
				self.e_data.add_crit("CatMatch")
				self.m_data.add_crit("CatMatchM")
				
		else:
				self.e_data = ''
				self.m_data = ''
				self.m_data_crits = ''
				
	def import_data(self):
		#reimports data, useful if it wasn't instantiated with file names
		self.e_data = Dict_lst(dictionarify(fname_eclipse))
		self.m_data = Dictify(fname_master).main()
		self.m_data_crits = Dictify(fname_master).just_header()
		


	def clean(self):
		self.cust_clean()
	def cust_clean(self):
		pass
	def cat_extract(self):
		pass
	def match(self):
		self.cust_match()
	def cust_match(self):
		pass


	def status_report(self):
		print("{0} matches found.".format(len(self._matches)))
	def _matchfilename(self, fname, debug = False):
		#for testing purposes the fname argument will be left in
		#however the release version should use the spiff_name field instead
		fname_comp = fname.split('.')
		tempname, ext = fname_comp[0], fname_comp[1]
		if debug: tempname = tempname + '_' + self.session_id + '_DEBUG.' + ext
		else: tempname = tempname + '_' + self.session_id + '.' + ext
		return tempname
	def _matchfilenameb(self,fname, debug = False):
		#for testing purposes the fname argument will be left in
		#however the release version should use the spiff_name field instead
		if debug: tempname = self.spiff_name + '_' + self.session_id + '_DEBUG.csv'
		else: tempname = self.spiff_name + '_' + self.session_id + '.csv'
		return self.t_dir + os.sep + tempname
	def testfname(self,fname):
		return self._matchfilenameb(fname,True)


	def export_matches(self, fname=''):
		#When exporting matches the program will also export the master file
		#the master file should contain a new column listing all of the extracted/transformed skus/cat#s/etc
		#that the eclipse file matched against. Since the eclipse file will also have a new column containing 
		#the skus taken from the desc column it should help to expedite manual checking of any questionable matches
		self.export(self.e_data.data, None, self._matchfilenameb(fname))
		self.export(self.m_data.data, None, self._matchfilenameb(fname, True))
	def export_master(self, fname):
		self.export(self.m_data.data, None, fname)


		
	def export(self, data, c= [], fname = 'report_file.csv' ):
		if c: crit = c
		else: crit = list(data[0].keys())
		res = [crit]
		for i in data:
			res.append(S_format(i).d_sort(crit))
		w_csv(res, fname)
	def main(self):
		self.clean()
		self.match()
		self.export_matches()

def spiff_session_id():
	temp = datetime.datetime.now()
	return "{0}-{1}-{2}_{3}-{4}-{5}".format(str(temp.month), str(temp.day), str(temp.year), str(temp.hour), str(temp.minute), str(temp.second))
class SpiffNameError(Exception):
	def __init__(self, spiff_name):
		self.spiff_name = spiff_name
		self.forbidden = ['.']
	def __str__(self):
		return repr("{0} is not a valid spiff name. Spiff names cannot have periods or forbidden characters".format(self.spiff_name))


