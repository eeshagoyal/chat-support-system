import socket
import select
from thread import *
import sys
from text_queries import text_queries #new

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
the first argument AF_INET is the address domain of the socket. This is used when we have an Internet Domain
with any two hosts
The second argument is the type of socket. SOCK_STREAM means that data or characters are read in a continuous flow
"""
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 8080))#((IP_address, Port)) 
#binds the server to an entered IP address and at the specified port number. The client must be aware of these parameters

server.listen(100)
#listens for 100 active connections. This number can be increased as per convenience
list_of_clients=[]

dictionary = text_queries().getquery() 

def clientthread(conn, addr):
    conn.send("Welcome to this chatroom!")
    #sends a message to the client whose user object is conn
    while True:
            try:     
                message = conn.recv(2048)
                message = message[:-1]
                # remove the extra new line character 
                if message:
                    print (message)
                    #prints the message and address of the user who just sent the message on the server terminal

                    if dictionary.get(message[11:]):
                        # message[11:-1] remove the first 11 characters "< Team > : " or "<Client> : "
                        print ("<Server> : " + dictionary[message[11:]])
                        conn.send("<Server> : " + dictionary[message[11:]])       

                    else :
                        message_to_send = message 
                        broadcast(message_to_send, conn)
                else:
                    remove(conn)
            except:
                continue

def broadcast(message,connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()
    """
    Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr which contains
    the IP address of the client that just connected
    """
    list_of_clients.append(conn)
    #maintains a list of clients for ease of broadcasting a message to all available people in the chatroom
    print (addr[0] + " connected")
    #Prints the address of the person who just connected
    start_new_thread(clientthread,(conn,addr))
    #creates and individual thread for every user that connects

conn.close()
server.close()




