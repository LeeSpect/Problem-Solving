import sys; input = sys. stdin.readline

string = input().rstrip()
ans = ''
for s in string:
    if s.isdigit():
        ans += f'#{s}'
    elif s.isalpha():
        if s.islower():
            ans += f'{ord(s) - 96:02d}'
        else:
            ans += f'{ord(s) - 38:02d}'
    else:
        ans += s
print(ans)
