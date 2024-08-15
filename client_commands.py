GAME_INVITATION = {
  "type": "GAME_INVITATION",
  "body": None
}

SHOT = {
  "type":"SHOT",
  "body":{
    "row": None,
    "column": None
  }
}

SHOT_REQUEST = {
  "type": "SHOT_REQUEST",
  "body": None
}

BOARD = {
  "type": "BOARD",
  "body": {
    "four": None,
    "three": None,
    "two": None,
    "one": None
    }
}


BAD_REQUEST = {
  "type": "UNKNOWN",
  "status": 4,
  "message": None,
  "body": None
}

SHOT_OK = {
  "type": "SHOT",
  "status": 0,
  "message": None,
  "body": "HIT"
}

SHOT_MISS = {
  "type": "SHOT",
  "status": 0,
  "message": None,
  "body": "MISS"
}

SHOT_SINKING = {
  "type": "SHOT",
  "status": 0,
  "message": None,
  "body": "SINKING"

}

SHOT_ERROR = {
  "type": "SHOT",
  "status": 2,
  "message": "The shot is not within the boundaries of the board.",
  "body": None

}