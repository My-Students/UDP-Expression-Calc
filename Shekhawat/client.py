import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

"""Mando l'intera operazione """

oper = input("Inseire l'intera operazione (senza spazi) : ")
s.sendto(oper.encode(), ('127.0.0.1', 80))

""" Ricevo il risultato"""
ris , address =  s.recvfrom(4096)

msg = ris.decode()
print(f"Il risultato e' : {msg}")

s.close()