from socket import *
HOST = '127.0.0.1'
PORT = 8000
mysocket = socket(AF_INET,SOCK_STREAM)
mysocket.connect((HOST, PORT))
i= True
while i is True:
	message = raw_input()
	mysocket.send(message)
	print 'awaiting reply'
	reply = mysocket.recv(1024)
	print 'received :', repr(reply)

mysocket.close()