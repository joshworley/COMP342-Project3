import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.17.112.74', 80))
s.send(b'GET /sensors HTTP/1.1\r\n\r\n')
reply = s.recv(1024)
print(reply)
reply = s.recv(1024)
print(reply)
