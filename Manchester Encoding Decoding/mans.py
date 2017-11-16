from socket import *

HOST = ''
PORT = 8000
mysocket = socket(AF_INET, SOCK_STREAM)
mysocket.bind((HOST, PORT))
mysocket.listen(1)
conn, addr = mysocket.accept()
print 'connected by', addr
reply1 = ''
reply = raw_input()
for i in reply:
	if i == '0':
		reply1 = reply1 + '10'
	else:
		reply1 = reply1 + '01'
conn.sendall(reply1)
conn.close()