x1,y1,z1 = map(int, input().split())
x2,y2,z2 = map(int, input().split())

if x1<=x2 and y1<=y2 and z1<=z2:
    print('A')
elif y1<=y2 and z1<=z2:
    if x2*2 >= x1:
        print('B')
    else: print('C')
else:
    if y2*2 >= y1:
        print('D')
    else: print('E')
