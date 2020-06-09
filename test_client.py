import socket
import threading
# from message_broker.chat import Chat


class Chat:

    @staticmethod
    def display_chat(client):
        sock = client.client_socket
        client_receive_thread = threading.Thread(target=client.receive_message, args=(sock,))
        client_sending_thread = threading.Thread(target=client.send_message, args=(sock,))
        client_receive_thread.start()
        client_sending_thread.start()


class Client:

    def __init__(self,):
        self.client_socket = None
        self.message = None

    def _create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = sock

    def create_connection(self, ip='127.0.0.1', port=8080):
        self._create_socket()
        self.client_socket.connect((ip, port))

    def receive_message(self, sock):
        try:
            while True:
                raw_message = sock.recv(1024)
                if raw_message:
                    self.message = raw_message.decode()
                    print(self.message)
        except KeyboardInterrupt:
            sock.sendall(bytes("\rClient left the chat", "UTF-8"))
            self.close_connection(sock)

    def send_message(self, sock):
        try:
            while True:
                message = input()
                sock.sendall(bytes(message, "UTF-8"))
        except KeyboardInterrupt:
            sock.sendall(bytes("\rClient left the chat", "UTF-8"))
            self.close_connection(sock)

    def close_connection(self, sock):
        sock.close()


client = Client()
client.create_connection()
Chat.display_chat(client)
