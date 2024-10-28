import sys
input = sys.stdin.readline

def main():
    t1 = int(input())
    d = {}

    for i in range(1, t1+1):
        d[i] = input().rstrip()

    t2 = int(input())
    for j in range(t2):
        k = int(input())
        if d.get(k):
            print(f'Rule {k}: {d[k]}')
        else:
            print(f'Rule {k}: No such rule')

if __name__ == "__main__":
    main()
