"""
Name : Roey Firan
Program name : Data_Base
Date : 27/11/2022
Description: Uses to sync the data_base using processing
"""
from multiprocessing import Process
from synchronization import Synchronization
from Data_to_file import Data_to_file
from time import sleep

FILE_NAME = "Process_Check.bin"


def main():
    """
    calls the reader and the writer methods.
     using threading.
     :return: None
     """
    list_process = Data_to_file(FILE_NAME)
    sync = Synchronization(list_process, False)
    list_process = []
    for number in range(10):
        process_write = Process(target=check_write_function, args=(sync,))
        process_write.start()
        sleep(1)
        process_read = Process(target=check_read_function, args=(sync,))
        process_read.start()
        list_process.append(process_write)
        list_process.append(process_read)
    for process in list_process:
        process.join()


def check_write_function(list_process):
    for number in range(1000):
        assert list_process.set_value(number, number)


def check_read_function(list_process):
    for number in range(1000):
        assert (number == list_process.get_value(number))


if __name__ == '__main__':
    main()
