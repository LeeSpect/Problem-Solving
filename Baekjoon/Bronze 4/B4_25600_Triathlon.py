import sys; input=sys.stdin.readline

def main():
    n = int(input())
    maxi = 0
    for i in range(n):
        a, d, g = map(int, input().split())
        total = a * (d + g)
        if a == (d + g):
            total *= 2
        maxi = max(maxi, total)
    print(maxi)

if __name__=='__main__':
    main()
