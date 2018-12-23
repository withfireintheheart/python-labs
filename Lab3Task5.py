def calculate_year(x: int, p: int, y: int):
    i = 0
    while x < y:
        x *= 1 + p / 100
        x = int(100 * x) / 100
        i += 1

    return i

if __name__ == '__main__':
    x = int(input("x: "))
    p = int(input("p: "))
    y = int(input("y: "))

    result = calculate_year(x = x, p = p, y = y)
    print(result)