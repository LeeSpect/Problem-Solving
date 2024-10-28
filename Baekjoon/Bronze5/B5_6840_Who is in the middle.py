import sys
input = sys.stdin.readline

def main():
    l = []
    for i in range(3):
        l.append(int(input()))
    l.sort()
    print(l[1])

if __name__=='__main__':
    main()
