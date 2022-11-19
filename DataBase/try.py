import pickle
from pickle import *

f = open("demofile2.txt", "a")
f.write("See you soon!")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile2.txt", "a")
f.write("\nSee you soon!")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile2.txt", "r")
print(f.read())
f.close()

f = open("demofile2.txt", "r")
print(f.readable())

f = open("demofile2.txt", "r")
print(f.readline())
print(f.tell())

f = open("demofile2.txt", "a")
print(f.writable())

f = open("demofile2.txt", "a")
f.writelines(["See you soon!", "Over and out."])
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile2.txt", "r")
f.seek(4)
print(f.readline())

dic = {'key1': 'val1', 'key2': 'val2'}

for values in dic.values():
    print(values)

list_of_the_values = list(dic.values())

print(list_of_the_values)
