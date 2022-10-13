# IMPORTS
import socket
import hashlib


# CONSTANTS
MAX_PACKET = 2048
LOW_PACKET = 1024
SERVER = "127.0.0.1"
CLIENT_SOCKET = socket.socket()
PORT = 3256
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
FULL_NUMBER = 9999999999
CLIENT1_NUMBER_BEGINS = 0
CLIENT1_NUMBER_ENDS = FULL_NUMBER / 4


def solve_function(msg):
    global final_result
    hello = False
    print(f'now the solving part of {msg}')
    client_number_begins = CLIENT1_NUMBER_BEGINS
    while client_number_begins != CLIENT1_NUMBER_ENDS and not hello:
        number_hash = str(client_number_begins)
        result = hashlib.md5(number_hash.encode())
        final_result = result.hexdigest()
        print(final_result)
        if msg[0] == final_result[0]:
            hello = True
        client_number_begins += 1
    if client_number_begins == CLIENT1_NUMBER_ENDS:
        print('Sorry i did not found it ')
    else:
        print(f'The result of the hash is: {final_result} and the number is: {client_number_begins}')
        print('I have found it!!')
        CLIENT.send('I have found it!!'.encode())
        CLIENT.send(final_result.encode())


def main():
    try:
        CLIENT.connect((SERVER, PORT))
        msg = CLIENT.recv(LOW_PACKET).decode()
        print(f'The server sent: {msg}')
        solve_function(msg)
    except socket.error and KeyboardInterrupt as err:
        print('received socket exception - ' + str(err))
    finally:
        print('The client is closing now ')


if __name__ == '__main__':
    main()
