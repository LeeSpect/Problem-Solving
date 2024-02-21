while True:
    l = list(map(int, input().split()))
    if l[0] == 0: break
    else:
        ans = 1
        for i in range(1, len(l), 2):
            ans = ans*l[i]-l[i+1]
    print(ans)
