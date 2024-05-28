import json
import socket
import server_data
# import menu
from utils import SystemUtilities
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
