import socket

serv_addr = ('localhost', 9090)

sock = socket.socket()
sock.connect(serv_addr)
data = input("Enter data for receive\n")
sock.send(data.encode())

result = sock.recv(1024)
sock.close()
print('Received data: %s' %(result))
