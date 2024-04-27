import sys
input=sys.stdin.readline

def main():
    type = ("1QAZ", "2WSX", "3EDC", "4RFV5TGB", "6YHN7UJM", "8IK,", "9OL.", "0P;/-['=]")
    ans = [0]*8
    for c in input().rstrip():
        for i in range(8):
            if c in type[i]:
                ans[i] += 1
    for i in ans:
        print(i)
    
if __name__ == '__main__':
    main()