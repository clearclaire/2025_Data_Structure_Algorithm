def gcd(a, b):
    c, d = max(a, b), min(a, b)
    while d != 0:
        c, d = d , c % d
    return c


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
