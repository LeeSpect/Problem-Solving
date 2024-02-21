L = list(map(int, input().split()))
if L[0]==L[1]==L[2]:
    print(10000+L[0]*1000)
elif L[0]==L[1] and L[1]!=L[2]:
    print(1000+L[0]*100)
elif L[0]!=L[1] and L[1]==L[2]:
    print(1000+L[1]*100)
elif L[0]==L[2] and L[1]!=L[2]:
    print(1000+L[2]*100)
else:
    print(max(L)*100)
