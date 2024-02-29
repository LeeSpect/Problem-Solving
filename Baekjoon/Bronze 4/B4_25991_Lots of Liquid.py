import sys; input = sys.stdin.readline

def main():
    T = int(input())
    l = list(map(float, input().split()))
    total = 0
    for i in l:
        total += i**3
    print(f'{total**(1/3):.6f}')

if __name__=='__main__':
    main()
