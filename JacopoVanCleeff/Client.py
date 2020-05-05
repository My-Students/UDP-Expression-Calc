import socket as sck

HOST = 'localhost'
PORTA = 5000
BYTE  = 4096

s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)

mex = (input("Inserire l'equazione: ")).encode()

s.sendto(mex,(HOST,PORTA))
data, addr = s.recvfrom(BYTE)

print(f"Risultato ricevuto ... {data.decode()}  \nChiusura ... ")

s.close()