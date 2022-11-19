class Database:
    def __init__(self, dict):
        self.dictionary = dict

    def set_value(self, key, val):
        self.dictionary[key] = val
        if self.dictionary[key] == val:
            return True

    def get_value(self, key):
        return self.dictionary[key]

    def delete_value(self, key):
        val = self.dictionary[key]
        self.dictionary[key] = None
        return val
