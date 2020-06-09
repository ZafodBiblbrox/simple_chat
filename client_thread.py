import threading


class ClientThread(threading.Thread):

    def __init__(self, server, client_sock, client_address, client_name):
        super().__init__()
        self.server = server
        self.client_sock = client_sock
        self.client_address = client_address
        self.client_name = client_name

    def run(self):
        while True:
            message = self.receive_message()
            if message:
                for users in self.server.active_connections:
                    self.send_message(users, message)


    def receive_message(self):
        raw_message = self.client_sock.recv(1024)
        message = raw_message.decode()
        return message

    def send_message(self, destination_sock, message):
        sender_name = self.client_name
        destination_sock.sendall(bytes(f"{sender_name}: {message}", 'UTF-8'))

