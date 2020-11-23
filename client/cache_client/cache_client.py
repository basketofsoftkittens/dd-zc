import socket
import sys


HOST, PORT = "server", 9999


class CacheClient:
    def set(self, key, value):
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            data = bytes("set " + str(key) + " " + str(value) + "\n", "utf-8")
            sock.sendall(data)

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

            print("Sent:     {}".format(data))
            print("Received: {}".format(received))

    def get(self, key):
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            data = bytes("get " + str(key) + "\n", "utf-8")
            sock.sendall(data)

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            print("Sent:     {}".format(data))
            print("Received: {}".format(received))

            lines = received.splitlines()
            if len(lines) == 1:
                value = ""
            else:
                value = lines[0]

            return value.strip()


cache_client = CacheClient()
