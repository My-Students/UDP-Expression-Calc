import socket

server_ip = '127.0.0.1'
server_port = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

while(True):
    equazione = input(">> ")    

    client.sendto(equazione.encode(), (server_ip, server_port)) 

    if(equazione[0:] == "exit()"):  
        break

    risultato = client.recv(4096)  

    print(">> " + risultato.decode()[0:])

client.close()

