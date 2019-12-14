import requests, sqlite3
from dictionarify import *
class Ca_tax_rates:
	def __init__(self, fname = ''):
		self.fname = fname
		if fname: self.data = dictionarify(fname)
		else: self.data = ''
		self.dbase= 'ca_taxes.db'
		self.table = 'ca_tax_rates'
		self._conn = sqlite3.connect(self.dbase)
		self.cursor = self._conn.cursor()

	def refresh(self):
		#should also be checking fname
		#if fname then it should check against csv contents
		self._load_tax_data()

	def _get_tax_data(self):
		 rdata = requests.get(
		 	"http://cdtfa.ca.gov/dataportal/api/odata/Effective_Sales_Tax_Rates").json()
		 data = rdata['value']
		 return data
	def _table_check(self):
		print("TABLE NAME:", self.table)
		t_query = "SELECT name FROM sqlite_master WHERE type = \"table\" AND name = \"{0}\"".format(self.table)

		self.cursor.execute(t_query)
		if not self.cursor.fetchall():
			t_query = "CREATE TABLE {0} (ID INTEGER PRIMARY KEY AUTOINCREMENT, CITY CHAR(50), COUNTY CHAR(50), RATE FLOAT(53), IS_INC BOOLEAN)".format(self.table) 
			self.cursor.execute(t_query)
			self._conn.commit()
			print("Created table {0}".format(self.table))
		else: print("Did not create table {0}".format(self.table))
		return
	def execute_query(self, comm):
		#testing only
		#should not be in final version of class
		if comm.split(' ')[0].upper() in ["CREATE", "INSERT", "DELETE", "UPDATE"]: raise RuntimeError("Not a query")
		self.cursor.execute(comm)
		data = self.cursor.fetchall()
		return data
	def test(self):
		self._table_check()
		return







	def _load_tax_data(self):
		data = self._get_tax_data()
		self._table_check()
		self.cursor.execute("SELECT COUNT(*) FROM ?", self.table)
		db_data = self.cursor.fetchall()

		#if the table doesn't have any rows it fills it with the data it took from cdtfa
		if not db_data[0][0]:
			for i in range(0, len(data)):
				
				if data[i]["IsIncorporated"] == 'False': inc = 0
				else: inc = 1 
				print("Inserting data now")
				cmd = "INSERT INTO {0} ".format(self.table)
				self.cursor.executemany(cmd + '(CITY, COUNTY, RATE, IS_INC) VALUES (?,?,?,?)', 
					(data[i]["City"], data[i]["County"], data[i]["Rate"], inc ))
				self._conn.commit()
		#NEEDS TESTING!!


m_inst = Ca_tax_rates()
m_inst.test()
#m_inst.refresh()



