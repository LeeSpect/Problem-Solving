l1 = list(map(int, input().split())); l2 = list(map(int, input().split()))

if l1[0]+l2[1] >= l1[1]+l2[0]:
    print(l1[1]+l2[0])
else:
    print(l1[0]+l2[1])
