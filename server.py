import socket
import threading
import pickle
import random

map = []
mapXMax = 5
mapYMax = 5

# Echo Function
def echo(c: socket.socket, map: list):

    spawnCoor = (random.randrange(0, mapXMax), random.randrange(0, mapYMax))

    map[spawnCoor[1]][spawnCoor[0]] = -1


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

# Main Server
def main():
    print("Starting server...")

    for i in range(mapYMax):
        map.append([])
        for j in range(mapXMax):
            map[i].append(0)

    # Host and Port to start the server on
    host = '127.0.0.1'
    port = 4040

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

        # Create a new thread to handle the connection
        t = threading.Thread(target=echo, args=([c, map]))
        t.start()
    
    s.close()

if __name__ == '__main__':
    main()