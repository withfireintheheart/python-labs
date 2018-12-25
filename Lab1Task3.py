
def check_for_triangle(a: int, b: int, c: int):
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    if check_for_triangle(a, b, c):
        result = "triangle"

    else:
        result = "not triangle"

    print(result)