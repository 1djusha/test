import socket
import sys
import asyncio

serv_addr = ('localhost', 9090)

sock = socket.socket()
sock.bind(serv_addr)
sock.listen(5)

while True:
    end = input('If you want to exit plese input "end"\n')
    if end == 'end':
        sock.close()
        sys.exit()
    
    conn, addr = sock.accept()
    print('Client %s connected' %(str(addr)))
    data = conn.recv(1024).decode()
    if not data:
        break
    print('Received data: %s' %(data))
    conn.send((data.upper()).encode())
    conn.close()
