from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
#from date_form import *
from text_l import *
from Spiff_report  import *
import getpass
from dictionarify import *
from tkinter.messagebox import *
from loadJson import *
from spiff_match_creator import *
#from Mti_spiff import *

class Spiff_match_app:
	def __init__(self):
		#self.__username = input("Enter username: ")
		#self.__password = getpass.getpass('Enter password: ')
		#self.m_inst = Spiff_report()
		self.fname_master = ''
		self.fname_eclipse = ''
		self.fname_spiffs = 'Select Spiff File'
		self.master_locs = loadJson('spiff_master_loc.json')
		window = Tk()
		self.lbl = Label(window, text='Select Spiff')
		self.lbl2 = Label(window, text="Submit data")
		self.lbl3 = Label(window, text='Select matching algorithm:')
		self.lbl4 = Label(window, textvariable = self.fname_master, padx = 10)
		#self.ent_field = Text(window, height = 1, width = 10)
		#function name only, no parentheses at the end
		self.btsub = Button(window, text="Click to create match file", command = self.get_text) 
		#master
		self.btsub2 = Button(window, text = 'Select Master File', command = self.get_file, state = 'disabled')
		#preview
		self.btsub3 = Button(window, text="Select Eclipse File", command = lambda : self.get_file(False))
		#self.lstbox = Listbox(window)
		#self.opts = ['MTI', 'Delta', 'Jason', 'Fleurco'] #more to be added
		self.spiff_select = ttk.Combobox(window, values = ['MTI', 'Delta', 'Jason', 'Fleurco', 'PCP', 'QMDRAIN'])
		self.auto_custom = ttk.Combobox(window, values = ['Auto', 'Custom (Select Master file yourself)'])
		self.auto_custom.bind("<<ComboboxSelected>>", self.refresh_cust)
		
		#for opt in self.opts: self.lstbox.insert(END, opt)

		#self.ent_field.pack()
		self.lbl.pack()
		self.spiff_select.pack()
		self.auto_custom.current(0)
		self.auto_custom.pack()
		
		#
		self.btsub2.pack()
		self.btsub3.pack()
		#self.lbl3.pack()
		#self.lstbox.pack()
		#self.lbl2.pack()
		self.btsub.pack()


		self.fname = ''
		self.dir_n = ''
		self.lst = []

		
		window.mainloop() 
	def get_text(self):
		#StringVar = self.spiff_select.get()
		spiff_opt = self.spiff_select.get()
		if self.auto_custom.get() == 'Auto': self.fname_master = self.master_locs[spiff_opt]
		report_inst = spiff_match_creator(spiff_opt, self.fname_eclipse, self.fname_master)

		print(self.fname_eclipse)
		print(self.fname_master)
		report_inst.main()


		StringVar = self.fname_eclipse
		#StringVar = re.sub('\n', '', StringVar)
		print(StringVar)
		#self.lst.append(StringVar)
		#self.lbl2["text"] = "Submitted data"
		#self.ent_field.delete('1.0', 'end')
		#spiff_opt = self.lstbox.get(self.lstbox.curselection()[0])
		#print(spiff_opt)
		#if spiff_opt == 'MTI':
			#from Mti_spiff import *
			#m_inst = Mti_spiff(self.fname_master, self.fname_spiffs)
			#pass


		#self.m_inst.export(StringVar)
	def get_lst(self):
		return self.lst
	def get_file(self, master = True):
		fname1 = askopenfilename()
		if '.csv' not in fname1.split('/')[len(fname1.split('/'))-1]:
			showerror("File Type Error", "Can only process csv files")
			return
			#raise TypeError("Can only import CSV files")
		
		if master:
			self.fname_master = fname1
		else:
			self.fname_eclipse = fname1
	def set_dir(self):
		new_dir = askdirectory()
		self.dir_n = new_dir
		print("Directory is now", new_dir)
	def sub_id(self):
		pass
	def refresh_cust(self, event):
		opt_sel = self.auto_custom.get()
		#print("It's working!")
		if opt_sel != 'Auto':
			self.btsub2['state'] = 'normal'
			
		else:
			self.btsub2['state'] = 'disabled'

			



#test_inst = Scraper_gui()
if __name__ == "__main__":
	test_inst = Spiff_match_app()
