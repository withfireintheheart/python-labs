if __name__ == '__main__':
    n = int(input("n: "))
    sum = 0
    sum_ind = 0
    for i in range(1, n):
        num = int(input("- "))

        sum += num
        sum_ind += i

    result = sum_ind - sum + n
    print(result)
	