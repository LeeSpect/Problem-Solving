# ----------------------------------------------------------------------------------------------------
# 틀린 코드: 덱으로 구현
import sys; input=sys.stdin.readline
from collections import deque

def main():
    N,S=map(int,input().split())
    D=deque()
    l=list(map(int,input().split()))
    len_of_D=0
    min_len=float('inf')
    for i in range(N):
        if l[i]>=S:
            print(1)
            exit()
        if not D:
            D.append(l[i])
            len_of_D+=1
        else:
            temp=len_of_D
            for j in range(temp):
                k=D.pop()
                if k+l[i]>=S:
                    min_len=min(len_of_D+1,min_len)
                    len_of_D-=1
                else:
                    D.appendleft(k+l[i])
            D.appendleft(l[i])
            len_of_D+=1
    print(min_len)

if __name__=='__main__':
    main()
# ----------------------------------------------------------------------------------------------------
# 틀린  코드: 위 코드를 보완하여 수정함. 여전히 덱으로 구현(시간 초과)
import sys; input=sys.stdin.readline
from collections import deque

def main():
    N,S=map(int,input().split())
    D=deque()
    l=list(map(int,input().split()))
    len_of_D=0
    min_len=float('inf')
    for i in range(N):
        if l[i]>=S:
            print(1)
            exit()
        if len_of_D==0:
            D.append(l[i])
            len_of_D+=1
        else:
            # print(D)
            temp=len_of_D
            for j in range(temp):
                k=D.pop()+l[i]
                if min_len<=len_of_D:
                    len_of_D-=1
                    continue
                if k>=S:
                    min_len=min(len_of_D+1,min_len)
                    len_of_D-=1
                else:
                    D.appendleft(k)
            D.appendleft(l[i])
            len_of_D+=1

    print(0 if min_len==float('inf') else min_len)

if __name__=='__main__':
    main()
# ----------------------------------------------------------------------------------------------------
# 틀린 수정 코드: 투 포인터로 구현해 봄
import sys; input=sys.stdin.readline

def main():
    N,S=map(int,input().split())
    arr=list(map(int,input().split()))
    Partial_sum,start,end=arr[0],0,1
    min_size,now_size=float('inf'),1
    if arr[0]>=S:
        print(1)
        exit()
    while start<=end and end<N:
        if min_size<=now_size:
            Partial_sum-=arr[start]
            start+=1
            now_size-=1
        if Partial_sum<S:
            Partial_sum+=arr[end]
            end+=1
            now_size+=1
        else:
            min_size=min(now_size,min_size)
            Partial_sum-=arr[start]
            start+=1
            now_size-=1
    print(min_size)

if __name__=='__main__':
    main()
# ----------------------------------------------------------------------------------------------------
# 수정 코드: end!=N일 때 end를 더이상 증가시키지 않았음. 만들 수 있는 경우가 없다면 0을 출력해야 함.
import sys; input=sys.stdin.readline

def main():
    N,S=map(int,input().split())
    arr=list(map(int,input().split()))
    if arr[0]>=S:
        print(1)
        exit()

    Partial_sum,start,end=arr[0]+arr[1],0,1
    min_size,now_size=float('inf'),2

    while start<=end and end<N:
        if start==end and Partial_sum>=S:
            print(1)
            exit()
        if min_size<=now_size:
            Partial_sum-=arr[start]
            start+=1
            now_size-=1
        if Partial_sum<S:
            end+=1
            if end!=N:
                Partial_sum+=arr[end]
                now_size+=1
        else:
            min_size=min(now_size,min_size)
            Partial_sum-=arr[start]
            start+=1
            now_size-=1
    print(0 if min_size==float('inf') else min_size)

if __name__=='__main__':
    main()
