while True:
    a,b,c = map(str, input().split())
    ans = 0
    if a == '0' and b == 'W' and c == '0':
        break
    elif b == 'W':
        ans = int(a) - int(c)
        if ans < -200: print('Not allowed')
        else:
            print(ans)
    elif b == 'D':
        print(int(a)+int(c))
