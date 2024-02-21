import sys; input = sys.stdin.readline

def main():
    n = int(input())
    total = 0
    for i in range(n):
        e = input().rstrip()
        k = e[2:]
        if int(k) <= 90:
            total += 1
    print(total)

if __name__=='__main__':
    main()
