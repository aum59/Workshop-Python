import socket
import time
from random import randint

#HOST = '10.130.0.72' :22,80
#HOST = '10.3.100.99' :22
#HOST = '10.3.111.231'
#HOST = '10.229.1.80' :80

HOST = '127.0.0.1'
#HOST = '10.202.104.153'

print('HOST IP ',HOST)
for i in range(1,11)  :
        time.sleep(1)
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


