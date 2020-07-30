def buddy(start, limit):
    for n in range(start, limit + 1):
        m = sum(n)
        if m > n and n == sum(m):
            return [n, m]
    return None

def sum(num):
    result = 0
    for i in range(2, int(round(num ** 0.5))):
        if num % i == 0:
            result += i
            result += num // i
    return result

# print(buddy(10, 50))
