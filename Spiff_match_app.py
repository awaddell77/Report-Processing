from tkinter import *
from tkinter.filedialog import *
#from date_form import *
from text_l import *
from Spiff_report  import *
import getpass
from dictionarify import *


class Spiff_match_app:
	def __init__(self):
		#self.__username = input("Enter username: ")
		#self.__password = getpass.getpass('Enter password: ')
		#self.m_inst = Spiff_report()
		self.fname_master = ''
		self.fname_spiffs = 'Select Spiff File'
		window = Tk()
		self.lbl = Label(window, text='Enter new file name')
		self.lbl2 = Label(window, text="Submit data")
		self.lbl3 = Label(window, text='Select matching algorithm:')
		self.lbl4 = Label(window, textvariable = self.fname_master, padx = 10)
		self.ent_field = Text(window, height = 1, width = 10)
		#function name only, no parentheses at the end
		self.btsub = Button(window, text="Click to create match file", command = self.get_text) 
		#master
		self.btsub2 = Button(window, textvariable=self.fname_spiffs, command = self.get_file)
		#preview
		self.btsub3 = Button(window, text="Select Product File", command = lambda : self.get_file(False))
		self.lstbox = Listbox(window)
		self.opts = ['MTI', 'Delta', 'Jason', 'Fleurco']
		
		for opt in self.opts: self.lstbox.insert(END, opt)


		self.ent_field.pack()
		self.lbl.pack()
		self.btsub.pack()
		self.btsub2.pack()
		self.btsub3.pack()
		self.lbl3.pack()
		self.lstbox.pack()
		self.lbl2.pack()

		self.fname = ''
		self.dir_n = ''
		self.lst = []

		#self.creds = text_l('C:\\Users\\Owner\\Documents\\Important\\catcred.txt')
		window.mainloop() 
	def get_text(self):
		StringVar = self.ent_field.get('1.0', 'end')
		StringVar = re.sub('\n', '', StringVar)
		print(StringVar)
		##self.m_inst.cat_obj.reconnect()
		#self.m_inst.standardize_keys()
		self.lst.append(StringVar)
		self.lbl2["text"] = "Submitted data"
		self.ent_field.delete('1.0', 'end')
		spiff_opt = self.lstbox.get(self.lstbox.curselection()[0])
		print(spiff_opt)
		if spiff_opt == 'MTI':
			from Mti_spiff import *
			m_inst = Mti_spiff(self.fname_master, self.fname_spiffs)


		#self.m_inst.export(StringVar)
	def get_lst(self):
		return self.lst
	def get_file(self, master = True):
		fname1 = askopenfilename()
		#if '.csv' not in fname1.split('/')[len(fname1.split('/'))-1]:
			#raise TypeError("Can only import CSV files")
		if master:
			self.fname_master = fname1
		else:
			self.fname_spiffs = fname1
	def set_dir(self):
		new_dir = askdirectory()
		self.dir_n = new_dir
		print("Directory is now", new_dir)
	def sub_id(self):
		pass



#test_inst = Scraper_gui()
if __name__ == "__main__":
	test_inst = Spiff_match_app()
