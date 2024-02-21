import sys; input = sys.stdin.readline

def main():
    n = int(input())
    total = 0
    for i in range(n):
        total += int(input())
    print(total)

if __name__=='__main__':
    main()
