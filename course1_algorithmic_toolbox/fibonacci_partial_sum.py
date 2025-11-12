# Uses python3
import sys

def fibonacci_sum(n):
    n = n % 60
    
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % 10
    
    return b

def fibonacci_partial_sum_naive(from_, to):

    to_sum = fibonacci_sum(to + 2)
    from_sum = fibonacci_sum(from_ + 1)

    return (to_sum - from_sum) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
