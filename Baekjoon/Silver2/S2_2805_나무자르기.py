import sys
input = sys.stdin.readline

def find():
    start, end = 0, tree_list[-1]
    while start+1 != end:          # start와 end가 같아지면 종료: start와 end가 같아지면 그 값이 정답
        mid = (start + end) // 2
        size = 0
        for i in range(N-1, -1, -1):
            if tree_list[i] - mid <= 0:
                break
            size += tree_list[i] - mid
        if size < M:  # 나무의 길이가 부족하면 높이를 줄인다
            end = mid # end를 mid로 설정하고 start와 end가 같아지면 종료
        else:         # 나무의 길이가 충분하면 높이를 늘린다
            start = mid # start를 mid로 설정하고 start와 end가 같아지면 종료
    print(start)

def main():
    global N, M, tree_list
    N, M = map(int, input().split())
    tree_list = sorted(list(map(int, input().split())))
    
    find()

if __name__ == "__main__":
    main()