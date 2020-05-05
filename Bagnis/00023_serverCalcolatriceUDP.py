"""
Server ECHO UDP 
"""
import socket

ip = '127.0.0.1'
porta = 2512

#creazione del socket UDP IPv4
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#bind del server per esporlo sulla rete
server.bind((ip, porta))   

#comunicazione dei dati del server all'utente
print(f"\nIl Server è online \t {ip}:{porta}")

while(True):
    #lettura dei dati inviati dall'utente
    data, indirizzo_client = server.recvfrom(4096)  
    
    #calcolo del risultato dell'equazione
    risultato = eval(data.decode())

    #comunicazione dei dati del calcolo all'utente
    print(str(indirizzo_client) + "\n\t" + data.decode() + " = " + str(risultato))    

    #restituisco il risultato al client
    server.sendto(str(risultato).encode(), indirizzo_client) 

#chiusura del socket
server.close()
