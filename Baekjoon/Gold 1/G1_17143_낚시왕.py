import sys
input = sys.stdin.readline

class Shark:
    def __init__(self, r, c, s, d, z):
        self.r = r
        self.c = c
        self.speed = s
        self.dir = d
        self.size = z

def set_position():
    sharks = []
    for r in range(R):
        for c in range(C):
            if maps[r][c] != 0:
                sharks.append(maps[r][c])

    new_maps = [[0] * C for _ in range(R)]

    while sharks:
        shark = sharks.pop()
        s = shark.speed

        if shark.dir < 2:
            s %= (2 * R - 2)
        else:
            s %= (2 * C - 2)

        for j in range(s):
            if shark.dir == 0 and shark.r == 0:
                shark.dir = 1
            elif shark.dir == 1 and shark.r == R - 1:
                shark.dir = 0
            elif shark.dir == 2 and shark.c == C - 1:
                shark.dir = 3
            elif shark.dir == 3 and shark.c == 0:
                shark.dir = 2

            shark.r += dr[shark.dir]
            shark.c += dc[shark.dir]

        if new_maps[shark.r][shark.c] == 0:
            new_maps[shark.r][shark.c] = shark
        elif new_maps[shark.r][shark.c].size < shark.size:
            new_maps[shark.r][shark.c] = shark

    return new_maps

if __name__ == '__main__':
    dr = (-1, 1, 0, 0)
    dc = (0, 0, 1, -1)
    R, C, M = map(int, input().split())
    maps = [[0] * C for _ in range(R)]
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        maps[r - 1][c - 1] = Shark(r - 1, c - 1, s, d - 1, z)

    answer = 0
    for t in range(C):
        for r in range(R):
            if maps[r][t] != 0:
                answer += maps[r][t].size
                maps[r][t] = 0
                break
        maps = set_position()
    print(answer)