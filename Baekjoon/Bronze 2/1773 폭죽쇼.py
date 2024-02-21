import sys; input=sys.stdin.readline

def main():
    N,C=map(int,input().split())
    l=[]
    bomb=set()
    for i in range(N):
        a=int(input())
        temp=a
        while temp<=C:
            bomb.add(temp)
            temp+=a
    print(len(bomb))

if __name__=='__main__':
    main()
