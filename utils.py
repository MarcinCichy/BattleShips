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

# -----------------------------------------------------------------------------------------

    @staticmethod
    def game_invitation():
        return server_response.GAME_INVITATION_OK


    def shot(self):
        return {"SHOT": "was shot"}

    def shot_request(self):
        print('SHOT_REQUEST')

    def result(self):
        print('RESULT')

    def board(self):
        print('BOARD')
