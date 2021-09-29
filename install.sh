
if [ $(id -u) -ne 0 ]; then
    echo "[-] Need root"
    exit 1

fi
apt-get install python3-pip
pip3 install colored
cp /home/kali/Desktop/vurgun/main/vurgun /bin/
chmod +x /bin/vurgun

