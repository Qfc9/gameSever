import socket
import threading
from libs.shared.configs import map, mapXMax, mapYMax
from libs.server.configs import host, port
from libs.server.playerManagement import PlayerManagement
from libs.server.player import Player

# Main Server
def main():
    print("Starting server...")
    pm = PlayerManagement()

    for i in range(mapYMax):
        map.append([])
        for j in range(mapXMax):
            map[i].append(0)

    # Create a socket object
    s = socket.socket()

    # Bind to the host and port
    s.bind((host,port))

    # Start listening for connections
    s.listen(1)

    while True:
        # Accept a connection, is a blocking function
        c, addr = s.accept()

        # Print the address of the connection
        print("Connection from: " + str(addr))

        player = Player(pm.nextId, c)
        player.spawn(map)    

        pm.addConnection(player)
    
    s.close()

if __name__ == '__main__':
    main()