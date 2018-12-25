def digit_at(number: int, n: int):
    return number // 10 ** n % 10

	
if __name__ == '__main__':
    a1 = int(input("a1: "))
    a2 = int(input("a2: "))
    luckyTickets = 0
    tickets = range(a1, a2)
    
    for ticket in tickets:
        s1 = 0
        for i in range(3):
            s1 += digit_at(ticket, i)

        s2 = 0
        for i in range(3, 6):
            s2 += digit_at(ticket, i)

        if s1 == s2:
            luckyTickets += 1

    print(luckyTickets)