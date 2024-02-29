L = [int(input()) for i in range(5)]
for i in range(len(L)):
    if L[i] < 40:
        L[i] = 40
print(sum(L)//len(L))
