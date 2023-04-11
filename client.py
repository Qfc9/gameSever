import socket
import pickle

# Main Client
def main():

    # Host and Port to connect to
    host = '127.0.0.1'
    port = 4040

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
    
    for line in map:
        print(line)

    # Close the connection
    s.close()

if __name__ == '__main__':
    main()