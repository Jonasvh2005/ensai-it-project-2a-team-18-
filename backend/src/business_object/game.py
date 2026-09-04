from business_object.player import Player


class Game:
    """
    Class representing a Game.
    Attributes:
        id_game (int): The unique identifier for the game.
        player1 (Player): One of the two players
        player2 (Player): The other player
        game_mode (str): The name of the game played
        winner (Player): The winning player
        description (str): The description of the game
        timestamp (datetime): la date of when the game was created
    """
    def __init__(self, player1, player2, game_mode, winner: Player or None, description, timestamp):
        """Constructor"""
        self.id_game = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

    def __str__(self):
        """Returns a string representation of the game.
        Returns:
            str: A string containing the type of game, players, winner.
        """
        return f"{self.game_mode} between {self.player1} and {self.player2}. Winner: {self.winner}"
