from datetime import datetime

"""
    Data for the Server part
"""

# ----------------------------------------------------

HOST = "127.0.0.1"
PORT = 65432
BUFFER_SIZE = 1024
ENCODE_FORMAT = "utf-8"
# USERS_DATABASE = "users.json"
# MESSAGES_DATABASE = "messages.json"

# ----------------------------------------------------

CLOSE = "close"

# ----------------------------------------------------

# START_TIME = datetime.now()
# DATE = datetime.now().strftime("%Y-%m-%d")
# VERSION = "0.1.8"

# ----------------------------------------------------
ALLOWED_COMMAND = ("GAME_INVITATION", "SHOT", "SHOT_REQUEST", "RESULT", "BOARD")



