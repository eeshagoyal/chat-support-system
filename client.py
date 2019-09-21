import socket
import select
import sys
#from text_queries import text_queries #new

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#if len(sys.argv) != 3:
#    print "Correct usage: script, IP address, port number"
#    exit()
#IP_address = str(sys.argv[1])
#Port = int(sys.argv[2])
server.connect(('127.0.0.1', 65432))#((IP_address, Port))

#dictionary = text_queries().getquery() #new

while True:
    # maintains a list of possible input streams 
    sockets_list = [sys.stdin, server]

    """ 
    There are two possible input situations. Either the 
    user wants to give  manual input to send to other people, 
    or the server is sending a message  to be printed on the 
    screen. Select returns from sockets_list, the stream that 
    is reader for input. So for example, if the server wants 
    to send a message, then the if condition will hold true 
    below.If the user wants to send a message, the else 
    condition will evaluate as true
    """
    read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            #print dictionary.keys() #new
            #if dictionary.has_key(str(message)): #new
                #message = dictionary[message] #new
            print message
        else:
            message = sys.stdin.readline()
            #if message in list(dictionary.keys()): #new
                #message = dictionary[message] #new
            server.send(message)#"<Client> : "+ 
            #sys.stdout.write("<You> : ")
            sys.stdout.flush()
server.close()