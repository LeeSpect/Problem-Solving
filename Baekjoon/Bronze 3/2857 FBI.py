import sys; input=sys.stdin.readline

flag=1
for i in range(1,6):
    k=input().rstrip()
    if 'FBI' in k:
        print(i)
        flag=0
if flag:
    print('HE GOT AWAY!')
