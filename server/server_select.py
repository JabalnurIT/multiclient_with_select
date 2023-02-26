import socket
import select
import sys
import os

# create a TCP/IP socket
server_address = ('192.168.1.5', 5001)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set socket options
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to a specific address and port
server_socket.bind(server_address)

# listen for incoming connections
server_socket.listen(5)

# print server status
print("Server is Running and Listening ...")
print(f"Server is estabilished in {server_address}")

# create a list of input sockets for the select() call
input_socket = [server_socket]

try:
    while True:
        # use select() to wait for input on sockets
        read_ready, write_ready, exception = select.select(input_socket, [], [])
        
        for sock in read_ready:
            if sock == server_socket:
                # if the input socket is the server socket, a new client is trying to connect
                # accept the connection and add the new socket to the input socket list
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)        
            
            else:            	
                # if the input socket is not the server socket, the client is requesting a file
                # receive the filename
                filename = sock.recv(1024).strip().decode("utf-8")
                
                # get the full path to the file
                path_file = "server/files/" + filename
                
                # open the file in binary mode
                file = open(path_file, "rb")
                
                # get the file size
                filesize = os.path.getsize(path_file)
                
                # print status message
                print(f">> Client meminta {filename} berukuran {filesize} bytes")
                
                # read the entire file into memory
                data = file.read()
                
                # construct the file header
                header = "file-name: "+ filename + "\n"
                header = header + "file-size: " + str(filesize)+"\n\n\n"
                
                # send the file header and data to the client
                if data:
                    sock.send(header.encode())
                    sock.sendall(data)
                    sock.send(b"<END>")
                    print(f">> Server Telah Mengirim {filename} berukuran {filesize} bytes")
                
                # if there is no data to send, close the socket and remove it from the input socket list
                else:                    
                    sock.close()
                    input_socket.remove(sock)
                
                # close the file
                file.close()
                
# handle keyboard interrupts
except KeyboardInterrupt:        
    server_socket.close()
    sys.exit(0)
