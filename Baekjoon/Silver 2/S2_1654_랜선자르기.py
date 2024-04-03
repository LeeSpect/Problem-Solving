import sys
input = sys.stdin.readline

def main():
    K, N = map(int, input().split())
    lines = sorted([int(input()) for _ in range(K)], reverse=True)

    start, end = 1, lines[0]*2

    ans=0
    while start <= end:
        mid = (start + end) // 2
        # print(start, mid, end)
        cnt = 0

        for line in lines:
            if line // mid == 0:
                break
            cnt += line // mid
        
        if cnt < N:
            end = mid-1
        else:
            ans=mid
            start = mid+1
    print(ans)

if __name__ == "__main__":
    main()