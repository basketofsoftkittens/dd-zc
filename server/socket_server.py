import socketserver
import time

from lru_cache.lru_cache import lru_cache


class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            if not self.rfile.peek():
                break
            data = self.rfile.readline().strip()
            print("{} wrote: {}".format(self.client_address[0], data))
            data_split = data.split()

            command = data_split[0].lower()
            key = data_split[1].lower()

            if command == b"set":
                value = data_split[2]
                lru_cache.set(key, value)
                self.wfile.write(b"END\r\n")

            elif command == b"get":
                output = b""

                if lru_cache.get(key):
                    value = lru_cache.get(key)
                    output += b"%s\r\n" % value

                self.wfile.write(output + b"END\r\n")


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
