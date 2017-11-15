from socket import *

HOST = ''
PORT = 8000
mysocket = socket(AF_INET, SOCK_STREAM)
mysocket.bind((HOST, PORT))
mysocket.listen(1)
conn, addr = mysocket.accept()
print 'connected by', addr
msg = ''
reply = raw_input()
if reply[0] == '0':
	msg = msg + '01'
else:
	msg = msg + '10'

for i in xrange(1,len(reply)):
	if reply[i] == '0':
		if msg[len(msg)-1] == '1':
			msg = msg + '01'
		else:
			msg = msg + '10'
	else:
		if msg[len(msg)-1] == '1':
			msg = msg + '10'
		else:
			msg = msg + '01'

conn.sendall(msg)
conn.close()