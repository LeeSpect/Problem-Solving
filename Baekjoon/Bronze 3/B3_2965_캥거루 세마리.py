# 틀린 코드
import sys

a,b,c = map(int, sys.stdin.readline().split())
if b-a > c-a:
    print(b-a-1)
else:
    print(c-b-1)

# ------------------------------------------------------------------------------------------
# 수정 코드 : c-a를 c-b로 표기해야 했음.
import sys

a,b,c = map(int, sys.stdin.readline().split())
if b-a > c-b:
    print(b-a-1)
else:
    print(c-b-1)
