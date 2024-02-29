import sys

cnt=1
while 1:
    l = list(map(int,sys.stdin.readline().split()))
    if len(l)==1 and l[0]==0: break
    print(f'Case {cnt}: Sorting... done!')
    cnt +=1
