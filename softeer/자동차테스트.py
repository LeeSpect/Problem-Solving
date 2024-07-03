# 51.35 MB, 316 ms
import sys
from collections import defaultdict
input = sys.stdin.readline

n, q = map(int, input().split())
cars = list(map(int, input().split()))  
dic = defaultdict(list)

cars.sort()
for i in range(len(cars)):
    dic[cars[i]] = [i, len(cars)-1 - i]

for _ in range(q):
    query = int(input())
    if dic[query]:
        print(dic[query][0] * dic[query][1])
    else:
        print(0)