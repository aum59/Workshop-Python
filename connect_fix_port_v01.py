import socket
import time
from random import randint

HOST = '127.0.0.1'
listen_PORT = 1234
send_PORT = 5678

print('HOST IP ',HOST)
for i in range(1,2) :
        #delay = randint(0, 4)
        time.sleep(0)
        try:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                print('try to connect port 1234 time',i)
                s.connect((HOST, 1234))
                s.send(b"Aum")
                print('maessage sent')
                data = s.recv(1024)
                print('Received massage from Server', repr(data))
                s.close()
        except:
                s.close()

