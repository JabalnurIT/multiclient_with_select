# import necessary modules
import socket
import sys

# specify server address and port
server_address = ('192.168.1.5', 5001)

# create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client_socket.connect(server_address)

# print message to indicate successful connection to server
print(f"Client is connected with server in {server_address}")

try:
    # start an infinite loop to receive user input
    while True:
        # prompt user to enter input
        inputs = input("Input: ")

        # split input into a command and filename
        inputs = inputs.split(" ")
        command = inputs[0]
        filename = inputs[1]

        # if command is "download"
        if command == "download":
            # send filename to server
            client_socket.sendall(bytes(filename + "\n", "utf-8"))

            # receive file header from server
            header = str(client_socket.recv(1024), "utf-8")

            # extract filename and filesize from header
            filename = header.split("\n")[0].split(" ")[-1]
            filesize = header.split("\n")[1].split(" ")[-1]

            # open file to write downloaded data
            file = open("client/files/"+filename, "wb")

            # initialize file_bytes to empty bytes
            file_bytes = b""

            # flag to indicate if file download is successful
            success = False

            # keep receiving data until the entire file is downloaded
            while not success:
                # receive data from server
                data = client_socket.recv(1024)

                # append received data to file_bytes
                file_bytes += data

                # check if the end of file tag is received
                if file_bytes[-5:]==b"<END>":
                    success = True
            
            # write file_bytes to file
            file.write(file_bytes)

            # print message to indicate successful file download
            print(f">> Berhasil Menyimpan {filename} berukuran {filesize} bytes")
            
            # close file
            file.close

        # if command is not "download"
        else:
            # print error message
            print("Your command is not download. You can only use command download nama_file\n")

# handle KeyboardInterrupt
except KeyboardInterrupt:
    # close client socket
    client_socket.close()

    # exit program
    sys.exit(0)
