# CONNECTION_CLOSE = {"Connection": "close"}

GAME_INVITATION_OK = {
  "type": "GAME_INVITATION",
  "status": 0,
  "message": None,
  "body": None
}

GAME_INVITATION_BUSY = {
  "type": "GAME_INVITATION",
  "status": 1,
  "message": "Server is playing the other game.",
  "body": None
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

# ----------------------------------------------------
# 0 - OK wszystko w porządku
# 1 - SERVER_BUSY serwer jest zajęty, ponieważ gra w inną grę
# 2 - ILLEGAL_ARGUMENTS przesłano do serwera nieprawidłowe dane
# 3 - INTERNAL_ERROR wewnętrzny błąd serwera, gra zostaje przerwana
# 4 - BAD_REQUEST serwer nie potrafi rozpoznać żądania