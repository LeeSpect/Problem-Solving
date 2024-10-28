# 112084 KB / 180 ms
import sys
input=sys.stdin.readline

N, C = map(int, input().split())
house_cords = [int(input()) for _ in range(N)]
house_cords.sort()

start = 1
end = house_cords[-1] - house_cords[0]
ans = -1

while start <= end:
    mid = (start + end) // 2
    
    cnt = 1
    last_house = house_cords[0]
    for i in range(1, N):
        next_house = house_cords[i]
        if next_house - last_house >= mid:
            cnt += 1
            last_house = next_house
    if cnt >= C: # C개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
    
print(ans)
        