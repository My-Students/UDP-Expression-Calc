import socket
import math

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


s.bind(('127.0.0.1', 80))

"""OP intera"""
dato, address = s.recvfrom(4096)
dato.decode()

ris = eval(dato)

ris = str(ris)

print(f"Connected to : {address} ")
s.sendto(ris.encode(), address)
    
s.close()