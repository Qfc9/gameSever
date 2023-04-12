import socket
import threading
import libs.server.player as Player

class PlayerManagement():
    def __init__(self) -> None:
        self.players: dict = {}
        self.__nextId = -1

    @property
    def nextId(self) -> int:
        self.__nextId -= 1
        return self.__nextId


    def addConnection(self, player: Player.Player):
        self.players[str(id)] = player
