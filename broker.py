import socket
from message_broker.client_thread import ClientThread
from message_broker.client_name_handler import ClientNameHandler


class Broker:

    def __init__(self, ip, port):
        self.IP = ip
        self.PORT = port
        self.sock = None
        self.active_users= {}
        self.client_name_handler = ClientNameHandler()

    def create_connection(self):
        name_handler = self.client_name_handler
        print('Server is online')
        sock = self.create_socket(self.IP, self.PORT)
        sock.listen(5)

        while True:
            client_sock, client_address = sock.accept()
            client_name = name_handler.request_client_name(client_sock)
            name_handler.set_client_name(self, client_address, client_name)
            name = name_handler.get_client_name(self, client_address)
            print(self.active_users)

            c_thread = ClientThread(sock,
                                    client_sock,
                                    client_address,
                                    name)
            c_thread.start()

    def create_socket(self, IP, PORT):
        b_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        b_sock.bind((IP, PORT))
        return b_sock

    def close_connection_with(self, client):
        client.close()


broker = Broker('127.0.0.1', 8080)
broker.create_connection()
