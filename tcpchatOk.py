import socket
import time

class Tcpchat:
    def __init__(self) -> None:
        self.key = ""
        self.chatkey = ""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dst_host = ""
        self.src_host = "0.0.0.0"
        self.dst_port = ""
        self.src_port = ""
        r = open("tcp.txt", "r+")
        buffer_src_port = r.read().split("\n")
        self.src_port = int(buffer_src_port[0])
        self.dst_host = buffer_src_port[1]
        self.dst_port = buffer_src_port[2]
        self.s.bind((self.src_host, self.src_port))
        print(f"\u001b[36m[!]\u001b[0m\tListening on port {self.src_port}")

    def sendchat(self):
        message = input("Message: ")
        buffermessage = str(message).encode("UTF-8")
        self.s.sendto(buffermessage, self.dst_host)
    def check(self):
        while True:
            data = ""
            data, client = self.s.recvfrom(1024)
            if data == "":
                break
            self.dst_host = client[0]
            self.dst_port = client[1]
            print(f"\u001b[36m[!]\u001b[0m\t{data.decode("UTF-8")} received from {self.dst_host}:{self.dst_port}")
            data = ""