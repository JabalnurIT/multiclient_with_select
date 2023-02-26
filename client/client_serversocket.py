# import necessary modules
import socket
import sys

# specify the server's address and port number
HOST, PORT = "192.168.1.5", 9999
server_address = (HOST, PORT)

# create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # connect to the server
    sock.connect(server_address)
    print(f"Client is connected with server in {server_address}")

    # prompt the user to enter a command and filename
    inputs = input("Input: ")
    inputs = inputs.split(" ")
    command = inputs[0]
    filename = inputs[1]

    # if the command is "download"
    if command == "download":
        # send the filename to the server
        sock.sendall(bytes(filename + "\n", "utf-8"))

        # receive the file header from the server
        header = str(sock.recv(1024), "utf-8")

        # extract the filename and filesize from the header
        filename = header.split("\n")[0].split(" ")[-1]
        filesize = header.split("\n")[1].split(" ")[-1]

        # create a new file to write the downloaded data
        file = open("client/files/"+filename, "wb")

        # initialize a variable to store the file data
        file_bytes = b""

        # set a flag to indicate if the file download is successful
        success = False

        # receive data from the server and write it to the file
        while not success:
            data = sock.recv(1024)
            file_bytes += data
            if file_bytes[-5:] == b"<END>":
                success = True
        
        file.write(file_bytes)

        # print a message to indicate successful file download
        print(f">> Berhasil Menyimpan {filename} berukuran {filesize} bytes")

        # close the file
        file.close
        
    # if the command is not "download"
    else:
        # print an error message
        print("Your command is not download. You can only use command download nama_file\n")
