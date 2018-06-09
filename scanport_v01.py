import socket
import time
from random import randint

#HOST = '10.202.104.153' P'Poom
#HOST = '10.3.13.140' P'Ake
HOST = '10.3.13.140'
st = []

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('HOST IP ',HOST)
for i in range(10,80) :
        #delay = randint(0, 4)
        #time.sleep(delay)
        try:
                print('try to connect port',i)
                s.connect((HOST, i))
                print('port ', i ,' open')
                st.append(str(i))
                s.send(b"Aum")
                print('maessage sent')
        except:
                s.close()
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print('HOST IP  =>>', HOST)
print('Open Port >>', st)
