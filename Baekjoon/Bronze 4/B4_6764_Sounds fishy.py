L = [int(input()) for i in range(4)]

if max(L) == min(L):
    print('Fish At Constant Depth')
elif L[0]<L[1] and L[1]<L[2] and L[2]<L[3]:
    print('Fish Rising')
elif L[0]>L[1] and L[1]>L[2] and L[2]>L[3]:
    print('Fish Diving')
else:
    print('No Fish')
