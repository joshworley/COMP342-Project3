import socket
import json

# port number
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get IP Address
ipAddress = input("Enter a host name (URL) or IP address for the FTP server: ")

try:
    # attempt to connect
    s.connect((ipAddress, int(port)))

    # list the valid actions available to the user
    print("These are the valid options")
    if (False):
        s.send(b'GET /sensors HTTP/1.1\r\n\r\n')
        reply = s.recv(1024)
        print(reply)
        reply = s.recv(1024)
        print(reply)

except:
    # failed to connect
    print("Failed to connect")
