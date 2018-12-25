def digit_at(number: int, n: int):
    return number // 10 ** n % 10

def count_holes(n):
    if isinstance(n, float) | ("." in str(n)):
        return "ERROR"

    try:
        n = int(n)
    except:
        return "ERROR"

    num_to_holes = {
        0: 1,
        4: 1,
        6: 1,
        8: 2,
        9: 1
    }

    count = 0
    r = range(len(str(abs(n))))
    for i in r:
        at = digit_at(abs(n), i)
        digit = abs(at)
        get = num_to_holes.get(digit, 0)
        count += get

    return count


if __name__ == '__main__':
    print(count_holes('123'))
    print(count_holes(906))
    print(count_holes('001'))
    print(count_holes(-8))
    print(count_holes(-8.0))