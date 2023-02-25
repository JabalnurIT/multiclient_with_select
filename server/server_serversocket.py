import os
import socketserver

# https://docs.python.org/3/library/socketserver.html

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.filename = self.request.recv(1024).strip().decode("utf-8")
        print("{} wrote:".format(self.client_address[0]))
        # print(self.data)
        path_file = "server/files/" + self.filename
        file = open(path_file, "rb")
        filesize = os.path.getsize(path_file)
        print(f">> Client meminta {self.filename} berukuran {filesize} bytes")

        # read file
        data = file.read()

        header = "file-name: "+self.filename+"\n"
        header = header + "file-size: "+str(filesize)+"\n\n\n"

        self.request.send(header.encode())

        self.request.sendall(data)

        self.request.send(b"<END>")

        print(f">> Server Telah Mengirim {self.filename} berukuran {filesize} bytes")

        file.close()

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
