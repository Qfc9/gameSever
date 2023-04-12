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

        self.currentCoor = [0, 0]

    def spawn(self, map: list):
        self.thread = threading.Thread(target=self.run, args=([map]))
        self.thread.start()


    def run(self, map: list):
        self.currentCoor = [random.randrange(0, mapXMax), random.randrange(0, mapYMax)]

        map[self.currentCoor[1]][self.currentCoor[0]] = self.id


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

        map[self.currentCoor[1]][self.currentCoor[0]] = 0