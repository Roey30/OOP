import os
from pickle import dump, dumps, load, loads
from Database import *


class Data_to_file(Database):
    def __init__(self, dict, file):
        super().__init__(dict)
        self.file = file
        if not os.path.isfile(self.file):
            file = open(self.file, "wb")
            dump(self.dictionary, file)
            file.close()

    def write(self):
        if os.path.isfile(self.file):
            file = open(self.file, "wb")
            dump(self.dictionary, file)
            file.close()

    def read(self):
        if os.path.isfile(self.file):
            file = open(self.file, "rb")
            self.dictionary = load(file)
            file.close()
            return self.dictionary

    def write_file(self):
        self.file = open("demofile", "wb")
        if self.file.writable() and self.dictionary is not None:
            self.file.write(dumps(self.dictionary))
        self.file.close()

    def read_file(self):
        self.file = open("demofile", "rb")
        if self.file.readable():
            return self.file.readlines()
