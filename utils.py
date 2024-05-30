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

    def game_invitation(self):
        print('GAME_INVITATION')

    @staticmethod
    def shot():
        shot_dict = {"SHOT": "was shot"}
        shot_json = json.dumps(shot_dict)
        return shot_json

    def shot_request(self):
        print('SHOT_REQUEST')

    def result(self):
        print('RESULT')

    def board(self):
        print('BOARD')
