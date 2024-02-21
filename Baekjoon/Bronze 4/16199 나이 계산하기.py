l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

#만나이
if l2[1] > l[1] or (l2[1]==l[1] and l2[2]>=l[2]):
    print(l2[0]-l[0])
else:
    print(l2[0]-l[0]-1)

#세는 나이
print(l2[0]-l[0]+1)

#연 나이
print(l2[0]-l[0])
