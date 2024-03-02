import sys
from collections import deque

input = sys.stdin.readline

def check_ok(minn, maxx):
    if maxx - minn < K+1:
        return True
    return False

def put_fish(minn):
    global deq
    for i in range(len(deq[0])):
        if deq[0][i] == minn:
            deq[0][i] += 1
    # return

def first_put_over_glass():
    global deq
    if len(deq) == 1:
        deq.appendleft(deque([deq[0].popleft()]))
    else:
        temp_deq = deque()
        for i in range(len(deq[0])):
            l = deque()
            for j in range(len(deq)-1, -1, -1):
                l.append(deq[j][i])
            temp_deq.append(l)
        for _ in range(len(deq[0])): deq[-1].popleft()
        temp_deq.append(deq[-1])
        deq = temp_deq
    # return

def compare():
    global deq
    temp_deq = deque()
    for i in range(len(deq)):
        temp_deq.append(deque())
        for j in range(len(deq[i])):
            temp_fish = 0
            for dx, dy in dxy:
                nx, ny = i+dx, j+dy
                if nx == -1 or ny == -1: continue
                try:
                    if abs(deq[i][j] - deq[nx][ny]) // 5 > 0:
                        if deq[i][j] < deq[nx][ny]:
                            temp_fish += abs(deq[i][j] - deq[nx][ny]) // 5
                        else:
                            temp_fish -= abs(deq[i][j] - deq[nx][ny]) // 5
                except:
                    continue
            temp_deq[i].append(deq[i][j] + temp_fish)
    deq = temp_deq

def reset_glass():
    global deq
    temp_deq = deque()
    temp_deq.append(deque())
    for y in range(len(deq[-1])):
        for x in range(len(deq)-1, -1, -1):
            try:
                temp_deq[0].append(deq[x][y])
            except:
                break
    deq = temp_deq
    # return

def fly_air():
    global deq
    temp_size = len(deq[0]) // 2
    deq.appendleft(deque())
    for i in range(temp_size):
        deq[0].appendleft(deq[1].popleft())
    temp_size = len(deq[0]) // 2
    idx = 1
    for i in range(len(deq)):
        deq.appendleft(deque())
        for j in range(temp_size):
            deq[0].appendleft(deq[idx].popleft())
        idx += 2
    # return

if __name__ == '__main__':
    dxy = ((1,0),(0,1),(-1,0),(0,-1))
    N, K = map(int, input().split())
    input_deq = deque(map(int, input().split()))
    deq = deque()
    deq.append(input_deq)

    ans = 0
    while True:
        minn, maxx = float('inf'), -float('inf')
        for glass in deq[0]:
            if minn > glass: minn = glass
            if maxx < glass: maxx = glass

        if check_ok(minn, maxx):
            print(ans)
            break

        put_fish(minn)

        while not len(deq) > len(deq[-1]) - len(deq[0]) or len(deq) == 1:
            first_put_over_glass()
        compare()
        reset_glass()
        fly_air()
        compare()
        reset_glass()
        ans += 1