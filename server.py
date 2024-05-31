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
                    com = self.decode_received_data(command).upper()
                    result = self.serialize_data(self.use_command(com))
                    print(f'Result is: {result}')
                    conn.sendall(result.encode(server_data.ENCODE_FORMAT))

    def decode_received_data(self, data):
        decoded_data = json.loads(data)
        print(f"Command received from Client: {decoded_data['command']}.")
        return decoded_data['command']

    def serialize_data(self, data):
        return json.dumps(data)

    def use_command(self, comm):
        if comm in server_data.ALLOWED_COMMAND:
            match comm:
                case "GAME_INVITATION":
                    return SystemUtilities.game_invitation()
                case "SHOT":
                    return SystemUtilities.shot()
                case "SHOT_REQUEST":
                    return SystemUtilities.shot_request()
                case "RESULT":
                    return SystemUtilities.result()
                case "BOARD":
                    return SystemUtilities.board()
        else:
            return SystemUtilities.unrecognised_command()


def start():
    SystemUtilities.clear_screen()
    server = Server(server_data.HOST, server_data.PORT, server_data.BUFFER_SIZE)
    server.server_connection()


start()



