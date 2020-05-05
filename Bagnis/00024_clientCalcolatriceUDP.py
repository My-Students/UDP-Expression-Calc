"""
Client ECHO UDP 
"""
import socket

ip_server = '127.0.0.1'
porta_server = 2512

#creazione del socket UDP IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

while(True):
    #richiesta dell'equazione
    equazione = input("calcolo: ")

    #controllo del comando di chiusura
    if(equazione == "close()"):
        break

    #invio dei dati al server
    client.sendto(equazione.encode(), (ip_server, porta_server))

    #leggo il risultato
    risultato = client.recv(4096) 

    #comunicazione risultato all'utente
    print("risultato: " + risultato.decode())

#chiusura del socket
client.close()