l = list(map(int, input().split()))
l.sort()

if l[1]/3 >= l[0]:
    print(l[0])
elif l[1]/3*2 > l[0]:
    print(l[1]/3)
else:
    print(l[0]/2)
