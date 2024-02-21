# ----------------------------------------------------------------------------------------------------
# 틀린 코드: 시간 초과 발생
import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_team(student, students_left_over, students_found_team, students_failed_team, check, up):
    flag = True
    if up[student] in check:
        return False
    elif up[student] in students_found_team or up[student] in students_failed_team:
        return True
    else:
        check.add(up[student])
        flag = find_team(up[student], students_left_over, students_found_team, students_failed_team, check, up)
    return flag

def make_fail(student, students_left_over, students_failed_team, down):
    while down[student]:
        i = down[student].pop()
        if i in students_left_over:
            students_left_over.discard(i)
            students_failed_team.add(i)
            make_fail(i, students_left_over, students_failed_team, down)

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        students_left_over = set([i for i in range(1, n+1)])
        students_found_team = set()
        students_failed_team = set()
        choices = list(map(int, input().split()))
        up = [0 for i in range(n+1)]
        down = [[] for i in range(n+1)]
        for i in range(1, n+1):
            if choices[i-1] == i:
                students_left_over.discard(i)
                students_found_team.add(i)
            elif choices[i-1] in students_found_team or choices[i-1] in students_failed_team:
                students_left_over.discard(i)
                students_failed_team.add(i)
            else:
                up[i] = choices[i-1]
                down[choices[i-1]].append(i)
        for student in range(1, n+1):
            if student in students_left_over:
                if not up[student] or not down[student]:
                    students_left_over.discard(student)
                    students_failed_team.add(student)
                else:
                    check = set()
                    flag = find_team(student, students_left_over, students_found_team, students_failed_team, check, up)
                    if flag:
                        for node in check:
                            if node in students_left_over:
                                students_left_over.discard(node)
                                students_failed_team.add(node)
                                make_fail(node, students_left_over, students_failed_team, down)
                        students_left_over.discard(student)
                        students_failed_team.add(student)
                        make_fail(student, students_left_over, students_failed_team, down)
                    elif student not in check:
                        students_left_over.discard(student)
                        students_failed_team.add(student) 
                    else:
                        for node in check:
                            if node in students_left_over:
                                students_left_over.discard(node)
                                students_found_team.add(node)
                        for node in check:
                            if node in students_left_over:
                                make_fail(node, students_left_over, students_failed_team, down)
            if student in students_failed_team:
                make_fail(student, students_left_over, students_failed_team, down)
        print(len(students_failed_team))

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------
# 수정 코드: 위상 정렬 방식처럼 선택받지 못한 사람들을 모아 in_degree에 넣고,
# 그 사람들이 지목한 사람의 '총 지목받은 수'에 -1을 하면서, 그 수가 0이 된다면 다시 in_degree에 넣는 방식으로 진행한다.
# 참조: https://www.acmicpc.net/board/view/29536
import sys; input=sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        choices = list(map(int, input().split()))
        insa = [0 for i in range(n+1)]
        for i in range(n):
            insa[choices[i]] += 1
        in_degree = []
        for i in range(1, n+1):
            if not insa[i]:
                in_degree.append(i)
        cnt = 0
        while in_degree:
            k = in_degree.pop()
            cnt += 1
            insa[choices[k-1]] -= 1
            if not insa[choices[k-1]]:
                in_degree.append(choices[k-1])
        print(cnt)

if __name__ == "__main__":
    main()
