import socket
import threading
import random
import pickle
from libs.shared.configs import map, mapXMax, mapYMax

class Player():
    def __init__(self, id: int, connection: socket.socket) -> None:
        self.id = id
        self.connection = connection
        self.thread: threading.Thread = None

    def spawn(self, map: list):
        self.thread = threading.Thread(target=self.run, args=([map]))
        self.thread.start()


    def run(self, map: list):
        spawnCoor = (random.randrange(0, mapXMax), random.randrange(0, mapYMax))

        map[spawnCoor[1]][spawnCoor[0]] = self.id


        # Receive data from the client
        data = self.connection.recv(1024).decode('utf-8')

        print("from connected user: " + str(data))

        print("sending: " + str(map))

        # Send the uppercase data back to the client
        
        # create code for pickling the map
        # send the pickled map to the client
        mapByte = pickle.dumps(map)

        self.connection.send(mapByte)

        # Close the connection
        self.connection.close()

        map[spawnCoor[1]][spawnCoor[0]] = 0