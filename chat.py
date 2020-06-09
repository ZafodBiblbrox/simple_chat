import threading

class Chat:

    @staticmethod
    def display_chat(client):
        sock = client.client_socket
        client_receive_thread = threading.Thread(target=client.receive_message, args=(sock,))
        client_sending_thread = threading.Thread(target=client.send_message, args=(sock,))
        client_receive_thread.start()
        client_sending_thread.start()

