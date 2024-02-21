l = list(map(int, input().split()))
if l[1]<=l[0]<=l[2]:    print(l[0])
elif l[0] < l[1]:    print(l[1])
else:    print(l[2])
