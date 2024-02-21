n,a,b,c,d = map(int, input().split())

ans1 = (n+a-1)//a*b; ans2 = (n+c-1)//c*d
if ans1 <= ans2:
    print(ans1)
else:
    print(ans2)
