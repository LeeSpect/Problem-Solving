import sys
input = sys.stdin.readline

from collections import Counter

def is_possible_strfry(str1, str2):
    if Counter(str1) == Counter(str2):
        return "Possible"
    else:
        return "Impossible"

N = int(input().rstrip())
results = []

for _ in range(N):
    s1, s2 = input().split()
    result = is_possible_strfry(s1, s2)
    results.append(result)

print("\n".join(results))