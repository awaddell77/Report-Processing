import socket, time
#will be used mostly as a proof of concept and for testing
#actual "Eclipse client" will be functional or a collection of static methods
class Eclipse_client:
	def __init__(self):
		self.host = '192.168.99.249'
		self.port = 3210


def connect(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))
	sock.settimeout(45.0)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
	return sock
def read_msg(sock, buff_size = 1024):
	while True:
		mess = sock.recv(buff_size)

		#if len(mess) <= 0: return mess

		#n_mess = mess.decode('ascii')
		return mess
def write_msg(sock, message, encoding='ascii'):
	sock.send(bytes(message, encoding))
	return
def read_report(sock, buff_size=1024):
	results = []
	first = True
	old_msg = bytes()
	while True:
		'''if first:
			msg = read_msg(sock, buff_size)
			buff_size = int(msg.decode('ascii')) #just changed
			print(buff_size)
			first = False'''
		try:
			msg = read_msg(sock, buff_size)
		except Exception as E:
			print("EXCEPTION: ", E)
			return results
		msg_len = len(msg)
		if msg_len <= 0: return results


		#print("Recieved:")
		#print(msg)
		#print(msg_len)

		if msg[msg_len-1:msg_len] == b'\n' and old_msg:
			results += process_report_chunk(old_msg + msg)
			old_msg = bytes()
		elif msg[msg_len-1:msg_len] == b'\n' and not old_msg:
			results += process_report_chunk(msg)
		else: old_msg += msg

			


		#st = msg.decode('ascii')
		#results.append(chunk)

	return results




def process_report_chunk(data, encoding = 'ascii'):
	#@TODO: needs error handling for the decoding
	results = []
	text=  data.decode(encoding).split('\n')
	text_len = len(text)
	#each element should be a list since they represent rows in a spreadsheet/report
	#text_len-1 because split('\n') leaves a single '' at the end of the list
	results = [text[i] for i in range(0, text_len-1)]
	#for i in range(0, text_len-1): results.append(text[i])
	return results




host = '192.168.99.249'
port = 3210

#sock = connect('192.168.99.249',3210)
#read_msg(sock)
def test_read():
	sock = connect(host, port)
	return read_msg(sock)
def test_write(data = 'Testing'):
	sock = connect(host, port)
	write_msg(sock, data)
	return

def exit():
	sock = connect(host, port)
	write_msg(sock, 'EXIT')
def test_tax():
	sock = connect(host, port)
	comm = "TAX_RATE 98177 WA"
	write_msg(sock, comm)
	res = read_report(sock)
	return res


def read_rep_test(report_com = 'territory CLEISO'):
	start = time.time()
	res = []
	sock = connect(host, port)
	#write_msg(sock, 'report')
	write_msg(sock, report_com)
	try:
		res = read_report(sock)
	except Exception as E:
		print("ERROR: ", E)
		#write_msg(sock, 'EXIT')
	##finally

	end = time.time()
	time_len = end - start
	print("Returned {0} rows".format(len(res)))
	if time_len <= 60.0: print("Took {0} seconds".format(str(round(time_len,2))))
	else: print("Took {0} minutes".format(str(round(time_len/60, 2))))
	return res

#b_tst = test()
res = test_tax()

