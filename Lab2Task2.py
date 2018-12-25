def reverse_string(string: str):
    return " ".join(reversed(string.split(" ")))

	
if __name__ == '__main__':
    string = input("string: ")

    print(reverse_string(string))