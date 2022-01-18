from enum import Enum


class PlayerStatus(Enum):
    HIT = 1
    STICK = 2
    WINNER = 3
    BUSTED = 4
    