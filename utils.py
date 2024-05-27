import json
from os import name, system
import server_response


class SystemUtilities:
    def __init__(self):
        self.username = ""
        self.comm = ""

    @staticmethod
    def clear_screen():
        """Clear the screen in depends on operating system
        (Windows, Linux or iOS)."""

        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    @staticmethod
    def unrecognised_command():
        un_comm_dict = server_response.UNRECOGNISED_COMMAND
        un_comm_json = json.dumps(un_comm_dict)
        return un_comm_json

    @staticmethod
    def clear():
        clear_dict = {"Clear": ""}
        clear_json = json.dumps(clear_dict)
        return clear_json

    def use_command(self, entrance_command):
        if isinstance(entrance_command, dict):
            self.comm = entrance_command.pop(self.username)

        if isinstance(self.comm, dict):
            print(f'REAL COMMAND = {list(self.comm.keys())[0]}')
            command = list(self.comm.keys())[0]
            data = self.comm[command]
        else:
            command = self.comm
            data = None
        if command in self.all_users_commands:
            match command:
                case "GAME_INVITATION":
                    pass
                case "SHOT":
                    pass
                case "SHOT_REQUEST":
                    pass
                case "RESULT":
                    pass
                case "BOARD":
                    pass
                case _:
                    pass