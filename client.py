import socket
import pickle
from libs.client.map import mapRenderer
from libs.client.configs import host, port
from libs.shared.playerConfigs import UP, DOWN, LEFT, RIGHT
import libs.client.commands as commands

def main():
    # Create a socket object
    s = socket.socket()

    # Connect to the server
    s.connect((host, port))

    # Send a message to the server
    message = input("Enter Username > ")
    s.send(message.encode('utf-8'))

    # Receive data from the server
    data = s.recv(1024)
    map = pickle.loads(data)

    print("Received from server: ")

    # Render the map
    mapRenderer(map)

    while True:
        # Send a message to the server
        # TODO Print out available commands
        message = input("Enter Command > ")

        if message.split(" ")[0] == "move":
            message = commands.move(message)

            if message is None:
                continue

        elif message == "exit":
            break

        else:
            print("Invalid command")
            continue

        s.send(message.encode('utf-8'))

        # Receive data from the server
        data = s.recv(1024)
        map = pickle.loads(data)

        print("Received from server: ")

        # Render the map
        mapRenderer(map)

    # Close the connection
    s.close()


if __name__ == '__main__':
    main()
