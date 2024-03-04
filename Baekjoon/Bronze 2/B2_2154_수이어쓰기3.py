import sys
input = sys.stdin.readline

N = int(input())
string = ''
for i in range(1, N+1):
    string += str(i)

print(string.index(str(N))+1)