import socket

ADDR = (socket.gethostbyname(socket.gethostname()),5553)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

msg = "heyyy...sokfadklfjkslfjkshkklasjlfjlds;jfljsal;jfl;sjldfkksfjksdjkfbksfjkasjkfj."

def send(msg):
	data = msg.encode('utf-8')
	length_of_msg = str(len(data)).encode('utf-8')
	length_of_msg += b' '*(64-len(length_of_msg))
	client.send(length_of_msg)
	client.send(data)
	print(client.recv(2048).decode())

send(msg)
send("DISCONNECT")