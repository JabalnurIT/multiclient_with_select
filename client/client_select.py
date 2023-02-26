import socket
import sys

server_address = ('127.0.0.1', 5001)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

try:
    while True:
        input = sys.stdin.readline()
        input = input.split(" ")
        command = input[0]
        filename = input[1]

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