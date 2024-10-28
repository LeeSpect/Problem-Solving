import sys; input=sys.stdin.readline

while 1:
    k=input().rstrip()
    if k=='END':
        break
    print(k[::-1])
