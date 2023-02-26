import socket
import sys

HOST, PORT = "localhost", 9999
input = sys.stdin.readline()
input = input.split(" ")
command = input[0]
filename = input[1]

if command == "download":
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(filename + "\n", "utf-8"))

        # Receive data from the server and shut down
        header = str(sock.recv(1024), "utf-8")
        filename = header.split("\n")[0].split(" ")[-1]
        filesize = header.split("\n")[1].split(" ")[-1]

        file = open("client/files/"+filename, "wb")

        file_bytes = b""

        success = False

        while not success:
            data = sock.recv(1024)
            file_bytes += data
            if file_bytes[-5:] == b"<END>":
                success = True
        
        file.write(file_bytes)
        print(f">> Berhasil Menyimpan {filename} berukuran {filesize} bytes")

        file.close

