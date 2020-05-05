import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',2000))

while(True):
    data,address = s.recvfrom(4096)
    if(data.decode() == "shutdown"):
        print("stop.")
        break
    #value = bin(eval(data.decode())).encode() #eval(string) calcola le operazioni in una stringa e ritorna un int
    #s.sendto(value,address) 
    s.sendto(data,address)

s.close()