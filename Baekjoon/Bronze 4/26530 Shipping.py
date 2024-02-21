import sys; input = sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        t = int(input())
        ans = 0
        for j in range(t):
            l = list(map(str, input().split()))
            ans += int(l[-2]) * float(l[-1])
        print(f'${ans:.2f}')

if __name__ == '__main__':
    main()
