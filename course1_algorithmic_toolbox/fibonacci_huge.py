def get_pisano_period(m):
    a, b = 0, 1
    for i in range(m * m):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return i + 1

def fibonacci_huge_naive(n, m):
    pisano_period = get_pisano_period(m)
    n = n % pisano_period

    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b

    return b % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))