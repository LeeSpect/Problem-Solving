import sys; input = sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        a, b = map(float, input().split())
        ans = max(a, b) - min(a, b)
        print(f'{ans:.1f}')

if __name__ == '__main__':
    main()
