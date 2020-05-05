"""
Alessia De Giovannini
Server
"""
import socket

ip = "127.0.0.1"
porta = 20001
bufferSize = 1024

#Creazione del Socket Server 
socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socketServer.bind((ip, porta))
print("il signor Server la puo' ricevere")

#Fase di Ascolto  
while(True):
    datiSocket = socketServer.recvfrom(bufferSize)
    #recvfrom => istruzione bloccante 
    #ovvero il programma si ferma qui 
    #perchè il Server rimane in ascolto 
    msgC = datiSocket[0]
    address = datiSocket[1] #ip + porta 
    msgClient = "Messaggio dal signor Client:{}".format(msgC)
    ipClient = "IP del signor Client:{}".format(address)

    msgPerClient = eval(str(msgC,'utf-8'))
    bytesSend = str.encode(str(msgPerClient))

    print(msgClient)
    print(ipClient)

    #Messaggio ECHO al signor Client 
    socketServer.sendto(bytesSend, address)