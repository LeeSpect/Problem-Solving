l = list(map(int, input().split()))
l.sort()
if l[2] - l[1] == l[1] - l[0]:
    print(2*l[2] - l[1])
elif l[2]-l[1] > l[1]-l[0]:
    print(2*l[1] - l[0])
else: # 1 7 10
    print(2*l[1]-l[2])
