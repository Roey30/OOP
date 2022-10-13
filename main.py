import hashlib


def print_hi():
    str2hash = 000000

    # encoding Geeks for Geeks using encode()
    # then sending to md5()
    str2hash = str(str2hash)
    result = hashlib.md5(str2hash.encode())

    # printing the equivalent hexadecimal value.
    print(f"The hexadecimal equivalent of hash for Geeks for Geeks is : {result.hexdigest()}")


if __name__ == '__main__':
    print_hi()
