import os
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):

        # self.request is the TCP socket connected to the client
        # Receive filename from the client
        self.filename = self.request.recv(1024).strip().decode("utf-8")

        # Construct the path to the file based on filename received from the client
        path_file = "server/files/" + self.filename

        # Open the file in binary mode for reading
        file = open(path_file, "rb")

        # Get the file size in bytes
        filesize = os.path.getsize(path_file)

        # Print message indicating which file is being requested and its size
        print(f">> Client meminta {self.filename} berukuran {filesize} bytes")

        # Read the file contents
        data = file.read()

        # Construct the response header to include filename and file size
        header = "file-name: "+self.filename+"\n"
        header = header + "file-size: "+str(filesize)+"\n\n\n"

        # Send the header to the client
        self.request.send(header.encode())

        # Send the file contents to the client
        self.request.sendall(data)

        # Send a terminating string to indicate the end of the file
        self.request.send(b"<END>")

        # Print message indicating that the server has sent the file to the client
        print(f">> Server Telah Mengirim {self.filename} berukuran {filesize} bytes")

        # Close the file
        file.close()

if __name__ == "__main__":
    # Set the IP address and port number for the server
    HOST, PORT = "192.168.1.5", 9999
    server_address = (HOST, PORT)

    # Print message indicating that the server is running and listening
    print("Server is Running and Listening ...")
    print(f"Server is estabilished in {server_address}")

    # Create the server, binding to the IP address and port number specified
    with socketserver.TCPServer(server_address, MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
