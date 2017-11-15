#server
import socket
import time

HOST = "127.0.0.1"
PORT = 5454
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST,PORT))
while True:
	print "Client says: " + s.recv(1024)
	data = raw_input("Enter..... ")  
	s.sendto(data,(HOST, PORT))
	
	if data=="bye" or s.recv(1024)=="bye":
		print "Exiting.................."
		time.sleep(1)
		break