# 108080 KB / 120 ms
import sys
input=sys.stdin.readline

ans = ""
while True:
    string = input().rstrip()
    
    if string == "END":
        break
    
    temp = string.replace(" ", "")
    
    # 유일성 검사
    if len(set(temp)) == len(temp):
        ans += string + "\n"

print(ans)
