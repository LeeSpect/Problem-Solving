l = [int(input()) for i in range(3)]
l2 = [int(input()) for i in range(3)]

a = l[0]*3 + l[1]*2 + l[2]
b = l2[0]*3 + l2[1]*2 + l2[2]
if a == b:
    print('T')
elif a > b:
    print('A')
else:
    print('B')
