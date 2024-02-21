import sys; input = sys.stdin.readline

def main():
    n, d = map(int, input().split())
    num = 0
    l = []
    for i in range(n):
        k = int(input())
        l.append(k)
        num += k
    for i in range(n):
        print(int(d/num*l[i]))

if __name__=='__main__':
    main()
