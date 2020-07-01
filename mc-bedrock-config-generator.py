#!/usr/bin/env python3
from os import getenv

def special_getenv(key: str, default: str, possibleValues: list = [], isNumber: bool = False, checkFunc = lambda x: True):
    value = getenv(key)
    if value == None:
        value = default
    elif isNumber == True and (not value.isdigit() or not checkFunc(int(key))):
        value = default
    elif len(possibleValues) > 0:
        value = value.lower()
        if not value.lower() in possibleValues:
            value = default
    return value

serverInfo = {
    "server-name": special_getenv("SERVER_NAME", "Dedicated Server"),
    "gamemode": special_getenv("GAMEMODE", "survival", ["survival", "creative", "adventure", "0", "1", "2"]),
    "difficulty": special_getenv("DIFFICULTY", "easy", ["peaceful", "easy", "normal", "hard", "0", "1", "2", "3"]),
    "allow-cheats": special_getenv("ALLOW_CHEATS", "false", ["false", "true"]),
    "max-players": special_getenv("MAX_PLAYERS", "10", isNumber=True, checkFunc = lambda x: True if x > 0 else False),
    "online-mode": special_getenv("ONLINE_MODE", "true", ["false", "true"]),
    "white-list": special_getenv("WHITE_LIST", "false", ["false", "true"]),
    "server-port": special_getenv("SERVER_PORT", "19132", isNumber=True),
    "server-portv6": special_getenv("SERVER_PORTV6", "19133", isNumber=True),
    "view-distance": special_getenv("VIEW_DISTANCE", "32", isNumber=True),
    "tick-distance": special_getenv("TICK_DISTANCE", "4", isNumber=True, checkFunc = lambda x: True if x in range(4, 13) else False),
    "player-idle-timeout": special_getenv("PLAYER_IDLE_TIMEOUT", "30", isNumber=True),
    "max-threads": special_getenv("MAX_THREADS", "8", isNumber=True),
    "level-name": special_getenv("LEVEL_NAME", "Bedrock level"),
    "level-seed": special_getenv("LEVEL_SEED", ""),
    "level-type": special_getenv("LEVEL_TYPE", "DEFAULT", ["FLAT", "LEGACY", "DEFAULT"]),
    "default-player-permission-level": special_getenv("DEFAULT_PLAYER_PERMISSION_LEVEL", "member", ["visitor", "member", "operator"]),
    "texturepack-required": special_getenv("TEXTUREPACK_REQUIRED", "false", ["false", "true"]),
    "content-log-file-enabled": special_getenv("CONTENT_LOG_FILE_ENABLED", "false", ["false", "true"]),
    "compression-threshold": special_getenv("COMPRESSION_THRESHOLD", "1", isNumber=True, checkFunc = lambda x: True if x in range(0, 65536) else False),
    "server-authoritative-movement": special_getenv("SERVER_AUTHORITATIVE_MOVEMENT", "true", ["false", "true"]),
    "player-movement-score-threshold": special_getenv("PLAYER_MOVEMENT_SCORE_THRESHOLD", "20", isNumber=True),
    "player-movement-distance-threshold": special_getenv("PLAYER_MOVEMENT_DISTANCE_THRESHOLD", "0.3"),
    "player-movement-duration-threshold-in-ms": special_getenv("PLAYER_MOVEMENT_DURATION_THRESHOLD_IN_MS", "500", isNumber=True),
    "correct-player-movement": special_getenv("CORRECT_PLAYER_MOVEMENT", "false", ["false", "true"])
}

buffer = ""
for key, value in serverInfo.items():
    buffer += f"{key}={value}\n"
with open("./server.properties", "w") as f:
    f.write(buffer)