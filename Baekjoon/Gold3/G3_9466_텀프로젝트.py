import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for t in range(T):
        ans = 0
        n = int(input())
        visited = [False for _ in range(n)]    # 외부 visited
        selects = list(map(int, input().split()))

        for i in range(n):
            if visited[i]: continue   # 외부 visited에서 방문됐으면 continue
            # find
            waiting = [i]
            inner_visited = set()      # 내부 visited
            inner_visited.add(i)
            temp_i = i
            while True:
                next = selects[temp_i] -1
                if visited[next]:       # 다음 사람이 외부 visited
                    for w in waiting:
                        visited[w] = True # 연결 안 되니까 전부 
                    break

                # 사이클을 돌다가 방문한 사람temp과 만나게 되면, 대기열을 돈다.
                    # + 외부 visited 배열에도 visited를 체크해준다.
                # 대기열을 돌 때는, 팀에 속하지 않는 사람으로 카운팅 하다가
                # temp를 만났을 때부터는 팀에 속하는 사람으로 카운팅 한다.(사이클이 생겼기 때문)
                if next in inner_visited:
                    flag = False
                    for w in waiting:
                        if w == next:
                            flag = True
                        if flag:
                            # print("w: ", w)
                            ans += 1
                        visited[w] = True
                    break
            
                inner_visited.add(next)
                waiting.append(next)
                temp_i = next

            # print("visited: ", visited, " ans: ", ans)
        print(n-ans)

if __name__ == "__main__":
    main()
