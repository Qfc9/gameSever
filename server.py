import socket
import threading
from libs.shared.configs import map, mapXMax, mapYMax
from libs.server.configs import host, port
from libs.server.playerManagement import PlayerManagement
from libs.server.player import Player


def main():
    print("Starting server...")
    pm = PlayerManagement()

    # Create the map
    for i in range(mapYMax):
        map.append([])
        for j in range(mapXMax):
            map[i].append(0)

    # Create a socket object
    s = socket.socket()

    # Bind to the host and port
    s.bind((host, port))

    # Start listening for connections
    s.listen(1)

    while True:
        # Accept a connection, is a blocking function
        c, addr = s.accept()

        # Print the address of the connection
        print("Connection from: " + str(addr))

        # Create a new player
        player = Player(pm.nextId, c, pm.refresh)
        # Spawn the player
        player.spawn(map)

        # Add the player to the player management
        pm.addConnection(player)

    s.close()


if __name__ == '__main__':
    main()
