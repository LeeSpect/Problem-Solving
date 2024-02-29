import sys
input = sys.stdin.readline

n, m = map(int, input().split())
print(m <= 2 and 'NEWBIE!' or m <= n and 'OLDBIE!' or 'TLE!')
