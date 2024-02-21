import sys
input = sys.stdin.readline

string = input().rstrip()

print(len(string) + string.count(':') + string.count('_') * 5)
