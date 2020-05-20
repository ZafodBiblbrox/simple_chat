class ClientNameHandler:

    def request_client_name(self, client_conn):
        client_conn.sendall(bytes("Please create your nick name: ", "UTF-8"))
        raw_name = client_conn.recv(1024)
        name = raw_name.decode()
        return name

    def set_client_name(self, server, client_addr, name):
        name_entered = name
        name_dict = server.active_users
        if not name_entered:
            name_entered = 'Anonym'

        same_names = [name for name in name_dict.values() if name == name_entered]

        if same_names == []:
            name_dict[client_addr] = name_entered
        else:
            name_extension = len(same_names) + 1
            name_dict[client_addr] = name_entered + str(name_extension)

    def get_client_name(self, server, client_addr):
        name_dict = server.clients
        return name_dict[client_addr]
