import sys; input = sys.stdin.readline

def main():
    while 1:
        n = int(input())
        if not n:
            break
        total = 0
        for i in range(1, n+1):
            total += i 
        print(total)

if __name__=='__main__':
    main()
