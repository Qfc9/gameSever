import socket
import threading

class PlayerManagement():
    def __init__(self) -> None:
        self.connection = {}
        self.__nextId = -1

    @property
    def nextId(self) -> int:
        self.__nextId -= 1
        return self.__nextId


    def addConnection(self, connection: socket.socket, thread: threading.Thread, id: int):
        self.connection[str(id)] = (connection, thread, id)
