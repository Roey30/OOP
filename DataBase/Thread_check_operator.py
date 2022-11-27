"""
Name : Roey Firan
Program name : Data_Base
Date : 27/11/2022
Description: Uses to sync the data_base using threading
"""
import threading
from synchronization import Synchronization
from Data_to_file import Data_to_file
from time import sleep

FILE_NAME = "Thread_Check.bin"


def main():
    """
    calls the reader and the writer methods.
     using threading.
     :return: None
     """
    list_threads = Data_to_file(FILE_NAME)
    sync = Synchronization(list_threads, True)
    list_threads = []
    for number in range(10):
        thread_write = threading.Thread(target=check_write_function, args=(sync,))
        thread_write.start()
        sleep(1)
        thread_read = threading.Thread(target=check_read_function, args=(sync,))
        thread_read.start()
        list_threads.append(thread_write)
        list_threads.append(thread_read)
    print(sync.dictionary)
    for thread in list_threads:
        thread.join()


def check_write_function(list_threads):
    for number in range(1000):
        assert list_threads.set_value(number, number)


def check_read_function(list_threads):
    for number in range(1000):
        assert (number == list_threads.get_value(number))


if __name__ == '__main__':
    main()
