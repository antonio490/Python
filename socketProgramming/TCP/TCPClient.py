

# TCP client 

# On this code snippet we are making some assumptions that we should comment.
# The first assumption we are making is assumming that the connection will always succeed, and the
# second is that the server is always expecting us to send some data (as oppossed to servers that 
# expect to send data to you first and await for a response). Our third assumption is that
# the server will always send us some data back in a timely fashion.


import socket

target_host = "0.0.0.0"
target_port = 9998

# create a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the client

client.connect((target_host, target_port))

# send some data

client.send("GET / HTTP/1.1\r\n\nHost: google.com\r\n\r\n".encode())

# receive some data

response = client.recv(4096)

print(response)


