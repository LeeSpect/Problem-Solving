import sys; input=sys.stdin.readline

def main():
    r, c = map(int, input().split())
    l1 = [list(input().rstrip()) for _ in range(r)]
    temp = input()
    l2 = [list(input().rstrip()) for _ in range(r)]
    cnt = 0
    for i in range(r):
        for j in range(c):
            if l1[i][j] == l2[i][j]:
                cnt += 1
    print(cnt)

if __name__=='__main__':
    main()
