import socket
#import time

HOST = '127.0.0.1'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
for i in range(1,2) :
#while True :
        conn, addr = s.accept()
        print('Connected by', addr)
        conn.sendall(b"www.sanook.com")
        #s.close()
        #except:
            #s.close()
