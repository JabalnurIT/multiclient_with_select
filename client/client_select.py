import socket
import sys

server_address = ('192.168.1.5', 5001)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
print(f"Client is connected with server in {server_address}")

try:
    while True:
        inputs = input("Input: ")
        inputs = inputs.split(" ")
        command = inputs[0]
        filename = inputs[1]

        if command == "download":
            # send filename to download
            client_socket.sendall(bytes(filename + "\n", "utf-8"))

            # receive data

            header = str(client_socket.recv(1024), "utf-8")
            filename = header.split("\n")[0].split(" ")[-1]
            filesize = header.split("\n")[1].split(" ")[-1]

            # save file
            file = open("client/files/"+filename, "wb")

            file_bytes = b""

            success = False

            while not success:
                data = client_socket.recv(1024)
                file_bytes += data
                if file_bytes[-5:]==b"<END>":
                    success = True
            
            
            file.write(file_bytes)
            print(f">> Berhasil Menyimpan {filename} berukuran {filesize} bytes")
            

            file.close

except KeyboardInterrupt:
    client_socket.close()
    sys.exit(0)