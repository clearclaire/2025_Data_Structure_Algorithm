def fibonacci_sum(n):
    n = n % 60

    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(n - 1):
        a, b = b, (a + b) % 10

    return b


if __name__ == '__main__':
    n = int(input())
    print((fibonacci_sum(n + 2) - 1) % 10)
