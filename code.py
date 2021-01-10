import socket
import threading
import os

os.system("tput setaf 3")
print("""\t\t-------------------------\n
\t\t\tOS CHAT APP\n
\t\t-------------------------""")
os.system("tput setaf 7")

net_family = socket.AF_INET
protocol = socket.SOCK_DGRAM

s = socket.socket(net_family, protocol)

ip = "192.168.42.223"
print("This is my IP : {0}".format(ip))
port = 1234
s.bind((ip, port))

os.system("tput setaf 2")
sip = input("Enter your Server IP (with which you want to Chat) : ")
os.system("tput setaf 7")


def receiver():
    while True:
        coming_data = s.recvfrom(1024)
        recv = coming_data[0].decode()
        os.system("tput setaf 2")
        print("\t\tOS_1 -> {0}".format(recv))
        os.system("tput setaf 7")

def sender():
    while True:
        msg = input("Me_(OS_2) : ")
        s.sendto(msg.encode(), (sip, port))

f1 = threading.Thread(target = receiver)
f2 = threading.Thread(target = sender)

f1.start()
f2.start()
