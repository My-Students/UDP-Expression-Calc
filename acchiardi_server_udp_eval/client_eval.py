import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while(True):
    msg = input("Put a mathematical operation:\t")
    if(msg == "shutdown"):
        print("Stop.")
        break
    s.sendto(msg.encode(),('localhost',2000))
    data = s.recv(4096)
    #data.decode()
    print(data)

s.close()