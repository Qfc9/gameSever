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


    def addConnection(self, connection: socket.socket, thread: threading.Thread, id: int):
        self.players[str(id)] = Player.Player(id, connection, thread)
