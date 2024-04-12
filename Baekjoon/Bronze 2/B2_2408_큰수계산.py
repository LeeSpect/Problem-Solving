import sys
input = sys.stdin.readline

N = int(input())
N += N - 1

string = ''
for _ in range(N):
    temp = input().rstrip()
    if temp == '/': temp = '//'

    string += temp

print(int(eval(string)))