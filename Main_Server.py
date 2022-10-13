# IMPORTS
import socket
from threading import Thread

# CONSTANTS
EXAMPLE = 'eC9C0F7EDCC18A98B1F31853B1813301'

MaxPacket = 1024
QUEUE_SIZE = 10
IP = '0.0.0.0'
PORT = 3256
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LIST_THREADS = []
NUMBER_OF_RANGE = 0


def main():
    ok = False
    number_clients = 0
    try:
        server_socket.bind((IP, PORT))
        server_socket.listen(QUEUE_SIZE)
        print("Listening for connections on port %d" % PORT)
        while not ok:
            client_socket, client_address = server_socket.accept()
            thread = Thread(target=handle_client, args=(client_socket, client_address))
            LIST_THREADS.append(thread)
            print(f'List of threads: {LIST_THREADS}')
            number_clients += 1
            if number_clients == 4:
                ok = True
        for i in LIST_THREADS:
            i.start()

    except socket.error as err:
        print('received socket exception - ' + str(err))
    finally:
        server_socket.close()


def handle_client(client_socket, client_address):
    number_if_true = ''
    number_of_client = 0
    print(f'connecting to client {client_address}')
    client_socket.send(EXAMPLE.encode())
    while number_if_true == '' and number_of_client > 4:
        new_msg = client_socket.recv(MaxPacket)
        new_msg = new_msg.decode()
        if new_msg == 'Sorry i did not found it ':
            print(f'Too bad! client {client_address} did not found it')
            number_of_client += 1
        elif new_msg == 'I have found it!!':
            number_if_true = ' '
    final = client_socket.recv(MaxPacket)
    print(f'well done client{client_address} fount it! The answer is {final.decode()}')
    if number_of_client == 4:
        print('No one found it too bad')


if __name__ == '__main__':
    main()
