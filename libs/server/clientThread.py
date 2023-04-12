import socket
import pickle
import random
from libs.shared.configs import map, mapXMax, mapYMax

# Client Thread
def clientThread(c: socket.socket, map: list, id: int):

    spawnCoor = (random.randrange(0, mapXMax), random.randrange(0, mapYMax))

    map[spawnCoor[1]][spawnCoor[0]] = id


    # Receive data from the client
    data = c.recv(1024).decode('utf-8')

    print("from connected user: " + str(data))

    print("sending: " + str(map))

    # Send the uppercase data back to the client
    
    # create code for pickling the map
    # send the pickled map to the client
    mapByte = pickle.dumps(map)

    c.send(mapByte)

    # Close the connection
    c.close()

    map[spawnCoor[1]][spawnCoor[0]] = 0