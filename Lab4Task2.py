def counter(a: int, b: int):
    a_set: set = set(str(a))
    b_set: set = set(str(b))

    return len(a_set.intersection(b_set))

if __name__ == '__main__':
    print(counter(123, 45))