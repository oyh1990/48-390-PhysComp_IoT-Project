import socket
import subprocess as sp
import time
import random

 
HOST = '128.237.253.177'   # Server IP or Hostname
PORT = 12345    # Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
extProc = sp.Popen(['python','run.py']) 
status = sp.Popen.poll(extProc) # status should be 'None'
#managing error exception
try:
    s.bind((HOST, PORT))
except socket.error:
    print 'Bind failed '
     
s.listen(5)
print 'Socket awaiting messages'
(conn, addr) = s.accept()
print 'Connected'

conn.send('type in "OFF"')

# awaiting for message
while True:
    data = conn.recv(1024)
    # process your message
    if data == 'OFF':               
    	num1 = random.randint(1, 10)
    	num2 = random.randint(1, 10)
    	answer = str(num1 * num2)
    	text = "What is " + str(num1) + " times " + str(num2)
    	sp.call('echo ' + text + ' |festival --tts', shell=True)
        conn.send(text)
    	answer1 = conn.recv(1024)
    	if(answer1==answer):
            reply = 'good morning!'
            sp.call('echo ' + reply + ' |festival --tts', shell=True)
            break
        else:
            reply='WRONG ANSWER! type "OFF" to get another question'
            conn.send(reply)
    else:
        reply = 'please type "OFF"'
        conn.send(reply)

sp.Popen.terminate(extProc) # closes the process
status = sp.Popen.poll(extProc) # st
conn.close() # Close connections