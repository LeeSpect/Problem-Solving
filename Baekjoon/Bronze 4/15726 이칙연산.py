a,b,c = map(int, input().split())
ans = int(a*b/c); ans2 = int(a/b*c)
print(ans if ans >= ans2 else ans2)
