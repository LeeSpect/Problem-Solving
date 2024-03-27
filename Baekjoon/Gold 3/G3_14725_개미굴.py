import sys
from collections import defaultdict
input = sys.stdin.readline

def printAll(dicts, cnt):
    if not dicts:
        return
    for data in sorted(dicts):
        print(cnt*'-' + data)
        printAll(dicts[data], cnt+2)

def main():
    N = int(input())
    dicts = defaultdict()
    
    
    for _ in range(N):
        data = list(map(str, input().rstrip().split()))
        temp = dicts
        for i in range(1, int(data[0])+1):
            datum = data[i]
            if datum not in temp:
                temp[datum] = defaultdict()
            temp = temp[datum]
    printAll(dicts, 0)

if __name__ == "__main__":
    main()