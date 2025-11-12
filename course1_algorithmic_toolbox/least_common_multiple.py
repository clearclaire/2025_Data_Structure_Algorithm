def lcm(a, b):
    c, d = max(a, b), min(a, b)
    while d != 0:
        c, d = d, c % d

    return (a * b) // c

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

