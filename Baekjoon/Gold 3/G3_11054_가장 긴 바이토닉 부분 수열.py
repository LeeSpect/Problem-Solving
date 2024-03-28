import sys; input=sys.stdin.readline
import bisect

def bi_search_left(A,N):
    L=[]
    dp=[]
    max_idx_dp=1
    for i in range(N):
        if not L:
            L.append(A[i])
            dp.append(max_idx_dp)
        else:
            if L[-1]==A[i]:
                dp.append(max_idx_dp)
            elif L[-1]<A[i]:
                L.append(A[i])
                max_idx_dp+=1
                dp.append(max_idx_dp)
            else:
                idx=bisect.bisect_left(L,A[i])
                L[idx]=A[i]
                dp.append(idx+1)
    return dp

def bi_search_right(A,N):
    L=[]
    dp=[]
    max_idx_dp=1
    for i in range(N-1,-1,-1):
        if not L:
            L.append(A[i])
            dp.append(max_idx_dp)
        else:
            if L[-1]==A[i]:
                dp.append(max_idx_dp)
            elif L[-1]<A[i]:
                L.append(A[i])
                max_idx_dp+=1
                dp.append(max_idx_dp)
            else:
                idx=bisect.bisect_left(L,A[i])
                L[idx]=A[i]
                dp.append(idx+1)
    return dp

def main():
    N=int(input())
    A=list(map(int,input().split()))
    dp1=bi_search_left(A,N)
    dp2=bi_search_right(A,N)
    maxi=0
    for i in range(N):
        if maxi<dp1[i]+dp2[-i-1]:
            maxi=dp1[i]+dp2[-i-1]
    print(maxi-1)

if __name__=='__main__':
    main()
