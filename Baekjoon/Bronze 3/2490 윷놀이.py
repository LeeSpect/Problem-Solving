for _ in range(3):
    l = list(map(int, input().split()))
    c = l.count(0)
    if c == 1:
        print('A')
        continue
    elif c == 2:
        print('B')
        continue
    elif c == 3:
        print('C')
        continue
    elif c == 4:
        print('D')
        continue
    else: print('E')
