import socket
import sys
import time
import datetime
from random import randint

host = '192.168.1.1'
Port = []
print('HOST IP ', host)
t1 = datetime.datetime.now()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for port in range(10, 1025):
        delay = 1 / randint(100, 900)
        time.sleep(delay)
        try:
                sock.connect((host, port))
                print('port {}: open'.format(port))
                Port.append(str(port))
        except KeyboardInterrupt:
                print('Abort Scanning.')
                sock.close()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sys.exit()
        except:
                sock.close()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t2 = datetime.datetime.now()
print('IP ' + host + ' Open Port: ', str(Port).strip('[]').replace("'",''))
print("time to complete scanning: " + str(t2.minute - t1.minute)
                             + ':' + str(t2.second - t1.second)
                             + ':' + str((t2.microsecond - t1.microsecond)%1000000))
