import gevent
from gevent.server import StreamServer
from gevent.socket import socket


class STServer(StreamServer):

    def __init__(self, address):
        super().__init__(address)

    def handle(self, socket, address):
        print('New connection from %s:%s' % address)
        socket.sendall(b'Welcome to the echo server! Type quit to exit.\r\n')
        # using a makefile because we want to use readline()
        while True:
            data = socket.recv(1024)
            print('{0} client send data is {1}'.format(address, data.decode()))#b'\xe8\xbf\x99\xe6\xac\xa1\xe5\x8f\xaf\xe4\xbb\xa5\xe4\xba\x86'
            gevent.sleep(1)
            if data == 'exit' or not data:
                print('{0} connection close'.format(address))
                socket.send(bytes('Connection closed!'),'UTF-8')
                break
            socket.send(bytes('Hello, {0}'.format(data),"UTF-8"))#TypeError: a bytes-like object is required, not 'str'


def startServer():
    print("starting server...")
    serv = STServer(('0.0.0.0', 8080))
    serv.serve_forever()


if __name__ == "__main__":
    startServer()