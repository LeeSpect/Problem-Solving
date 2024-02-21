import sys
input = sys.stdin.readline

def main():
    n = int(input())
    for i in range(n):
        y, m, d = map(int, input().split())
        if y < 1989 or y == 1989 and m < 2 or y == 1989 and m == 2 and d <= 27:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
