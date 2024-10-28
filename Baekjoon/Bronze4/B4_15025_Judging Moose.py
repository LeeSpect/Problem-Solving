l = list(map(int, input().split()))
if l[0] == 0 and l[1] == 0:
    print('Not a moose')
elif l[0] == l[1]:
    print(f'Even {l[0]*2}')
else:
    print(f'Odd {max(l)*2}')
