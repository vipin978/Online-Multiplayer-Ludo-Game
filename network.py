import socket
import pickle

class Network:
	def __init__(self):
		self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server = '192.168.43.35'
		self.port = 8754
		self.addr = (self.server,self.port)
		self.p = self.connect()
		print(self.p)

	def connect(self):
		try:
			self.client.connect(self.addr)
			return self.client.recv(4098).decode()
		except:
			print("error")	

	def send(self,game,types):
		try:
			if types == "GET":
				self.client.send("GET".encode('utf-8').strip())
				return pickle.loads(self.client.recv(4098)) 
			elif types == "CLOSE":
				self.client.send(str.encode("CLOSE"))
				return	
			elif types == "SEND_ME":
				self.client.send(str.encode("SEND_ME"))
				return pickle.loads(self.client.recv(4098)) 	
			elif types == "POST":	
				self.client.send(str.encode("POST"))			
				self.client.send(pickle.dumps(game))
				return pickle.loads(self.client.recv(4098))	
		except socket.error as e:
			print(e)		