if __name__ == '__main__':
    n = int(input("n: "))
    m = int(input("m: "))
    k = int(input("k: "))

    result: str
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        result = 'YES'
    else:
        result = 'NO'

    print(result)