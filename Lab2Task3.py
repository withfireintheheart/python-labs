def is_valid(string: str):
    openBrackets = 0

    for c in string:
        if c == '(':
            openBrackets += 1
        elif c == ')':
            if openBrackets == 0:
                return False
            openBrackets -= 1
    if openBrackets == 0:
        result = True
    else:
        result = False

    return result

	
if __name__ == '__main__':
    string = input("sentence: ")

    if is_valid(string):
        result = "YES"
    else:
        result = "NO"

    print(result)