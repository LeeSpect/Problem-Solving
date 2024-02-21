# M개 O, N-m개 X
# K개 O, N-k개 X

l = list(map(int, input().split()))
l2 = [l[1], l[2]]; l3 = [l[0]-l[1], l[0]-l[2]]

print(min(l2)+min(l3))
