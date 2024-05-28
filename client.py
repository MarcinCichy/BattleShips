import socket
import client_data
import json
import utils



class Client:
    def __init__(self, srv_host, srv_port, srv_buff):
        self.srv_host = srv_host
        self.srv_port = srv_port
        self.srv_buff = srv_buff

    def client_connection(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.srv_host, int(self.srv_port)))
            in_comm = self.input_command()
            s.sendall(in_comm)
            data = s.recv(self.srv_buff)
            if self.decode_received_data(data) == "close":
                break

    def input_command(self):
        command = input("Command: ")
        encoded_command = self.serialize_command(command).encode(client_data.ENCODE_FORMAT)
        return encoded_command

    def serialize_command(self, comm):
        comm_dict = {
            "command": comm,
            "name": "client_1"
        }
        comm_json = json.dumps(comm_dict)
        return comm_json

    def decode_received_data(self, data):
        decoded_data = json.loads(data)
        for key, value in decoded_data.items():
            if value == "is stopped":
                print(key, value)
                return "close"
            else:
                print(key, ':', value)


def start():
    utils.SystemUtilities.clear_screen()
    client = Client(client_data.HOST, client_data.PORT, client_data.BUFFER_SIZE)
    client.client_connection()


start()
