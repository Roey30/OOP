from Data_to_file import *

data = Data_to_file({'firstName': 'Roey', 'lastName': 'Firan'}, 'example.txt')

print(data.get_value('firstName'))
print(data.get_value('lastName'))

print(data.dictionary)

data.set_value('age', 18)
data.get_value('age')


data.delete_value('lastName')
print(data.dictionary)

data.set_value('lastName', 'Firan')
data.write_file()

print(data.read_file())

