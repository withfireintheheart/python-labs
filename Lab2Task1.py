def is_palindrom(string: str):
    string = string.lower().replace(" ", "")
    length = len(string)

    if length == 0:
        return True

    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True

if __name__ == '__main__':
    string = input("word: ")

    if is_palindrom(string):
        result = "palindrom"
    else:
        result = "not palindrom"

    print(result)