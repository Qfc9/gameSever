import socket
import threading

class Player():
    def __init__(self, id: int, connection: socket.socket, thread: threading.Thread) -> None:
        self.id = -1
        self.connection = None
        self.thread = None