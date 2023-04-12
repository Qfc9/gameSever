import socket
import pickle
from libs.client.map import mapRenderer
from libs.client.configs import host, port

# Main Client
def main():
    # Create a socket object
    s = socket.socket()

    # Connect to the server
    s.connect((host,port))

    # Send a message to the server
    message = input("-> ")
    s.send(message.encode('utf-8'))

    # Receive data from the server
    data = s.recv(1024)
    map = pickle.loads(data)

    print ("Received from server: ")
    
    mapRenderer(map)

    # Close the connection
    s.close()

if __name__ == '__main__':
    main()