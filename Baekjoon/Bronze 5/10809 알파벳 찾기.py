# 97 a ~ 122 z

S = str(input())
ans = str()

for i in range(97, 123):
    if chr(i) in S:
        ans += str(S.index(chr(i)))+' '
    else:
        ans += '-1 '
print(ans[:-1])
