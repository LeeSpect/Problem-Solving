l = list(map(int, input().split()))
l.sort()
l2 = [(l[0]-1)%4, (l[1]-1)%4]
print(((l[1]-1)//4 - (l[0]-1)//4) + max(l2)-min(l2))
