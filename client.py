import socket
from message_broker.chat import Chat

def main():
    class Client:

        def __init__(self,):
            self.client_socket = None


        @property
        def name(self):
            return self.name

        @name.setter
        def name(self, name):
            self.name = name

        def create_socket(self):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket = sock

        def create_connection(self, ip='127.0.0.1', port=8080):
            self.create_socket()
            self.client_socket.connect((ip, port))

        def start_chat(self):
            client_sock = self.client_socket
            self.receive_message(client_sock)
            try:
                while True:
                    self.send_message(client_sock)
                self.close_connection(self.client_socket)
            except KeyboardInterrupt:
                client_sock.sendall(bytes("\rClient left the chat", "UTF-8"))
                self.close_connection(client_sock)

        def receive_message(self, sock):
            raw_message = sock.recv(1024)
            message = raw_message.decode()
            print(message)

        def send_message(self, sock):
            message = input()
            sock.sendall(bytes(message, 'UTF-8'))

        def close_connection(self, sock):
            sock.close()

    client = Client()
    client.create_connection()
    client.start_chat()



if __name__ == '__main__':
    main()
