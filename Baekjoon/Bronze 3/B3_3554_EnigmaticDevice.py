# 참조: https://blog.naver.com/tnsgh9603/222859223404
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    m = int(input())
    for i in range(m):
        q, w, e = map(int, input().split())
        if q == 1:
            for j in range(w - 1, e):
                l[j] = l[j]**2 % 2010
        else:
            sum = 0
            for j in range(w - 1, e):
                sum += l[j]
            print(sum)

if __name__ == '__main__':
    main()
