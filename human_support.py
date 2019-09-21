import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('localhost', 8080))#((IP_address, Port))

print "<Server> : The server does not have answer to client's queries. Provide human support. " 

while True:
    sockets_list = [sys.stdin, server]

    """ 
    If the server wants to send a message, then the if condition will hold true 
    below.If the user wants to send a message, the else condition will evaluate as true
    """
    read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print (message)
        else:
            message = sys.stdin.readline()
            server.send("< Team > : "+ message)
            sys.stdout.flush()
server.close()