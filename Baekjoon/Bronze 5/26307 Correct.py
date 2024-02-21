import sys; input = sys.stdin.readline

def main():
    HH, MM = map(int, input().split())
    h = HH - 9
    print(h*60 + MM)

if __name__=='__main__':
    main()
