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
            self.receive_message()
            self.send_message()

    def receive_message(self):
        raw_message = self.client_sock.recv(1024)
        message = raw_message.decode()
        #print(f"{self.client_name}: {message}")
        return message

    def send_message(self):
        message = self.receive_message()
        client_name = self.client_name
        self.client_sock.sendall(bytes(f"{client_name}: {message}", 'UTF-8'))
