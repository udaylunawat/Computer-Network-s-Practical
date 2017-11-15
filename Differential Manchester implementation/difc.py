from socket import *

HOST = '127.0.0.1'
PORT = 8000
mysocket = socket(AF_INET, SOCK_STREAM)
mysocket.connect((HOST , PORT))
reply = mysocket.recv(1024)
masg = ''
print 'recieved : ', repr(reply)
mysocket.close()