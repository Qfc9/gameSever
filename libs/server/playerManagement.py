import socket
import threading
import libs.server.player as Player


class PlayerManagement():
    """The player management class is used to manage the players"""

    def __init__(self) -> None:
        """
            The player management class is used to manage the players
        """
        self.players: dict = {}
        self.__nextId = -1

    @property
    def nextId(self) -> int:
        """Produces unique ids for the players"""

        self.__nextId -= 1
        return self.__nextId

    def addConnection(self, player: Player.Player):
        """
            Adds a player to the player management
        """
        self.players[str(id)] = player
