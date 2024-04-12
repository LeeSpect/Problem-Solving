import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    l = list(map(int, input().split()))
    
    maxi = max(l)
    trees = []
    for tree in l:
        if maxi - tree:
            trees.append(maxi - tree)
    
    trees = deque(sorted(trees))
    day = 0
    while trees:
        #print(trees)
        if day % 2 == 0: # 홀수
            if trees[-1] == 3:
                trees.append(trees.pop()-1)
                trees = deque(sorted(list(trees)))
            else:
                temp = trees.popleft()
                if temp == 2 and len(trees) == 0:
                    trees.appendleft(temp)
                elif temp == 1:
                    pass
                else:
                    trees.appendleft(temp-1)
        else:
            if trees[-1] == 1:
                pass
            elif trees[-1] == 2:
                trees.pop()
            else:
                trees.append(trees.pop() - 2)
                trees = deque(sorted(list(trees)))
        day += 1


    print(f'#{tc} {day}')