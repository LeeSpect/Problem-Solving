import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    string = input().rstrip()
    len_string = len(string)
    for i in range(len_string):
        if i == 0:
            print(string)
        elif i == len_string - 1:
            print(string[::-1])
        else:
            print(string[i] + ' '*(len_string-2) + string[len_string - i -1])
