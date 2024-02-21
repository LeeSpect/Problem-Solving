# ----------------------------------------------------------------------------------------------------
# 내 답안
a = int(input()); b = input()
ans = 0
for i in range(1, len(b)+1):
    ans += int(str(a*int(b[-i]))+'0'*(i-1))
    while str(ans).count('2') != 0 or str(ans).count('3') != 0:
        # str[str(ans).index(str(ans).count(2))]
        ans = str(ans)
        ans = ans.replace('23', '31')
        ans = ans.replace('13', '21')
        ans = ans.replace('03', '11')
        ans = ans.replace('22', '30')
        ans = ans.replace('12', '20')
        ans = ans.replace('02', '10')
        if ans[0] == '2':
            ans = '10'+ans[1:]
        elif ans[0] == '3':
            ans = '11'+ans[1:]
        ans = int(ans)

print(ans)

# ----------------------------------------------------------------------------------------------------
# 다른 사람 숏코딩
b1 = input()
b2 = input()
print(bin(int(b1, 2) * int(b2, 2))[2:])
