def fibonacci_number(n):
    a = [0, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        for i in range(2, n + 1):
            a.append(a[i - 1] + a[i - 2])
        return a[-1]

if __name__ == '__main__' :
    input_n = int(input())
    print(fibonacci_number(input_n))