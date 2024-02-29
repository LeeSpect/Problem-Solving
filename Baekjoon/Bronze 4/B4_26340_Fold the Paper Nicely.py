import sys; input = sys.stdin.readline

def main():
    n = int(input())
    for i in range(1, n+1):
        a, b, c = map(int, input().split())
        print(f'Data set: {a} {b} {c}')
        for j in range(c):
            a, b = max(a, b), min(a, b)
            a //= 2
        a, b = max(a, b), min(a, b)
        print(a, b)
        print()

if __name__=='__main__':
    main()
