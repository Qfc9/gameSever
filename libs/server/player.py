import socket
import threading
import random
import pickle
import time
from libs.shared.configs import map, mapXMax, mapYMax


class Player():
    """The player class is used to manage the player's connection and thread"""

    def __init__(self, id: int, connection: socket.socket, refresh) -> None:
        """
            The player class is used to manage the player's connection and thread
        """
        self.id = id
        self.connection = connection
        self.thread: threading.Thread = None
        self.username = ""
        self.pending = True
        self.refresh = refresh

        self.currentCoor = []

    def export(self):
        """
            Sanitizes the player
        """
        p = Player(self.id, None, self.refresh)

        p.thread = None
        p.connection = None
        p.username = self.username
        p.currentCoor = self.currentCoor
        p.pending = self.pending
        p.refresh = None

        return p

    def reload(self, id: int, currentCoor: list):
        """
            Reloads the player
        """
        self.id = id
        self.currentCoor = currentCoor

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
        # Receive username from the client
        self.username = self.connection.recv(1024).decode('utf-8')
        if not self.username.isalpha():
            print("Username from {}:{} was invalid".format(self.connection.getpeername()[0], self.connection.getpeername()[1]))
            self.connection.close()

        self.username = self.username.lower()

        self.pending = False
        self.refresh()

        if self.currentCoor == []:
            # Starting spawn location
            self.currentCoor = [random.randrange(
                0, mapXMax), random.randrange(0, mapYMax)]

        # Put the player on the map, the player id is the value
        map[self.currentCoor[1]][self.currentCoor[0]] = self.id

        print("Connected - trying to auth with username: " + str(self.username))

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

        # TODO bug on load, some people will spawn in a new location
