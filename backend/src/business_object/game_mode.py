import secrets
from abc import ABC, abstractmethod

from business_object.game import Game
from business_object.player import Player


class GameMode(ABC):
    """abstract class of game modes"""
    @abstractmethod
    def play(p1, p2):
        pass


class DiceMode(GameMode):
    """class representing dice rolls"""
    def play(self, p1: Player, p2: Player):
        d1 = secrets.choice([1, 7])
        d2 = secrets.choice([1, 7])
        if d1 > d2:
            winner = p1
        elif d2 > d1:
            winner = p2
        else:
            winner = None
        return Game(p1, p2, "dice", winner, None, "lancer de dé")


class CoinFlipMode(GameMode):
    """class representing coin flips"""
    def play(self, p1: Player, p2: Player, choice="heads" | None):
        results = secrets.choice(["heads", "tails"])
        if (choice is None) or (results == choice):
            winner = p1
        else:
            winner = p2
        return Game(p1, p2, "coinflip", winner, None, "lancer de pièce")
