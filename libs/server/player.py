import socket
import threading
import random
import pickle
import time
from libs.shared.configs import map, mapXMax, mapYMax


class Player():
    """The player class is used to manage the player's connection and thread"""

    def __init__(self, id: int, connection: socket.socket) -> None:
        """
            The player class is used to manage the player's connection and thread
        """
        self.id = id
        self.connection = connection
        self.thread: threading.Thread = None

        self.currentCoor = [0, 0]

    def spawn(self, map: list):
        """
            Spawn the player by spinning up a new thread
        """
        self.thread = threading.Thread(target=self.run, args=([map]))
        self.thread.start()

    def run(self, map: list):
        """
            The run function is the main functino function that is ran in the thread
        """
        # Starting spawn location
        self.currentCoor = [random.randrange(
            0, mapXMax), random.randrange(0, mapYMax)]

        # Put the player on the map, the player id is the value
        map[self.currentCoor[1]][self.currentCoor[0]] = self.id

        # Receive data from the client
        data = self.connection.recv(1024).decode('utf-8')

        print("from connected user: " + str(data))

        print("sending: " + str(map))

       # create code for pickling the map
        # send the pickled map to the client
        mapByte = pickle.dumps(map)
        self.connection.send(mapByte) 

        time.sleep(10)

        # Close the connection
        self.connection.close()

        # Remove the player from the map
        map[self.currentCoor[1]][self.currentCoor[0]] = 0
