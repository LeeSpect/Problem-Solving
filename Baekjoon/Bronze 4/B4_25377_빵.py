import sys; input=sys.stdin.readline

def main():
    n = int(input())
    mini = float('inf')
    for i in range(n):
        a, b = map(int, input().split())
        if a <= b and b < mini:
            mini = b
    print(mini if mini != float('inf') else -1)

if __name__ == '__main__':
    main()
