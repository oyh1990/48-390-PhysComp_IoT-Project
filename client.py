import socket


HOST = '128.237.253.177'   # Enter IP or Hostname of your server
PORT = 12345    # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

print s.recv(1024)

#Lets loop awaiting for your input
while True:
	command = raw_input('')
	s.send(command)
	reply = s.recv(1024)
	print reply
