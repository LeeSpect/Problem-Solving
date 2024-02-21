import sys; input=sys.stdin.readline

def main():
    print('Gnomes:')
    t=int(input())
    for i in range(t):
        l=list(map(int,input().split()))
        if l[0]<l[1]<l[2] or l[0]>l[1]>l[2]:
            print('Ordered')
        else:
            print('Unordered')

if __name__=='__main__':
    main()
