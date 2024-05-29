""" server.py """
import socket
from utils import SystemUtilities
import json
import server_data


class Server:
    def __init__(self, srv_host, srv_port, srv_buff):
        self.srv_host = srv_host
        self.srv_port = srv_port
        self.srv_buff = srv_buff

    def server_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.srv_host, self.srv_port))
            s.listen()
            print("Server started.")
            print("-" * 17)
            while True:
                conn, addr = s.accept()
                SystemUtilities.clear_screen()
                with conn:
                    print(f"Connected by {addr}")
                    command = conn.recv(self.srv_buff)
                    com = self.decode_received_data(command)
                    # result = menu.handler.use_command(com)
                    result = com
                    print(f"Result is: {result}")
                    conn.sendall(result.encode(server_data.ENCODE_FORMAT))

                    if "Connection" in result:
                        if (json.loads(result))["Connection"] == server_data.CLOSE:
                            print("Server stopped")
                            break

    def decode_received_data(self, data):
        decoded_data = json.loads(data)
        # print(f"Command: {decoded_data['command']},  received from Client name: {decoded_data['name']}")
        # return decoded_data['command']
        return decoded_data

    def use_command(self, comm):
        if comm in server_data.ALLOWED_COMMAND:
            match comm:
                case "game_invitation":
                    return SystemUtilities.game_invitation()
                case "shot":
                    return SystemUtilities.shot()
                case "shot_request":
                    return SystemUtilities.shot_request()
                case "result":
                    return SystemUtilities.result()
                case "board":
                    return SystemUtilities.board()
        else:
            return SystemUtilities.unrecognised_command()


def start():
    SystemUtilities.clear_screen()
    server = Server(server_data.HOST, server_data.PORT, server_data.BUFFER_SIZE)
    server.server_connection()


start()






class Server:
    def __init__(self, srv_host, srv_port, srv_buff):
        self.srv_host = srv_host
        self.srv_port = srv_port
        self.srv_buff = srv_buff

    def server_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.srv_host, self.srv_port))
            s.listen()
            print("Server started.")
            print("-" * 17)
            while True:
                conn, addr = s.accept()
                SystemUtilities.clear_screen()
                with conn:
                    print(f"Connected by {addr}")
                    command = conn.recv(self.srv_buff)
                    com = self.decode_received_data(command)
                    # result = menu.handler.use_command(com)
                    result = com
                    print(f"Result is: {result }")
                    conn.sendall(result.encode(server_data.ENCODE_FORMAT))

                    if "Connection" in result:
                        if (json.loads(result))["Connection"] == server_data.CLOSE:
                            print("Server stopped")
                            break

    @staticmethod
    def decode_received_data(received_data):
        if received_data is None:
            SystemUtilities.unrecognised_command()

        else:
            decoded_data = json.loads(received_data)
            print(f"Command received from Client: {decoded_data['command']}")
            if decoded_data in server_data.ALLOWED_COMMAND:
                print(f"Command is correct")  # to hide showing login and password
                return decoded_data
            else:
                print("to dupa)")
                return SystemUtilities.unrecognised_command()


def start():
    SystemUtilities.clear_screen()
    server = Server(server_data.HOST, server_data.PORT, server_data.BUFFER_SIZE)
    server.server_connection()


start()


