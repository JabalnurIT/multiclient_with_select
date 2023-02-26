import socket
import select
import sys
import os

server_address = ('192.168.1.5', 5001)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

print("Server is Running and Listening ...")
print(f"Server is estabilished in {server_address}")

input_socket = [server_socket]

try:
    while True:
        read_ready, write_ready, exception = select.select(input_socket, [], [])
        
        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)        
            
            else:            	
                # receive filename
                filename = sock.recv(1024).strip().decode("utf-8")
                
                path_file = "server/files/" + filename
                file = open(path_file, "rb")
                filesize = os.path.getsize(path_file)
                print(f">> Client meminta {filename} berukuran {filesize} bytes")
                
                # read file
                data = file.read()
            
                header = "file-name: "+ filename + "\n"
                header = header + "file-size: " + str(filesize)+"\n\n\n"

                if data:
                    sock.send(header.encode())

                    sock.sendall(data)
                    sock.send(b"<END>")

                    print(f">> Server Telah Mengirim {filename} berukuran {filesize} bytes")
                else:                    
                    sock.close()
                    input_socket.remove(sock)
                file.close()
                
                



except KeyboardInterrupt:        
    server_socket.close()
    sys.exit(0)