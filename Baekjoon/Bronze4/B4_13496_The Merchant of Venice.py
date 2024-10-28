import sys; input=sys.stdin.readline

def main():
    T = int(input())
    for i in range(1,T+1):
        n, s, d = map(int, input().split())
        ans = 0
        for j in range(n):
            a, b = map(int, input().split())
            if a/s <= d:
                ans += b
        print(f'Data Set {i}:')
        print(ans)
        print()

if __name__=='__main__':
    main()
