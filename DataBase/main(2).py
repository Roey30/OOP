import random
import threading
from synchronization import Sync
from Data_to_file import Data_to_file
import logging
from multiprocessing import Process

FILE_NAME = "database.bin"
DICTIONARY = {}


def main():
    db = Data_to_file(DICTIONARY, FILE_NAME)
    for i in range(1, 40):
        s = Sync(db, True)
        thread = threading.Thread(target=handle_thread, args=(s, i))
        thread.start()


def handle_thread(s, num):
    try:
        s.set_value(num, num)
        g = s.get_value(num)
        if g != num:
            print("Error")
        print(g)
        print(s.dictionary)
    except SystemError as er:
        logging.error(str(er))


if __name__ == '__main__':
    main()
