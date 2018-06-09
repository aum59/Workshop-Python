import socket

HOST = ''
listen_PORT = 1234
send_PORT = 5678

print('Server IP ',HOST)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, listen_PORT))
s.listen(5)
print('Server listen 0n Port',listen_PORT)
addr = s.accept()
print('Connected by', addr)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#for i in range(1,11) :
#        addr = s.accept()
#        print('Connected by', addr)
        #conn.sendall(b"www.sanook.com")
#        try:
                #s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#                print('try to connect port 5678 time',i)
#                s.connect((HOST, send_PORT))
#                s.send(b"Aum")
#                print('maessage sent')
#                data = s.recv(1024)
#                print('Received massage from Server', repr(data))
#                s.close()
#        except:
#                s.close()

#for i in range(1,11)  :
#        time.sleep(1)
#        try:
#                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#                print('try to connect port 5678 time',i)
#                s.connect((HOST, send_PORT))
#                s.send(b"Aum")
#                print('maessage sent')
#                data = s.recv(1024)
#                print('Received massage from Server', repr(data))
#                s.close()
#        except:
#                s.close()
