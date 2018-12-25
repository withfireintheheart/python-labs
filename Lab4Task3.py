def super_fibonacci(n, m):
    l = []
    while m != 0:
        l.append(1)
        m -= 1
    z_list = len(l) - 1
    while len(l) < n:
        l.append(sum(l[-1 - z_list:]))
    return l[-1]


if __name__ == '__main__':
    print(super_fibonacci(2, 1))
    print(super_fibonacci(3, 5))
    print(super_fibonacci(8, 2))
    print(super_fibonacci(9, 3))
	