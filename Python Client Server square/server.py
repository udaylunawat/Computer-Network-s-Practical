from socket import *

HOST = '127.0.0.1'
PORT = 8000
mysocket = socket(AF_INET,SOCK_STREAM)
mysocket.bind((HOST, PORT))
mysocket.listen(1)
conn, addr = mysocket.accept()
print 'connected by', addr
i= True
while i is True:
	data = conn.recv(1024)
	print 'recieved',repr(data)
	#reply = raw_input('reply :')
	square = int(data)*int(data)
	conn.sendall(str(square))

conn.close()