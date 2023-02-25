import socket
import sys
import tqdm

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

        file_bytes = b"ada"

        success = False

        progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(filesize))

        while not success:
            data = sock.recv(1024)
            if file_bytes[-5:] == b"<END>":
                success = True
            else:
                file_bytes += data
            progress.update(1024)
        
        file.write(file_bytes)

        file.close

    # print("Sent:     {}".format(data))
    # print("Received: {}".format(received))

