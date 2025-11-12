def fibonacci(n):
    n = n % 60

    if n <= 1:
        return n

    # previous, current, sum = 0, 1, 1
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % 10
        # sum += b * b
    return b
    # return sum % 10    


def fibonacci_sum_squares(n):
    return ((fibonacci(n) * fibonacci(n+1)) % 10)


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
