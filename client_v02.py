import socket
import time
#from random import randint

HOST = '127.0.0.1'
#HOST = '10.202.104.153'

listen_PORT = 5678
send_PORT = 1234


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
for i in range(1,11) :
        conn, addr = s.accept()
        print('Connected by', addr)
        conn.sendall(b"www.sanook.com")


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


