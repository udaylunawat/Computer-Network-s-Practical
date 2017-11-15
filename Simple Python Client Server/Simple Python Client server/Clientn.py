#client
import socket
import time

HOST = "127.0.0.1"
PORT = 5454
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST,PORT))
while True:
	data = raw_input("Enter..... ")
	s.sendto(data,(HOST,PORT))
	print "Server says: " + s.recv(1024)
	if data=="bye" or s.recv(1024)=="bye":
		print "Exiting..........."
		time.sleep(1)
		break