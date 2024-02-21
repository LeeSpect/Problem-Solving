while True:
    b, n = map(int, input().split())
    if b == n == 0: break
    else:
        c = 1000001
        i = 1
        while True:
            if abs(b - i**n) < c:
                c = abs(b - i**n)
            else:
                print(i - 1)
                break
            i += 1
