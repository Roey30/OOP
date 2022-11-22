import os
from pickle import *
from Database import *


class Data_to_file(Database):
    def __init__(self, dict, file):
        super().__init__(dict)
        self.file = file

    def write_file(self):
        self.file = open("demofile", "wb")
        if self.file.writable() and self.dictionary is not None:
            dump(self.dictionary, self.file)
        self.file.close()

    def read_file(self):
        self.file = open("demofile", "rb")
        if self.file.readable():
            self.dictionary = load(self.file)
            self.file.close()
            return self.dictionary
        self.file.close()
