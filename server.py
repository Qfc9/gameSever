import socket

def main():
    host = '127.0.0.1'
    port = 4040

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)

    c, addr = s.accept()

    print ("Connection from: " + str(addr))
    while True:
        data = c.recv(1024).decode('utf-8')

        if not data:
            break

        print("from connected user: " + str(data))
        data = str(data).upper()

        print("sending: " + str(data))
        c.send(data.encode('utf-8'))

    c.close()
    
    s.close()

if __name__ == '__main__':
    main()