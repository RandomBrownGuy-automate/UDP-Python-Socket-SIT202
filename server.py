from socket import *
serverName = '127.0.0.1'
serverPort = 11500

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))

message, clientAddress = serverSocket.recvfrom(1024)
print('Incoming from', str(clientAddress))
while True:
    i = 0
    while i < 2:
        message_received = message.decode()
        message_reply = str(message_received) + ", What is your name?"
        serverSocket.sendto(message_reply.encode(), clientAddress)
        message, serverAddress = serverSocket.recvfrom(1024)
        i += 5

        message_received1 = message.decode()
        print(message_received1)
        message_reply = "Hello" + str(message_received1) + ", Welcome to SIT202"
        serverSocket.sendto(message_reply.encode(), clientAddress)

        message = serverSocket.recvfrom(1024)


