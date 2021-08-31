from socket import *
serverName='127.0.0.1'  # local Ip
serverPort=11500        # port

clientSocket = socket(AF_INET, SOCK_DGRAM)  # initiating client socket
clientSocket.connect((serverName, serverPort))  # connecting to client socket

i = 0

while i < 1:
    message = input('Type your message here: ')
    clientSocket.send(message.encode())
    message_received, serverAddress = clientSocket.recvfrom(1024)
    i += 1

message = input('Enter your name here')
clientSocket.send(message.encode())
message_received1, serverAddress1 = clientSocket.recvfrom(1024)
print(message_received1.decode())
clientSocket.close()

