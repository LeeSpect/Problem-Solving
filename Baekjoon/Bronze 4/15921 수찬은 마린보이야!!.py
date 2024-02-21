n = int(input())
if n == 0:
    print('divide by zero')
else:
    l = map(int, input().split())
    if sum(l) == 0:
        print('divide by zero')
    else:
        print(f'{1:0.2f}')
