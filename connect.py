import socket

HOST = ''
PORT = 10223                              #Define port serial 
BUFSIZ = 1024                             #Define buffer size
ADDR = (HOST, PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)                      #Start server,waiting for client
print('waiting for connection...')
tcpCliSock, addr = tcpSerSock.accept()