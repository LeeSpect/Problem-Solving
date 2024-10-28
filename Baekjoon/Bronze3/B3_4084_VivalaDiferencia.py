while 1:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0: break
    else:
        cnt = 0
        while 1:
            if a == b == c == d:
                print(cnt)
                break
            else:
                a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
                cnt += 1
