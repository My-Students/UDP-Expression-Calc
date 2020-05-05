import socket

server_ip = '127.0.0.1'
server_port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   

server.bind((server_ip, server_port)) 

while(True):
    data, address = server.recvfrom(4096)

    if(data.decode()[1:] == "exit()"):
        break

    equation = eval(data.decode()[0:])

    print( str(address) + ">> " + data.decode()[0:] + " = " + str(equation))

    server.sendto(str(equation).encode(), address)
    
server.close()



